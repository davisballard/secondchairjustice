"""
Fix IMG 1 and IMG 3 for V1 - The Lowball
Record ID: reclu6lReElgWVsCF

IMG 1: Keep urgency, add auto accident tie-in, left=bad right=good faces
IMG 3: Keep guy, add ridiculous Easter eggs in background for scroll-stop
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

IMAGE_PROMPTS = [
    # IMG 1: Vegas Math - AUTO ACCIDENT focused, emotional faces
    """Bold dramatic split-frame infographic about car accident insurance settlement,
URGENT flashy scroll-stopping design,
LEFT SIDE shows the BAD outcome:
small defeated red number "$2,500" with "INSURANCE OFFERED",
sad frustrated person's face looking down or upset,
crashed damaged car visible behind them,
muted dark depressing colors,
RIGHT SIDE shows the GOOD outcome:
MASSIVE triumphant green number "$127,500" with "CASE SETTLED FOR",
happy relieved person celebrating or smiling,
same car now fixed or person walking away victorious,
bright energetic winning colors,
thick dramatic arrow connecting the two sides,
clearly about AUTO ACCIDENTS and car crash settlements,
Nevada desert suburban backdrop visible,
typography is BOLD CHUNKY and AGGRESSIVE,
feels URGENT like breaking news,
the contrast between sad and happy outcomes is dramatic,
4:5 vertical aspect ratio,
maximum scroll-stopping visual impact""",

    # IMG 3: Nevada Driver - Easter eggs in background
    """Candid amateur iPhone photo of 40-year-old Nevada man with ARM IN SLING,
standing proudly next to his CRASHED CAR with visible front-end damage,
BIG GENUINE SMILE despite the injury, victorious expression,
his wife took this photo on her phone, NOT professional quality,
casual clothes jeans and t-shirt,
Las Vegas suburb background with tan stucco homes,
RIDICULOUS EASTER EGGS hidden in the background that make people stop:
a cactus wearing sunglasses in someone's yard,
a pink flamingo lawn ornament,
a bumper sticker on a car that says something funny,
a cat sitting on a fence watching,
a neighbor peeking through their blinds being nosy,
a kid's bike left randomly in a driveway,
an inflatable pool flamingo deflated on the ground,
subtle absurd details that reward people who look closely,
natural harsh afternoon Nevada sunlight,
Spring Mountains visible in distance,
authentic amateur snapshot quality with slight blur,
real person NOT a model,
the crashed car damage clearly visible,
4:5 vertical aspect ratio filling entire frame,
the vibe is: this guy WON and his whole neighborhood knows it"""
]


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
    
    print(f"[*] Fixing IMG 1 and IMG 3 for record {RECORD_ID}...")
    print()
    print("  IMG 1 Changes:")
    print("  - Tied to AUTO ACCIDENTS more clearly")
    print("  - Left=sad face/bad outcome, Right=happy face/good outcome")
    print("  - Keep urgency and flashiness")
    print()
    print("  IMG 3 Changes:")
    print("  - Keep the guy with sling")
    print("  - Add ridiculous Easter eggs in background")
    print()
    
    image_names = ["Vegas Math (Auto Accident)", "Nevada Driver (Easter Eggs)"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/2] Generating: Vegas Math with faces...")
    print("  [2/2] Generating: Nevada Driver with Easter eggs...")
    print()
    print("  (Running in parallel...)")
    print()
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    image_urls = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"  ❌ {image_names[i]} failed: {result}")
            image_urls.append(None)
        else:
            print(f"  ✅ {image_names[i]} generated")
            image_urls.append(result)
    
    print()
    print(f"[*] Updating Airtable record {RECORD_ID}...")
    
    api = Api(creds["airtable_pat"])
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    update_fields = {}
    
    # IMG 1
    if image_urls[0]:
        update_fields[field_map.get("img_1", "IMG")] = [{"url": image_urls[0]}]
    
    # IMG 3
    if image_urls[1]:
        update_fields[field_map.get("img_3", "IMG 3")] = [{"url": image_urls[1]}]
    
    try:
        table.update(RECORD_ID, update_fields)
        print(f"  ✅ IMG 1 and IMG 3 updated")
    except Exception as e:
        print(f"  ❌ Update failed: {e}")
    
    print()
    print("=" * 60)
    print("[DONE] IMG 1 and IMG 3 fixed")
    print()
    print("Image URLs:")
    if image_urls[0]:
        print(f"  IMG 1: {image_urls[0][:80]}...")
    if image_urls[1]:
        print(f"  IMG 3: {image_urls[1][:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
