"""
Generate Ad Mockups for Second Chair

Creates pixel-perfect platform mockups showing how ads will appear.
Currently supports: Meta (Facebook/Instagram Feed)

Usage:
    python generate_ad_mockup.py --record RECORD_ID
    python generate_ad_mockup.py --all  # Process all records with images but no mockup
    python generate_ad_mockup.py --record RECORD_ID --platform tiktok
"""

import argparse
import asyncio
import io
import os
import sys
import tempfile
from pathlib import Path
from typing import Optional

import fal_client
import requests
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
root_env = Path(__file__).resolve().parents[4] / ".env"
load_dotenv(root_env)

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "08_Ad_Factory"))

from config_loader import load_brand_config
from pyairtable import Api

# Set FAL_KEY for upload
FAL_KEY = os.getenv("FAL_KEY")
if FAL_KEY:
    os.environ["FAL_KEY"] = FAL_KEY

# ═══════════════════════════════════════════════════════════════════════════════
# MOCKUP CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

# Meta Feed Ad Dimensions
MOCKUP_WIDTH = 1080
CONTENT_PADDING = 48

# Colors (Facebook Dark Mode inspired, but cleaner)
COLORS = {
    "bg": "#FFFFFF",
    "text_primary": "#050505",
    "text_secondary": "#65676B", 
    "text_link": "#0064D1",
    "border": "#DADDE1",
    "cta_bg": "#0866FF",
    "cta_text": "#FFFFFF",
    "divider": "#E4E6EB",
    "sponsored": "#65676B",
}

# Typography sizes
FONT_SIZES = {
    "brand_name": 42,
    "sponsored": 32,
    "primary_text": 36,
    "headline": 44,
    "description": 32,
    "cta": 36,
    "engagement": 28,
}


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Get a font, falling back to defaults if system fonts unavailable."""
    font_names = [
        # macOS system fonts (Facebook uses Helvetica-like)
        "/System/Library/Fonts/SFNSText.ttf",
        "/System/Library/Fonts/Helvetica.ttc", 
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/SF-Pro-Text-Regular.otf",
        "/Library/Fonts/SF-Pro-Text-Semibold.otf" if bold else None,
        # Fallbacks
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ]
    
    for font_name in font_names:
        if font_name and os.path.exists(font_name):
            try:
                return ImageFont.truetype(font_name, size)
            except:
                continue
    
    # Ultimate fallback
    return ImageFont.load_default()


def truncate_text(text: str, max_chars: int, suffix: str = "... See more") -> str:
    """Truncate text and add suffix if too long."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars - len(suffix)].rstrip() + suffix


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    """Wrap text to fit within max_width."""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = font.getbbox(test_line)
        if bbox[2] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines


def download_image(url: str) -> Image.Image:
    """Download image from URL and return as PIL Image."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return Image.open(io.BytesIO(response.content))


def create_rounded_rectangle(width: int, height: int, radius: int, color: str) -> Image.Image:
    """Create a rounded rectangle image."""
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([(0, 0), (width, height)], radius=radius, fill=color)
    return img


def create_circle(size: int, color: str) -> Image.Image:
    """Create a circle image."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.ellipse([(0, 0), (size, size)], fill=color)
    return img


