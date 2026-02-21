"""
Generate Hero Images for Second Chair Homepage

Creates 4 settlement check hero images and uploads to Airtable.
"""

import asyncio
import os
import sys
from pathlib import Path

# Add parent path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '08_Ad_Factory'))

# Load .env from project root first
from dotenv import load_dotenv
project_root = Path(__file__).parent.parent.parent.parent.parent
root_env = project_root / ".env"
if root_env.exists():
    load_dotenv(root_env)

# Also load brand-specific .env
brand_env = Path(__file__).parent / ".env"
if brand_env.exists():
    load_dotenv(brand_env, override=True)

import fal_client
from pyairtable import Api
from config_loader import load_brand_config

# Hero image prompts - polished style with giant novelty checks
HERO_PROMPTS = [
    {
        "ad_title": "Hero Image V1 - Six-Figure Victory",
        "image_prompt": """Photorealistic, professional photography. Tight framing, subject fills frame. A confident Black woman in her late 30s, well-dressed in a clean blouse and cardigan, visible arm sling and small bandage on temple, holds a giant oversized novelty settlement check - classic lottery winner presentation style with decorative blue border, printed routing numbers, "CLAIM ESTIMATE NOW" as the issuer, amount clearly showing $385,425 in large bold numbers. She's smiling with genuine relief. Behind her, a silver sedan with moderate front bumper damage (dented, not destroyed). Las Vegas Strip skyline glowing in golden hour background. Cinematic lighting, sharp focus, high production value. Clean, aspirational, empowering.""",
        "strategy": "Homepage Hero",
        "channel": "Landing Page",
    },
    {
        "ad_title": "Hero Image V2 - The Big Check",
        "image_prompt": """Professional advertising photography. Close-up framing. A Latino man in his early 50s, clean-shaven, wearing a nice polo shirt, neck brace visible, holds an enormous ceremonial presentation check - the classic oversized novelty style with green decorative border, bank-style design, "CLAIM ESTIMATE NOW" printed as issuer, amount showing $247,500 in large bold numbers. Expression of relief and gratitude. His pickup truck with rear quarter damage visible in background. Las Vegas Stratosphere tower and Strip hotels in soft focus behind. Warm afternoon sunlight, polished aesthetic, billboard-ready quality.""",
        "strategy": "Homepage Hero",
        "channel": "Landing Page",
    },
    {
        "ad_title": "Hero Image V3 - Quarter Million Club",
        "image_prompt": """Cinematic photography, high production value. Tight framing like a portrait. A white woman in her late 30s, dressed professionally in a blazer, walking boot on one leg, confidently holds a giant novelty settlement check - classic oversized lottery winner style with blue/gold decorative border, official check design with routing numbers, "CLAIM ESTIMATE NOW" as issuer, amount clearly displaying $312,750 in large bold font. Direct eye contact, hopeful confident expression. Her SUV with side door dent visible behind her. Caesars Palace and Flamingo casino signs in Las Vegas background. Golden hour lighting, sharp and clean.""",
        "strategy": "Homepage Hero",
        "channel": "Landing Page",
    },
    {
        "ad_title": "Hero Image V4 - Justice Paid",
        "image_prompt": """Professional portrait photography. Tight framing, subject prominent. A Black man in his mid-40s, sharp in business casual (blazer, crisp open-collar shirt), small forehead bandage and wrist brace, holds a massive oversized novelty presentation check - classic giant lottery winner style with decorative border, official bank check design, "CLAIM ESTIMATE NOW" as the issuer, amount showing $425,000 in large bold numbers. Confident, reassuring expression looking directly at camera. His silver sedan with T-bone door damage behind him. Famous "Welcome to Las Vegas" sign visible in background. Midday Nevada sun, high contrast, clean and polished.""",
        "strategy": "Homepage Hero",
        "channel": "Landing Page",
    },
]


async def generate_image(prompt: str, fal_key: str) -> str:
    """Generate a single image using Fal.ai."""
    os.environ["FAL_KEY"] = fal_key
    
    handler = await fal_client.submit_async(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": prompt,
            "num_images": 1,
            "aspect_ratio": "1:1",
            "resolution": "2K",
            "output_format": "png",
        }
    )
    
    result = await handler.get()
    
    if result and "images" in result and len(result["images"]) > 0:
        return result["images"][0]["url"]
    
    raise ValueError("No image returned")


def upload_to_airtable(results: list[dict], config: dict) -> int:
    """Upload hero images to Airtable as new rows."""
    creds = config["credentials"]
    tables = config["airtable"]
    field_map = config.get("field_mapping", {})
    defaults = config.get("defaults", {})
    
    api = Api(creds["airtable_pat"])
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    records_created = 0
    
    for result in results:
        fields = {
            field_map.get("ad_title", "Ad Title"): result["ad_title"],
            field_map.get("image_prompt", "IMG_Prompts"): result["image_prompt"],
            field_map.get("strategy", "Strategy"): result["strategy"],
            field_map.get("channel", "Channel"): result["channel"],
            field_map.get("client", "Client"): defaults.get("client", "Jacoby & Meyers"),
            field_map.get("state", "State"): "NV",
            field_map.get("aspect_ratio_field", "Aspect Ratio"): "1:1",
        }
        
        # Attach the generated image
        if result.get("image_url"):
            fields[field_map.get("img_1", "IMG")] = [{"url": result["image_url"]}]
        
        try:
            table.create(fields)
            records_created += 1
            print(f"  ✅ Created: {result['ad_title']}")
        except Exception as e:
            print(f"  ❌ Failed: {result['ad_title']} - {e}")
    
    return records_created


async def main():
    print("=" * 60)
    print("Second Chair Hero Image Generator")
    print("=" * 60)
    
    # Load config
    try:
        config = load_brand_config("Lead_Faucet")
        print(f"✅ Loaded config for Lead_Faucet")
    except Exception as e:
        print(f"❌ Config error: {e}")
        return
    
    fal_key = config["credentials"]["fal_key"]
    
    # Generate all 4 images
    print(f"\n[GENERATE] Creating 4 hero images...")
    
    results = []
    for i, prompt_data in enumerate(HERO_PROMPTS):
        print(f"  [{i+1}/4] Generating: {prompt_data['ad_title']}...")
        try:
            image_url = await generate_image(prompt_data["image_prompt"], fal_key)
            results.append({**prompt_data, "image_url": image_url})
            print(f"         ✅ Generated")
        except Exception as e:
            print(f"         ❌ Failed: {e}")
            results.append({**prompt_data, "image_url": None})
    
    # Upload to Airtable
    print(f"\n[UPLOAD] Uploading to Airtable...")
    created = upload_to_airtable(results, config)
    
    print(f"\n{'=' * 60}")
    print(f"[DONE] Created {created} hero image records in Airtable")
    print(f"       Review at: Image Ads table")


if __name__ == "__main__":
    asyncio.run(main())
