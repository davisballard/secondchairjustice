"""
Generate Audio Assets for "The Boardroom" (Colorado) - STANDALONE
------------------------------------------------------------------
Direct fal_client calls without complex imports.

Run: python3 generate_boardroom_audio_standalone.py
"""

import asyncio
import os

try:
    import fal_client
except ImportError:
    print("ERROR: fal_client not installed.")
    print("Run: pip3 install fal-client --user")
    exit(1)


async def generate_voiceover():
    """Generate the locked voiceover script with Bill voice."""
    
    script = """One crash. One family. One claim.

On the other side? A machine that denies seventy-three percent before anyone even looks.

Your first move? See what you're owed."""

    print("\n" + "="*60)
    print("GENERATING VOICEOVER (Bill - gruff, working-class)")
    print("="*60)
    print(f"Script: {script}")
    print(f"\nSettings: stability=0.75, similarity=0.70, style=0.15, speed=1.0")
    
    try:
        handler = await fal_client.submit_async(
            "fal-ai/elevenlabs/tts/eleven-v3",
            arguments={
                "text": script,
                "voice": "Bill",
                "stability": 0.75,
                "similarity_boost": 0.70,
                "style": 0.15,
                "speed": 1.0,
            }
        )
        
        result = await handler.get()
        
        if result and "audio" in result:
            audio_url = result["audio"]["url"]
            print(f"\n✅ VOICEOVER GENERATED:")
            print(f"   {audio_url}")
            return audio_url
        else:
            print(f"❌ No audio in response: {result}")
            return None
            
    except Exception as e:
        print(f"\n❌ VO GENERATION FAILED: {e}")
        return None


def generate_music(prompt: str, duration: int = 20) -> str:
    """Generate music using Stable Audio 2.5."""
    
    result = fal_client.subscribe(
        "fal-ai/stable-audio-25/text-to-audio",
        arguments={
            "prompt": prompt,
            "seconds_total": duration,
            "num_inference_steps": 8,
            "guidance_scale": 3.0,
        }
    )
    
    audio_url = result.get("audio", {}).get("url")
    if not audio_url:
        raise ValueError(f"No audio URL in response: {result}")
    
    return audio_url


def generate_all_music():
    """Generate 4 music options at 20 seconds (5s padding for fade)."""
    
    music_prompts = {
        "A_investigator": {
            "name": "Option A: The Investigator (RECOMMENDED)",
            "prompt": "Tense documentary underscore, building tension first 5 seconds, cold sterile menacing electronic middle section, resolving into determined hopeful strings at end, cinematic, news investigation style, no vocals, modern orchestral with subtle electronics",
        },
        "B_david_goliath": {
            "name": "Option B: David vs Goliath",
            "prompt": "Epic underdog music, starting quiet and tense, building to defiant, powerful drums enter at 10 seconds, fighting spirit, determined not aggressive, no vocals no lyrics, cinematic trailer style, minor key transitioning to major",
        },
        "C_cold_warm": {
            "name": "Option C: Cold Machine / Warm Human",
            "prompt": "Two contrasting moods: first half cold electronic industrial minimal, second half warm emotional piano and strings, transition at 10 seconds, cinematic, no vocals, contrast between sterile corporate and human warmth",
        },
        "D_news_alert": {
            "name": "Option D: News Alert Evolved",
            "prompt": "Breaking news underscore style, urgent opening, serious investigative middle section, resolving into hopeful determined ending, broadcast quality, no vocals, professional news documentary, modern",
        },
    }
    
    results = {}
    
    print("\n" + "="*60)
    print("GENERATING MUSIC OPTIONS (20 seconds each for fade padding)")
    print("="*60)
    
    for key, config in music_prompts.items():
        print(f"\n🎵 Generating: {config['name']}")
        print(f"   Prompt: {config['prompt'][:70]}...")
        
        try:
            music_url = generate_music(
                prompt=config["prompt"],
                duration=20,
            )
            print(f"   ✅ Generated: {music_url}")
            results[key] = {
                "name": config["name"],
                "url": music_url,
            }
        except Exception as e:
            print(f"   ❌ Failed: {e}")
            results[key] = {
                "name": config["name"],
                "url": None,
                "error": str(e),
            }
    
    return results


async def main():
    print("\n" + "#"*60)
    print("# THE BOARDROOM - AUDIO PRODUCTION")
    print("# Colorado MVA - Hegarty Cut")
    print("#"*60)
    
    # Check for FAL_KEY
    if not os.environ.get("FAL_KEY"):
        print("\n⚠️  WARNING: FAL_KEY environment variable not set!")
        print("   Set it with: export FAL_KEY='your-key-here'")
        print("   Or the script may fail.\n")
    
    # Generate VO
    vo_url = await generate_voiceover()
    
    # Generate Music
    music_results = generate_all_music()
    
    # Summary
    print("\n" + "="*60)
    print("📋 PRODUCTION SUMMARY")
    print("="*60)
    
    print("\n📢 VOICEOVER (Bill voice):")
    if vo_url:
        print(f"   ✅ {vo_url}")
    else:
        print("   ❌ Failed to generate")
    
    print("\n🎵 MUSIC OPTIONS (20 seconds each):")
    for key, result in music_results.items():
        status = "✅" if result.get("url") else "❌"
        print(f"\n   {status} {result['name']}")
        if result.get("url"):
            print(f"      {result['url']}")
    
    print("\n" + "="*60)
    print("📋 CAPCUT ASSEMBLY INSTRUCTIONS:")
    print("="*60)
    print("""
1. Download all audio files above
2. Import VO + your preferred music to CapCut
3. VO: Add 0.2 second delay at start
4. Music: Set to 30% volume
5. Music: Apply fade out in last 5 seconds
6. Add text overlays synced to VO:
   
   | Time     | Text                              |
   |----------|-----------------------------------|
   | 0:00-2s  | One crash. One family. One claim. |
   | 2-5s     | On the other side?                |
   | 5-8s     | A machine that denies 73%         |
   | 8-10s    | before anyone even looks.         |
   | 10-13s   | Your first move?                  |
   | 13-15s   | See what you're owed.             |

7. Export at 9:16 (1080x1920)
""")
    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
