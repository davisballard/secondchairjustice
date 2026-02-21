"""
Generate Settlement Gap V1 Images - The Lowball
Record ID: reclu6lReElgWVsCF

3 distinct image concepts:
- IMG 1: Vegas Math (Raw Gap Numbers + Nevada Identity)
- IMG 2: Text Thread (Screenshot Native)  
- IMG 3: Nevada Driver (Identity Portrait + Gap Overlay)
"""

import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "08_Ad_Factory"))

from config_loader import load_brand_config
from pyairtable import Api
import fal_client

RECORD_ID = "reclu6lReElgWVsCF"

# Three distinct prompts for IMG, IMG 2, IMG 3
IMAGE_PROMPTS = [
    # IMG 1: Vegas Math
    """Clean infographic split-frame design showing insurance settlement gap, 
left side small muted red number "$2,500" with text "INSURANCE OFFERED" below, 
right side large bold electric green number "$127,500" with text "CASE SETTLED FOR" below, 
dramatic bold arrow connecting the two numbers, 
subtle Las Vegas skyline silhouette in background at dusk, 
Stratosphere tower visible in distance, desert mountains on horizon, 
NOT tourist Strip, working-class Vegas residential aesthetic, 
warm desert sunset tones burnt orange and dusty purple sky, 
high contrast bold sans-serif typography, 
lo-fi paper texture overlay, authentic iPhone screenshot aesthetic, 
NOT polished or corporate, raw and real""",

    # IMG 2: Text Thread  
    """Realistic iPhone screenshot of iMessage text conversation in dark mode, 
authentic iOS interface with battery percentage and time visible at top,
text message bubbles showing settlement conversation:
gray bubble "They offered me $3,200"  
gray bubble "That's it??"
blue bubble "Attorney just called. Settlement: $127,000"
gray bubble "Holy shit"
phone lock screen wallpaper barely visible showing Las Vegas Strip at night,
authentic smartphone screenshot quality with slight screen glare,
cropped casually like someone quickly screenshotted and shared,
subtle grain and realistic lighting as if photographed from actual phone screen,
NOT mockup, looks genuinely captured and shared""",

    # IMG 3: Nevada Driver
    """Candid documentary portrait photograph of 42-year-old working-class Nevada resident,
authentic natural appearance with slight sun weathering on face,
confident knowing expression not smiling but assured,
standing near their car in Las Vegas suburb residential neighborhood,
desert landscaping with rocks and cacti visible, palm trees in distance,
wearing casual work clothes like a polo shirt or simple t-shirt,
genuine real person NOT a model, natural imperfections,
afternoon golden hour lighting, shot on 35mm film,
shallow depth of field with soft bokeh on suburban background,
documentary journalism photography style,
Henderson or North Las Vegas residential area aesthetic,
empty space in upper portion of frame for text overlay"""
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
            "resolution": "1K",
            "output_format": "png",
        }
    )
    
    result = await handler.get()
    
    if result and "images" in result and len(result["images"]) > 0:
        return result["images"][0]["url"]
    
    raise ValueError(f"No image returned for prompt: {prompt[:50]}...")


async def main():
    print("[*] Loading Second Chair configuration...")
    config = load_brand_config("Lead_Faucet")
    
    fal_key = config["credentials"]["fal_key"]
    creds = config["credentials"]
    tables = config["airtable"]
    field_map = config.get("field_mapping", {})
    
    print(f"[*] Generating 3 images for record {RECORD_ID}...")
    print()
    
    # Generate all 3 images in parallel
    image_names = ["Vegas Math", "Text Thread", "Nevada Driver"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/3] Generating: Vegas Math...")
    print("  [2/3] Generating: Text Thread...")
    print("  [3/3] Generating: Nevada Driver...")
    print()
    print("  (Running in parallel...)")
    print()
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Collect successful URLs
    image_urls = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"  ❌ {image_names[i]} failed: {result}")
            image_urls.append(None)
        else:
            print(f"  ✅ {image_names[i]} generated")
            image_urls.append(result)
    
    # Update Airtable record
    print()
    print(f"[*] Updating Airtable record {RECORD_ID}...")
    
    api = Api(creds["airtable_pat"])
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    # Build update fields
    img_fields = [
        field_map.get("img_1", "IMG"),
        field_map.get("img_2", "IMG 2"),
        field_map.get("img_3", "IMG 3"),
    ]
    
    update_fields = {}
    for i, url in enumerate(image_urls):
        if url and i < len(img_fields):
            update_fields[img_fields[i]] = [{"url": url}]
    
    # Also store the prompts for reference
    prompt_text = "\n\n---\n\n".join([
        f"IMG {i+1} ({image_names[i]}):\n{prompt}" 
        for i, prompt in enumerate(IMAGE_PROMPTS)
    ])
    update_fields[field_map.get("image_prompt", "Image Prompt")] = prompt_text
    
    try:
        table.update(RECORD_ID, update_fields)
        print(f"  ✅ Record updated with {len([u for u in image_urls if u])} images")
    except Exception as e:
        print(f"  ❌ Update failed: {e}")
    
    print()
    print("=" * 60)
    print("[DONE] V1 - The Lowball images generated")
    print()
    print("Image URLs:")
    for i, url in enumerate(image_urls):
        if url:
            print(f"  IMG {i+1}: {url[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
