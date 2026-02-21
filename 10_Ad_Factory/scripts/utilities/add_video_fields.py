#!/usr/bin/env python3
"""
Add Video Production Fields to Airtable

Adds the simplified video clip fields to your Video Scripts table.
Run once to set up, then delete or ignore this script.

Requirements:
- AIRTABLE_PAT with `schema.bases:write` scope
- AIRTABLE_BASE_ID in .env
"""

import os
import requests
from urllib.parse import quote
from dotenv import load_dotenv

# Load environment
load_dotenv()

AIRTABLE_PAT = os.getenv("AIRTABLE_PAT")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TABLE_NAME = "Image Ads"  # Adding video fields to same table
TABLE_ID = "tblqHvuHyuVwfiDG7"  # Image Ads table ID

# API endpoint for creating fields (using table ID)
BASE_URL = f"https://api.airtable.com/v0/meta/bases/{AIRTABLE_BASE_ID}/tables/{TABLE_ID}/fields"

HEADERS = {
    "Authorization": f"Bearer {AIRTABLE_PAT}",
    "Content-Type": "application/json"
}

# Fields to add (simplified list - just outputs)
FIELDS_TO_ADD = [
    {
        "name": "Video_Format",
        "type": "singleSelect",
        "options": {
            "choices": [
                {"name": "Motion Still", "color": "blueLight2"},
                {"name": "TikTok Slide", "color": "greenLight2"},
                {"name": "Extended", "color": "purpleLight2"}
            ]
        }
    },
    {
        "name": "Clip1_Image",
        "type": "multipleAttachments"
    },
    {
        "name": "Clip1_Video",
        "type": "multipleAttachments"
    },
    {
        "name": "Clip2_Image",
        "type": "multipleAttachments"
    },
    {
        "name": "Clip2_Video",
        "type": "multipleAttachments"
    },
    {
        "name": "Clip3_Image",
        "type": "multipleAttachments"
    },
    {
        "name": "Clip3_Video",
        "type": "multipleAttachments"
    },
    {
        "name": "Voiceover_Script",
        "type": "multilineText"
    },
    {
        "name": "Voiceover_Audio",
        "type": "multipleAttachments"
    },
    {
        "name": "Environment_Audio",
        "type": "multipleAttachments"
    },
    {
        "name": "Final_Video",
        "type": "multipleAttachments"
    }
]


def create_field(field_config):
    """Create a single field in Airtable."""
    response = requests.post(BASE_URL, headers=HEADERS, json=field_config)
    
    if response.status_code == 200:
        print(f"✅ Created: {field_config['name']}")
        return True
    elif response.status_code == 422 and "DUPLICATE_FIELD_NAME" in response.text:
        print(f"⏭️  Skipped (already exists): {field_config['name']}")
        return True
    else:
        print(f"❌ Failed: {field_config['name']}")
        print(f"   Status: {response.status_code}")
        print(f"   Error: {response.text}")
        return False


def main():
    print("=" * 50)
    print("Adding Video Production Fields to Airtable")
    print("=" * 50)
    print(f"Base ID: {AIRTABLE_BASE_ID}")
    print(f"Table: {TABLE_NAME}")
    print(f"Fields to add: {len(FIELDS_TO_ADD)}")
    print("=" * 50)
    
    if not AIRTABLE_PAT:
        print("❌ Error: AIRTABLE_PAT not found in .env")
        print("   Add your Personal Access Token to .env")
        return
    
    if not AIRTABLE_BASE_ID:
        print("❌ Error: AIRTABLE_BASE_ID not found in .env")
        print("   Add your Base ID to .env")
        return
    
    success_count = 0
    for field in FIELDS_TO_ADD:
        if create_field(field):
            success_count += 1
    
    print("=" * 50)
    print(f"Done! {success_count}/{len(FIELDS_TO_ADD)} fields ready")
    print("=" * 50)


if __name__ == "__main__":
    main()
