"""
Fix IMG 2 FINAL - The Text Thread
Record ID: reclu6lReElgWVsCF

SPECIFIC REQUIREMENTS:
- Photo of iPhone held in someone's hand
- Vegas Strip lights visible as REFLECTION on phone glass (person is outside on Strip)
- Contact name with avatar at top
- Time: 4:20 on TOP LEFT (correct iOS)
- Battery: 69%
- Same conversation
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

IMAGE_PROMPT = """Photograph of someone's hand holding an iPhone at night outdoors,
the phone screen shows an iMessage text conversation in dark mode,
correct iOS interface: time "4:20" in TOP LEFT corner, battery "69%" on right side,
contact name "Danny" with small circular profile photo avatar at top of conversation,
text message bubbles on screen:
gray incoming bubble: "They offered me $3,200"
gray incoming bubble: "That's it??"
blue outgoing bubble: "Attorney just called. Settlement: $127,000"
gray incoming bubble: "Holy shit"
the person holding the phone is standing OUTSIDE on the Las Vegas Strip at night,
Las Vegas casino lights and neon signs visible as REFLECTIONS on the phone's glass screen,
subtle bokeh city lights reflected in the glossy phone display,
the reflection shows the photographer is on the Strip taking this pic,
realistic nighttime lighting with ambient neon glow,
authentic candid photo someone snapped of their friend's phone outside,
phone held at slight angle,
4:5 vertical aspect ratio,
the vibe is: friend just showed me his settlement text while we were out in Vegas"""


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
    
    print(f"[*] FINAL FIX IMG 2 for record {RECORD_ID}...")
    print()
    print("  Requirements:")
    print("  - Vegas lights as REFLECTION on phone glass (outside on Strip)")
    print("  - Contact 'Danny' with avatar visible")
    print("  - Time: 4:20 (top left)")
    print("  - Battery: 69%")
    print("  - Hand holding phone at night")
    print()
    
    print("  Generating: Text Thread (Vegas reflection)...")
    
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
    print("[DONE] IMG 2 FINAL - Vegas reflection style")
    print()
    print(f"  URL: {image_url}")


if __name__ == "__main__":
    asyncio.run(main())
