# Second Chair — Color System
*Session: March 1, 2026 | Massimo Vignelli (lead)*

---

## COLOR REGISTER DECISION — LOCKED March 1, 2026

| Context | Color Register | System Document | Notes |
|---|---|---|---|
| **Website / Marketing** | Editorial B&W | `02c_BW_Chart_System.md` | Warm charcoal tonal ladder + pattern fills + oxblood accent only. No categorical palette. Gold excluded. |
| **Dashboard / Product UI** | Full color system | `02_Color_System.md` (this file) | All 6 categorical series colors available. Status palette active. |
| **Print / Identity** | Core brand palette only | `02_Color_System.md` (this file) | Oxblood, Old Gold, Cream, Charcoal. Physical applications only. No extended data palette. |
| **Reports / Decks / Exhibits** | Editorial B&W | `02c_BW_Chart_System.md` | Same as website register. Tonal grays + patterns + oxblood accent. Gold excluded. |

**Rationale:** The website and all editorial materials live in the same visual register as a masthead publication — authority comes from restraint, typography, and tonal precision, not color. Color is reserved for where it earns its place: inside the product, visualizing data that requires categorical distinction across multiple concurrent series.

**Gold (`#B8962E`) is excluded from all chart, document, and screen contexts.** Contrast ratio on cream is ~1.6:1 (near-invisible). Gold exists as a physical material color only — foil, embossing, engraving. See `02c_BW_Chart_System.md` for full rationale.

---

## MASSIMO ON COLOR

*"Every color in this system has a physical origin. Not a digital origin, not a trend reference, not a competitive gap calculation. A physical object that exists in the prestige legal world. We have derived these colors from things. That is what makes them ownable and what makes them authentic.*

*Colors derived from things are not arbitrary. When an attorney sees Cream `#F5F0E8`, their nervous system connects it to the cotton-rag letterhead on a partner's desk. When they see Burgundy `#6B1A1A`, it is the West Federal Reporter spine they pulled off a shelf in law school. These are not colors we chose because they look good together. They look good together because they are from the same physical world.*

*One absolute rule before I specify anything: once these are locked, they do not change. Byron Sharp's work is clear on this — distinctive assets build through repetition. The temptation to 'refresh' the palette within three years destroys the mental structures that the palette builds through consistency. These values are locked. The only acceptable reason to adjust them is a print production calibration between screen values and the Pantone-printed physical object.*"

---

## THE SEVEN COLORS — MASTER SPECIFICATION

### COLOR 1: CREAM / IVORY
**The Highest-Priority Track 2 Asset**

| Attribute | Value |
|---|---|
| **Name** | Cream |
| **Hex** | `#F5F0E8` |
| **RGB** | R: 245, G: 240, B: 232 |
| **HSL** | H: 40°, S: 38%, L: 93% |
| **Pantone (starting point)** | Pantone 9183 C (calibrate vs. physical Crane Lettra 110lb — screen-to-print accuracy critical) |
| **Paper stock** | Crane Lettra 110lb Cover (letterhead/cards); Mohawk Superfine Ultrawhite Eggshell 80lb Text (documents) |
| **CSS variable** | `--sc-cream: #F5F0E8` |
| **Physical origin** | Cotton-rag letterhead stationery; Harvard Law Review paper stock; West Reporter text block |

**WCAG Contrast Ratios on Cream:**
| Text color on Cream | Ratio | Rating |
|---|---|---|
| Warm Charcoal `#2C2C2C` | ~10.1:1 | AAA |
| Oxford Navy `#1B2A4A` | ~9.8:1 | AAA |
| Burgundy `#6B1A1A` | ~7.4:1 | AA (large text passes AA, all text passes AA) |
| Old Gold `#B8962E` | ~2.7:1 | Fail — decorative use only, never text |
| Forest Green `#1E4D2B` | ~8.5:1 | AAA |

