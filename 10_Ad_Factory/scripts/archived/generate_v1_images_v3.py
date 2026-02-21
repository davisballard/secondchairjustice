"""
Generate Settlement Gap V1 Images - The Lowball (V3 - Final Push)
Record ID: reclu6lReElgWVsCF

CHANGES FROM V2:
- IMG 1: LOUDER, more aggressive, maximum scroll-stop
- IMG 2: Danny's face visible, 4:20 time, 69% battery, more messages, no dead space
- IMG 3: ARM SLING injury, wife took this on iPhone, NOT professional, no white border
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

# Three distinct prompts — PUSHED HARDER
IMAGE_PROMPTS = [
    # IMG 1: Vegas Math — LOUDER, more scroll-stopping
    """BOLD aggressive infographic showing massive insurance settlement gap,
LOUD high contrast design that DEMANDS attention,
split frame with DRAMATIC tension between the two numbers,
left side: small crushed defeated red number "$2,500" with "INSURANCE OFFERED" in harsh blocky text,
right side: MASSIVE dominant electric neon green number "$127,500" with "CASE SETTLED FOR" in bold,
THICK aggressive arrow slashing across connecting them,
colors are SATURATED and PUNCHY not muted,
background: Nevada desert landscape with Spring Mountains,
tan stucco Las Vegas suburb homes, gravel desert yards,
Red Rock Canyon red tones visible on horizon,
harsh bright desert sunlight, clear deep blue Nevada sky,
typography is CHUNKY and AGGRESSIVE like a tabloid headline,
feels URGENT and IMPORTANT,
4:5 vertical aspect ratio,
the vibe is: THIS IS OUTRAGEOUS and you need to see this NOW""",

    # IMG 2: Text Thread — Danny visible, 4:20, 69%, more messages
    """Ultra realistic iPhone screenshot of active iMessage conversation in dark mode,
4:5 vertical aspect ratio filling the frame completely,
authentic iOS 17 interface at top: time showing "4:20" and battery at "69%",
contact name "Danny" with visible profile photo showing young man's face NOT blurred,
ACTIVE busy text thread with multiple messages showing they talk often:
gray bubble: "dude you're not gonna believe this"
gray bubble: "They offered me $3,200 for the whole thing"  
blue bubble: "wait what"
blue bubble: "that's insane"
gray bubble: "I know right"
gray bubble: "anyway attorney just called"
gray bubble: "Settled for $127,000"
blue bubble: "HOLY SHIT"
blue bubble: "WHO DID YOU USE"
messages fill the screen naturally with no dead space at bottom,
realistic iMessage bubble styling with proper spacing,
authentic screenshot quality with subtle screen texture,
looks exactly like a real screenshot someone just took to share,
cropped tight like grabbed quickly off the phone""",

    # IMG 3: Nevada Driver — ARM SLING, wife took this on iPhone, authentic
    """Candid amateur iPhone photo of 38-year-old working-class Nevada man,
he has his LEFT ARM IN A SLING from the accident,
standing proudly next to his DAMAGED crashed car with dented hood and cracked bumper,
BIG GENUINE SMILE on his face despite the injury, victorious expression,
his wife just took this photo of him on her iPhone, NOT professional at all,
slightly off-center framing like a quick snapshot,
authentic amateur photography quality with slight motion blur,
natural harsh afternoon sunlight with hard shadows,
Las Vegas suburb background: tan stucco homes, gravel desert landscaping,
Spring Mountains visible in distance under bright Nevada sky,
he's wearing casual clothes jeans and a t-shirt,
real authentic person NOT a model, weathered desert sun face,
the crashed car damage is clearly visible beside him,
NO white border NO professional composition,
shot looks like it was just posted to Facebook by his wife,
the vibe is: this guy got hurt, fought back, WON, and is PROUD,
4:5 vertical aspect ratio filling entire frame edge to edge"""
]


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
    
    raise ValueError(f"No image returned for prompt: {prompt[:50]}...")


async def main():
    print("[*] Loading Second Chair configuration...")
    config = load_brand_config("Lead_Faucet")
    
    fal_key = config["credentials"]["fal_key"]
    creds = config["credentials"]
    tables = config["airtable"]
    field_map = config.get("field_mapping", {})
    
    print(f"[*] V3 FINAL PUSH - Regenerating for record {RECORD_ID}...")
    print()
    print("  Changes:")
    print("  - IMG 1: LOUDER, more aggressive, maximum scroll-stop power")
    print("  - IMG 2: Danny's face visible, 4:20 time, 69% battery, busy thread")
    print("  - IMG 3: ARM SLING, wife took this on iPhone, authentic amateur")
    print()
    
    image_names = ["Vegas Math (LOUD)", "Text Thread (4:20/69%)", "Nevada Driver (Sling)"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/3] Generating: Vegas Math (LOUDER)...")
    print("  [2/3] Generating: Text Thread (Danny visible, 4:20, 69%)...")
    print("  [3/3] Generating: Nevada Driver (arm sling, wife's iPhone)...")
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
    print("[DONE] V1 - The Lowball V3 FINAL images generated")
    print()
    print("Image URLs:")
    for i, url in enumerate(image_urls):
        if url:
            print(f"  IMG {i+1}: {url[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
