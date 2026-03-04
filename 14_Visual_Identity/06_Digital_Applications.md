# Second Chair — Digital Applications: The Intelligence Register
*The Second Register: Screens, Dashboards, Data, and Digital Product*
*Massimo Vignelli (systems) + Graham Fink (art direction) | March 1, 2026*

---

## WHAT THIS DOCUMENT IS

The analog authority layer is built: wordmark, stationery, physical collateral, the law library world. That register communicates trust and aspiration to PI attorneys before Second Chair says a word.

This document builds the second register: every digital surface Second Chair produces. CRM dashboards, performance reports, sales presentations, email templates, web interfaces. The screens that prove Second Chair can actually deliver what the brand promises.

**These are not two separate brands.** They are two rooms in the same building. The typefaces are the same. The rule weights are the same. The Exhibit convention bridges both. What changes is the context — physical object versus illuminated screen — and the color approach that context requires.

---

## THE DESIGN PREMISE

The source of this register's aesthetic is **what the best print designers of 1986–1995 were doing in annual reports, consulting presentations, and business editorial** — applied now to digital surfaces, without the technological constraints that existed then. The references are IBM Annual Reports, McKinsey exhibits, WSJ data pages, HBR editorial layouts.

What computer screens actually looked like in that era is not the reference. CRT monitors and early Mac UI are **selective inputs** — the grid discipline and high-contrast rule logic of early Mac, the pixel-precision craft of Susan Kare — not the dominant aesthetic. The overall read of any Second Chair screen must be: authoritative and modern. Era-intelligent craft details appear on closer inspection, never as the first impression.

**The synthesis test (applied before every design decision):**
1. Does this read as authoritative and modern first?
2. Does the era-specific craft intelligence show itself on closer inspection?
3. Is the aesthetic serving the function — or getting in the way of it?

If question 1 fails, or question 3 is "getting in the way" — redesign toward function.

---

## THE FAILURE MODES

Before specifications: what this system explicitly is not.

**Not generic SaaS:** No Salesforce. No HubSpot. No rounded corners on everything, no colored sidebars, no "card" layouts with shadow effects, no gradient buttons, no emoji in UI copy. The entire category of PI lead gen tools looks like this. Second Chair does not.

**Not flat and stale:** Restricting data visualization to one accent color on a cream background produces the visual equivalent of a black-and-white page in a color magazine — technically correct, completely lifeless. The Nigel Holmes / Time Magazine model is the antidote: full-spectrum color applied within a disciplined typographic structure. Color should communicate; it should have energy; it should make an attorney want to look at the data, not dread opening the dashboard.

**Not retrofuturism:** No neon, no CRT-dominated screens, no terminal green-on-black, no fake scanlines, no holographic effects. These communicate "novelty product" to a PI attorney, not "credible analytical partner."

**Not an old law firm's IT department:** No Comic Sans, no Times New Roman in system default rendering, no blue hyperlink underlines, no clip art icons, no tables with blue header rows. The dated aesthetic in the other direction.

**The defensible territory:** Print design intelligence applied natively to digital. Modern in function, principled in aesthetic. The kind of product that makes an attorney say "these people clearly know what they're doing" — not from a single flashy element, but from the accumulated evidence of deliberate choices at every level of the interface.

---

## SURFACE SPECIFICATIONS

### 01 — SCREEN BACKGROUNDS

**Primary screen surface:** `#F0EBE3`
A slightly cooler, slightly more neutral version of Cream `#F5F0E8`. Warm cast without being too amber for sustained screen reading. Distinguishable from pure white (`#FFFFFF`) — which reads as blank, digital, default — and from full cream — which can feel heavy on backlit screens at standard brightness.

**Secondary screen surface (panels, sidebars):** `#E8E3DC`
One step darker and cooler than primary. Used for sidebar panels, secondary content areas, modal backgrounds. Creates gentle surface hierarchy without introducing a new color.

**Inverse surface (dark panels, high-contrast moments):** `#2C2C2C`
Warm Charcoal — the same as the primary text color. When a dark surface is needed (a header bar, a modal overlay, a data panel in high-contrast mode), it uses Warm Charcoal — not pure black, not a navy, not a dark grey. The continuity is intentional: the same value that makes type on cream reads as warm and quality makes a dark panel feel considered rather than harsh.

**Background never:** `#FFFFFF` pure white, `#000000` pure black, any blue-grey, any cool neutral.

---

