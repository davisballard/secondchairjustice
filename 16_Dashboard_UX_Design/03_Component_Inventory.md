# Second Chair — Component Inventory
*Every UI Component, Mapped to the Visual System*
*Luke Grabowski (lead) + Massimo Vignelli (spec verification) | Session: March 2, 2026*

---

## MASSIMO'S FRAMING

*"Every component in this inventory has a direct reference in `06_Digital_Applications.md`. If a component appears here without a reference, it has not been designed — it has been invented, and invention requires my sign-off before it goes into Figma. Luke has been rigorous. Everything here traces back to the specification. That is the correct order of operations."*

## LUKE'S FRAMING

*"I have organized this inventory by component category. Each entry specifies: what the component is, where it appears in the architecture, which section of the visual spec governs it, all functional states, and the content rules that govern what data it displays. A Figma builder should be able to build each component without opening any other document — this inventory is complete."*

---

## COMPONENT CATEGORY 01: SURFACE AND LAYOUT

### 01-A: PRIMARY SCREEN SURFACE

**Visual spec reference:** `06_Digital_Applications.md` § 01 — Screen Backgrounds

| Attribute | Value |
|---|---|
| Background color | `#F0EBE3` |
| Grain overlay | Crane Lettra grain at 3–5% opacity (tileable PNG, 200×200px) |
| Applies to | Main content area background; all screens |

**Never:** `#FFFFFF`, any blue-grey, any cool neutral.

---

### 01-B: SECONDARY SCREEN SURFACE

**Visual spec reference:** `06_Digital_Applications.md` § 01 — Screen Backgrounds

| Attribute | Value |
|---|---|
| Background color | `#E8E3DC` |
| Applies to | Sidebar navigation, secondary panels, alert panel background, data field backgrounds |

---

### 01-C: INVERSE SURFACE

**Visual spec reference:** `06_Digital_Applications.md` § 01 — Screen Backgrounds

| Attribute | Value |
|---|---|
| Background color | `#2C2C2C` (Warm Charcoal) |
| Applies to | High-severity alert banners, dark panel variant (if needed), header bar in dark mode contexts |

---

### 01-D: 12-COLUMN GRID

**Visual spec reference:** `06_Digital_Applications.md` § 05 — Grid and Layout

| Attribute | Value |
|---|---|
| Container width | 1280px |
| Columns | 12 |
| Gutter | 24px |
| Outer margin | 48px |
| Base unit | 8px |
| All element sizes and positions | Snap to 8px grid |

---

## COMPONENT CATEGORY 02: EXHIBIT PANEL (THE PRIMARY CONTAINER)

**Visual spec reference:** `06_Digital_Applications.md` § 04 — Thick-Bordered Chart Panels

This is the most important component in the system. Every analytical output — every chart, every data table, every hero metric — lives inside an Exhibit Panel. The panel is not a card. It does not have rounded corners. It does not have a shadow. It has a thick rule border and deliberate internal structure.

### 02-A: EXHIBIT PANEL (Standard)

| Attribute | Value |
|---|---|
| Border weight | 2px (2pt) Warm Charcoal `#2C2C2C` |
| Border radius | 0px — no radius whatsoever |
| Interior padding | 24px all sides |
| Background | Primary screen surface `#F0EBE3` (same as page — the border creates the object) |
| Box shadow | None |

**Internal structure (top-down order):**
1. Exhibit label: "EXHIBIT [N]:" — Caslon Pro Small Caps, 8–9px, Warm Grey `#8C8680`, tracking +20, positioned 0px from interior top-left (already inside the 24px padding)
2. Exhibit title line: Caslon Pro Regular Italic, 14–16px, Warm Charcoal `#2C2C2C` — states the conclusion, not the subject
3. [Chart or data element]
4. Optional: Source attribution — Caslon Pro Regular 9–10px, Warm Grey, bottom of panel

**States:**
- Default (Populated): Border at full opacity; exhibit label, title, and chart content visible
- Loading: Border visible; exhibit label and title visible; Burgundy 1px progress line animating horizontally within chart area
- Empty: Border visible; exhibit label and title visible; centered Caslon Italic message "No data available for this period."
- Error: Border visible; exhibit label and title visible; Caslon Italic "Data unavailable" in Burgundy; secondary line in Warm Grey Söhne Regular

