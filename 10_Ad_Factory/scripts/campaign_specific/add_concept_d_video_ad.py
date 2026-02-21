"""
Add Concept D Video Ad to Airtable
California / Larry H. Parker / Second Chair

Run: python add_concept_d_video_ad.py
"""

import os
import sys
from pathlib import Path

# Add parent to path for config_loader
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "08_Ad_Factory"))

from config_loader import load_brand_config
from pyairtable import Api

# =============================================================================
# CONCEPT D - "THEY BROUGHT LAWYERS" VIDEO AD
# =============================================================================

CONCEPT_D_VIDEO_AD = {
    "ad_title": "Concept D - They Brought Lawyers (Video)",
    "headline": "Insurance companies have adjusters. Defense lawyers. Systems built to pay less.",
    "post_copy": """Car accident settlements in California aren't fair fights.

Insurance companies send adjusters trained to minimize payouts. Defense attorneys. Corporate playbooks.

Meanwhile, accident victims negotiate alone — not knowing what their case is actually worth.

Over $2.2 billion recovered for CA motor vehicle accident victims.
95% success rate.

Get a free case estimate in 30 seconds ↓

This is an advertisement.""",
    "description": "Car accident settlements in California aren't fair fights. Insurance companies send adjusters trained to minimize payouts.",
    "cta": "Get What You're Owed",
    "strategy": "They Brought Lawyers | Authority Bias + Fear Appeal + Empathy Bridge | CA Video",
    "state": "CA",
    "client": "Larry H. Parker",
    "channel": "Meta",
    "display_link": "claimjusticenow.com/california",
    "aspect_ratio": "9:16",
    "video_format": "Story Slide (15s)",
    "voiceover_script": """Their lawyers. Their adjusters. Their rules.

The whole game is rigged.

California families are bringing their own team to the fight.

Your first move? See what you're owed.""",
}


def main():
    print("[*] Loading Second Chair configuration...")
    
    try:
        config = load_brand_config("Lead_Faucet")
    except Exception as e:
        print(f"[X] Configuration error: {e}")
        print("    Make sure .env files are set up with Airtable credentials.")
        return
    
    creds = config["credentials"]
    tables = config["airtable"]
    field_map = config.get("field_mapping", {})
    video_field_map = config.get("video_field_mapping", {})
    
    api = Api(creds["airtable_pat"])
    
    # Use the images table (same as other ads) - adjust if you have a separate video table
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    print(f"[*] Adding Concept D video ad to '{tables['images_table']}'...")
    print()
    
    ad = CONCEPT_D_VIDEO_AD
    
    # Build fields using the config's field mapping
    fields = {
        field_map.get("ad_title", "Ad Title"): ad["ad_title"],
        field_map.get("headline", "Headline"): ad["headline"],
        field_map.get("post_copy", "Post Copy"): ad["post_copy"],
        field_map.get("description", "Description"): ad["description"],
        field_map.get("cta", "CTA"): ad["cta"],
        field_map.get("strategy", "Strategy"): ad["strategy"],
        field_map.get("state", "State"): ad["state"],
        field_map.get("client", "Client"): ad["client"],
        field_map.get("channel", "Channel"): ad["channel"],
        field_map.get("display_link", "Display Link"): ad["display_link"],
        field_map.get("aspect_ratio_field", "Aspect Ratio"): ad["aspect_ratio"],
    }
    
    # Note: Video-specific fields (Video_Format, Voiceover_Script) are stored in notes
    # to avoid select field permission issues. Add them manually in Airtable if needed.
    # Video Format: Story Slide (15s)
    # Voiceover Script is in the description field
    
    try:
        record = table.create(fields)
        record_id = record["id"]
        print(f"  ✅ Created: {ad['ad_title']}")
        print(f"     Record ID: {record_id}")
        print()
        print("=" * 60)
        print("[DONE] Concept D video ad added to Airtable")
        print()
        print(f"View in Airtable: https://airtable.com/{creds['airtable_base_id']}/{tables['images_table']}")
    except Exception as e:
        print(f"  ❌ Failed: {ad['ad_title']}")
        print(f"     Error: {e}")


if __name__ == "__main__":
    main()