### 02 — TYPOGRAPHY IN DIGITAL CONTEXTS

The typography system (Tiempos + Caslon + Söhne) carries from the analog register into digital without modification. The typefaces are the strongest continuity signal across both rooms.

**UI Primary — Söhne Regular / Medium (Klim Type Foundry)**
All navigation, labels, metadata, table column headers, button text, tag text, form field labels. The UI's working voice. Söhne is Klim's contemporary grotesque — engineered for screen clarity while retaining the warmth of its historical antecedents (Akzidenz-Grotesk, early Helvetica). It pairs with Caslon and Tiempos without visual conflict.

| Context | Size | Weight | Case | Tracking |
|---|---|---|---|---|
| Navigation items | 13px | Regular | Title | +2 |
| Table column headers | 11px | Medium | ALL CAPS | +8 |
| Button text | 13px | Medium | Title | +2 |
| Form labels | 12px | Regular | Title | 0 |
| Tag/badge text | 10px | Medium | ALL CAPS | +10 |
| Tooltip text | 11px | Regular | Sentence | 0 |

**Display / Section Headers — Tiempos Headline Bold (Klim Type Foundry)**
Page titles, section headers, dashboard panel titles, report headers. The editorial authority of Tiempos in digital contexts carries the same weight as in print — it signals that this screen is a document, not an application.

| Context | Size | Weight | Case |
|---|---|---|---|
| Dashboard page title | 28–36px | Bold | Title |
| Section header | 22–28px | Bold | Title |
| Report title | 32–48px | Bold | Title |
| Panel title | 18–22px | Bold | Title |

**Data & Prose — Adobe Caslon Pro**
Exhibit labels, long-form report prose, analytical descriptions, footnotes. Caslon appears wherever the content is analytical or documentary in nature — where the user is reading, not scanning.

| Context | Size | Style | Case |
|---|---|---|---|
| Exhibit label ("EXHIBIT N:") | 8–9px | Small Caps | SC |
| Report body prose | 13–14px | Regular | Sentence |
| Chart conclusion titles | 14–16px | Regular Italic | Sentence |
| Source attribution | 9–10px | Regular | Sentence |
| Footnotes | 10–11px | Regular | Sentence |

**Raw Data / Metadata — IBM Plex Mono (IBM)**
Used selectively in contexts where the data is machine-generated, highly precise, or technical: API response timestamps, lead IDs, tracking codes, raw performance numbers in dense tables, system log entries. The monospace signals precision and machine accuracy — it appears as a craft detail in data fields, never as the dominant typeface on a surface.

| Context | Size | Weight |
|---|---|---|
| Lead ID / reference number | 11px | Regular |
| Timestamp | 10px | Regular |
| Dense data table values | 11px | Regular |
| System/log metadata | 10px | Light |

**The monospace rule:** IBM Plex Mono appears only where the data's machine origin is functionally relevant. If removing the monospace would not change what the data communicates, it should not be monospace. This is a functional signal, not an aesthetic one — the aesthetic benefit is a consequence, not the reason.

---

### 03 — THE EXHIBIT CONVENTION — THE BRIDGE BETWEEN BOTH REGISTERS

The single most important distinctive asset in the digital register. Every data panel, every chart, every table, every analytical output carries this label.

**"EXHIBIT [N]:"**

| Attribute | Specification |
|---|---|
| Typeface | Adobe Caslon Pro |
| Style | True optical small caps (never CSS `font-variant: small-caps` on scaled caps) |
| Size | 8–9px on screen; 7–8pt in print |
| Color | Warm Grey `#8C8680` |
| Position | Top-left of the exhibit/panel, above the exhibit title |
| Tracking | +20 |
| Numbering | Sequential within a report/session; resets per document |

**Exhibit title line (below the label):**
- Typeface: Adobe Caslon Pro Regular Italic
- Size: 14–16px
- Color: Warm Charcoal `#2C2C2C`
- Content: The conclusion, not the subject. "Cost per signed case declined 23% in Q4" not "CPSC Performance."

**Why this works:**
- Zero PI lead gen competitors use it — it is completely unclaimed territory
- Every attorney with exposure to BigLaw, consulting, or serious litigation recognizes it as a signal of analytical rigor
- It creates immediate categorical separation: this is not another vendor dashboard, this is an analytical document
- It works at every scale — a single chart on a screen, a printed monthly report, a slide in a pitch deck
- The courtroom origin (evidence designation) resonates unconsciously with the audience whether or not they consciously identify it

