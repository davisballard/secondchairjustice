"""
Generate Audio Assets for "The Boardroom" (Colorado)
-----------------------------------------------------
Generates:
1. Voiceover (Bill voice)
2. 4 Music Options (20 seconds each for fade padding)

Run from: Agency_Simulation_Root/06_Brands/Lead_Faucet/10_Ad_Factory/
"""

import asyncio
import os
import sys

# Add parent paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '08_Ad_Factory'))

from audio_models.elevenlabs import generate_voiceover
from audio_models.stable_audio import generate_music

# Output directory
OUTPUT_DIR = os.path.dirname(__file__)


async def generate_vo():
    """Generate the locked voiceover script with Bill voice."""
    
    script = """One crash. One family. One claim.

On the other side? A machine that denies seventy-three percent before anyone even looks.

Your first move? See what you're owed."""

    print("\n" + "="*60)
    print("GENERATING VOICEOVER")
    print("="*60)
    print(f"Script: {script[:50]}...")
    print(f"Voice: Bill (gruff, working-class)")
    print(f"Settings: stability=0.75, similarity=0.70, style=0.15")
    
    try:
        audio_url = await generate_voiceover(
            text=script,
            voice="Bill",
            stability=0.75,
            similarity_boost=0.70,
            style=0.15,
            speed=1.0,
        )
        print(f"\n✅ VOICEOVER GENERATED:")
        print(f"   {audio_url}")
        return audio_url
    except Exception as e:
        print(f"\n❌ VO GENERATION FAILED: {e}")
        return None


def generate_music_options():
    """Generate 4 music options at 20 seconds (5s padding for fade)."""
    
    music_prompts = {
        "A_investigator": {
            "name": "The Investigator (RECOMMENDED)",
            "prompt": "Tense documentary underscore, building tension first 5 seconds, cold sterile menacing electronic middle section, resolving into determined hopeful strings at end, cinematic, news investigation style, no vocals, modern orchestral with subtle electronics",
        },
        "B_david_goliath": {
            "name": "David vs Goliath",
            "prompt": "Epic underdog music, starting quiet and tense, building to defiant, powerful drums enter at 10 seconds, fighting spirit, determined not aggressive, no vocals no lyrics, cinematic trailer style, minor key transitioning to major",
        },
        "C_cold_warm": {
            "name": "Cold Machine / Warm Human",
            "prompt": "Two contrasting moods: first half cold electronic industrial minimal, second half warm emotional piano and strings, transition at 10 seconds, cinematic, no vocals, contrast between sterile corporate and human warmth",
        },
        "D_news_alert": {
            "name": "News Alert Evolved",
            "prompt": "Breaking news underscore style, urgent opening, serious investigative middle section, resolving into hopeful determined ending, broadcast quality, no vocals, professional news documentary, modern",
        },
    }
    
    results = {}
    
    print("\n" + "="*60)
    print("GENERATING MUSIC OPTIONS (20 seconds each)")
    print("="*60)
    
    for key, config in music_prompts.items():
        print(f"\n🎵 Generating: {config['name']}")
        print(f"   Prompt: {config['prompt'][:60]}...")
        
        try:
            music_url = generate_music(
                prompt=config["prompt"],
                duration=20,  # 5 seconds extra for fade
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
    
    # Generate VO
    vo_url = await generate_vo()
    
    # Generate Music
    music_results = generate_music_options()
    
    # Summary
    print("\n" + "="*60)
    print("PRODUCTION SUMMARY")
    print("="*60)
    
    print("\n📢 VOICEOVER:")
    if vo_url:
        print(f"   ✅ {vo_url}")
    else:
        print("   ❌ Failed to generate")
    
    print("\n🎵 MUSIC OPTIONS:")
    for key, result in music_results.items():
        status = "✅" if result.get("url") else "❌"
        print(f"   {status} {result['name']}")
        if result.get("url"):
            print(f"      {result['url']}")
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Download VO and music files")
    print("2. Import to CapCut")
    print("3. Add 0.2s delay to VO start")
    print("4. Set music to 30% volume")
    print("5. Apply fade out to music in last 5 seconds")
    print("6. Add text overlays synced to VO")
    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