---

### 02-B: EXHIBIT LABEL

**Visual spec reference:** `06_Digital_Applications.md` § 03 — The Exhibit Convention

| Attribute | Value |
|---|---|
| Typeface | Adobe Caslon Pro |
| Style | True optical small caps (OpenType `smcp` feature — NOT CSS `font-variant: small-caps` on scaled caps) |
| Size | 8–9px on screen |
| Color | Warm Grey `#8C8680` |
| Tracking | +20 |
| Content format | "EXHIBIT [N]:" — colon included, sequential numbering per view |

**Non-negotiable:** True small caps only. Faux small caps (CSS scaling of regular caps) are forbidden. This requires Adobe Caslon Pro or a font file with true `smcp` glyphs.

---

### 02-C: EXHIBIT TITLE LINE

**Visual spec reference:** `06_Digital_Applications.md` § 03 — The Exhibit Convention

| Attribute | Value |
|---|---|
| Typeface | Adobe Caslon Pro Regular Italic |
| Size | 14–16px |
| Color | Warm Charcoal `#2C2C2C` |
| Content rule | States the finding, not the subject: "Lead volume declined 12% in Q1" not "Lead Volume — Q1 2026" |

---

## COMPONENT CATEGORY 03: HERO METRIC DISPLAY

**Visual spec reference:** `06_Digital_Applications.md` § 04 — Dimensional Hero Numbers

### 03-A: PRIMARY HERO NUMBER

Used for the three top-row exhibit panels (Lead Volume, CPSC, Cases Signed).

| Attribute | Value |
|---|---|
| Typeface | Tiempos Headline Bold |
| Size | 64–96px |
| Depth treatment | Side face at -25% lightness of primary color, offset 3–4px right and down |
| Primary face color | Lead Volume: Burgundy `#6B1A1A` | CPSC: Burgundy `#6B1A1A` | Cases Signed: Success Green `#2A6B3C` |
| Shadow | 15% opacity warm shadow, 2px Y offset, 6px blur, `#2C2C2C` |

**Context label (below hero number):**
| Attribute | Value |
|---|---|
| Typeface | Adobe Caslon Pro Small Caps |
| Size | 10px |
| Color | Warm Grey `#8C8680` |
| Content | All caps, describes what the number represents: "LEADS DELIVERED" / "COST PER SIGNED CASE" / "CASES SIGNED" |

**Supporting stat (below context label):**
| Attribute | Value |
|---|---|
| Typeface | Caslon Pro Regular / Söhne Regular |
| Size | 12–13px |
| Content | Delta from prior period: "↓ 12 from last month" — color-coded: Success Green if improvement, Burgundy if decline, Amber if neutral |

---

### 03-B: SECONDARY STAT BLOCK

Used for supporting numbers that appear below hero metrics or in summary panels.

| Attribute | Value |
|---|---|
| Typeface | Söhne Regular 13px |
| Color | Warm Charcoal `#2C2C2C` |
| Delta indicator | Söhne Medium 13px, color-coded per performance direction |
| Label | Söhne Regular 11px, ALL CAPS, +8 tracking, Warm Grey |

---

## COMPONENT CATEGORY 04: CHART COMPONENTS

### 04-A: ISOMETRIC BAR CHART

**Visual spec reference:** `06_Digital_Applications.md` § 04 — Isometric Bar Charts

| Attribute | Value |
|---|---|
| Projection angle | 30-degree true isometric (not perspective distortion) |
| Front face | Primary series color at 100% |
| Top face | Primary color at +20% lightness |
| Side face (right) | Primary color at -25% lightness |
| Bar width | 60% of column slot; 40% spacing |
| Baseline | Single 1px Warm Grey `#8C8680` rule |
| Value labels | Directly above top face of each bar — Caslon Pro 10px, Warm Charcoal |
| Axis labels | Below each bar — Söhne Regular 10px, ALL CAPS, Warm Grey |
| Color key | Caslon Small Caps 8px, inline below chart — only when multi-series |