**Usage rules:**
- Primary background for all documents, decks, website, letterhead, presentations
- The field that all Second Chair content lives on
- Never use pure white (`#FFFFFF`) in any Second Chair context — cream replaces white as the base
- Digital: Use as `background-color` on `body` and all primary surface elements
- Print: Specify the Pantone value AND the paper stock — both matter

**The cream test:** If you print a Second Chair document on standard white laser paper, it should look wrong. The cream is not a subtle background choice. It is a deliberate one.

---

### COLOR 2: BURGUNDY / OXBLOOD
**The Primary Chromatic Distinctive Asset**

| Attribute | Value |
|---|---|
| **Name** | Burgundy |
| **Hex** | `#6B1A1A` |
| **RGB** | R: 107, G: 26, B: 26 |
| **HSL** | H: 0°, S: 61%, L: 26% |
| **Pantone (starting point)** | Pantone 202 C (calibrate vs. West Federal Reporter spine — the physical object is the reference) |
| **CSS variable** | `--sc-burgundy: #6B1A1A` |
| **Physical origin** | West Federal Reporter spine binding; Harvard Law Review binding (maroon/burgundy buckram); oxblood leather chair |

**WCAG Contrast Ratios for Burgundy:**
| Context | Ratio | Rating |
|---|---|---|
| Burgundy on Cream `#F5F0E8` | ~7.4:1 | AA (passes for all text sizes) |
| Burgundy on White `#FFFFFF` | ~8.2:1 | AAA |
| Cream `#F5F0E8` on Burgundy | ~7.4:1 | AA |
| Old Gold `#B8962E` on Burgundy | ~2.8:1 | Fail — decorative only |

**Usage rules — strict:**
- **Applied as:** 0.5pt horizontal rule (primary), single chart accent color (data visualization only), foil on physical covers, 0.25pt rule under brand name on letterhead
- **Never applied as:** A field color filling large areas (Burgundy is not a background color)
- **Never paired with:** Any shade of red, any warm orange. It lives alongside cream, charcoal, and navy — not alongside warm analogues.
- The Burgundy rule convention: The same 0.5pt weight is used across ALL applications — letterhead, web dividers, data exhibits, business cards, decks. The weight never changes.

**Competitive status:** Zero PI lead gen vendors in the category use Burgundy. The entire category is navy, grey, white, red. Burgundy is permanently unclaimed territory. Every time Second Chair deploys Burgundy, it is building a distinctive asset with zero competitive interference.

---

### COLOR 3: OLD GOLD / BRASS
**Precision Accent — Rules and Lettering Only**

| Attribute | Value |
|---|---|
| **Name** | Old Gold |
| **Hex** | `#B8962E` |
| **RGB** | R: 184, G: 150, B: 46 |
| **HSL** | H: 42°, S: 60%, L: 45% |
| **Pantone (starting point)** | Pantone 872 C (metallic gold — for offset printing; use 109 C for non-metallic spot) |
| **CSS variable** | `--sc-gold: #B8962E` |
| **Physical origin** | Brass door placards; West Reporter spine gold lettering; engraved nameplate lettering; Crane & Co. letterhead embossing |

**Usage rules — very strict:**
- **Applied as:** Rule lines on physical collateral, foil stamping on covers and cards, engraved or letterpress lettering on physical items, reverse text on Navy backgrounds (Gold letters on Navy)
- **Never applied as:** A field color. Never as a background. Never in digital interfaces as a primary element.
- **The aged brass test:** This is aged brass, not polished brass. Pantone 872 C is the starting point — but calibrate toward a warm, slightly desaturated finish. It should look like the nameplate on a 1987 firm's door, not a new trophy.
- **Digital usage:** Use sparingly in digital contexts — primarily for decorative rules on cream backgrounds, never as interactive element states. At small sizes on screens, gold is difficult to render consistently.

---

### COLOR 4: WARM CHARCOAL
**Primary Text Color**

