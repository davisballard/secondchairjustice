"""
Generate Audio Assets for "On The Nose" (Colorado)
---------------------------------------------------
Generates:
1. Voiceover (Bill voice) - Direct opportunity tone
2. Music - Warmer/hopeful (different from The Boardroom's investigative feel)

Run from: Agency_Simulation_Root/06_Brands/Lead_Faucet/10_Ad_Factory/

Usage:
    python generate_on_the_nose_audio.py

Requires FAL_KEY environment variable.
"""

import asyncio
import os
import sys

# Add parent paths for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '08_Ad_Factory'))

from audio_models.elevenlabs import generate_voiceover

# Output directory
OUTPUT_DIR = os.path.dirname(__file__)


# =============================================================================
# LOCKED SCRIPT: Version B — "The Numbers Forward"
# =============================================================================

SCRIPT = """Accident cases in Colorado have settled for millions.

Most people never find out what they're owed.

Free claim estimate. Sixty seconds. See what experienced attorneys can do."""

# Word count: 30 words
# Pacing: 2.0 words/second — punchy, leaves room for breath


async def generate_vo():
    """Generate the voiceover with Bill voice — conversational, opportunity tone."""
    
    print("\n" + "="*60)
    print("GENERATING VOICEOVER — ON THE NOSE")
    print("="*60)
    print(f"Script ({len(SCRIPT.split())} words):")
    print("-"*40)
    print(SCRIPT)
    print("-"*40)
    print(f"Voice: Bill (gruff, working-class)")
    print(f"Tone: Conversational, opportunity — NOT investigative")
    print(f"Settings: stability=0.75, similarity=0.70, style=0.15, speed=1.0")
    
    try:
        audio_url = await generate_voiceover(
            text=SCRIPT,
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


async def main():
    print("\n" + "#"*60)
    print("# ON THE NOSE — AUDIO PRODUCTION")
    print("# Colorado MVA — Direct Opportunity Cut")
    print("#"*60)
    
    # Generate VO
    vo_url = await generate_vo()
    
    # Summary
    print("\n" + "="*60)
    print("PRODUCTION SUMMARY")
    print("="*60)
    
    print("\n📢 VOICEOVER:")
    if vo_url:
        print(f"   ✅ {vo_url}")
    else:
        print("   ❌ Failed to generate")
    
    print("\n🎵 MUSIC:")
    print("   Consider reusing The Boardroom Option C (Cold Machine / Warm Human)")
    print("   Use only the warm second half, or generate something new:")
    print("   - Hopeful documentary")
    print("   - Warm determination")
    print("   - Morning light feel")
    
    print("\n" + "="*60)
    print("BEAT 2 VISUALS NEEDED:")
    print("="*60)
    print("Kitchen Table scene — two 2-second clips needed (4-8s total)")
    print("See PENDING_CO_ON_THE_NOSE_2026-02-05.md for prompts")
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Download VO")
    print("2. Generate Beat 2 images (Nano Banana Pro)")
    print("3. Generate Beat 2 videos (Kling 2.6 Pro) — TWO clips")
    print("4. Select/generate music")
    print("5. Assemble in CapCut:")
    print("   - 0.2s delay on VO start")
    print("   - Music at 30%")
    print("   - Text overlays synced to VO")
    print("="*60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