**Single-series:** Burgundy `#6B1A1A`
**Multi-series order:** Burgundy `#6B1A1A` → Forest Blue `#1B3A6B` → Success Green `#2A6B3C` → Amber `#C9943A` → Warm Teal `#2A6B5C` → Terracotta `#8B3A1E`
**Maximum series:** 6. Overflow grouped as "Other" in Warm Grey `#8C8680`.

**Functional states:**
- Hover: Non-hovered bars shift to 80% opacity; hovered bar remains 100% opacity + tooltip appears
- Loading: Burgundy progress line replaces bars
- Empty: "No data available for this period." — Caslon Italic, Warm Grey, centered

**Tooltip on hover:**
- Background: Secondary surface `#E8E3DC`
- Border: 0.5px Warm Charcoal `#2C2C2C`
- Text: Söhne Regular 12px; Caslon Pro 12px for data values
- Content: [Period label] | [Series name] | [Value]
- No rounded corners, no shadow

---

### 04-B: AREA CHART

**Visual spec reference:** `06_Digital_Applications.md` § 04 — Area Charts

| Attribute | Value |
|---|---|
| Fill opacity | 25% of series color over screen surface |
| Top line | 1.5px solid, 100% opacity of series color |
| Multi-series overlap | Fill opacity reduces to 15% at overlap zone |
| Baseline rule | 0.5px Warm Grey at zero |
| Gridlines | None |
| Value labels | Direct labels at intervals (every 4th period; always current period) — Caslon Pro 10px |

**Functional states:** Same hover, loading, empty behavior as 04-A.

---

### 04-C: DIMENSIONAL DONUT CHART

**Visual spec reference:** `06_Digital_Applications.md` § 04 — Dimensional Pie/Donut Charts

| Attribute | Value |
|---|---|
| Disk height | 12–16px visible edge depth |
| Face | Categorical slices at 100% opacity on top |
| Edge | Each slice's edge at -30% lightness of slice color |
| Drop shadow | 20% opacity warm shadow (`#2C2C2C`), 4px Y offset, 12px blur |
| Inner radius | 40% (donut variant) |
| Hero number (donut center) | Tiempos Headline Bold 28–36px, primary metric total |
| Hero label (below center number) | Caslon Pro Small Caps 9px, Warm Grey |
| Primary slice | Offset 10px outward from center |

**Color key:** Caslon Small Caps 8px, listed horizontally below chart (one line per series: color swatch [8×8px] + label).

**Functional states:** Same as 04-A.

---

### 04-D: CONVERSION FUNNEL CHART

*No direct `06_Digital_Applications.md` component (it is implied by the exhibit system). Massimo sign-off required for this component's visual spec.*

| Attribute | Value |
|---|---|
| Orientation | Vertical (top = largest, bottom = smallest) |
| Stage bars | Horizontal — width proportional to stage count |
| Bar height | 20px per stage |
| Stage gap | 24px between stages |
| Bar color | Burgundy `#6B1A1A` throughout — the narrowing is the visual |
| Stage labels | Caslon Pro Small Caps 9px, Warm Grey, left-aligned of each bar |
| Stage counts | Söhne Medium 12px, right-aligned within each bar |
| Conversion rates | Between stages: Söhne Regular 11px, Warm Grey (e.g., "↓ 68% contacted") |
| Bottom stage | Success Green `#2A6B3C` bar — the signed case count |
| Bottom label | "CASES SIGNED: [N]" — Caslon Pro Small Caps 9px, Success Green |

*Massimo note: "The funnel is the one chart type not fully specified in the digital applications document. The above spec is consistent with the system — single-color treatment, no decorative connectors, Caslon labels, Söhne values, the thick-bordered panel containing it. I approve this treatment."*

---

## COMPONENT CATEGORY 05: DATA TABLES

**Visual spec reference:** `06_Digital_Applications.md` § 04 — Table Rules

### 05-A: STANDARD DATA TABLE