| Attribute | Value |
|---|---|
| **Name** | Warm Charcoal |
| **Hex** | `#2C2C2C` |
| **RGB** | R: 44, G: 44, B: 44 |
| **HSL** | H: 0°, S: 0%, L: 17% |
| **Pantone** | Pantone Black 7 C (warm black) |
| **CSS variable** | `--sc-charcoal: #2C2C2C` |
| **Physical origin** | Quality offset printing on cream paper — the color of well-printed black type that is not pure black |

**Usage rules:**
- Primary text color for all Second Chair copy — body text, headlines, captions, footnotes
- **Why not pure black (`#000000`):** Pure black on cream creates too much contrast — the result reads as harsh, digital, printer-paper. `#2C2C2C` on `#F5F0E8` reads as warm, printed, quality. The difference is perceived, not measured, and it is significant.
- The standard printing equivalent: Request "rich black" or "warm black" from printers rather than 4-color process black
- Works on: Cream `#F5F0E8` (primary), White `#FFFFFF` (acceptable), light grey surfaces

---

### COLOR 5: OXFORD NAVY
**Foreground Element — Not a Field Color**

| Attribute | Value |
|---|---|
| **Name** | Oxford Navy |
| **Hex** | `#1B2A4A` |
| **RGB** | R: 27, G: 42, B: 74 |
| **HSL** | H: 220°, S: 46%, L: 20% |
| **Pantone (starting point)** | Pantone 282 C |
| **CSS variable** | `--sc-navy: #1B2A4A` |
| **Physical origin** | Brooks Brothers suit fabric; American Express Platinum card; Oxford University Press binding |

**Usage rules:**
- **Applied as:** Foreground elements — text on cream, borders, structural elements in specific contexts
- **Never applied as:** The primary field color. The category convention is navy as background. Second Chair does the opposite — cream is the background, navy appears as an element on cream.
- **When to use Navy over Burgundy:** Navy communicates institutional structure. Burgundy communicates legal-specific identity. For data labels and structural typography, Navy can appear alongside Charcoal. For signature elements (the rule, the chart accent, the distinctive system marker), Burgundy is always preferred.
- **Exception:** The Gold-on-Navy combination for engraved/physical items is intentional and specific — it references the West Reporter spine and the brass nameplate directly.

---

### COLOR 6: FOREST GREEN
**Secondary/Variant — West State Reporter**

| Attribute | Value |
|---|---|
| **Name** | Forest Green |
| **Hex** | `#1E4D2B` |
| **RGB** | R: 30, G: 77, B: 43 |
| **HSL** | H: 134°, S: 44%, L: 21% |
| **Pantone (starting point)** | Pantone 350 C |
| **CSS variable** | `--sc-green: #1E4D2B` |
| **Physical origin** | West state/regional reporter spines; Harvard Law Review alternative cover; law school library woodwork |

**Usage rules:**
- Secondary variant for contexts where Burgundy is not appropriate
- May be used as the field color for physical variants of stationery (e.g., a Second Chair deck cover variant)
- Specifically useful for state-market material where the state reporter spine color carries meaning to the attorney audience
- In digital interfaces: Use very sparingly. Primarily a print/physical asset color.

---

### COLOR 7: WARM GREY
**Secondary Text — Supporting Information**

| Attribute | Value |
|---|---|
| **Name** | Warm Grey |
| **Hex** | `#8C8680` |
| **RGB** | R: 140, G: 134, B: 128 |
| **HSL** | H: 30°, S: 5%, L: 53% |
| **CSS variable** | `--sc-grey: #8C8680` |
| **Physical origin** | Marble courthouse floors; Indiana limestone courthouse exterior; aged photocopier paper |

**WCAG Contrast on Cream:**
| Context | Ratio | Rating |
|---|---|---|
| Warm Grey on Cream `#F5F0E8` | ~2.8:1 | Fail for body text — use for captions/labels at 9pt+ only |
| Warm Grey on White `#FFFFFF` | ~3.2:1 | Fail for body text — decorative/caption only |

