"""
Add Settlement Gap Ad Variations to Airtable
Nevada / Jacoby & Meyers / Second Chair

Run: python add_settlement_gap_ads.py
"""

import os
import sys
from pathlib import Path

# Add parent to path for config_loader
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "08_Ad_Factory"))

from config_loader import load_brand_config
from pyairtable import Api

# =============================================================================
# SETTLEMENT GAP AD VARIATIONS - Nevada Aggressive
# =============================================================================

SETTLEMENT_GAP_ADS = [
    # VARIATION 1: The Lowball
    {
        "ad_title": "Settlement Gap - V1 - The Lowball",
        "headline": "Insurance Lowballed Another Vegas Driver. See What Actually Happened.",
        "post_copy": """Insurance adjusters are trained to close fast and pay less. Another Nevada driver just proved what fighting back looks like.

The first offer is never the real number. It's a test — to see if you'll take it and disappear.

Accident victims who push back recover significantly more. That's not opinion. That's pattern.

Past results do not guarantee future outcomes.""",
        "description": "Insurance adjusters are trained to close fast and pay less. Another Nevada driver just proved what fighting back looks like.",
        "cta": "Get What You're Owed",
        "strategy": "Settlement Gap | Loss Aversion + Anchoring | Nevada Aggressive",
        "state": "NV",
        "client": "Jacoby & Meyers",
        "channel": "Meta",
        "display_link": "claimjusticenow.com/nevada",
        "aspect_ratio": "1:1",
    },
    
    # VARIATION 2: The System
    {
        "ad_title": "Settlement Gap - V2 - The System",
        "headline": "This Is How Insurance Companies Keep More of Your Money",
        "post_copy": """They call within 48 hours. They have a number ready. That number is designed to be low. Here's what they're counting on:

That you don't know what cases like yours actually settle for.

That gap — between what they offer and what cases are worth — is their profit margin. Nevada accident victims are closing that gap.

Past results do not guarantee future outcomes.""",
        "description": "They call within 48 hours. They have a number ready. That number is designed to be low. Here's what they're counting on:",
        "cta": "Get What You're Owed",
        "strategy": "Settlement Gap | Loss Aversion + Insider Knowledge | Nevada Aggressive",
        "state": "NV",
        "client": "Jacoby & Meyers",
        "channel": "Meta",
        "display_link": "claimjusticenow.com/nevada",
        "aspect_ratio": "1:1",
    },
    
    # VARIATION 3: The Fighter
    {
        "ad_title": "Settlement Gap - V3 - The Fighter",
        "headline": "They Offered Low. Someone Fought Back. Look What Happened.",
        "post_copy": """Insurance has teams of lawyers trained to minimize payouts. Most people don't fight back. This Nevada driver did.

The first check is never the final answer. It's the opening move in a negotiation most people don't know they're in.

Accident victims with representation recover more. The gap between first offer and final settlement proves it.

Past results do not guarantee future outcomes.""",
        "description": "Insurance has teams of lawyers trained to minimize payouts. Most people don't fight back. This Nevada driver did.",
        "cta": "Get What You're Owed",
        "strategy": "Settlement Gap | Loss Aversion + Fighter Positioning | Nevada Aggressive",
        "state": "NV",
        "client": "Jacoby & Meyers",
        "channel": "Meta",
        "display_link": "claimjusticenow.com/nevada",
        "aspect_ratio": "1:1",
    },
]


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
    
    api = Api(creds["airtable_pat"])
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    print(f"[*] Adding {len(SETTLEMENT_GAP_ADS)} ads to '{tables['images_table']}'...")
    print()
    
    created_ids = []
    
    for i, ad in enumerate(SETTLEMENT_GAP_ADS):
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
        
        try:
            record = table.create(fields)
            record_id = record["id"]
            created_ids.append(record_id)
            print(f"  [{i+1}] ✅ Created: {ad['ad_title']}")
            print(f"       Record ID: {record_id}")
        except Exception as e:
            print(f"  [{i+1}] ❌ Failed: {ad['ad_title']}")
            print(f"       Error: {e}")
    
    print()
    print("=" * 60)
    print(f"[DONE] Created {len(created_ids)} records in Airtable")
    print()
    print("Record IDs (for image generation later):")
    for rid in created_ids:
        print(f"  - {rid}")


if __name__ == "__main__":
    main()
