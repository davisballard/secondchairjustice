#!/usr/bin/env python3
"""
Infographic Animation Pipeline

Takes a still infographic image and animates:
- Graphic elements and background only (text stays static)
- Adds dramatic background music
- Outputs 5-second video to Airtable final_video field

Usage:
    python animate_infographic.py --record reccmz4eDX2Wni7Pd --script "don't let them control the clock, know your rights"
"""

import argparse
import asyncio
import os
import sys
import tempfile
from pathlib import Path

import fal_client
import httpx
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
root_env = Path(__file__).resolve().parents[4] / ".env"
load_dotenv(root_env)

# Add parent directory for imports
# parents[0] = 10_Ad_Factory, [1] = Lead_Faucet, [2] = 06_Brands, [3] = Agency_Simulation_Root
ad_factory_path = Path(__file__).resolve().parents[3] / "08_Ad_Factory"
sys.path.insert(0, str(ad_factory_path))

from audio_models.stable_audio import generate_music
from audio_models.mixer import add_audio_to_video, download_audio_sync

# Config
AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
FAL_KEY = os.getenv("FAL_KEY")
TABLE_ID = "tblqHvuHyuVwfiDG7"  # Image Ads table

if FAL_KEY:
    os.environ["FAL_KEY"] = FAL_KEY
else:
    raise ValueError("FAL_KEY not found in environment")


def fetch_record(record_id: str) -> dict:
    """Fetch a record from Airtable."""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_ID}/{record_id}"
    headers = {"Authorization": f"Bearer {AIRTABLE_PAT}"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["fields"]


def get_image_url(fields: dict) -> str:
    """Extract the main image URL from record fields (IMG field)."""
    img_attachments = fields.get("IMG", [])
    if not img_attachments:
        raise ValueError("No image found in IMG field")
    return img_attachments[0]["url"]


async def animate_infographic(
    image_url: str,
    duration: str = "10",
) -> str:
    """
    Animate an infographic image - BACKGROUND ONLY, TEXT STAYS STATIC.
    
    Rules:
    - 10 seconds, loop-friendly
    - ONLY background elements animate (particles, gradients, ambient glow)
    - Text remains 100% static and sharp - NO text movement or warping
    - NO zoom, NO camera movement, locked frame composition
    - "Living poster" aesthetic - subtle but mesmerizing
    
    Uses Kling Pro exclusively.
    """
    # BACKGROUND-ONLY animation prompt - text stays frozen, background lives
    motion_prompt = """Subtle animated background ONLY,
    floating dust particles drifting slowly in the background,
    gentle ambient light shifts and soft gradient transitions,
    slight atmospheric haze movement behind the static elements,
    soft pulsing glow on background graphic elements only,
    ALL TEXT AND FOREGROUND ELEMENTS REMAIN COMPLETELY FROZEN AND STATIC,
    absolutely NO camera movement NO zoom NO pan,
    locked static frame composition throughout,
    seamless loop-friendly animation that returns to start position,
    living poster aesthetic like a high-end animated wallpaper,
    the text is sharp and frozen like a print ad,
    only the atmospheric background has gentle life and motion,
    professional subtle ambient animation"""
    
    print(f"[ANIMATE] Generating {duration}-second loop-friendly animation...")
    print(f"          Model: Kling Pro (locked in)")
    print(f"          Style: Background-only, text static, no zoom")
    
    # Use Kling Pro - THE model for everything
    handler = await fal_client.submit_async(
        "fal-ai/kling-video/v2.5-turbo/pro/image-to-video",
        arguments={
            "prompt": motion_prompt,
            "image_url": image_url,
            "duration": duration,
            "negative_prompt": "text movement, text warping, text animation, zoom, camera movement, pan, tilt, reframing, aggressive motion, fast motion, distortion, blur on text",
            "cfg_scale": 0.5,
        }
    )
    
    result = await handler.get()
    
    if result and "video" in result:
        video_url = result["video"]["url"]
        print(f"          [OK] Video generated: {video_url[:60]}...")
        return video_url
    
    raise RuntimeError(f"No video returned. Response: {result}")


def generate_dramatic_music(script_context: str, duration: int = 5) -> str:
    """
    Generate dramatic background music based on script context.
    
    Args:
        script_context: The script/concept to inform the mood
        duration: Length in seconds
    
    Returns:
        URL to generated audio
    """
    # Dramatic music prompt for legal/rights messaging
    music_prompt = f"""Dramatic cinematic underscore music,
    tense building urgency,
    powerful determined energy,
    fighting for justice mood,
    inspired by: {script_context},
    professional legal ad background music,
    no vocals no lyrics,
    epic tension with hope undertones,
    newsworthy serious tone"""
    
    print(f"[MUSIC] Generating {duration}s dramatic background music...")
    print(f"        Script context: {script_context}")
    
    audio_url = generate_music(
        prompt=music_prompt,
        duration=duration,
        guidance_scale=3.5,
    )
    
    print(f"        [OK] Music generated: {audio_url[:60]}...")
    return audio_url


async def download_video(url: str) -> str:
    """Download video to temp file and return path."""
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        
        fd, temp_path = tempfile.mkstemp(suffix=".mp4")
        with os.fdopen(fd, 'wb') as f:
            f.write(response.content)
        
        return temp_path


def upload_to_fal(file_path: str) -> str:
    """Upload a local file to Fal.ai storage and return URL."""
    return fal_client.upload_file(file_path)


def update_airtable_final_video(record_id: str, video_url: str):
    """Upload final video URL to the Final_Video field."""
    url = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{TABLE_ID}/{record_id}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_PAT}",
        "Content-Type": "application/json"
    }
    
    data = {
        "fields": {
            "Final_Video": [{"url": video_url}]
        }
    }
    
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"[UPLOAD] ✅ Final video uploaded to Airtable")
    else:
        print(f"[UPLOAD] ❌ Failed to upload: {response.text}")
        response.raise_for_status()