| Attribute | Value |
|---|---|
| Column header typeface | Söhne Medium, 11px, ALL CAPS, tracking +8, Warm Grey `#8C8680` |
| Row data typeface | Söhne Regular 13px, Warm Charcoal `#2C2C2C` |
| Numerical values | IBM Plex Mono 11px, Warm Charcoal (right-aligned) |
| Lead IDs / codes | IBM Plex Mono 11px, Warm Grey |
| Row separator rule | 0.25pt Warm Grey `#8C8680` |
| Section divider rule | 0.5pt Burgundy `#6B1A1A` |
| Totals/summary row separator | Double 0.25pt Warm Grey, 2px apart |
| Row hover | Background shifts to Amber Pale `#F2E4C0` — 150ms ease-out |
| Active/selected row | Background `#E8E3DC` (secondary surface) |
| Column alignment | Left: text labels | Right: numerical values | Center: status indicators |

### 05-B: INLINE BAR TABLE (for geographic/categorical breakdowns)

Same as 05-A with an additional column type:

| Attribute | Value |
|---|---|
| Inline bar column | Proportional-width filled bar within the cell — Burgundy `#6B1A1A` at 60% height of row |
| Bar background | Warm Grey `#8C8680` at 20% opacity (shows full cell width; fill shows proportion) |
| Bar width | Proportional to value (widest = 100% of cell width) |

---

## COMPONENT CATEGORY 06: NAVIGATION COMPONENTS

**Visual spec reference:** `06_Digital_Applications.md` § 06, § 08

### 06-A: SIDEBAR NAVIGATION

| Attribute | Value |
|---|---|
| Sidebar width | 220px |
| Background | Secondary surface `#E8E3DC` |
| Logotype | Second Chair wordmark, top, 24px padding |
| Logotype separator | 0.5pt Burgundy rule, full sidebar width |
| Nav item typeface | Söhne Regular 13px, Title Case |
| Nav item color (default) | Warm Charcoal `#2C2C2C` |
| Nav item color (hover) | No change — cursor changes to pointer |
| Nav item active state | Söhne Medium 13px + 0.5pt Burgundy `#6B1A1A` left-border rule |
| Active indicator width | 3px Burgundy rule flush to left edge |
| Nav item padding | 12px top/bottom, 24px left |
| Bottom rule | 0.5pt Burgundy, above account section items |

### 06-B: PERIOD SELECTOR

| Attribute | Value |
|---|---|
| Typeface | Söhne Regular 11px, ALL CAPS, tracking +8 |
| Active option | Söhne Medium 11px, Burgundy `#6B1A1A` |
| Inactive options | Warm Grey `#8C8680` |
| Separator | Warm Grey `#8C8680` | character (pipe) between options |
| Position | Below main nav items, above bottom section rule in sidebar |

### 06-C: PAGE HEADER

| Attribute | Value |
|---|---|
| Page title typeface | Tiempos Headline Bold, 28–36px, Warm Charcoal |
| Client/account line | Söhne Regular 13px, Warm Grey |
| Period indicator | Söhne Regular 13px, Warm Grey |
| Bottom separator | 0.5pt Burgundy rule, full content-area width |
| Background | Primary screen surface (no separate header background) |

---

## COMPONENT CATEGORY 07: BUTTON AND INTERACTIVE CONTROLS

**Visual spec reference:** `06_Digital_Applications.md` § 06, § 08

### 07-A: PRIMARY BUTTON

| Attribute | Value |
|---|---|
| Background | Warm Charcoal `#2C2C2C` |
| Text | Cream `#F5F0E8`, Söhne Medium 13px, Title Case, tracking +2 |
| Border radius | 0px — no radius |
| Padding | 10px top/bottom, 20px left/right |
| Hover state | Background shifts to Oxford Navy `#1B2A4A` — 150ms ease-out |
| No gradient | None. Flat fill only. |
| No shadow | None. |

### 07-B: SECONDARY BUTTON / TEXT LINK

| Attribute | Value |
|---|---|
| Background | None (transparent) |
| Text | Burgundy `#6B1A1A`, Söhne Medium 13px, Title Case |
| Hover state | Underline appears (0.5pt, Burgundy) — no color change |
| Border | None |

### 07-C: FOCUS STATE (all interactive elements)

| Attribute | Value |
|---|---|
| Outline | 2px Burgundy `#6B1A1A`, 2px offset |
| No browser default | The default blue focus ring is replaced system-wide |

---

## COMPONENT CATEGORY 08: FILTER AND FORM CONTROLS

### 08-A: DROPDOWN / SELECT