---

### 04 — CHART AND DATA VISUALIZATION SYSTEM

**The reference model has expanded.** Initial specs referenced IBM Annual Reports and WSJ chart discipline — precise, restrained, one-accent. That discipline remains for printed documents, single-series exhibits, and table-format data. But dashboards, performance reports, and multi-series analytical views now operate under the Nigel Holmes / Time Magazine model: full-spectrum color, editorial energy, tactful dimensionality. The calibration standard: "Would this appear in a 1989 Fortune Magazine infographic?" Not "Would this appear in a 2023 SaaS dashboard?"

**The non-negotiable typographic structure (unchanged):**
The typography, exhibit labels, rule weights, and grid discipline do not change. Color and dimensionality work *within* this structure, never instead of it. The Exhibit convention is still the first thing seen. The chart title still states the conclusion. Labels are still directly on data elements. The structure is still invisible — felt, not announced.

---

**THE CHART RULES — UPDATED:**

**01 — Title = Conclusion.**
Every chart title states the finding, not the subject. "Cost per signed case declined 23% in Q4" not "CPSC Trend." The reader knows the point before reading the chart. This does not change.

**02 — Direct labels only.**
Data values labeled directly on or immediately adjacent to the data element. No floating legend boxes — the series colors are distinct enough to be identified from a color key at the bottom of the chart (Caslon small caps, 8pt, inline). No color key tables that require the eye to travel off-chart to understand the data.

**03 — Full categorical palette for multi-series charts.**
Single-series charts: Burgundy `#6B1A1A` as the primary accent — unchanged.
Multi-series charts: Use the 6-series categorical palette in order (Burgundy → Forest Blue → Success Green → Amber → Warm Teal → Terracotta). Series 1 is always the most important or primary data series. Maximum 6 series per chart; group overflow as "Other" in Warm Grey `#8C8680`.
Status/performance charts: Success Green `#2A6B3C` = positive, Burgundy `#6B1A1A` = negative, Amber `#C9943A` = pending — universal conventions honored.

**04 — Structure from rules and borders, not from decoration.**
No gridlines except a single 0.5px baseline at zero. No rounded corners on bars. Chart panels sit inside thick 2pt rule borders (see Dimensional Treatments below) — the border frames the chart as an object with presence. Color communicates meaning; rule weight communicates structure; dimensional form communicates importance. These jobs do not overlap.

**05 — Cream canvas.**
Every chart lives on screen surface `#F0EBE3`. No white chart backgrounds. No colored panel backgrounds behind charts. The chart is part of the surface.

**06 — Table rules (unchanged).**
Column separators: 0.25pt Warm Grey rule. Section dividers: 0.5pt Burgundy rule. Total/summary rows: double 0.25pt rules, 2pt apart. Column headers: Söhne Medium, ALL CAPS, +8 tracking.

---

**DIMENSIONAL CHART FORMS — THE ACTUAL SPEC:**

The previous version described "a 4% top highlight on bars." That is not dimensional. The following are the actual chart form specifications that produce visual energy, designed presence, and the Time Magazine / Fortune register that distinguishes Second Chair from every other tool in the category.

The test before any dimensional treatment: does it read as *designed on purpose*, not as a Microsoft Office default? If an attorney looks at it and thinks "Excel," the treatment has failed.

---

**01 — ISOMETRIC BAR CHARTS**

Bar charts are rendered in isometric 3D projection. Each bar is a rectangular prism with three visible faces — not a flat rectangle with a highlight.

- **Projection angle:** 30-degree isometric (true isometric, not a perspective distortion)
- **Front face:** The primary color of the series (e.g., Burgundy `#6B1A1A` for Series 1)
- **Top face:** The primary color at +20% lightness — this is the face that catches "light"
- **Side face (right):** The primary color at -25% lightness — this is the shadow face
- **Bar width:** Each bar occupies 60% of its column slot; 40% is spacing
- **Baseline:** All bars share a single 1px Warm Grey baseline rule — the isometric floor
- **Labels:** Data values sit directly above the top face of each bar, in Caslon 10pt Warm Charcoal
- **Color key:** Caslon small caps, 8pt, inline below the chart — never a floating legend box

The isometric treatment makes the dashboard read as deliberately designed — the same bars in a flat chart read as a spreadsheet export. The same bars in isometric 3D read as a data product with intention.

---

**02 — DIMENSIONAL PIE / DONUT CHARTS**

