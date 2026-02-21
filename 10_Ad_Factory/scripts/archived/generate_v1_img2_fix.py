"""
Fix IMG 2 Only - The Text Thread
Record ID: reclu6lReElgWVsCF

Make it a PHOTO OF the phone (at angle, phone edges visible)
Las Vegas lights in background wallpaper
NO contact avatar - just "iMessage" at top
Same conversation flow
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

# IMG 2 ONLY - photo of phone at angle
IMAGE_PROMPT = """Photograph of an iPhone being held at a slight angle,
physical phone edges and frame visible,
the phone screen shows an iMessage conversation in dark mode,
screen displays "iMessage" text at top with NO contact name or avatar,
status bar shows time and battery percentage,
text message bubbles on screen:
gray bubble: "They offered me $3,200"
gray bubble: "That's it??"
blue bubble: "Attorney just called. Settlement: $127,000"
gray bubble: "Holy shit"
phone wallpaper visible behind messages showing Las Vegas Strip city lights at night,
bokeh city lights visible through the translucent message background,
photo taken at slight angle like someone snapped a pic of their friend's phone,
realistic photograph OF a phone NOT a screenshot,
slight reflection and glare on phone screen,
dark ambient lighting environment,
authentic candid photo quality,
4:5 vertical aspect ratio"""


async def generate_image(prompt: str, fal_key: str) -> str:
    """Generate a single image using Fal.ai at 4:5 ratio."""
    os.environ["FAL_KEY"] = fal_key
    
    handler = await fal_client.submit_async(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": prompt,
            "num_images": 1,
            "aspect_ratio": "4:5",
            "resolution": "1K",
            "output_format": "png",
        }
    )
    
    result = await handler.get()
    
    if result and "images" in result and len(result["images"]) > 0:
        return result["images"][0]["url"]
    
    raise ValueError(f"No image returned")


async def main():
    print("[*] Loading Second Chair configuration...")
    config = load_brand_config("Lead_Faucet")
    
    fal_key = config["credentials"]["fal_key"]
    creds = config["credentials"]
    tables = config["airtable"]
    field_map = config.get("field_mapping", {})
    
    print(f"[*] Fixing IMG 2 only for record {RECORD_ID}...")
    print()
    print("  Changes:")
    print("  - Photo OF the phone at angle (not screenshot)")
    print("  - Phone edges/frame visible")
    print("  - Vegas lights in wallpaper background")
    print("  - No contact avatar - just 'iMessage' at top")
    print()
    
    print("  Generating: Text Thread (photo of phone)...")
    
    try:
        image_url = await generate_image(IMAGE_PROMPT, fal_key)
        print(f"  ✅ Generated successfully")
    except Exception as e:
        print(f"  ❌ Failed: {e}")
        return
    
    print()
    print(f"[*] Updating IMG 2 in Airtable record {RECORD_ID}...")
    
    api = Api(creds["airtable_pat"])
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    update_fields = {
        field_map.get("img_2", "IMG 2"): [{"url": image_url}]
    }
    
    try:
        table.update(RECORD_ID, update_fields)
        print(f"  ✅ IMG 2 updated")
    except Exception as e:
        print(f"  ❌ Update failed: {e}")
    
    print()
    print("=" * 60)
    print("[DONE] IMG 2 fixed - photo of phone style")
    print()
    print(f"  URL: {image_url}")


if __name__ == "__main__":
    asyncio.run(main())