| Attribute | Value |
|---|---|
| Background | Primary surface `#F0EBE3` |
| Border | 0.5px Warm Charcoal `#2C2C2C` |
| Border radius | 0px |
| Label typeface | Söhne Regular 12px, Title Case, Warm Charcoal |
| Value typeface | Söhne Medium 12px, Warm Charcoal |
| Dropdown icon | Single 1px stroke chevron, Warm Grey, from standard icon set (Lucide Icons) |
| Open state | Same border; options list appears below with `#E8E3DC` background, 0.25pt rules between options |

### 08-B: DATE RANGE SELECTOR

| Attribute | Value |
|---|---|
| Format | Two text fields: "From [date]" to "To [date]" — IBM Plex Mono 12px for the date values |
| Field background | Secondary surface `#E8E3DC` |
| Calendar popup | Uses standard system/library component; styled to match: `#F0EBE3` background, Burgundy for selected date, Söhne for day labels |

---

## COMPONENT CATEGORY 09: STATUS AND ALERT COMPONENTS

### 09-A: ALERT BANNER (high severity)

| Attribute | Value |
|---|---|
| Background | Warm Charcoal `#2C2C2C` |
| Text | Cream `#F5F0E8`, Söhne Regular 13px |
| Left rule | 3px Burgundy `#6B1A1A` flush left |
| Position | Full content-area width, below page header, above Exhibit 1 |
| Dismiss | "×" right-aligned, Söhne Regular 16px, Cream `#F5F0E8` |

### 09-B: ALERT ITEM (medium/low severity, in alert panel)

| Attribute | Value |
|---|---|
| Left severity rule | 1px left border: Burgundy (high) | Amber `#C9943A` (medium) | Warm Grey `#8C8680` (low/informational) |
| Text | Söhne Regular 13px, Warm Charcoal |
| Action link | Söhne Medium 13px, Burgundy — hover: underline |
| Row separator | 0.25pt Warm Grey |
| Background | Secondary surface `#E8E3DC` |

### 09-C: BADGE / COUNT INDICATOR

| Attribute | Value |
|---|---|
| Background | Burgundy `#6B1A1A` |
| Text | Cream `#F5F0E8`, Söhne Medium 10px, ALL CAPS |
| Shape | 16×16px minimum, no rounded corners (2px max radius — structural not aesthetic) |
| Position | Top-right corner of relevant nav item |

---

## COMPONENT CATEGORY 10: LOADING AND PROGRESS

**Visual spec reference:** `06_Digital_Applications.md` § 06 — Loading States

### 10-A: PANEL LOADING INDICATOR

| Attribute | Value |
|---|---|
| Form | 1px Burgundy `#6B1A1A` horizontal rule |
| Animation | Animate from left to right across panel width |
| Duration | 200ms ease-out per sweep |
| Position | Top of chart area within exhibit panel (below exhibit title line) |
| No spinners | Explicitly forbidden |
| No skeleton screens with colored elements | Explicitly forbidden |

### 10-B: PAGE-LEVEL LOADING INDICATOR

| Attribute | Value |
|---|---|
| Form | 1px Burgundy `#6B1A1A` horizontal rule at very top of viewport |
| Width | Grows from 0% to 100% of viewport width as page loads |
| Disappears | On complete load |

---

## COMPONENT CATEGORY 11: TOOLTIP

**Visual spec reference:** `06_Digital_Applications.md` § 06

| Attribute | Value |
|---|---|
| Background | Secondary surface `#E8E3DC` |
| Border | 0.5px Warm Charcoal `#2C2C2C` |
| Border radius | 0px |
| Text | Söhne Regular 11px, Warm Charcoal |
| Data values within tooltip | Caslon Pro Regular 12px, Warm Charcoal |
| Shadow | None |
| Appear delay | 300ms hover — prevents tooltip flash on pass-through |
| Disappear | Immediate on mouseout |

---

## COMPONENT CATEGORY 12: TYPOGRAPHY TOKENS

*Summary of all type styles used in the product, in one reference location.*

**Visual spec reference:** `06_Digital_Applications.md` § 02

