"""
Generate Settlement Gap V3 Images - The Fighter
Record ID: recsJClIWKEhaD49G

Headline: They Offered Low. Someone Fought Back. Look What Happened.
Theme: THE FIGHT / David vs Goliath / Fighting Back and WINNING

IMAGES MATCH THE SPECIFIC ANGLE: Fighting back against insurance
"""

import asyncio
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "08_Ad_Factory"))

from config_loader import load_brand_config
from pyairtable import Api
import fal_client

RECORD_ID = "recsJClIWKEhaD49G"

IMAGE_PROMPTS = [
    # IMG 1: Infographic - DAVID VS GOLIATH / THE FIGHT
    """Bold aggressive infographic about fighting back against insurance,
visual metaphor of DAVID VS GOLIATH battle,
LEFT SIDE: massive intimidating corporate insurance building or suited figures,
dark threatening corporate colors, army of lawyers,
text: "THEIR TEAM" with imposing imagery,
RIGHT SIDE: single determined Nevada person standing strong,
bright empowering colors, confident stance,
text: "YOUR FIGHTER" with powerful imagery,
VS symbol or lightning bolt dividing them,
the small fighter is clearly WINNING despite the odds,
boxing or battle energy without being literal,
Nevada desert tones in background,
typography is BOLD AGGRESSIVE championship fight poster style,
feels like a MATCHUP announcement,
4:5 vertical aspect ratio,
the vibe is: they have an army but you have a fighter""",

    # IMG 2: Screenshot - THE VICTORY TEXT
    """Close-up photograph of hand holding iPhone showing iMessage conversation,
phone tilted at casual angle,
shot with older iPhone camera quality,
time "3:33" top left, battery "100%" top right,
contact name "Carlos" with visible profile avatar,
dark mode iMessage conversation showing VICTORY moment:
gray bubble: "BRO"
gray bubble: "THEY CAVED"
gray bubble: "after months of fighting they finally settled"
blue bubble: "HOW MUCH"
gray bubble: "138k"
gray bubble: "they only offered 4200 at first"
blue bubble: "LETS GOOOO"
blue bubble: "told you to fight it"
Las Vegas Strip lights visible as REFLECTION on phone glass,
nighttime celebratory energy,
authentic candid snapshot quality,
4:5 vertical aspect ratio,
the vibe is: my friend just won his fight against insurance""",

    # IMG 3: Person - THE VICTORY MOMENT
    """Candid amateur iPhone photo of 38-year-old Nevada man CELEBRATING outside courthouse,
he has a CAST ON HIS WRIST from the accident,
holding up paperwork triumphantly with his good hand,
HUGE GENUINE VICTORY SMILE, fist pump energy,
his wife or friend took this photo, amateur quality,
wearing his best casual clothes like he dressed up for court,
Las Vegas courthouse or legal building visible in background,
bright midday Nevada sunlight,
EASTER EGGS in scene:
his beat-up car visible in parking lot behind him with damage,
a "FIGHT FOR YOUR RIGHTS" bumper sticker on a nearby car,
someone else leaving the courthouse giving him a thumbs up,
a lawyer walking out behind him carrying a briefcase,
Spring Mountains visible in the distance,
authentic snapshot quality with slight motion blur from celebration,
real person NOT a model, genuine joy on face,
4:5 vertical aspect ratio,
the vibe is: this guy just beat the insurance company and is on top of the world"""
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
    
    print(f"[*] V3 - The Fighter ({RECORD_ID})...")
    print()
    print("  Theme: FIGHTING BACK and WINNING")
    print("  - IMG 1: David vs Goliath infographic")
    print("  - IMG 2: Victory text thread (Carlos, 3:33, 100%)")
    print("  - IMG 3: Guy celebrating outside courthouse with cast")
    print()
    
    image_names = ["David vs Goliath", "Victory Text (Carlos)", "Courthouse Celebration"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/3] Generating: David vs Goliath infographic...")
    print("  [2/3] Generating: Victory text thread...")
    print("  [3/3] Generating: Courthouse celebration...")
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
    
    update_fields[field_map.get("aspect_ratio_field", "Aspect Ratio")] = "4:5"
    
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
    print("[DONE] V3 - The Fighter images generated")
    print()
    print("Image URLs:")
    for i, url in enumerate(image_urls):
        if url:
            print(f"  IMG {i+1}: {url[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
