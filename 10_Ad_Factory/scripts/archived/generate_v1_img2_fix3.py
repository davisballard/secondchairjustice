"""
Fix IMG 2 - ZOOMED IN, older phone camera quality
Record ID: reclu6lReElgWVsCF

CHANGES:
- ZOOM IN more so text is legible on feed
- Less symmetrical, more casual angle
- Shot on OLDER iPhone camera (not DSLR, not hyper-real)
- Text must be clearly readable
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

IMAGE_PROMPT = """Close-up photograph of someone holding an iPhone showing iMessage conversation,
ZOOMED IN tight on the phone screen so text messages are LARGE and clearly legible,
phone tilted at casual asymmetrical angle not perfectly straight,
photo taken with an OLDER iPhone camera like iPhone 8 or iPhone X quality,
slight grain and softer focus typical of older smartphone cameras,
NOT DSLR quality NOT hyper-real, authentic older phone camera aesthetic,
the phone screen shows dark mode iMessage conversation:
correct iOS interface with time "4:20" top left and battery "69%" top right,
contact name "Danny" with small profile avatar photo visible at top,
LARGE readable text message bubbles:
gray bubble: "They offered me $3,200"
gray bubble: "That's it??"
blue bubble: "Attorney just called. Settlement: $127,000"  
gray bubble: "Holy shit"
text is SHARP and LEGIBLE even when viewing small,
Las Vegas neon lights visible as subtle reflection on phone glass,
nighttime ambient lighting with warm casino glow,
hand holding phone casually not posed,
the vibe is: my buddy just showed me this outside the casino and I snapped a pic,
4:5 vertical aspect ratio,
frame filled mostly with phone screen for maximum text readability"""


async def generate_image(prompt: str, fal_key: str) -> str:
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
    
    print(f"[*] Zoomed in + older phone camera fix for {RECORD_ID}...")
    print()
    print("  Changes:")
    print("  - ZOOMED IN for text legibility")
    print("  - Less symmetrical, casual angle")
    print("  - Older iPhone camera quality (not DSLR)")
    print("  - Text must be clearly readable")
    print()
    
    print("  Generating: Text Thread (zoomed, older phone)...")
    
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
    print("[DONE] IMG 2 - zoomed + older phone camera")
    print()
    print(f"  URL: {image_url}")


if __name__ == "__main__":
    asyncio.run(main())
