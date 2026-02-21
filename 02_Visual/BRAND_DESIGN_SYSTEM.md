# Second Chair Brand Design System

**Last Updated:** February 12, 2026  
**Source:** Extracted from secondchair.co  
**Scope:** B2B brand (parent brand) visual standards

---

## Overview

Second Chair's visual identity communicates **elite, selective, and professional** positioning. The design system emphasizes clarity, confidence, and scarcity through minimal aesthetics, bold typography, and restrained color usage.

**Design Philosophy:**
- Confidence through simplicity
- Premium positioning through restraint
- Authority through bold typography
- Exclusivity through negative space

---

## Color Palette

### Primary Colors

| Color | Hex/RGB | Usage |
|-------|---------|-------|
| **Deep Black** | `rgb(10, 10, 10)` / `#0A0A0A` | Primary text, headlines, body copy |
| **Off-White / Light Gray** | `rgb(237, 237, 237)` / `#EDEDED` | Backgrounds, light surfaces |
| **Brand Green** | `rgb(16, 183, 127)` / `#10B77F` | Accent color, CTAs, highlights |

### Secondary Colors

| Color | Hex/RGB | Usage |
|-------|---------|-------|
| **Medium Gray** | `rgb(102, 102, 102)` / `#666666` | Secondary text, metadata, subtitles |
| **Transparent Gray** | `rgba(102, 102, 102, 0.3)` | Borders, dividers, subtle elements |

### Color Usage Guidelines

**Do:**
- Use deep black for all primary content and headlines
- Reserve brand green for strategic emphasis and CTAs
- Use generous white/light gray space to create premium feel
- Keep color palette minimal and restrained

**Don't:**
- Use multiple accent colors
- Add bright or saturated colors
- Use color for decoration—every color has purpose
- Overwhelm with green—it's an accent, not a primary

### Contrast Requirements

- All text must meet WCAG AA standards minimum
- Black on off-white = excellent contrast
- Green accent used sparingly for visibility
- Gray text only for secondary information

---

## Typography

### Font Family

**Primary Typeface:** Inter

```css
font-family: Inter, system-ui, sans-serif;
```

**Why Inter:**
- Clean, modern, professional
- Excellent readability at all sizes
- Strong weight range (100-900)
- Open-source and widely available

### Type Scale & Hierarchy

#### Display / Hero (H1)
- **Font:** Inter
- **Size:** 102.4px (6.4rem)
- **Weight:** 800 (Extra Bold)
- **Line Height:** 94.208px (0.92 of font size)
- **Usage:** Homepage hero, major page headlines
- **Style Notes:** Tight line-height creates impact and density

#### Section Headlines (H2)
- **Font:** Inter
- **Size:** 48px (3rem)
- **Weight:** 800 (Extra Bold)
- **Line Height:** 48px (1.0)
- **Usage:** Section dividers, major statements
- **Style Notes:** Bold, declarative, confident

#### Subsection Titles (H3)
- **Font:** Inter
- **Size:** 20px (1.25rem)
- **Weight:** 600 (Semi-Bold)
- **Line Height:** 28px (1.4)
- **Usage:** Cards, subsections, feature titles
- **Style Notes:** More readable, less aggressive than H1/H2

#### Body Copy
- **Font:** Inter
- **Size:** 16-18px (estimated from rendering)
- **Weight:** 400-500 (Normal to Medium)
- **Line Height:** 1.5-1.6
- **Usage:** Paragraphs, descriptions, explanations