def generate_meta_mockup(
    ad_image: Image.Image,
    brand_name: str = "Jacoby & Meyers",
    primary_text: str = "",
    headline: str = "",
    description: str = "",
    cta: str = "Learn More",
    display_link: str = "secondchair.io",
) -> Image.Image:
    """
    Generate a Meta (Facebook) feed ad mockup.
    
    Args:
        ad_image: The main ad creative (4:5 ratio)
        brand_name: Advertiser name
        primary_text: Post copy (shown above image)
        headline: Bold headline (shown below image)
        description: Subtitle (shown below headline)
        cta: Call-to-action button text
        display_link: URL shown above headline
    
    Returns:
        PIL Image of the complete mockup
    """
    
    # Calculate dimensions
    content_width = MOCKUP_WIDTH - (CONTENT_PADDING * 2)
    
    # Resize ad image to fit width (maintaining 4:5 aspect)
    img_width = MOCKUP_WIDTH
    img_height = int(img_width * 1.25)  # 4:5 ratio
    ad_image_resized = ad_image.resize((img_width, img_height), Image.Resampling.LANCZOS)
    
    # Load fonts
    font_brand = get_font(FONT_SIZES["brand_name"], bold=True)
    font_sponsored = get_font(FONT_SIZES["sponsored"])
    font_primary = get_font(FONT_SIZES["primary_text"])
    font_headline = get_font(FONT_SIZES["headline"], bold=True)
    font_desc = get_font(FONT_SIZES["description"])
    font_cta = get_font(FONT_SIZES["cta"], bold=True)
    font_engagement = get_font(FONT_SIZES["engagement"])
    
    # Calculate heights for each section
    header_height = 140
    
    # Primary text section
    primary_display = truncate_text(primary_text, 200) if primary_text else ""
    primary_lines = wrap_text(primary_display, font_primary, content_width) if primary_display else []
    primary_height = len(primary_lines) * 48 + 32 if primary_lines else 0
    
    # Info bar (link + headline + description + CTA)
    info_height = 200
    
    # Engagement bar
    engagement_height = 100
    
    # Total mockup height
    total_height = header_height + primary_height + img_height + info_height + engagement_height
    
    # Create mockup canvas
    mockup = Image.new("RGB", (MOCKUP_WIDTH, total_height), COLORS["bg"])
    draw = ImageDraw.Draw(mockup)
    
    y_pos = 0
    
    # ─────────────────────────────────────────────────────────────────────────
    # HEADER: Avatar + Brand Name + Sponsored
    # ─────────────────────────────────────────────────────────────────────────
    
    y_pos += 32
    
    # Avatar (placeholder circle)
    avatar_size = 80
    avatar = create_circle(avatar_size, "#1877F2")  # Facebook blue
    avatar_draw = ImageDraw.Draw(avatar)
    # Add initials
    initials = "".join(word[0].upper() for word in brand_name.split()[:2])
    initials_font = get_font(32, bold=True)
    bbox = initials_font.getbbox(initials)
    initials_x = (avatar_size - bbox[2]) // 2
    initials_y = (avatar_size - bbox[3]) // 2
    avatar_draw.text((initials_x, initials_y), initials, fill="white", font=initials_font)
    mockup.paste(avatar, (CONTENT_PADDING, y_pos), avatar)
    
    # Brand name
    text_x = CONTENT_PADDING + avatar_size + 24
    draw.text((text_x, y_pos + 8), brand_name, fill=COLORS["text_primary"], font=font_brand)
    
    # Sponsored label
    draw.text((text_x, y_pos + 48), "Sponsored · 🌐", fill=COLORS["sponsored"], font=font_sponsored)
    
    # Three dots menu (simulated)
    dots_x = MOCKUP_WIDTH - CONTENT_PADDING - 40
    for i in range(3):
        draw.ellipse(
            [(dots_x, y_pos + 30 + i * 12), (dots_x + 8, y_pos + 38 + i * 12)],
            fill=COLORS["text_secondary"]
        )
    
    y_pos += header_height
    
    # ─────────────────────────────────────────────────────────────────────────
    # PRIMARY TEXT (Post Copy)
    # ─────────────────────────────────────────────────────────────────────────
    
    if primary_lines:
        for i, line in enumerate(primary_lines):
            # Make "See more" blue if it's the last line and contains it
            if i == len(primary_lines) - 1 and "See more" in line:
                parts = line.split("... See more")
                if parts[0]:
                    draw.text(
                        (CONTENT_PADDING, y_pos),
                        parts[0] + "... ",
                        fill=COLORS["text_primary"],
                        font=font_primary
                    )
                    bbox = font_primary.getbbox(parts[0] + "... ")
                    draw.text(
                        (CONTENT_PADDING + bbox[2], y_pos),
                        "See more",
                        fill=COLORS["text_link"],
                        font=font_primary
                    )
            else:
                draw.text((CONTENT_PADDING, y_pos), line, fill=COLORS["text_primary"], font=font_primary)
            y_pos += 48
        
        y_pos += 16
    
    # ─────────────────────────────────────────────────────────────────────────
    # AD IMAGE
    # ─────────────────────────────────────────────────────────────────────────
    
    mockup.paste(ad_image_resized, (0, y_pos))
    y_pos += img_height
    
    # ─────────────────────────────────────────────────────────────────────────
    # INFO BAR: Display Link + Headline + Description + CTA
    # ─────────────────────────────────────────────────────────────────────────
    
    # Light gray background for info section
    draw.rectangle(
        [(0, y_pos), (MOCKUP_WIDTH, y_pos + info_height)],
        fill="#F7F8FA"
    )
    
    y_pos += 24
    
    # Display link
    draw.text(
        (CONTENT_PADDING, y_pos),
        display_link.upper(),
        fill=COLORS["text_secondary"],
        font=font_desc
    )
    y_pos += 40
    
    # Headline (truncate if too long)
    headline_display = truncate_text(headline, 50, "...")
    draw.text(
        (CONTENT_PADDING, y_pos),
        headline_display,
        fill=COLORS["text_primary"],
        font=font_headline
    )
    y_pos += 56
    
    # Description (truncate if too long)
    if description:
        desc_display = truncate_text(description, 40, "...")
        draw.text(
            (CONTENT_PADDING, y_pos),
            desc_display,
            fill=COLORS["text_secondary"],
            font=font_desc
        )
    
    # CTA Button (right aligned, auto-width based on text)
    cta_bbox = font_cta.getbbox(cta)
    cta_width = max(220, cta_bbox[2] + 48)  # Min 220, or text width + padding
    cta_height = 72
    cta_x = MOCKUP_WIDTH - CONTENT_PADDING - cta_width
    cta_y = y_pos - 24
    
    cta_btn = create_rounded_rectangle(cta_width, cta_height, 8, COLORS["cta_bg"])
    mockup.paste(cta_btn, (cta_x, cta_y), cta_btn)
    
    # CTA text (centered in button)
    cta_text_x = cta_x + (cta_width - cta_bbox[2]) // 2
    cta_text_y = cta_y + (cta_height - cta_bbox[3]) // 2 - 4
    draw.text((cta_text_x, cta_text_y), cta, fill=COLORS["cta_text"], font=font_cta)
    
    y_pos += 60
    
    # ─────────────────────────────────────────────────────────────────────────
    # ENGAGEMENT BAR: Like, Comment, Share
    # ─────────────────────────────────────────────────────────────────────────
    
    # Divider line
    draw.line(
        [(CONTENT_PADDING, y_pos), (MOCKUP_WIDTH - CONTENT_PADDING, y_pos)],
        fill=COLORS["divider"],
        width=2
    )
    y_pos += 24
    
    # Engagement icons (simplified text for now)
    engagement_items = ["👍 Like", "💬 Comment", "↗️ Share"]
    item_width = content_width // 3
    
    for i, item in enumerate(engagement_items):
        item_x = CONTENT_PADDING + (item_width * i) + (item_width // 2)
        bbox = font_engagement.getbbox(item)
        draw.text(
            (item_x - bbox[2] // 2, y_pos),
            item,
            fill=COLORS["text_secondary"],
            font=font_engagement
        )
    
    return mockup


def generate_tiktok_mockup(
    ad_image: Image.Image,
    brand_name: str = "Jacoby & Meyers",
    caption: str = "",
    cta: str = "Learn More",
) -> Image.Image:
    """
    Generate a TikTok in-feed ad mockup.
    
    Args:
        ad_image: The main ad creative (9:16 ratio preferred, will be resized)
        brand_name: Advertiser name
        caption: Caption text
        cta: Call-to-action button text
    
    Returns:
        PIL Image of the complete mockup
    """
    
    # TikTok uses 9:16 aspect ratio for in-feed ads
    mockup_width = 1080
    mockup_height = 1920
    
    # Resize ad image to fill frame
    ad_image_resized = ad_image.resize((mockup_width, mockup_height), Image.Resampling.LANCZOS)
    
    # Create mockup starting from the ad image
    mockup = ad_image_resized.copy().convert("RGBA")
    draw = ImageDraw.Draw(mockup)
    
    # Load fonts
    font_username = get_font(40, bold=True)
    font_caption = get_font(34)
    font_cta = get_font(36, bold=True)
    font_small = get_font(28)
    
    # Semi-transparent overlay at bottom for text legibility
    overlay = Image.new("RGBA", (mockup_width, 400), (0, 0, 0, 160))
    mockup.paste(overlay, (0, mockup_height - 400), overlay)
    
    # ─────────────────────────────────────────────────────────────────────────
    # RIGHT SIDE: TikTok action buttons (heart, comment, share, etc.)
    # ─────────────────────────────────────────────────────────────────────────
    
    button_x = mockup_width - 100
    button_start_y = 1100
    button_spacing = 100
    
    # Simplified icons (circles with emoji/text)
    buttons = ["❤️", "💬", "↗️", "🔖"]
    for i, icon in enumerate(buttons):
        y = button_start_y + (i * button_spacing)
        draw.text((button_x, y), icon, font=get_font(48), anchor="mm")
    
    # ─────────────────────────────────────────────────────────────────────────
    # BOTTOM: Username, caption, CTA, music
    # ─────────────────────────────────────────────────────────────────────────
    
    bottom_padding = 200
    y_pos = mockup_height - bottom_padding
    
    # Username with "Sponsored" label
    draw.text(
        (48, y_pos - 120),
        f"@{brand_name.lower().replace(' ', '')}",
        fill="white",
        font=font_username
    )
    draw.text(
        (48, y_pos - 80),
        "Sponsored",
        fill="#AAAAAA",
        font=font_small
    )
    
    # Caption (truncated)
    caption_display = truncate_text(caption, 100, "...")
    caption_lines = wrap_text(caption_display, font_caption, mockup_width - 200)
    for i, line in enumerate(caption_lines[:2]):  # Max 2 lines
        draw.text(
            (48, y_pos - 30 + (i * 40)),
            line,
            fill="white",
            font=font_caption
        )
    
    # CTA Button
    cta_width = 300
    cta_height = 60
    cta_x = 48
    cta_y = y_pos + 50
    
    cta_btn = create_rounded_rectangle(cta_width, cta_height, 8, "#FE2C55")  # TikTok red
    mockup.paste(cta_btn, (cta_x, cta_y), cta_btn)
    
    # CTA text
    cta_bbox = font_cta.getbbox(cta)
    cta_text_x = cta_x + (cta_width - cta_bbox[2]) // 2
    cta_text_y = cta_y + (cta_height - cta_bbox[3]) // 2 - 4
    draw.text((cta_text_x, cta_text_y), cta, fill="white", font=font_cta)
    
    # Music ticker at very bottom
    draw.text(
        (48, mockup_height - 60),
        "♫ Original Sound - " + brand_name,
        fill="white",
        font=font_small
    )
    
    # Convert back to RGB for saving
    return mockup.convert("RGB")


def upload_to_fal(file_path: str) -> str:
    """Upload a local file to Fal.ai storage and return URL."""
    return fal_client.upload_file(file_path)


def update_airtable_mockup(
    record_id: str,
    mockup_url: str,
    config: dict,
):
    """Upload mockup URL to the Social Mockup field."""
    creds = config["credentials"]
    tables = config["airtable"]
    field_map = config.get("field_mapping", {})
    
    url = f"https://api.airtable.com/v0/{creds['airtable_base_id']}/{tables['images_table']}/{record_id}"
    headers = {
        "Authorization": f"Bearer {creds['airtable_pat']}",
        "Content-Type": "application/json"
    }
    
    mockup_field = field_map.get("social_mockup", "Social Mockup")
    data = {
        "fields": {
            mockup_field: [{"url": mockup_url}]
        }
    }
    
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"  ☁️  Uploaded to Airtable: {mockup_field}")
    else:
        print(f"  ❌ Failed to upload to Airtable: {response.text}")
        response.raise_for_status()


async def process_record(
    record_id: str,
    config: dict,
    table,
    platform: str = "meta",
    upload: bool = True,
    image_field: str = "img_1",
) -> Optional[str]:
    """
    Process a single ad record and generate mockup.
    
    Returns the mockup URL if successful, None otherwise.
    """
    field_map = config.get("field_mapping", {})
    
    # Fetch record
    try:
        record = table.get(record_id)
    except Exception as e:
        print(f"  ❌ Failed to fetch record: {e}")
        return None
    
    fields = record.get("fields", {})
    ad_title = fields.get(field_map.get("ad_title", "Ad Title"), "Untitled")
    print(f"  📋 Ad: {ad_title[:50]}...")
    
    # Get ad image (use specified field or default to IMG 1)
    img_field = field_map.get(image_field, "IMG")
    print(f"  🖼️  Using image field: {img_field}")
    img_data = fields.get(img_field, [])
    
    if not img_data or len(img_data) == 0:
        print(f"  ⚠️ No image found in {img_field}")
        return None
    
    img_url = img_data[0].get("url")
    if not img_url:
        print(f"  ⚠️ No URL in image data")
        return None
    
    # Get ad copy elements
    headline = fields.get(field_map.get("headline", "Headline"), "")
    description = fields.get(field_map.get("description", "Description"), "")
    cta = fields.get(field_map.get("cta", "CTA"), "Learn More")
    primary_text = fields.get(field_map.get("post_copy", "Post Copy"), "")
    display_link = fields.get(field_map.get("display_link", "Display Link"), "secondchair.io")
    
    # Get brand name (use display_brand_name from config, fallback to client field)
    client = config.get("display_brand_name", "Claim Justice Now")
    
    print(f"  📥 Downloading ad image...")
    try:
        ad_image = download_image(img_url)
    except Exception as e:
        print(f"  ❌ Failed to download image: {e}")
        return None
    
    print(f"  🎨 Generating {platform.upper()} mockup...")
    
    if platform == "meta":
        mockup = generate_meta_mockup(
            ad_image=ad_image,
            brand_name=client,
            primary_text=primary_text,
            headline=headline,
            description=description,
            cta=cta,
            display_link=display_link,
        )
    elif platform == "tiktok":
        mockup = generate_tiktok_mockup(
            ad_image=ad_image,
            brand_name=client,
            caption=primary_text,
            cta=cta,
        )
    else:
        print(f"  ❌ Unsupported platform: {platform}")
        return None
    
    # Save locally with temp file
    fd, temp_path = tempfile.mkstemp(suffix=".png")
    os.close(fd)
    mockup.save(temp_path, "PNG", quality=95)
    print(f"  💾 Saved mockup locally")
    
    if upload:
        # Upload to Fal.ai storage
        print(f"  ☁️  Uploading to cloud storage...")
        mockup_url = upload_to_fal(temp_path)
        print(f"  ✅ Uploaded: {mockup_url[:60]}...")
        
        # Update Airtable
        update_airtable_mockup(record_id, mockup_url, config)
        
        # Cleanup temp file
        Path(temp_path).unlink(missing_ok=True)
        
        return mockup_url
    else:
        # Keep local file for inspection
        local_path = Path(config["paths"]["ad_factory"]) / f"mockup_{record_id}_{platform}.png"
        Path(temp_path).rename(local_path)
        print(f"  💾 Saved to: {local_path.name}")
        return str(local_path)


async def main():
    parser = argparse.ArgumentParser(description="Generate ad mockups for Second Chair")
    parser.add_argument("--record", type=str, help="Airtable record ID to process")
    parser.add_argument("--all", action="store_true", help="Process all records with images but no mockup")
    parser.add_argument("--platform", type=str, default="meta", choices=["meta", "tiktok"], 
                       help="Platform to generate mockup for (default: meta)")
    parser.add_argument("--image-field", type=str, default="img_1", choices=["img_1", "img_2", "img_3"],
                       help="Which image field to use (default: img_1)")
    parser.add_argument("--dry-run", action="store_true", help="Generate mockup but don't upload to Airtable")
    args = parser.parse_args()
    
    if not args.record and not args.all:
        print("Error: Provide --record RECORD_ID or --all")
        sys.exit(1)
    
    print("=" * 60)
    print("AD MOCKUP GENERATOR")
    print("=" * 60)
    print(f"Platform: {args.platform.upper()}")
    print(f"Image Field: {args.image_field.upper()}")
    print(f"Upload: {'No (dry run)' if args.dry_run else 'Yes'}")
    print()
    
    print("[*] Loading Second Chair configuration...")
    config = load_brand_config("Lead_Faucet")
    
    creds = config["credentials"]
    tables = config["airtable"]
    
    api = Api(creds["airtable_pat"])
    table = api.base(creds["airtable_base_id"]).table(tables["images_table"])
    
    if args.record:
        print(f"\n[*] Processing record: {args.record}")
        result = await process_record(
            args.record, 
            config, 
            table, 
            platform=args.platform,
            upload=not args.dry_run,
            image_field=args.image_field,
        )
        if result:
            print(f"\n✅ Mockup generated: {result[:80]}...")
        else:
            print(f"\n❌ Failed to generate mockup")
    
    elif args.all:
        print(f"\n[*] Fetching all records with images...")
        
        field_map = config.get("field_mapping", {})
        img_field = field_map.get("img_1", "IMG")
        mockup_field = field_map.get("social_mockup", "Social Mockup")
        
        # Get all records
        records = table.all()
        
        # Filter: has image, no mockup
        to_process = []
        for record in records:
            fields = record.get("fields", {})
            has_image = bool(fields.get(img_field))
            has_mockup = bool(fields.get(mockup_field))
            
            if has_image and not has_mockup:
                to_process.append(record["id"])
        
        print(f"  Found {len(to_process)} records needing mockups")
        
        for i, record_id in enumerate(to_process, 1):
            print(f"\n[{i}/{len(to_process)}] Processing: {record_id}")
            await process_record(
                record_id, 
                config, 
                table, 
                platform=args.platform,
                upload=not args.dry_run,
                image_field=args.image_field,
            )
    
    print("\n" + "=" * 60)
    print("[DONE] Mockup generation complete")


if __name__ == "__main__":
    asyncio.run(main())