**Usage rules:**
- Supporting text: captions, footnotes, exhibit labels ("Exhibit n:" in 8pt small caps), page folios, running heads, source attributions
- At the small sizes where it's used, Warm Grey provides visual hierarchy without the emphasis of Charcoal
- Never use for body text — insufficient contrast for extended reading
- In data visualization: secondary data series (supporting bars/lines when Burgundy is the primary accent)

---

## FIGMA COLOR STYLE SETUP

**Create as Figma local styles in this order:**

```
— BRAND COLORS —
SC / Cream         #F5F0E8    (Primary background)
SC / Burgundy      #6B1A1A    (Primary accent)
SC / Charcoal      #2C2C2C    (Primary text)
SC / Gold          #B8962E    (Rules, lettering, foil)
SC / Navy          #1B2A4A    (Foreground elements)
SC / Green         #1E4D2B    (Secondary variant)
SC / Grey          #8C8680    (Supporting text)

— FUNCTIONAL —
SC / White         #FFFFFF    (Never use as background — print white only)
```

**Naming convention:** Use the `SC / [Name]` prefix for all color styles. This namespace separates Second Chair colors from Figma defaults.

---

## CSS DESIGN TOKENS (Three-Tier Architecture)

### Tier 1 — Primitives (Raw Values)

```css
/* Second Chair Color Primitives */
--sc-primitive-cream: #F5F0E8;
--sc-primitive-burgundy: #6B1A1A;
--sc-primitive-charcoal: #2C2C2C;
--sc-primitive-gold: #B8962E;
--sc-primitive-navy: #1B2A4A;
--sc-primitive-green: #1E4D2B;
--sc-primitive-grey: #8C8680;
--sc-primitive-white: #FFFFFF;
```

### Tier 2 — Semantic Tokens (Named by Purpose)

```css
/* Surface */
--sc-surface-primary: var(--sc-primitive-cream);
--sc-surface-secondary: var(--sc-primitive-white);
--sc-surface-inverse: var(--sc-primitive-charcoal);
--sc-surface-brand: var(--sc-primitive-navy);

/* Text */
--sc-text-primary: var(--sc-primitive-charcoal);
--sc-text-secondary: var(--sc-primitive-grey);
--sc-text-inverse: var(--sc-primitive-cream);
--sc-text-brand: var(--sc-primitive-burgundy);
--sc-text-decorative: var(--sc-primitive-gold);

/* Border / Rule */
--sc-border-brand: var(--sc-primitive-burgundy);
--sc-border-subtle: var(--sc-primitive-grey);
--sc-border-strong: var(--sc-primitive-charcoal);

/* Accent */
--sc-accent-primary: var(--sc-primitive-burgundy);
--sc-accent-secondary: var(--sc-primitive-gold);
--sc-accent-tertiary: var(--sc-primitive-navy);

/* Data Visualization */
--sc-data-highlight: var(--sc-primitive-burgundy);
--sc-data-supporting: var(--sc-primitive-grey);
--sc-data-background: var(--sc-primitive-cream);
```

### Tier 3 — Component Tokens (Named by Use)

```css
/* Logo */
--sc-logo-text: var(--sc-text-primary);
--sc-logo-rule: var(--sc-border-brand);
--sc-logo-background: var(--sc-surface-primary);

/* Document */
--sc-doc-background: var(--sc-surface-primary);
--sc-doc-body-text: var(--sc-text-primary);
--sc-doc-caption: var(--sc-text-secondary);
--sc-doc-rule: var(--sc-border-brand);
--sc-doc-exhibit-label: var(--sc-text-secondary);

/* Button (primary) */
--sc-button-bg: var(--sc-primitive-charcoal);
--sc-button-text: var(--sc-primitive-cream);
--sc-button-bg-hover: var(--sc-primitive-navy);

/* Chart */
--sc-chart-field: var(--sc-surface-primary);
--sc-chart-axis: var(--sc-border-subtle);
--sc-chart-data-primary: var(--sc-accent-primary);
--sc-chart-data-supporting: var(--sc-data-supporting);
--sc-chart-title-text: var(--sc-text-primary);
--sc-chart-label-text: var(--sc-text-secondary);
```

---

