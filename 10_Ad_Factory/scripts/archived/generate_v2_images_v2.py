"""
Generate Settlement Gap V2 Images - The System (REVISED)
Record ID: reccmz4eDX2Wni7Pd

THIS IS ABOUT THE 48-HOUR CALL TACTIC - NOT SETTLEMENT GAP NUMBERS

Headline: This Is How Insurance Companies Keep More of Your Money
Theme: Insurance calls within 48 hours with a lowball ready

COMPLETELY DIFFERENT approaches from V1
"""

import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "08_Ad_Factory"))

from config_loader import load_brand_config
from pyairtable import Api
import fal_client

RECORD_ID = "reccmz4eDX2Wni7Pd"

IMAGE_PROMPTS = [
    # IMG 1: Infographic - THE 48-HOUR CLOCK / TIMELINE
    """Bold aggressive infographic about insurance company 48-hour call tactic,
NOT about settlement numbers - about THE SYSTEM and TIMING,
large dramatic clock or stopwatch showing "48 HOURS" prominently,
timeline visual showing:
HOUR 0: "Your Accident" with car crash icon
HOUR 24: "Adjuster Assigned" with corporate figure
HOUR 48: "LOWBALL CALL" with phone ringing icon and dollar sign
below the timeline: "They're trained to call BEFORE you know what your case is worth"
urgent warning colors: red, orange, yellow hazard stripes,
feels like an EXPOSE or WARNING infographic,
Nevada desert tones in background,
typography is BOLD AGGRESSIVE tabloid style,
the vibe is: THIS IS THEIR PLAYBOOK and now you know,
4:5 vertical aspect ratio,
maximum scroll-stopping urgent energy""",

    # IMG 2: Screenshot - INCOMING CALL FROM INSURANCE
    """Close-up photograph of hand holding iPhone showing INCOMING CALL screen,
phone tilted at casual angle,
shot with older iPhone camera quality,
the screen shows incoming call interface:
caller ID showing "State Farm Claims" or "Insurance Adjuster" with generic icon,
green ACCEPT and red DECLINE buttons visible,
the call has been ringing, shows "incoming call" animation,
timestamp visible showing call coming in at weird hour like "7:47 AM",
the person is clearly hesitant about answering,
dim morning lighting like they just woke up,
coffee cup or bedside table visible in background,
Las Vegas apartment window with morning desert light,
authentic photo someone took of their phone buzzing,
4:5 vertical aspect ratio,
the vibe is: they called at 7am two days after my accident""",

    # IMG 3: Person - KITCHEN TABLE AMBUSH (paperwork moment)
    """Candid amateur iPhone photo of 42-year-old Nevada man sitting at kitchen table,
he looks OVERWHELMED and STRESSED surrounded by paperwork,
medical bills, insurance forms, and envelopes scattered on table,
he's on the phone with insurance company, hand on forehead stressed,
wearing casual home clothes sweatpants and t-shirt,
the kitchen is a typical Nevada home: tan walls, basic decor,
morning light through window showing desert landscaping outside,
EASTER EGGS in scene:
a kid's cereal bowl left on counter,
a dog watching from the doorway looking concerned,
a calendar on the wall with the accident date circled,
an unpaid bill with "FINAL NOTICE" visible,
coffee getting cold next to him,
authentic amateur snapshot quality his wife took,
real person NOT a model, tired frustrated expression,
Spring Mountains visible through kitchen window,
4:5 vertical aspect ratio,
the vibe is: insurance called and now he's drowning in their paperwork game"""
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
    
    print(f"[*] REVISED V2 - The System ({RECORD_ID})...")
    print()
    print("  COMPLETELY DIFFERENT approaches (48-hour call theme):")
    print("  - IMG 1: 48-Hour Clock/Timeline infographic")
    print("  - IMG 2: Incoming call from 'Insurance Adjuster' on phone")
    print("  - IMG 3: Stressed guy at kitchen table with paperwork")
    print()
    
    image_names = ["48-Hour Timeline", "Incoming Insurance Call", "Kitchen Table Ambush"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/3] Generating: 48-Hour Timeline infographic...")
    print("  [2/3] Generating: Incoming call screenshot...")
    print("  [3/3] Generating: Kitchen table paperwork scene...")
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
    
    img_fields = [
        field_map.get("img_1", "IMG"),
        field_map.get("img_2", "IMG 2"),
        field_map.get("img_3", "IMG 3"),
    ]
    
    update_fields = {}
    for i, url in enumerate(image_urls):
        if url and i < len(img_fields):
            update_fields[img_fields[i]] = [{"url": url}]
    
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
    print("[DONE] V2 - The System REVISED images generated")
    print()
    print("Image URLs:")
    for i, url in enumerate(image_urls):
        if url:
            print(f"  IMG {i+1}: {url[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
