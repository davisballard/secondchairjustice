#!/usr/bin/env python3
"""
Comprehensive website scraper for secondchair.co
Extracts all copy, messaging, design elements, and structure
"""

import asyncio
from playwright.async_api import async_playwright
import json
from datetime import datetime
from urllib.parse import urljoin, urlparse

async def extract_design_elements(page):
    """Extract colors, fonts, and visual design elements"""
    design = {
        "colors": [],
        "fonts": [],
        "typography": {}
    }
    
    # Extract computed styles from key elements
    styles = await page.evaluate("""() => {
        const elements = document.querySelectorAll('h1, h2, h3, h4, h5, h6, p, a, button, body');
        const colors = new Set();
        const fonts = new Set();
        const typography = {};
        
        elements.forEach(el => {
            const computed = window.getComputedStyle(el);
            const tagName = el.tagName.toLowerCase();
            
            // Collect colors
            if (computed.color) colors.add(computed.color);
            if (computed.backgroundColor && computed.backgroundColor !== 'rgba(0, 0, 0, 0)') {
                colors.add(computed.backgroundColor);
            }
            
            // Collect fonts
            if (computed.fontFamily) fonts.add(computed.fontFamily);
            
            // Typography hierarchy for headings
            if (tagName.match(/^h[1-6]$/)) {
                typography[tagName] = typography[tagName] || [];
                typography[tagName].push({
                    fontSize: computed.fontSize,
                    fontWeight: computed.fontWeight,
                    lineHeight: computed.lineHeight,
                    letterSpacing: computed.letterSpacing,
                    fontFamily: computed.fontFamily
                });
            }
        });
        
        return {
            colors: Array.from(colors),
            fonts: Array.from(fonts),
            typography: typography
        };
    }""")
    
    return styles

async def extract_page_content(page, url):
    """Extract all content from a page"""
    print(f"  Scraping: {url}")
    
    try:
        await page.goto(url, wait_until="networkidle", timeout=30000)
        await page.wait_for_timeout(2000)  # Wait for any animations
        
        # Extract all text content with structure
        content = await page.evaluate("""() => {
            const result = {
                title: document.title,
                meta_description: document.querySelector('meta[name="description"]')?.content || '',
                headings: {
                    h1: [],
                    h2: [],
                    h3: [],
                    h4: []
                },
                paragraphs: [],
                buttons_ctas: [],
                links: [],
                lists: [],
                forms: []
            };
            
            // Extract headings
            document.querySelectorAll('h1').forEach(h => result.headings.h1.push(h.innerText.trim()));
            document.querySelectorAll('h2').forEach(h => result.headings.h2.push(h.innerText.trim()));
            document.querySelectorAll('h3').forEach(h => result.headings.h3.push(h.innerText.trim()));
            document.querySelectorAll('h4').forEach(h => result.headings.h4.push(h.innerText.trim()));
            
            // Extract paragraphs
            document.querySelectorAll('p').forEach(p => {
                const text = p.innerText.trim();
                if (text.length > 0) result.paragraphs.push(text);
            });
            
            // Extract buttons and CTAs
            document.querySelectorAll('button, a.button, a.btn, [role="button"]').forEach(btn => {
                const text = btn.innerText.trim();
                const href = btn.href || '';
                if (text.length > 0) result.buttons_ctas.push({text, href});
            });
            
            // Extract all links
            document.querySelectorAll('a').forEach(a => {
                const text = a.innerText.trim();
                const href = a.href;
                if (text.length > 0 && href) result.links.push({text, href});
            });
            
            // Extract lists
            document.querySelectorAll('ul, ol').forEach(list => {
                const items = Array.from(list.querySelectorAll('li')).map(li => li.innerText.trim());
                if (items.length > 0) result.lists.push(items);
            });
            
            // Extract form fields
            document.querySelectorAll('form').forEach(form => {
                const fields = Array.from(form.querySelectorAll('input, select, textarea')).map(field => ({
                    type: field.type,
                    name: field.name,
                    placeholder: field.placeholder || '',
                    label: field.labels?.[0]?.innerText || ''
                }));
                if (fields.length > 0) result.forms.push(fields);
            });
            
            return result;
        }""")
        
        return content
        
    except Exception as e:
        print(f"  Error scraping {url}: {e}")
        return None

async def scrape_website():
    """Main scraping function"""
    base_url = "https://www.secondchair.co/"
    scraped_data = {
        "scrape_date": datetime.now().isoformat(),
        "base_url": base_url,
        "pages": {},
        "design": {},
        "all_links": []
    }
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        print("\n🔍 Scraping secondchair.co homepage...")
        
        # Scrape homepage
        homepage_content = await extract_page_content(page, base_url)
        if homepage_content:
            scraped_data["pages"]["homepage"] = homepage_content
            
            # Extract design elements from homepage
            design = await extract_design_elements(page)
            scraped_data["design"] = design
            
            # Get full page text for reference
            full_text = await page.evaluate("() => document.body.innerText")
            scraped_data["pages"]["homepage"]["full_text"] = full_text
        
        # Find and scrape subpages
        print("\n🔍 Finding subpages...")
        all_links = homepage_content.get("links", []) if homepage_content else []
        subpages = set()
        
        for link in all_links:
            href = link.get("href", "")
            if href and href.startswith(base_url):
                parsed = urlparse(href)
                clean_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
                if clean_url != base_url and clean_url not in subpages:
                    subpages.add(clean_url)
        
        print(f"  Found {len(subpages)} subpages")
        scraped_data["all_links"] = list(subpages)
        
        # Scrape each subpage
        for subpage_url in list(subpages)[:10]:  # Limit to first 10 subpages
            page_name = urlparse(subpage_url).path.strip('/').replace('/', '_') or 'page'
            content = await extract_page_content(page, subpage_url)
            if content:
                scraped_data["pages"][page_name] = content
        
        await browser.close()
    
    return scraped_data