## PRINT SPECIFICATIONS

### Letterhead (Crane Lettra 110lb)
- Background: Crane Lettra 110lb Fluorescent White (the paper is the cream — DO NOT print cream on white stock)
- Text: 100K (black) — not 4-color process black for small type
- Burgundy rule: Pantone 202 C, 0.5pt
- Gold lettering (engraved version): Pantone 872 C metallic, or deboss + foil on standard

### Business Cards (Engraved)
- Stock: Crane Lettra 220lb duplex (for rigidity)
- Primary: Engraved text in Warm Charcoal equivalent — thermographed or letterpress
- Burgundy rule: Letterpress 0.5pt
- Gold embossed variant: Foil stamp on navy card — the reverse card

### Presentation Decks (Digital → Print)
- Screen: Cream `#F5F0E8` as slide background
- Print: Specify "print on [Mohawk Superfine Ultrawhite Eggshell]" — not standard laser paper
- Burgundy rules: Screen 0.5pt, print 0.5pt hairline at 600dpi minimum

### Pantone Calibration Note
All Pantone starting points listed above (202 C for Burgundy, 872 C for Gold) are **starting points only**. Before final production lockdown, calibrate against:
1. A physical West Federal Reporter volume (Burgundy)
2. The brass nameplate of a pre-1995 law firm building (Gold)
3. Cotton-rag letterhead from Crane & Co. (Cream)
These physical objects are the references. The Pantone numbers are the approximation.

---

## MOTIONAL / INTERACTIVE BRAND PERSONALITY

For digital contexts, the color system communicates the brand's motion personality:

**Brand motion profile:** Professional / Precise (Massimo Mode E token)
- Duration bias: Fast (100–200ms)
- Easing: ease-out
- Spring: No

**Color transition rule for digital:**
- Hover states: Charcoal → Navy (background transitions); Cream → off-white `#EDE8E0` (surface shifts)
- No gradients. No color-to-color transitions between brand colors. Transitions are opacity and position, not color blending.

---

## DATA VISUALIZATION PALETTE EXTENSION
*Updated: March 1, 2026 — Full-Spectrum Expansion. Reference: Nigel Holmes / Time Magazine.*

The brand identity palette (Oxblood, Gold, Cream, Charcoal) is locked for the wordmark, letterhead, stationery, and physical collateral. It does not change.

Data visualization and product dashboards operate under a different mandate. A dashboard showing six data series, status indicators, performance trends, and categorical breakdowns cannot communicate in three colors. Attempting to constrain it produces flat, unreadable, aesthetically stale output — which is exactly what Davis identified in the first round of references.

**The expanded model:** Nigel Holmes at Time Magazine (1977–1993) — 16 years of full-color editorial infographics that were simultaneously typographically disciplined and visually alive. Fortune Magazine, Business Week, National Geographic infographics from the same era. The full spectrum of color, applied at print-register saturation, within an editorial framework of strong typographic structure and clear informational hierarchy.

**The calibration rule:** Every data color should feel like it came from a 1989 Fortune Magazine infographic — muted and deep, not neon and bright. Print quality, not screen maximum. Color serves the data story; it is never decoration.

---

### THE SIX-SERIES CATEGORICAL PALETTE

These are the primary colors for multi-series charts and categorical data. The brand anchor (Burgundy) is Series 1. All added series are calibrated to harmonize with the brand anchor — same saturation register, all slightly warmed or muted from their pure hue.

| Series | Name | Hex | RGB | Character |
|---|---|---|---|---|
| **1** | Burgundy | `#6B1A1A` | R:107 G:26 B:26 | Brand anchor. Primary/negative. Authority. |
| **2** | Forest Blue | `#2B5580` | R:43 G:85 B:128 | Warm steel blue. Deep, serious — not SaaS electric. |
| **3** | Success Green | `#2A6B3C` | R:42 G:107 B:60 | Muted deep green. Universal success convention honored. |
| **4** | Amber | `#C9943A` | R:201 G:148 B:58 | Warm amber. Caution, pending, in-progress. |
| **5** | Warm Teal | `#1E5C55` | R:30 G:92 B:85 | Dark warm teal. Fifth categorical series. |
| **6** | Terracotta | `#8B4522` | R:139 G:69 B:34 | Warm brown-red. Earthy, sixth series. |