| Token | Typeface | Size | Weight | Case | Color | Tracking |
|---|---|---|---|---|---|---|
| `page-title` | Tiempos Headline Bold | 28–36px | Bold | Title | Warm Charcoal | 0 |
| `section-header` | Tiempos Headline Bold | 22–28px | Bold | Title | Warm Charcoal | 0 |
| `panel-title` | Tiempos Headline Bold | 18–22px | Bold | Title | Warm Charcoal | 0 |
| `exhibit-label` | Caslon Pro Small Caps | 8–9px | Regular SC | SC | Warm Grey | +20 |
| `exhibit-title` | Caslon Pro Regular Italic | 14–16px | Italic | Sentence | Warm Charcoal | 0 |
| `body-prose` | Caslon Pro Regular | 13–14px | Regular | Sentence | Warm Charcoal | 0 |
| `source-attr` | Caslon Pro Regular | 9–10px | Regular | Sentence | Warm Grey | 0 |
| `nav-item` | Söhne Regular | 13px | Regular | Title | Warm Charcoal | +2 |
| `nav-item-active` | Söhne Medium | 13px | Medium | Title | Warm Charcoal | +2 |
| `table-header` | Söhne Medium | 11px | Medium | ALL CAPS | Warm Grey | +8 |
| `table-body` | Söhne Regular | 13px | Regular | Sentence | Warm Charcoal | 0 |
| `button-text` | Söhne Medium | 13px | Medium | Title | (set by button) | +2 |
| `tag-badge` | Söhne Medium | 10px | Medium | ALL CAPS | (set by context) | +10 |
| `tooltip` | Söhne Regular | 11px | Regular | Sentence | Warm Charcoal | 0 |
| `data-mono` | IBM Plex Mono | 11px | Regular | — | Warm Charcoal | 0 |
| `meta-mono` | IBM Plex Mono | 10px | Light | — | Warm Grey | 0 |

---

## COMPONENT CATEGORY 13: COLOR TOKENS

*CSS variable names for all colors used in the product.*

| Token | Value | Usage |
|---|---|---|
| `--sc-cream` | `#F5F0E8` | Brand background (print); email background |
| `--sc-screen` | `#F0EBE3` | Primary screen surface |
| `--sc-screen-secondary` | `#E8E3DC` | Sidebar, secondary panels, field backgrounds |
| `--sc-charcoal` | `#2C2C2C` | Primary text; panel borders; inverse surface |
| `--sc-burgundy` | `#6B1A1A` | Brand accent; active states; rules; Series 1 |
| `--sc-navy` | `#1B2A4A` | Button hover; Oxford Navy; Series 2 alt |
| `--sc-forest-blue` | `#1B3A6B` | Series 2 in multi-series charts |
| `--sc-gold` | `#B8962E` | Old Gold; physical collateral; decorative only |
| `--sc-green` | `#2A6B3C` | Success / positive / cases signed |
| `--sc-amber` | `#C9943A` | Pending / caution / warning |
| `--sc-amber-pale` | `#F2E4C0` | Table row hover |
| `--sc-teal` | `#2A6B5C` | Series 5 |
| `--sc-terracotta` | `#8B3A1E` | Series 6 |
| `--sc-grey-warm` | `#8C8680` | Secondary text; metadata; axis labels; Series overflow |

---

## MASSIMO'S COMPONENT SIGN-OFF

*"This inventory is complete and system-consistent. Every component traces to the specification. The one component that required new specification — the Conversion Funnel Chart (04-D) — has been signed off above.*

*Before Figma build begins, I want to confirm three things in the actual Figma file:*

*First: The Adobe Caslon Pro small caps are rendering with true optical small caps, not scaled regular caps. This is visible immediately — true small caps are slightly wider and have optical compensation; scaled caps look compressed. If it looks compressed, the wrong method is being used.*

*Second: The isometric bar chart projection is true 30-degree isometric, not a perspective distortion. In Figma this means building the bar faces as separate rectangles at the correct angles, not using the 3D transform tool.*

*Third: The 2px panel border is 2px. Not 2pt at 72dpi. Not 1.5px. 2px. At 2x and 3x screen resolution, this should be 4px and 6px respectively in the exported assets. The weight communicates importance. It must be right.*"

---

*Next: `04_Screen_Specifications.md` — the primary Dashboard view, specified panel by panel at Figma-ready detail.*
