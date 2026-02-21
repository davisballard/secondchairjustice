"""
Generate Settlement Gap V2 Images - The System
Record ID: reccmz4eDX2Wni7Pd

Headline: This Is How Insurance Companies Keep More of Your Money

Following IMAGE_STYLE_GUIDE.md with VARIED details
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
    # IMG 1: Infographic - The System Exposed
    """Bold aggressive infographic exposing insurance company tactics,
split frame showing THE SYSTEM vs THE TRUTH,
LEFT SIDE - THE SYSTEM (what insurance wants):
confused worried person holding small check,
insurance adjuster figure looming in shadow,
small pathetic red number "$4,800" with "THEIR OFFER" label,
dark manipulative corporate colors,
RIGHT SIDE - THE TRUTH (what cases settle for):
confident informed person holding large check,
bright victorious green number "$142,000" with "ACTUAL VALUE" label,
empowering bright colors,
crashed car visible connecting both sides,
Nevada desert suburb backdrop with tan stucco homes,
typography is BOLD CHUNKY tabloid headline style,
feels like an EXPOSE revealing a secret,
arrows showing money flowing from left to right,
4:5 vertical aspect ratio,
maximum scroll-stopping urgent energy""",

    # IMG 2: Text Thread - different details than V1
    """Close-up photograph of hand holding iPhone showing iMessage conversation,
phone tilted at casual asymmetrical angle,
shot with older iPhone camera quality slight grain and softer focus,
time "11:11" top left, battery "1%" top right,
contact name "Mike" with visible profile avatar photo of a guy,
dark mode iMessage conversation:
gray bubble: "insurance just called me"
gray bubble: "offered 4800 for the whole thing"
blue bubble: "thats their play. they lowball everyone first"
gray bubble: "what should I do"
blue bubble: "get a lawyer. my cousin got 142k for way less"
gray bubble: "wait seriously??"
Las Vegas casino neon lights visible as REFLECTION on phone glass,
nighttime ambient lighting with warm glow,
authentic candid snapshot someone took outside a casino,
4:5 vertical aspect ratio,
text is LARGE and clearly legible""",

    # IMG 3: Nevada Driver - different person, different Easter eggs
    """Candid amateur iPhone photo of 35-year-old Nevada woman with NECK BRACE,
standing confidently next to her DAMAGED minivan with side panel dent and scratches,
GENUINE PROUD SMILE despite the neck brace, victorious expression,
her husband took this photo on his phone, amateur quality,
wearing casual mom clothes yoga pants and oversized t-shirt,
Las Vegas suburb background Henderson neighborhood,
tan stucco homes with tile roofs,
EASTER EGGS in background: 
someone BBQing in their driveway,
"Beware of Dog" sign but tiny chihuahua visible in window,
delivery package sitting on wrong porch,
kid's plastic basketball hoop knocked over,
natural harsh afternoon Nevada sunlight with hard shadows,
Spring Mountains visible in distance,
authentic snapshot quality with slight blur,
real authentic woman NOT a model,
the damaged minivan clearly visible beside her,
4:5 vertical aspect ratio,
the vibe is: this mom fought the insurance company and WON"""
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
    
    print(f"[*] Generating 3 images for V2 - The System ({RECORD_ID})...")
    print()
    print("  Following IMAGE_STYLE_GUIDE.md with varied details:")
    print("  - IMG 1: Infographic - System vs Truth expose style")
    print("  - IMG 2: Text Thread - Mike, 11:11, 1% battery")
    print("  - IMG 3: Nevada Driver - Woman with neck brace, different Easter eggs")
    print()
    
    image_names = ["Infographic (System Expose)", "Text Thread (Mike)", "Nevada Driver (Mom)"]
    tasks = [generate_image(prompt, fal_key) for prompt in IMAGE_PROMPTS]
    
    print("  [1/3] Generating: System vs Truth infographic...")
    print("  [2/3] Generating: Text Thread with Mike...")
    print("  [3/3] Generating: Nevada Mom with neck brace...")
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
    print("[DONE] V2 - The System images generated")
    print()
    print("Image URLs:")
    for i, url in enumerate(image_urls):
        if url:
            print(f"  IMG {i+1}: {url[:80]}...")


if __name__ == "__main__":
    asyncio.run(main())