Pie charts are rendered as physical disk objects with visible edge depth — not flat circles.

- **Disk height:** 12–16px of visible edge depth below the flat face of the pie
- **Face:** The pie slices in their full categorical colors on the flat top surface
- **Edge:** Each slice's edge in that color at -30% lightness — the shadow side of the disk
- **Drop shadow:** 20% opacity warm shadow (color: `#2C2C2C`) at 4px Y offset, 12px blur beneath the entire disk — lifts the chart off the surface
- **Highlighted/exploded slice:** The primary slice (the most important data point) is offset 10px outward from the center, with a visible gap to the rest of the disk
- **Donut variant:** A 40% inner radius version of the above — the donut hole shows the screen surface color (`#F0EBE3`), and a single hero number (the total or primary metric) sits centered inside in Tiempos Headline Bold at 28–36px

The disk form is how Nigel Holmes and Fortune Magazine rendered pies in the 1980s — physical objects on a surface, not flat SVG circles. The difference in perceived quality is immediate.

---

**03 — DIMENSIONAL HERO NUMBERS**

Featured single-metric callouts (the most important number on the dashboard) are rendered with dimensional depth — the number appears to have physical material and presence.

- **Depth treatment:** The numeral is rendered with a side face and bottom face at -25% lightness of the number color, offset 3–4px right and down from the main face
- **Main face color:** Series 1 Burgundy `#6B1A1A` or Success Green `#2A6B3C` depending on metric type
- **Shadow:** 15% opacity warm shadow, 2px Y offset, 6px blur, `#2C2C2C`
- **Size:** 64–96px Tiempos Headline Bold — the number is the largest element on the screen
- **Context label:** Caslon Pro small caps, 10pt, Warm Grey `#8C8680`, beneath the number — "COST PER SIGNED CASE" or "LEADS SIGNED THIS MONTH"
- **Supporting micro-data:** Caslon Pro 12pt below the context label — trend direction, period comparison, delta percentage

This is the equivalent of a magazine cover number — the stat that an attorney photographs and sends to their partner. It has presence because it is designed to have presence.

---

**04 — THICK-BORDERED CHART PANELS**

Every chart element sits inside a thick rule-bordered panel. This is the frame that makes the dashboard read as a collection of designed objects, not a grid of floating data elements.

- **Border weight:** 2pt (2px) Warm Charcoal `#2C2C2C` — the same color as primary text
- **Border style:** Solid rule, no radius (no rounded corners)
- **Interior padding:** 24px on all sides between the border and the chart content
- **Exhibit label position:** Inside the panel, top-left, 8px from the top border — the "EXHIBIT N:" label sits inside the frame, not above it
- **Panel background:** Screen surface `#F0EBE3` — same as the page; the border creates the object, not a background color change
- **Panel sizing:** Panels snap to the 8-point grid and 12-column layout — no arbitrary sizing

The thick border is the single most visible signal that a dashboard was designed by someone, not generated by a SaaS template. It is the equivalent of the matt frame on a gallery photograph — it transforms the contents from data to an analytical object.

---

**05 — AREA CHARTS**

Area charts use semi-transparent fills with solid lines — the standard editorial treatment from the Holmes / Fortune era.

- **Fill opacity:** 25% of the series color (calculated over the screen surface `#F0EBE3`)
- **Top line:** 1.5px solid line at the top of the fill, 100% opacity of the series color
- **Multi-series stacking:** Where series overlap, the fill opacity reduces to 15% at the overlap zone — two overlapping fills create natural depth without muddying
- **Baseline rule:** Single 0.5px Warm Grey rule at zero — the floor the area sits on

---

**THE 3D TEST (always apply):**
Does this dimensional form read as *designed* — something an attorney would notice and feel good about using — or does it read as a template choice someone made without thinking? If it's the latter, redesign toward either a simpler flat element or a more committed dimensional treatment. The worst outcome is halfway — dimensionality that looks like an accident.

**Never permitted:**
- Default PowerPoint/Excel extruded 3D (perspective rotation, fake vanishing point)
- Drop shadows on text elements
- Beveled or embossed UI chrome
- Fake lighting rigs or specular highlights on interface elements
- Gradient fills on bars (the isometric three-face treatment replaces gradients entirely)

---

### 05 — GRID AND LAYOUT

**The invisible structure:**
Every Second Chair screen operates on an 8-point base grid (8px increments). Every element snaps to this grid. This is never announced — it is only felt as the sense that everything is in the right place.