async def main(record_id: str, script: str):
    """Main pipeline: fetch image → animate → add music → upload."""
    print("=" * 60)
    print("INFOGRAPHIC ANIMATION PIPELINE")
    print("=" * 60)
    print(f"Record ID: {record_id}")
    print(f"Script: {script}")
    print()
    
    # Step 1: Fetch record and get image URL
    print("[1/5] Fetching record from Airtable...")
    fields = fetch_record(record_id)
    ad_title = fields.get("Ad Title", "Untitled")
    print(f"       Ad Title: {ad_title}")
    
    image_url = get_image_url(fields)
    print(f"       Image URL: {image_url[:60]}...")
    
    # Step 2: Animate the infographic
    print()
    print("[2/5] Animating infographic (10 seconds, loop-friendly)...")
    video_url = await animate_infographic(image_url, duration="10")
    
    # Step 3: Generate dramatic music (10 seconds to match video)
    print()
    print("[3/5] Generating background music...")
    music_url = generate_dramatic_music(script, duration=10)
    
    # Step 4: Download video and audio, then mix
    print()
    print("[4/5] Mixing video with music...")
    video_path = await download_video(video_url)
    audio_path = download_audio_sync(music_url)
    
    # Mix audio into video (replace any existing audio)
    final_video_path = add_audio_to_video(
        video_path=video_path,
        audio_path=audio_path,
        replace_audio=True,
    )
    
    # Upload to Fal.ai storage for URL
    print()
    print("[5/5] Uploading final video...")
    final_video_url = upload_to_fal(final_video_path)
    print(f"       Final video URL: {final_video_url[:60]}...")
    
    # Update Airtable
    update_airtable_final_video(record_id, final_video_url)
    
    # Cleanup temp files
    Path(video_path).unlink(missing_ok=True)
    Path(audio_path).unlink(missing_ok=True)
    Path(final_video_path).unlink(missing_ok=True)
    
    print()
    print("=" * 60)
    print("✅ COMPLETE!")
    print("=" * 60)
    print(f"Final video uploaded to record {record_id}")
    print(f"URL: {final_video_url}")
    
    return final_video_url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Animate an infographic image with background music"
    )
    parser.add_argument(
        "--record",
        required=True,
        help="Airtable record ID (e.g., reccmz4eDX2Wni7Pd)"
    )
    parser.add_argument(
        "--script",
        required=True,
        help="Script/concept for music mood (e.g., 'don't let them control the clock, know your rights')"
    )
    parser.add_argument(
        "--image-field",
        default="IMG",
        help="Which image field to use (default: IMG)"
    )
    
    args = parser.parse_args()
    
    asyncio.run(main(args.record, args.script))