def format_as_markdown(data):
    """Convert scraped data to markdown format"""
    md = f"""# LeadFaucet.co Website Scrape
    
**Scrape Date:** {data['scrape_date']}  
**Base URL:** {data['base_url']}

---

## Design Elements

### Color Palette

"""
    
    # Colors
    colors = data.get('design', {}).get('colors', [])
    for color in colors[:20]:  # Limit to first 20
        md += f"- `{color}`\n"
    
    md += "\n### Typography\n\n"
    
    # Fonts
    fonts = data.get('design', {}).get('fonts', [])
    for font in fonts:
        md += f"- {font}\n"
    
    md += "\n### Typography Hierarchy\n\n"
    typography = data.get('design', {}).get('typography', {})
    for tag, styles in typography.items():
        if styles:
            style = styles[0]  # Take first occurrence
            md += f"**{tag.upper()}:**\n"
            md += f"- Font: {style.get('fontFamily', 'N/A')}\n"
            md += f"- Size: {style.get('fontSize', 'N/A')}\n"
            md += f"- Weight: {style.get('fontWeight', 'N/A')}\n"
            md += f"- Line Height: {style.get('lineHeight', 'N/A')}\n\n"
    
    md += "\n---\n\n## Page Content\n\n"
    
    # Homepage content
    homepage = data.get('pages', {}).get('homepage', {})
    if homepage:
        md += f"""### Homepage

**Title:** {homepage.get('title', 'N/A')}  
**Meta Description:** {homepage.get('meta_description', 'N/A')}

#### Headlines (H1)

"""
        for h1 in homepage.get('headings', {}).get('h1', []):
            md += f"- {h1}\n"
        
        md += "\n#### Subheadlines (H2)\n\n"
        for h2 in homepage.get('headings', {}).get('h2', []):
            md += f"- {h2}\n"
        
        md += "\n#### H3 Headings\n\n"
        for h3 in homepage.get('headings', {}).get('h3', []):
            md += f"- {h3}\n"
        
        md += "\n#### Call-to-Action Buttons\n\n"
        for cta in homepage.get('buttons_ctas', []):
            md += f"- **{cta.get('text')}**"
            if cta.get('href'):
                md += f" → `{cta.get('href')}`"
            md += "\n"
        
        md += "\n#### Body Copy (Paragraphs)\n\n"
        for i, para in enumerate(homepage.get('paragraphs', [])[:30], 1):  # Limit to first 30
            md += f"{i}. {para}\n\n"
        
        md += "\n#### Lists\n\n"
        for i, lst in enumerate(homepage.get('lists', []), 1):
            md += f"**List {i}:**\n"
            for item in lst:
                md += f"- {item}\n"
            md += "\n"
        
        md += "\n#### Forms\n\n"
        for i, form in enumerate(homepage.get('forms', []), 1):
            md += f"**Form {i}:**\n"
            for field in form:
                md += f"- {field.get('type')}: {field.get('label') or field.get('placeholder') or field.get('name')}\n"
            md += "\n"
        
        md += "\n---\n\n### Full Page Text\n\n```\n"
        md += homepage.get('full_text', '')[:5000]  # Limit to first 5000 chars
        md += "\n```\n\n"
    
    # Other pages
    for page_name, page_content in data.get('pages', {}).items():
        if page_name == 'homepage':
            continue
        
        md += f"\n---\n\n### Page: {page_name}\n\n"
        md += f"**Title:** {page_content.get('title', 'N/A')}\n\n"
        
        if page_content.get('headings', {}).get('h1'):
            md += "**Headlines:**\n"
            for h1 in page_content.get('headings', {}).get('h1', []):
                md += f"- {h1}\n"
            md += "\n"
    
    # Links found
    md += "\n---\n\n## All Links Found\n\n"
    for link in data.get('all_links', []):
        md += f"- {link}\n"
    
    return md

async def main():
    print("=" * 60)
    print("LeadFaucet.co Website Scraper")
    print("=" * 60)
    
    data = await scrape_website()
    
    print("\n📝 Converting to markdown...")
    markdown = format_as_markdown(data)
    
    # Save markdown
    output_file = f"07_Research/Strategic_Analysis/Website_Scrape_Raw_{datetime.now().strftime('%Y-%m-%d')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print(f"\n✅ Scrape complete! Saved to: {output_file}")
    print(f"   Pages scraped: {len(data['pages'])}")
    print(f"   Links found: {len(data.get('all_links', []))}")
    print(f"   Colors extracted: {len(data.get('design', {}).get('colors', []))}")
    print(f"   Fonts extracted: {len(data.get('design', {}).get('fonts', []))}")

if __name__ == "__main__":
    asyncio.run(main())
