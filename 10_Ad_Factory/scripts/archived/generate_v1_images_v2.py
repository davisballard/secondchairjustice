"""
Generate Settlement Gap V1 Images - The Lowball (V2 - Improved)
Record ID: reclu6lReElgWVsCF

CHANGES FROM V1:
- Aspect ratio: 4:5 (optimal for Meta feed)
- IMG 1: More distinctly Nevada, less California, no phone aesthetic
- IMG 2: Real contact name instead of whited out
- IMG 3: PUSH IT - show crashed/damaged vehicle (Nevada allows)
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

# Three distinct prompts for IMG, IMG 2, IMG 3 — all at 4:5
IMAGE_PROMPTS = [
    # IMG 1: Vegas Math — distinctly Nevada, not California
    """Bold infographic design showing insurance settlement gap,
split frame composition with dramatic contrast,
left side: small dim muted red number "$2,500" with "INSURANCE OFFERED" label,
right side: large bold electric green number "$127,500" with "CASE SETTLED FOR" label,
thick bold arrow connecting the two numbers,
background showing distinctly NEVADA Las Vegas suburb landscape:
tan and beige stucco homes, desert rocky landscaping with gravel yards,
Spring Mountains visible in distance with desert haze,
Red Rock Canyon red and brown tones on horizon,
NO lush palm trees or green grass, arid desert aesthetic,
clear blue Nevada sky, afternoon harsh desert sunlight,
high contrast bold sans-serif typography,
clean graphic design style, editorial quality,
4:5 vertical aspect ratio optimized for mobile feed""",

    # IMG 2: Text Thread — with real contact name
    """Realistic iPhone screenshot of iMessage text conversation in dark mode,
4:5 vertical aspect ratio,
authentic iOS 17 interface with battery percentage signal bars and time visible,
contact name at top showing "Danny" with small profile photo circle,
text message conversation bubbles:
gray incoming bubble: "They offered me $3,200 for the whole thing"
gray incoming bubble: "That's it?? After all that?"
blue outgoing bubble: "Attorney just called. Settled for $127,000"
gray incoming bubble: "Holy shit dude"
gray incoming bubble: "Who did you use"
realistic iMessage styling with proper bubble shapes and spacing,
subtle screen glare and reflection,
cropped casually like quickly screenshotted to share,
authentic smartphone capture quality NOT a mockup,
slight finger shadow visible at edge like holding phone""",

    # IMG 3: Nevada Driver with CRASHED VEHICLE — push it
    """Documentary photograph of 40-year-old working-class Nevada man,
standing next to his DAMAGED crashed car in Las Vegas suburb,
car has visible front-end damage: dented hood, cracked bumper, broken headlight,
man has confident knowing expression, arms crossed, NOT sad or distressed,
wearing casual work clothes jeans and t-shirt,
authentic real person NOT a model, natural weathered face from desert sun,
Las Vegas suburb background: tan stucco homes, gravel desert landscaping,
Spring Mountains visible in distance under clear Nevada sky,
late afternoon golden hour lighting,
shot on 35mm documentary journalism style,
shallow depth of field with damaged car in sharp focus,
empty space in upper portion of frame for text overlay,
4:5 vertical aspect ratio,
the vibe is: this guy fought back and WON, standing proud next to the evidence"""
]


async def generate_image(prompt: str, fal_key: str) -> str:
    """Generate a single image using Fal.ai at 4:5 ratio."""
    os.environ["FAL_KEY"] = fal_key
    
    handler = await fal_client.submit_async(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": prompt,
            "num_images": 1,
            "aspect_ratio": "4:5",  # Optimal for Meta feed
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
    
    print(f"[*] Regenerating 3 images at 4:5 for record {RECORD_ID}...")
    print()
    print("  Changes:")
    print("  - Aspect ratio: 4:5 (optimal for Meta feed)")
    print("  - IMG 1: More distinctly Nevada/desert, less California")
    print("  - IMG 2: Contact name 'Danny' instead of whited out")
    print("  - IMG 3: PUSHED - crashed/damaged vehicle visible")
    print()
    
    # Generate all 3 images in parallel
    image_names = ["Vegas Math (Nevada)", "Text Thread (Danny)", "Nevada Driver (Crashed Car)"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/3] Generating: Vegas Math (distinctly Nevada)...")
    print("  [2/3] Generating: Text Thread (with contact name)...")
    print("  [3/3] Generating: Nevada Driver (with crashed car)...")
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
    
    # Update aspect ratio field
    update_fields[field_map.get("aspect_ratio_field", "Aspect Ratio")] = "4:5"
    
    # Also store the prompts for reference
    prompt_text = "\n\n---\n\n".join([
        f"IMG {i+1} ({image_names[i]}):\n{prompt}" 
        for i, prompt in enumerate(IMAGE_PROMPTS)
    ])
    update_fields[field_map.get("image_prompt", "Image Prompt")] = prompt_text
    
    try:
        table.update(RECORD_ID, update_fields)
        print(f"  ✅ Record updated with {len([u for u in image_urls if u])} images at 4:5")
    except Exception as e:
        print(f"  ❌ Update failed: {e}")
    
    print()
    print("=" * 60)
    print("[DONE] V1 - The Lowball images regenerated at 4:5")
    print()
    print("Image URLs:")
    for i, url in enumerate(image_urls):
        if url:
            print(f"  IMG {i+1}: {url[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