**Why each color was chosen:**
- Burgundy: brand anchor, already in identity system, most authoritative
- Forest Blue: every attorney has interacted with serious institutional blue (federal court, AmLaw publications) — this is that blue desaturated and warmed, not the SaaS category blue
- Success Green: universal data convention. Users will read green as positive regardless of brand intent. Fighting this wastes cognitive load. The green chosen (`#2A6B3C`) is distinct from brand Forest Green (`#1E4D2B`) — darker, slightly cooler — to avoid confusion
- Amber: warmest of the series, reads naturally as caution/in-progress/pending, continuous with the Old Gold brand color at a lighter value
- Warm Teal: rounds out the cool-warm spectrum, distinctive from both blue and green
- Terracotta: a sixth earthy warm tone for complex dashboards requiring six categorical series

---

### FILL VARIANTS — AREA CHARTS AND BACKGROUNDS

Each series color has three variants for semi-transparent fills, area charts, and background differentiation.

| Series | Fill (30%) | Fill (15%) | Pale Background |
|---|---|---|---|
| Burgundy | `#C47878` | `#E1BCBC` | `#F3E8E8` |
| Forest Blue | `#7CA8CC` | `#BED4E6` | `#E5EFF7` |
| Success Green | `#7AB88E` | `#BDDBC7` | `#E5F2EA` |
| Amber | `#E4C07A` | `#F2E0BD` | `#FAF3E4` |
| Warm Teal | `#76AFAA` | `#BBD7D5` | `#E5F0EF` |
| Terracotta | `#C4947A` | `#E2CABD` | `#F5EDE8` |

**Implementation note:** These fill values are computed at the specified opacity over the screen surface `#F0EBE3`. In CSS, use `rgba()` or `opacity` property rather than hex — the hex values above are approximate composites for Figma use.

---

### STATUS INDICATOR MAPPING

Universal data conventions are honored. These are the single-instance status colors — for badges, indicators, alerts, and performance signals.

| Status | Color | Hex | Convention |
|---|---|---|---|
| **Positive / Success** | Success Green | `#2A6B3C` | Universal: green = good |
| **Caution / Pending** | Amber | `#C9943A` | Universal: yellow/amber = watch |
| **Negative / Alert** | Burgundy | `#6B1A1A` | Brand anchor doubles as alert |
| **Informational** | Forest Blue | `#2B5580` | Institutional blue = reference |
| **Neutral / Inactive** | Warm Grey | `#8C8680` | Already in brand system |

**Status fill backgrounds (for badge/chip backgrounds):**
| Status | Background Hex |
|---|---|
| Positive | `#E5F2EA` |
| Caution | `#FAF3E4` |
| Negative | `#F3E8E8` |
| Informational | `#E5EFF7` |
| Neutral | `#EDEAE7` |

---

### WCAG CONTRAST — CATEGORICAL SERIES ON SCREEN SURFACE

Screen surface: `#F0EBE3`

| Color | Hex | Ratio on `#F0EBE3` | Rating |
|---|---|---|---|
| Burgundy | `#6B1A1A` | ~7.0:1 | AA — all text |
| Forest Blue | `#2B5580` | ~5.8:1 | AA — all text |
| Success Green | `#2A6B3C` | ~5.5:1 | AA — all text |
| Amber | `#C9943A` | ~2.7:1 | Fill/large elements only — not for body text |
| Warm Teal | `#1E5C55` | ~5.9:1 | AA — all text |
| Terracotta | `#8B4522` | ~4.3:1 | AA — large text and UI |

**The label rule:** All data labels, axis labels, exhibit titles, and annotations are always Warm Charcoal `#2C2C2C` or Warm Grey `#8C8680` — regardless of bar/line color. The data element communicates the category through color; the text label communicates the value through high-contrast type. These are separate jobs and should never be combined.