**Column structure:**
Dashboard and report layouts use a 12-column grid at 1280px container width, with 24px gutters and 48px outer margins. On narrower screens, the grid collapses to 8 columns (tablet) and 4 columns (mobile) — the content reorganizes, the grid discipline does not relax.

**White space as structure:**
The area around a data exhibit communicates that the exhibit is what matters. Minimum 32px clearance between exhibits on the same surface. Minimum 48px from any exhibit to the panel edge. The space is not wasted — it is structural.

**Panel hierarchy:**
- Primary panels: 100% surface width, Tiempos Headline Bold title, 48px top padding
- Secondary panels: up to 6/12 columns, Tiempos Headline Bold title at smaller scale, 32px top padding
- Inline exhibits (within prose): full content width, flush left, Caslon exhibit label

---

### 06 — INTERACTIVE STATES AND MOTION

**Hover states:**
- Text links: Color shift from Charcoal `#2C2C2C` to Burgundy `#6B1A1A`. No underline added (underline is not part of the typographic system).
- Button hover: Background shifts from Charcoal `#2C2C2C` to Navy `#1B2A4A`. Transition: 150ms ease-out. No scale change, no shadow addition.
- Table rows: Background shifts from transparent to Amber Pale `#F2E4C0`. Subtle, warm, deliberate.
- Data bars: Opacity shift to 80% on hover of adjacent non-selected bars. The selected bar remains at 100%.

**Focus states (accessibility):**
- A 2px Burgundy `#6B1A1A` outline, 2px offset. Visible and on-brand. Never the browser default blue focus ring.

**Motion profile:**
- Duration: 100–200ms for UI transitions (hover, state changes)
- Duration: 200–350ms for panel appearances, modal entries
- Easing: ease-out for all transitions
- No spring physics, no bounce, no elastic easing — these read as playful; the register is precise
- No color-to-color transitions between brand colors — transitions are opacity and position changes, not color blends

**Loading states:**
- A thin 1px Burgundy `#6B1A1A` progress line at the top of the loading area — the same rule weight as the brand rule, animated
- No spinner icons with rounded corners, no pulsing skeleton screens with blue gradients
- If a skeleton screen is functionally necessary: a subtle opacity pulse (60–100%) on the surface color `#F0EBE3` — the surface itself breathes, no colored skeleton elements

---

### 07 — TEXTURE AND CRAFT DETAILS

**Paper grain overlay:**
A subtle noise/grain texture is applied at 3–5% opacity over all screen surfaces. This prevents the flat, anti-aliased uniformity of digital backgrounds from reading as generic. The texture source: high-resolution scan of Crane Lettra cotton-rag paper (the same physical stock used for Second Chair letterhead). At 3–5% it is not visible as a distinct element — it is felt as warmth.

**Implementation:**
```css
.sc-surface {
  background-color: #F0EBE3;
  background-image: url('/assets/textures/crane-lettra-grain.png');
  background-size: 200px 200px;
  background-repeat: repeat;
  /* grain layer at 4% opacity, overlaid on solid background */
}
```

The texture file: a 200×200px tileable PNG of the Crane Lettra grain, exported at full resolution from a physical scan, then reduced to 4% opacity in the layer. The tiling seams should be imperceptible.

**Rule weights (locked, no exceptions):**
| Rule | Weight | Color |
|---|---|---|
| Brand rule (letterhead, cards, section dividers, chart dividers) | 0.5pt / 1px | Burgundy `#6B1A1A` |
| Table column separator | 0.25pt / 0.5px | Warm Grey `#8C8680` |
| Table total row | Double 0.25pt, 2px apart | Warm Grey `#8C8680` |
| Focus outline | 2px | Burgundy `#6B1A1A` |
| Chart baseline (zero line) | 0.5px | Warm Grey `#8C8680` |

These weights are identical to the analog register's rule conventions. The continuity is deliberate and non-negotiable.

**Monospace data field treatment:**
In any field displaying machine-generated data (IDs, timestamps, codes): IBM Plex Mono at 11px, Warm Grey `#8C8680`. The field background shifts to `#E8E3DC` (secondary surface) to frame the data field as distinct from prose. No border on the field — the surface color contrast is sufficient.

---

### 08 — COMPONENTS THAT DO NOT EXIST IN THIS SYSTEM

The following UI components are specifically excluded because they carry the visual language of generic SaaS or consumer apps:

- **Rounded corners on cards or buttons** — No radius above 2px (a 2px radius is structural, not aesthetic). Cards with 8px, 12px, or 24px radius are explicitly not Second Chair.
- **Colored sidebar navigation** — The sidebar (if present) is the secondary surface `#E8E3DC` — not burgundy, not charcoal, not any color that makes it read as an accent element.
- **Gradient buttons** — All buttons are flat, single color. No gradient fills.
- **Card shadow effects** — No `box-shadow` creating lifted or floating card appearances. Surface hierarchy is communicated by background color difference, not by shadow.
- **Color-coded navigation items** — Navigation items do not change color by section or category. They are Söhne Regular in Charcoal, with active state indicated by a 0.5pt Burgundy left-border rule, not by color fill.
- **Emoji in UI copy** — Not in labels, button text, empty states, or system messages.
- **Progress bars with gradient fill** — A progress indicator is a thin 1px Burgundy rule filling from left to right. No gradient, no glow, no animation faster than 200ms.
- **Illustration or abstract icons** — Icons are a single-weight 1px stroke, Warm Grey `#8C8680`, from a single consistent icon set (e.g., Lucide Icons — stroke-based, minimal). No filled illustrations, no decorative iconography.

---

### 09 — EMAIL TEMPLATES

Email clients cannot reliably render custom fonts, paper grain textures, or precise color management. The degraded environment requires additional guidance.

**Email-safe font stack:**
```css
font-family: 'Söhne', 'Helvetica Neue', Helvetica, Arial, sans-serif;
```

**Email-safe color fallbacks:**
- Background: `#F0EBE3` (most clients render hex colors correctly — cream is safe)
- Primary text: `#2C2C2C`
- Burgundy rule: `#6B1A1A` — rendered as a 1px top/bottom border on a `<div>`, not as a CSS rule
- If cream cannot render: fallback to `#FFFFFF` pure white — this is the only context where white is acceptable

**Email layout:**
- Single column, 600px max-width
- No multi-column layouts (email client fragmentation)
- The brand rule appears as a horizontal divider between header and body
- The "EXHIBIT N:" convention can appear in email performance reports — rendered as HTML text in Caslon-stack equivalent

---

### 10 — THE SEQUENCE: UI BEFORE EDITORIAL PHOTOGRAPHY

The dashboard and digital product must be **designed first**. Actual screens must exist before any editorial photography or mockup context is created. The sequence:

1. Design the actual UI (screens, charts, dashboard panels) according to this specification
2. Test against the synthesis test: authoritative and modern first; craft details on closer inspection
3. Only after the screens are approved: generate Higgsfield editorial photography showing the screens in brand-world physical contexts
4. The photographic mockup shows the real screen — not a representation of what the screen might look like

This is not a visual direction problem being solved by AI-generated imagery. It is a product design problem being solved by a designer. The imagery follows the product.

---

## WHAT THIS REGISTER DOES FOR THE BRAND

| | The Analog Register | The Intelligence Register |
|---|---|---|
| **Context** | Law library, brass, cream paper, oxblood cloth | Dashboard, report, pitch deck, digital surface |
| **Typefaces** | Same: Tiempos + Caslon + Söhne | Same: Tiempos + Caslon + Söhne |
| **Background** | Cream `#F5F0E8` | Screen cream `#F0EBE3` |
| **Primary accent** | Burgundy `#6B1A1A` | Burgundy `#6B1A1A` |
| **Rule weight** | 0.5pt everywhere | 0.5pt everywhere |
| **Exhibit convention** | In print decks and proposals | On every digital data panel |
| **What it says** | "We understand who you are" | "We can deliver what we promise" |
| **When attorneys see it** | First impression (sales materials, physical presence) | After signing (dashboard, reports, ongoing relationship) |

The McKinsey Exhibit convention is the bridge that makes both rooms feel like the same building. An attorney sees "EXHIBIT 1:" in the pitch deck → sees "EXHIBIT 7:" in the dashboard → sees "EXHIBIT 3:" in the monthly report. Same label, same typeface, same 8pt small caps. The brand is consistent without being repetitive.

---

*Digital Applications specification complete.*
*See `02_Color_System.md` for extended data visualization palette.*
*See `07_Research/04_Visual_Research/11_Tech_And_Data_Visual_Layer/` for the full reference research.*
*UI design execution: Begin in Figma. Build the actual screens before any editorial photography.*
