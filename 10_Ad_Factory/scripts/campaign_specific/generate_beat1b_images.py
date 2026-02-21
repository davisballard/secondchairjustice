"""
Generate Beat 1B: Post-Crash Aftermath Images
Using Maria reference image for character consistency
Luca Maxim cinematic style
"""

import asyncio
import os

try:
    import fal_client
except ImportError:
    print("ERROR: fal_client not installed")
    exit(1)

# Maria reference image
MARIA_REFERENCE = "/Users/davisballard/.cursor/projects/Users-davisballard-Documents-claude-creative-work/assets/hf_20260202_073226_b0b8cda9-8699-441c-bd2d-43ab4dbd821b__1_-fcdae2f2-baab-4031-9133-8995ce91776c.png"

# Luca Maxim style lock
STYLE_LOCK = """cinematic color grading, desaturated with lifted blacks, 
subtle film grain, shallow depth of field, motivated natural lighting, 
hyperrealistic detail, Roger Deakins atmospheric quality, 9:16 vertical format,
movie-trailer production value"""

# Post-crash prompts - 2 options
PROMPTS = {
    "option_1_exterior": {
        "name": "Option 1: Exterior - Maria Standing by Damaged Car",
        "prompt": f"""The same Latina woman from the reference image, now standing outside 
her damaged 2015 silver Honda Accord after a rear-end collision. She stands beside 
the driver door, one hand on her neck feeling whiplash, dazed expression of shock 
transitioning to concern. Same grey hoodie over light blue medical scrubs, same 
messy ponytail with pieces falling out, same small gold cross necklace.

Rear-end damage visible on bumper and trunk. Child's booster seat clearly visible 
through the rear window — the family this could have destroyed. Airbag deployed 
visible through driver window. Rosary beads hanging from rearview mirror.

Aurora Colorado suburban intersection, harsh overcast winter light, grey sky, 
strip mall in distance, bare trees. The mundane made tragic.

{STYLE_LOCK}""",
    },
    
    "option_2_interior": {
        "name": "Option 2: Interior - Maria in Car After Impact",
        "prompt": f"""The same Latina woman from the reference image, now sitting in her 
car immediately after being rear-ended. Airbag has deployed in front of her, 
she grips the steering wheel with white knuckles, expression of shock and 
disbelief. Same grey hoodie over light blue medical scrubs, same messy ponytail, 
same gold cross necklace now askew.

Through the cracked rear window, child's booster seat visible — reminder of 
what could have been lost. Rosary beads swinging from the impact. Dashboard 
lights glowing. Harsh light flooding from behind — the other car's headlights.

The moment of processing. Not crying, not screaming — stunned silence.

{STYLE_LOCK}""",
    },
}


def generate_image(prompt: str, reference_image_path: str = None) -> str:
    """Generate image using Nano Banana Pro."""
    
    arguments = {
        "prompt": prompt,
        "aspect_ratio": "9:16",
        "resolution": "2K",
        "output_format": "png",
    }
    
    # Add reference image if provided
    if reference_image_path and os.path.exists(reference_image_path):
        # Upload image first
        print(f"   Uploading reference image...")
        image_url = fal_client.upload_file(reference_image_path)
        arguments["image_url"] = image_url
        arguments["image_strength"] = 0.35  # Keep character, change scene
        print(f"   Reference uploaded: {image_url[:60]}...")
    
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro",
        arguments=arguments
    )
    
    # Extract image URL
    if result and "images" in result and len(result["images"]) > 0:
        return result["images"][0]["url"]
    
    raise ValueError(f"No image in response: {result}")


def main():
    print("\n" + "#"*60)
    print("# BEAT 1B: POST-CRASH AFTERMATH")
    print("# Luca Maxim Cinematic Style")
    print("#"*60)
    
    results = {}
    
    for key, config in PROMPTS.items():
        print(f"\n{'='*60}")
        print(f"Generating: {config['name']}")
        print(f"{'='*60}")
        print(f"Prompt: {config['prompt'][:100]}...")
        
        try:
            image_url = generate_image(
                prompt=config["prompt"],
                reference_image_path=MARIA_REFERENCE,
            )
            print(f"\n✅ Generated: {image_url}")
            results[key] = {
                "name": config["name"],
                "url": image_url,
            }
        except Exception as e:
            print(f"\n❌ Failed: {e}")
            results[key] = {
                "name": config["name"],
                "url": None,
                "error": str(e),
            }
    
    # Summary
    print("\n" + "="*60)
    print("📋 RESULTS")
    print("="*60)
    
    for key, result in results.items():
        status = "✅" if result.get("url") else "❌"
        print(f"\n{status} {result['name']}")
        if result.get("url"):
            print(f"   {result['url']}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