---

### DATA VISUALIZATION USAGE RULES

**Rule 1 — Color serves the data story.**
Following the Nigel Holmes model: color communicates category, magnitude, comparison, status. If a color element were removed and the meaning of the chart didn't change, the color is not doing its job.

**Rule 2 — Use the series palette in order.**
For multi-series charts, assign Series 1 (Burgundy) to the primary or most important data series, then Series 2, 3, 4 in order. Never skip series or assign colors out of order — the palette is calibrated as a set, and skipping creates visual imbalance.

**Rule 3 — Maximum 6 series per chart.**
Six categorical colors is the maximum for a single chart. If more than six categories exist, group the lower categories into an "Other" series in Warm Grey `#8C8680`. More than six distinct colors on a single chart produces visual noise, not information.

**Rule 4 — Labels are always high-contrast.**
All text on charts (axis labels, data labels, titles, annotations) is Warm Charcoal `#2C2C2C`. The only exception: text on a dark colored bar (Burgundy or Forest Blue series) may be Cream `#F5F0E8` if the bar is wide enough to contain the label. Never amber, teal, or terracotta text anywhere.

**Rule 5 — Area fills at 20–30% opacity, solid line at top.**
Area charts use semi-transparent fills (20–30% of the series color) with a solid 1.5px line at the top of the fill. This is the standard editorial area chart treatment from the Holmes/Fortune era. The fill reads the area; the line reads the trend.

**Rule 6 — The structure comes from rules, not color.**
Column separators: 0.25pt Warm Grey. Section dividers: 0.5pt Burgundy. Total rows: double 0.25pt rules. The grid is invisible. Structure is communicated by rule weight; status is communicated by color. Never use color to do what a rule weight should do.

**Rule 7 — The Exhibit label governs everything.**
Every chart, data panel, and table carries "EXHIBIT N:" in Adobe Caslon Pro small caps, 8pt, Warm Grey `#8C8680`, at the top left. Non-negotiable. This is what makes Second Chair's data output immediately recognizable as Second Chair.

---

### FIGMA DATA STYLE ADDITIONS — UPDATED

```
— CATEGORICAL SERIES —
SC / Data / S1 Burgundy       #6B1A1A    (= SC/Burgundy — reused)
SC / Data / S2 ForestBlue     #2B5580
SC / Data / S3 SuccessGreen   #2A6B3C
SC / Data / S4 Amber          #C9943A
SC / Data / S5 WarmTeal       #1E5C55
SC / Data / S6 Terracotta     #8B4522

— STATUS INDICATORS —
SC / Status / Positive        #2A6B3C
SC / Status / Caution         #C9943A
SC / Status / Negative        #6B1A1A    (= SC/Burgundy — reused)
SC / Status / Info            #2B5580
SC / Status / Neutral         #8C8680    (= SC/Grey — reused)

— STATUS BACKGROUNDS —
SC / Status / Positive BG     #E5F2EA
SC / Status / Caution BG      #FAF3E4
SC / Status / Negative BG     #F3E8E8
SC / Status / Info BG         #E5EFF7
SC / Status / Neutral BG      #EDEAE7
```

---

### CSS DATA TOKENS — FULL-SPECTRUM UPDATE

**Tier 1 additions:**
```css
/* Categorical Series Primitives */
--sc-primitive-forest-blue: #2B5580;
--sc-primitive-success-green: #2A6B3C;
--sc-primitive-amber: #C9943A;
--sc-primitive-warm-teal: #1E5C55;
--sc-primitive-terracotta: #8B4522;

/* Status Background Primitives */
--sc-primitive-positive-bg: #E5F2EA;
--sc-primitive-caution-bg: #FAF3E4;
--sc-primitive-negative-bg: #F3E8E8;
--sc-primitive-info-bg: #E5EFF7;
--sc-primitive-neutral-bg: #EDEAE7;
```