#### Small Text / Metadata
- **Font:** Inter
- **Size:** 14px (0.875rem)
- **Weight:** 400 (Normal)
- **Color:** Medium gray (#666666)
- **Usage:** Captions, labels, footer text

### Typography Usage Guidelines

**Do:**
- Use heavy weights (800) for H1 and H2 to create confidence
- Keep line-height tight on large display type for impact
- Use generous line-height (1.5+) on body copy for readability
- Trust Inter's built-in character and spacing

**Don't:**
- Mix multiple typefaces
- Use decorative or script fonts
- Set body copy in bold weights
- Use all-caps for long passages (short labels OK)

---

## Visual Style

### Photography & Imagery Direction

Based on website analysis:

**Style:** Minimal or absent
- Website relies primarily on typography and negative space
- No heavy use of photography or illustration
- Clean, text-focused layouts

**When imagery is used:**
- Professional, not stock-photo generic
- Documentary/authentic feel preferred over staged
- Support the message, don't distract from it

### Layout Patterns

**Grid & Spacing:**
- Generous white space between sections
- Clear vertical rhythm
- Content-first, decoration-last approach
- Breathing room emphasizes premium positioning

**Content Structure:**
- Bold headlines lead each section
- Short, declarative paragraphs
- Bulleted or numbered lists for clarity
- Clear visual hierarchy guides the eye

**Alignment:**
- Left-aligned text for readability
- Centered layouts for impact statements
- Consistent margins and padding

### UI Patterns

**Buttons / CTAs:**
- Primary action: Brand green background
- Clean, minimal style (no heavy shadows or gradients)
- Clear, action-oriented text
- Ample padding for touch targets

**Cards / Containers:**
- Subtle borders or backgrounds
- Not heavy drop shadows
- Information hierarchy within cards
- Consistent spacing

**Navigation:**
- Clean, minimal header
- Clear link hierarchy
- Professional, restrained

---

## Logo Usage

**Current Status:** Logo not prominently featured on website scrape
**Implication:** Brand relies on typography and voice, not mark-driven identity

**For future logo applications:**
- Should complement minimal, professional aesthetic
- No busy or decorative marks
- Clean, confident, modern
- Works in black/white and with brand green

---

## Brand Applications

### Website
- Clean, minimal layouts
- Typography-first design
- Strategic use of white space
- Bold headlines with restrained body copy
- Green used sparingly for CTAs

### B2B Collateral
- Professional, not flashy
- Trust through clarity
- Authority through simplicity
- Premium feel through restraint

### Documents & Proposals
- Inter for all typography
- Black and green color scheme
- Clean formatting, generous margins
- Hierarchy through size and weight, not color

---

## Competitive Context

**vs. Generic Lead Gen Companies:**
- They use: Busy designs, stock photos, aggressive colors, hype-driven layouts
- We use: Minimal design, bold typography, restrained color, confidence-driven layouts

**Why This Works:**
- Signals premium positioning
- Stands out from crowded, noisy category
- Builds trust through professionalism
- Attracts "elite" firms we're targeting

---

## Design Principles

1. **Confidence Through Simplicity**
   - We don't need decoration to prove our value
   - Clean design signals we're the real deal

2. **Authority Through Typography**
   - Bold, heavy weights establish presence
   - Clear hierarchy guides understanding
   - Text-first design emphasizes substance

3. **Exclusivity Through Restraint**
   - Limited color palette = selective brand
   - Generous white space = premium positioning
   - What we don't show is as important as what we do

4. **Clarity Above All**
   - No confusion about what we do
   - No gimmicks or tricks
   - Straightforward, professional, trustworthy

---

## Technical Specifications

### CSS Variables (Suggested)

```css
:root {
  /* Colors */
  --color-black: #0A0A0A;
  --color-gray-light: #EDEDED;
  --color-gray-medium: #666666;
  --color-gray-transparent: rgba(102, 102, 102, 0.3);
  --color-green: #10B77F;
  
  /* Typography */
  --font-primary: Inter, system-ui, sans-serif;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-extrabold: 800;
  
  /* Type Scale */
  --text-display: 102.4px;
  --text-h2: 48px;
  --text-h3: 20px;
  --text-body: 16px;
  --text-small: 14px;
}
```

### Web Fonts

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
```

---

## Accessibility

- All text meets WCAG AA contrast requirements
- Font sizes are readable at standard viewing distances
- Typography hierarchy supports screen readers
- Color is never the only indicator of meaning
- Interactive elements have sufficient size and spacing

---

## Notes for Designers

**When creating new assets:**
1. Start with typography—let bold headlines do the work
2. Use white space generously—it signals premium
3. Limit color—black, gray, green only
4. Trust the system—don't add decoration
5. Ask: "Does this look like it's for elite firms?" If no, simplify further

**The brand doesn't shout. It states.**

---

## Related Files

- [`BRAND_POSITIONING_CORE.md`](../01_Identity/BRAND_POSITIONING_CORE.md) — Core brand positioning
- [`BRAND_MASTER.md`](../00_Project_Hub/BRAND_MASTER.md) — Brand hub document
- [`Website_Scrape_Raw_2026-02-12.md`](../07_Research/Strategic_Analysis/Website_Scrape_Raw_2026-02-12.md) — Raw scrape data
