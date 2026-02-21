#!/usr/bin/env python3
"""
Generate Video Clip Images for Second Chair TikTok Slide

Settlement Gap V3 - The Fighter
Record ID: recsJClIWKEhaD49G

Theme: FIGHTING BACK and WINNING
Using Nano Banana Pro with Davis's style guide
"""

import os
import fal_client
import requests
from dotenv import load_dotenv
from pathlib import Path

# Load local .env first, then root .env for FAL_KEY
load_dotenv()
root_env = Path(__file__).resolve().parents[4] / ".env"  # claude-creative-work/.env
load_dotenv(root_env)

# Config
AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
FAL_KEY = os.getenv("FAL_KEY")
TABLE_ID = "tblqHvuHyuVwfiDG7"

# Set FAL key
if FAL_KEY:
    os.environ["FAL_KEY"] = FAL_KEY
else:
    raise ValueError("FAL_KEY not found in any .env file")

# Record to update
RECORD_ID = "recsJClIWKEhaD49G"

# 3-Clip TikTok Slide for "Settlement Gap - Fighter"
# Each clip designed for video animation (motion-friendly compositions)
CLIPS = [
    {
        "name": "Clip 1 - Hook (The Lowball)",
        "field": "Clip1_Image",
        "text_overlay": "Insurance offered you HOW MUCH?",
        "prompt": """POV shot looking down at weathered hands holding a CRUMPLED insurance letter,
the letter clearly shows "$3,200" offer amount visible on paper,
person's rough working hands visible gripping the paper with FRUSTRATION,
sitting at messy kitchen table in Nevada home,
bright harsh overhead fluorescent lighting,
shot on older iPhone camera quality like iPhone 8,
authentic candid angry moment, someone just snapped this photo,
off-center framing NOT perfectly composed,
4:5 vertical aspect ratio,
EASTER EGGS visible on table:
overdue bills with red "PAST DUE" stamps scattered around,
prescription medicine bottles,
coffee mug that says "World's Okayest Dad",
car keys with damaged keychain,
the vibe is: this person just opened this insulting offer and is PISSED"""
    },
    {
        "name": "Clip 2 - Action (The Fighter)", 
        "field": "Clip2_Image",
        "text_overlay": "They offered $3,500. She got $175,000.",
        "prompt": """Candid amateur iPhone photo of 42-year-old Nevada woman with ARM IN SLING,
standing PROUD AND DEFIANT in her driveway next to her CRASHED CAR,
the car has visible front-end damage dented hood cracked bumper,
she has weathered face from desert sun with natural imperfections NOT a model,
wearing casual work clothes jeans and faded t-shirt,
FIERCE DETERMINED EXPRESSION like a boxer before a fight,
her good hand is making a fist or pointing defiantly at camera,
her wife or friend took this photo amateur snapshot quality,
bright harsh Nevada afternoon sunlight with hard shadows,
tan stucco Nevada suburb homes visible behind her,
desert gravel landscaping with cacti,
4:5 vertical aspect ratio,
EASTER EGGS in background:
pink flamingo lawn ornament,
nosy neighbor clearly peeking through blinds watching the scene,
garden gnome lying on its side knocked over,
"BEWARE OF DOG" sign but tiny chihuahua visible in window,
funny bumper sticker on neighbor's car,
the vibe is: this woman is about to go to WAR with the insurance company"""
    },
    {
        "name": "Clip 3 - CTA (The Victory)",
        "field": "Clip3_Image", 
        "text_overlay": "Get What You're Owed",
        "prompt": """Candid amateur iPhone photo of 42-year-old Nevada woman CELEBRATING outside a courthouse,
she still has CAST ON HER ARM from the accident,
holding up paperwork TRIUMPHANTLY above her head with her good hand,
HUGE GENUINE VICTORY SMILE beaming with joy,
fist pump energy like she just won the championship,
wearing her nicest casual clothes like she dressed up for court,
her friend just snapped this photo on their phone amateur quality,
bright midday Nevada sunlight,
Las Vegas courthouse or legal building visible behind her,
Spring Mountains visible in the distance,
slight motion blur from celebration movement,
4:5 vertical aspect ratio,
EASTER EGGS in scene:
her beat-up damaged car visible in parking lot behind her,
another person leaving courthouse giving her a thumbs up,
lawyer walking out behind her carrying briefcase,
someone else in background on phone probably calling to share good news,
a "FIGHT FOR YOUR RIGHTS" bumper sticker on a car in lot,
the vibe is: this woman just BEAT the insurance company and is on TOP OF THE WORLD"""
    }
]


def generate_image(prompt: str, name: str) -> str:
    """Generate image using Nano Banana Pro and return URL."""
    print(f"\n🎨 Generating: {name}")
    print(f"   Prompt preview: {prompt[:100]}...")
    
    result = fal_client.subscribe(
        "fal-ai/nano-banana-pro",
        arguments={
            "prompt": prompt.strip(),
            "num_images": 1,
            "aspect_ratio": "4:5",
            "resolution": "1K",
            "output_format": "png"
        }
    )
    
    image_url = result["images"][0]["url"]
    print(f"   ✅ Generated: {image_url[:60]}...")
    return image_url


def update_airtable(record_id: str, field: str, image_url: str):
    """Upload image URL to Airtable attachment field."""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_ID}/{record_id}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_PAT}",
        "Content-Type": "application/json"
    }
    
    data = {
        "fields": {
            field: [{"url": image_url}]
        }
    }
    
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"   ✅ Uploaded to {field}")
    else:
        print(f"   ❌ Failed to upload: {response.text}")


def main():
    print("=" * 60)
    print("Generating TikTok Slide Images for Settlement Gap - Fighter")
    print("=" * 60)
    print(f"Record: {RECORD_ID}")
    print(f"Clips: {len(CLIPS)}")
    
    # Also set Video_Format
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_ID}/{RECORD_ID}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_PAT}",
        "Content-Type": "application/json"
    }
    requests.patch(url, headers=headers, json={"fields": {"Video_Format": "TikTok Slide"}})
    print("\n📹 Set Video_Format to 'TikTok Slide'")
    
    # Generate each clip
    for clip in CLIPS:
        image_url = generate_image(clip["prompt"], clip["name"])
        update_airtable(RECORD_ID, clip["field"], image_url)
        print(f"\n   📝 Text overlay for this clip: \"{clip['text_overlay']}\"")
    
    print("\n" + "=" * 60)
    print("✅ All 3 clip images generated and uploaded!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Review images in Airtable")
    print("2. Tell me which to regenerate (if any)")
    print("3. When approved, I'll animate them to video")


if __name__ == "__main__":
    main()