**Tier 2 additions (data semantic layer):**
```css
/* Categorical Series */
--sc-data-series-1: var(--sc-primitive-burgundy);
--sc-data-series-2: var(--sc-primitive-forest-blue);
--sc-data-series-3: var(--sc-primitive-success-green);
--sc-data-series-4: var(--sc-primitive-amber);
--sc-data-series-5: var(--sc-primitive-warm-teal);
--sc-data-series-6: var(--sc-primitive-terracotta);

/* Status Indicators */
--sc-status-positive: var(--sc-primitive-success-green);
--sc-status-caution: var(--sc-primitive-amber);
--sc-status-negative: var(--sc-primitive-burgundy);
--sc-status-info: var(--sc-primitive-forest-blue);
--sc-status-neutral: var(--sc-primitive-grey);

/* Status Backgrounds */
--sc-status-positive-bg: var(--sc-primitive-positive-bg);
--sc-status-caution-bg: var(--sc-primitive-caution-bg);
--sc-status-negative-bg: var(--sc-primitive-negative-bg);
--sc-status-info-bg: var(--sc-primitive-info-bg);
--sc-status-neutral-bg: var(--sc-primitive-neutral-bg);
```

---

## WHAT THIS COLOR SYSTEM EXCLUDES

Two separate exclusion lists now apply: one for brand identity materials, one for data visualization.

### Exclusions for Brand Identity Materials (Wordmark, Stationery, Letterhead, Physical Collateral)

These rules apply when Second Chair's brand appears as an *identity* — the wordmark, the stationery suite, the physical objects that carry the prestige register.

**Permanently excluded from brand identity:**
- Pure white `#FFFFFF` as a background (reads as photocopier paper)
- Pure black `#000000` as a text color (too harsh against cream)
- Any blue as a primary or accent color (category convention — differentiation requires avoiding it in the identity layer)
- Any red that reads as urgency or ambulance-chaser (saturated reds, fire-truck reds)
- Any orange as a primary color (consumer brand warmth — wrong register)
- Any purple (no physical origin in the prestige legal world)
- Gradients of any kind
- Any color used purely decoratively, without derivation from a physical object in the prestige legal world

### Exclusions for Data Visualization (Dashboards, Charts, Reports, Decks)

The full-spectrum categorical palette is available in data visualization contexts. The following remain excluded even there:

- **Neon / RGB-maximum saturation:** Any color that reads as backlit digital rather than print quality. Run every proposed data color against the calibration question: "Would this color appear in a 1989 Fortune Magazine infographic?" If no, it doesn't belong.
- **Gradients between data states:** Transitions from one performance state to another are communicated through discrete data elements (two bars, a delta arrow, a percentage change label) — never through a gradient fill
- **More than 6 categorical series per chart:** More than six creates visual noise; group overflow into "Other" in Warm Grey
- **Cool greys as neutral:** Warm Grey `#8C8680` is the neutral data color. Cool greys (blue-grey, silver) feel like generic SaaS defaults and conflict with the brand's warm palette

**The one exception that proves the rule:** The screen-only pure white (`#FFFFFF`) in the `--sc-surface-secondary` semantic token is available for contexts where cream cannot be rendered accurately (some email clients). Use only as fallback.

---

**Permanently excluded:**
- Pure white `#FFFFFF` as a background (reads as photocopier paper)
- Pure black `#000000` as a text color (too harsh against cream)
- Any blue (category convention — completely unavailable for Second Chair's differentiation strategy)
- Any red (urgency/ambulance-chaser signal)
- Any orange (consumer brand warmth — wrong register)
- Any purple (arbitrary, no physical origin in the legal world)
- Gradients of any kind
- Any color not derivable from a physical object in the prestige legal world

**The one exception that proves the rule:** The screen-only pure white (`#FFFFFF`) in the `--sc-surface-secondary` semantic token is available for contexts where the cream cannot be rendered accurately (some email clients). Use only as fallback.

---

*Color system complete. See `03_Typography_System.md` for the typographic system that lives on this palette.*
