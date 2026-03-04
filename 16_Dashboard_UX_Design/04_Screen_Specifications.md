# Second Chair — Screen Specifications
*Primary Dashboard View: Panel-by-Panel Figma-Ready Detail*
*Luke Grabowski (lead) + Massimo Vignelli + Graham Fink | Session: March 2, 2026*

---

## HOW TO USE THIS DOCUMENT

This document specifies the primary Dashboard view at pixel-level detail for Figma execution. It should be read alongside:

- `03_Component_Inventory.md` — component definitions and all states
- `14_Visual_Identity/06_Digital_Applications.md` — the master visual specification
- `14_Visual_Identity/02_Color_System.md` — all color values

**Coordinate system used here:**
- X: measured from left edge of content area (right edge of sidebar)
- Y: measured from top of content area (below browser chrome)
- Columns: 1–12 of the 12-column grid within the content area

**Viewport assumption:** 1280px total width. Sidebar: 220px + 48px outer margin = 268px. Content area: 1012px, beginning at X:268.

---

## CANVAS SETUP (Figma)

```
Frame name: Dashboard — Populated State
Frame width: 1440px (browser at 1440px viewport)
Frame height: 960px minimum (extend as needed for content)
Background: --sc-screen (#F0EBE3)
Grain overlay: Yes — Crane Lettra grain PNG at 4% opacity, tiled
Grid: 12-column, 24px gutter, 48px margin (within 1012px content area)
Font styles: Load from Component Inventory typography tokens
Color styles: Load from Component Inventory color tokens
```

---

## PANEL 00: SIDEBAR

```
Component: Sidebar Navigation (06-A)
X: 0
Y: 0
Width: 220px
Height: 960px (full viewport height)
Background: --sc-screen-secondary (#E8E3DC)
```

**Internal elements (top to bottom):**

```
[SECOND CHAIR LOGOTYPE]
  Component: Wordmark (Direction A or B per logo decision)
  X: 24px from sidebar left
  Y: 24px from sidebar top
  Width: 172px (172 = 220 - 24 - 24)
  Scale: Equivalent to ~14px type size
  Color: --sc-charcoal (#2C2C2C)

[LOGOTYPE SEPARATOR]
  Component: Brand rule
  X: 0
  Y: [logotype baseline + 16px]
  Width: 220px (full sidebar width)
  Height: 0.5px
  Color: --sc-burgundy (#6B1A1A)

[NAV ITEMS — vertical list]
  Starting Y: [separator Y + 24px]
  Item height: 44px (12px top + 20px line height + 12px bottom)
  Item width: 220px

  Item 1: "Dashboard" — ACTIVE
    Text: Söhne Medium 13px, --sc-charcoal, Title Case
    Left rule: 3px × 44px, --sc-burgundy, flush left
    Text X: 24px (left padding)

  Item 2: "Leads"
    Text: Söhne Regular 13px, --sc-charcoal, Title Case
    Left rule: none
    Text X: 24px

  Item 3: "Performance"
    Text: Söhne Regular 13px, --sc-charcoal, Title Case

  Item 4: "Reports"
    Text: Söhne Regular 13px, --sc-charcoal, Title Case

[PERIOD SELECTOR]
  Y: [after nav items + 32px gap]
  Label: "PERIOD" — Söhne Regular 10px, ALL CAPS, +8 tracking, --sc-grey-warm
  Options (horizontal row): "MTD | QTD | 30D | 90D"
    - Active: Söhne Medium 11px, --sc-burgundy
    - Inactive: Söhne Regular 11px, --sc-grey-warm
    - Separator " | ": --sc-grey-warm
  Y: [label baseline + 8px]

[BOTTOM SEPARATOR RULE]
  Y: 920px (pushed near bottom)
  Width: 220px
  Height: 0.5px
  Color: --sc-burgundy

[BOTTOM NAV ITEMS — below rule]
  Item: "Account"
    Text: Söhne Regular 13px, --sc-charcoal, Title Case
    Y: [rule Y + 16px]
```

---

## PANEL 00-B: PAGE HEADER

```
X: 268px (start of content area)
Y: 0
Width: 1172px (content area to right margin: 1440 - 268 - 48 outer right = but let's use 1172)
Height: 80px
Background: --sc-screen (same as page)
```

**Internal elements:**

```
[PAGE TITLE]
  Text: "Dashboard"
  Typeface: Tiempos Headline Bold
  Size: 36px
  Color: --sc-charcoal (#2C2C2C)
  X: 0 (flush to content area left)
  Y: 16px from top of header

[ACCOUNT INFO LINE]
  Text: "[Client Firm Name] · Account #[ID]"
  Typeface: Söhne Regular 13px
  Color: --sc-grey-warm (#8C8680)
  X: 0
  Y: [page title baseline + 8px]

[PERIOD INDICATOR — right-aligned]
  Text: "March 2026 — Month to Date"
  Typeface: Söhne Regular 13px
  Color: --sc-grey-warm
  X: right-aligned to content area right edge
  Y: [same Y as account info line]

[HEADER SEPARATOR RULE]
  X: 0
  Y: 76px (bottom of header area)
  Width: full content area width
  Height: 0.5px
  Color: --sc-burgundy (#6B1A1A)
```

---

## PANEL 01: EXHIBIT 1 — LEAD VOLUME (HERO)

```
Component: Exhibit Panel (02-A) containing Hero Metric (03-A)
Grid position: Columns 1–4
X: 0 (relative to content area)
Y: 112px (header 80px + separator 0.5px + 32px gap)
Width: [4 columns = (1012px content - 3×24px gutters) / 12 × 4 + 3×24px gutters]
  = (1012 - 72) / 12 × 4 + 72 = 940/12 × 4 + 72 = 78.33 × 4 + 72 = 313.33 + 72 ≈ 385px
  → Use 385px
Height: 200px
Panel border: 2px solid --sc-charcoal
Panel background: --sc-screen
Interior padding: 24px
```

**Internal elements (all X/Y relative to panel interior origin, i.e., 24px from panel edges):**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 1:"
  Typeface: Adobe Caslon Pro, OpenType smcp (true small caps)
  Size: 9px
  Color: --sc-grey-warm (#8C8680)
  Tracking: +20
  X: 0, Y: 0

[EXHIBIT TITLE]
  Text: "47 leads delivered in March — up 12% from February"
  (Replace with actual data; "up" = +, Success Green; "down" = −, Burgundy)
  Typeface: Adobe Caslon Pro Regular Italic
  Size: 14px
  Color: --sc-charcoal
  X: 0, Y: [exhibit label baseline + 6px]
  Max width: 85% of interior width (allow right margin)

[HERO NUMBER]
  Text: "47"
  Typeface: Tiempos Headline Bold
  Size: 80px
  Primary face color: --sc-burgundy (#6B1A1A)
  Depth effect:
    - Duplicate text layer
    - Offset: +4px X, +3px Y
    - Color: Burgundy at -25% lightness = #3D0F0F
    - Place below primary layer
  Shadow: Drop shadow — color #2C2C2C, opacity 15%, Y offset 2px, blur 6px
  X: 0, Y: [exhibit title baseline + 16px]

[CONTEXT LABEL]
  Text: "LEADS DELIVERED"
  Typeface: Adobe Caslon Pro Small Caps (true, via smcp)
  Size: 10px
  Color: --sc-grey-warm
  X: 0, Y: [hero number baseline + 8px]

[DELTA STAT]
  Text: "+12 from February (↑ 34%)"
  Typeface: Söhne Regular 13px
  Color: [positive = --sc-green #2A6B3C; negative = --sc-burgundy; neutral = --sc-grey-warm]
  X: 0, Y: [context label baseline + 6px]
```

---

## PANEL 02: EXHIBIT 2 — COST PER SIGNED CASE (HERO)

```
Grid position: Columns 5–8
X: [Exhibit 1 right edge + 24px gutter]
Y: 112px (same row as Exhibit 1)
Width: 385px (same as Exhibit 1)
Height: 200px
Panel border: 2px solid --sc-charcoal
```

**Internal elements:**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 2:"
  [same spec as Exhibit 1 label]

[EXHIBIT TITLE]
  Text: "Cost per signed case is $847 — down 18% from last month"
  [same spec as Exhibit 1 title]

[HERO NUMBER]
  Text: "$847"
  [same spec as Exhibit 1 hero]
  Primary face color: --sc-burgundy (efficiency is the inverse — lower = better)

[CONTEXT LABEL]
  Text: "COST PER SIGNED CASE"

[DELTA STAT]
  Text: "−$186 from February (↓ 18%)"
  Color: --sc-green (cost declining = positive)

[INTEGRATION NOTE — conditional]
  Appears only if intake integration is not connected.
  Text: "Based on cases reported via intake — connect your CRM for automatic tracking."
  Typeface: Caslon Pro Regular 10px
  Color: --sc-grey-warm
  Position: Below delta stat
```

---

## PANEL 03: EXHIBIT 3 — CASES SIGNED

```
Grid position: Columns 9–12
X: [Exhibit 2 right edge + 24px gutter]
Y: 112px
Width: 385px (note: 3 panels × 385px + 2 gutters × 24px = 1155 + 48 = 1203px — slightly over 1012px due to rounding)
```

*Column math correction: 1012px content area ÷ 12 columns = 84.33px/column + gutters. For 4-column panel: 4 × 84.33 + 3 × 24 = 337.33 + 72 = 409.33 ≈ 409px. Three 4-column panels + 2 gutters = 3 × 409 + 2 × 24 = 1227 + 48 = 1275px — this exceeds 1012px because the formula needs to account for the 12-column grid precisely.*

*Corrected calculation: Total content width = 1012px. 11 gutters of 24px = 264px. Column width = (1012 - 264) / 12 = 62.33px. 4-column panel = 4 × 62.33 + 3 × 24 = 249.33 + 72 = 321.33 ≈ 321px.*

*Revised: Three 4-col panels = 3 × 321 + 2 × 24 = 963 + 48 = 1011px. Correct.*

**Corrected width for all hero trio panels: 321px each.**

```
Grid position: Columns 9–12
X: [Content area start + 321px + 24px + 321px + 24px = Content area start + 690px]
Y: 112px
Width: 321px
Height: 200px
Panel border: 2px solid --sc-charcoal
```

**Internal elements:**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 3:"

[EXHIBIT TITLE]
  Text: "9 cases signed from Second Chair leads this month"

[HERO NUMBER]
  Text: "9"
  Primary face color: --sc-green (#2A6B3C)
  Depth color: --sc-green at -25% lightness = #173D21

[CONTEXT LABEL]
  Text: "CASES SIGNED"

[SUPPORTING STATS]
  Row 1: "Sign rate: 19.1% of leads" — Söhne Regular 12px
  Row 2: Case type mini-breakdown (if 3 or fewer types):
    "Auto: 6  ·  Slip & Fall: 2  ·  Other: 1"
    Typeface: Söhne Regular 12px, --sc-grey-warm
```

---

## SECTION SEPARATOR RULE

```
X: 0 (content area left)
Y: [hero trio bottom edge + 32px]
Width: full content area (1012px)
Height: 0.5px
Color: --sc-burgundy
```

---

## PANEL 04: EXHIBIT 4 — LEAD VOLUME TREND

```
Component: Exhibit Panel (02-A) containing Isometric Bar Chart (04-A)
Grid position: Columns 1–8
X: 0
Y: [section separator Y + 32px]
Width: [8 columns = 8 × 62.33 + 7 × 24 = 498.67 + 168 = 666.67 ≈ 667px]
Height: 280px
Panel border: 2px solid --sc-charcoal
Interior padding: 24px
```

**Internal elements:**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 4:"

[EXHIBIT TITLE]
  Text: "Lead volume has held steady over 13 weeks — average 41 leads/week"
  (Title dynamically reflects trend: "grown," "declined," "held steady")

[ISOMETRIC BAR CHART]
  Chart area: Interior width minus padding = 667 - 48 = 619px
  Chart height: 160px
  Bars: 13 bars (one per week, trailing 13 weeks)
  Bar type: Isometric 3D (30-degree true isometric)
  Bar color:
    - Weeks 1–12: --sc-burgundy front face | #7F2020 top | #45100F side
    - Week 13 (current, incomplete): --sc-amber front | #D9A440 top | #7A5520 side
  Bar width: 60% of column slot
  Baseline: 0.5px --sc-grey-warm rule

  [AXIS LABELS — below bars]
    Typeface: Söhne Regular 10px, ALL CAPS, --sc-grey-warm
    Content: Week ending date (abbreviated: "FEB 3", "FEB 10", etc.)
    Label every bar; if too crowded, label every 2nd bar
    Current period: "THIS WEEK" in Söhne Medium, --sc-amber

  [VALUE LABELS — above each bar]
    Typeface: Caslon Pro Regular 10px, --sc-charcoal
    Content: Lead count (e.g., "43")
    Position: Centered above top face of each bar

  [TREND ANNOTATION — inside panel, below chart]
    Text: "13-week average: 41 leads/week  ·  Trailing 13 weeks: Jan 13 – Mar 9, 2026"
    Typeface: Caslon Pro Regular Italic 12px, --sc-grey-warm
    Y: [chart bottom + 12px]
```

---

## PANEL 05: EXHIBIT 5 — CONVERSION FUNNEL

```
Component: Exhibit Panel (02-A) containing Conversion Funnel Chart (04-D)
Grid position: Columns 9–12
X: [Exhibit 4 right edge + 24px gutter]
Y: [same Y as Exhibit 4]
Width: [4 columns = 321px]
Height: 280px (matches Exhibit 4)
Panel border: 2px solid --sc-charcoal
Interior padding: 24px
```

**Internal elements:**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 5:"

[EXHIBIT TITLE]
  Text: "19.1% of leads become signed cases — up from 14.2% last month"

[FUNNEL CHART]
  Available width: 321 - 48 = 273px
  Available height: 280 - 48 - [exhibit label + title heights ≈ 50px] = ~182px

  Stage 1: LEADS DELIVERED
    Bar width: 100% of available (273px)
    Bar height: 20px
    Color: --sc-burgundy
    Label (left): "LEADS DELIVERED" — Caslon Pro Small Caps 9px, --sc-grey-warm
    Count (in bar): "47" — Söhne Medium 12px, --sc-cream

  [CONVERSION RATE BETWEEN STAGES]
    Text: "↓ 68% contacted"
    Typeface: Söhne Regular 11px, --sc-grey-warm
    Y: [Stage 1 bottom + 6px]

  Stage 2: CONTACTED
    Bar width: 68% of 273px = 186px (proportional to contact rate)
    Bar height: 20px
    Color: --sc-burgundy
    Label: "CONTACTED" — Caslon Pro Small Caps 9px
    Count: "32" — Söhne Medium 12px, --sc-cream

  [CONVERSION RATE]
    Text: "↓ 53% consulted"

  Stage 3: CONSULTATIONS
    Bar width: 53% of 186px = 99px
    Bar height: 20px
    Color: --sc-burgundy
    Label: "CONSULTATIONS"
    Count: "17"

  [CONVERSION RATE]
    Text: "↓ 53% signed"

  Stage 4: CASES SIGNED
    Bar width: 53% of 99px = 52px
    Bar height: 20px
    Color: --sc-green (#2A6B3C)
    Label: "CASES SIGNED" — Caslon Pro Small Caps 9px, --sc-green
    Count: "9" — Söhne Medium 12px, --sc-cream

  Note: All stage bars are LEFT-aligned within the panel. The progressive narrowing reads as the funnel effect.
```

---

## SECTION SEPARATOR RULE 2

```
X: 0
Y: [Exhibits 4+5 bottom edge + 32px]
Width: 1012px
Height: 0.5px
Color: --sc-burgundy
```

---

## PANEL 06: EXHIBIT 6 — CPSC TREND

```
Component: Exhibit Panel (02-A) containing Area Chart (04-B)
Grid position: Columns 1–6
X: 0
Y: [Section separator 2 Y + 32px]
Width: [6 columns = 6 × 62.33 + 5 × 24 = 374 + 120 = 494px]
Height: 240px
Panel border: 2px solid --sc-charcoal
Interior padding: 24px
```

**Internal elements:**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 6:"

[EXHIBIT TITLE]
  Text: "Cost per signed case has declined 18% over 13 weeks — from $1,033 to $847"

[AREA CHART]
  Chart area: 494 - 48 = 446px wide, ~140px tall
  Series: Single — CPSC by week, trailing 13 weeks
  Line: 1.5px solid --sc-burgundy
  Fill: --sc-burgundy at 25% opacity over --sc-screen background
  Baseline: 0.5px --sc-grey-warm rule at chart bottom

  Y-axis: No labels on axis itself — values labeled directly on line
    Label at weeks: Week 1, Week 4, Week 8, Week 13 (always label first and last)
    Label format: "$1,033" — Caslon Pro Regular 10px, --sc-charcoal
    Position: Above the line at labeled points; if first/last, allow right-align on last

  X-axis labels: Week ending dates, abbreviated — Söhne Regular 10px, ALL CAPS, --sc-grey-warm
    Label week 1, week 7, week 13

  Trend annotation: Inside panel, below chart
    Text: "↓ 18% over 13 weeks · Average: $921/signed case"
    Text color: --sc-green (declining cost = improvement)
    Typeface: Caslon Pro Regular Italic 12px
```

---

## PANEL 07: EXHIBIT 7 — CHANNEL EFFICIENCY

```
Component: Exhibit Panel (02-A) containing Isometric Bar Chart (04-A) — multi-series
Grid position: Columns 7–12
X: [Exhibit 6 right edge + 24px gutter]
Y: [same Y as Exhibit 6]
Width: [6 columns = 494px]
Height: 240px
Panel border: 2px solid --sc-charcoal
Interior padding: 24px
```

**Internal elements:**

```
[EXHIBIT LABEL]
  Text: "EXHIBIT 7:"

[EXHIBIT TITLE]
  Text: "Meta delivers leads at $31 CPL vs. $54 on Google — 42% more efficient"

[ISOMETRIC BAR CHART — MULTI-SERIES]
  Chart area: 494 - 48 = 446px wide, ~130px tall
  Groups: 2 (Meta, Google)
  Series per group: 2 (Lead Count, CPL)
  
  Series 1: Lead Count
    Color: --sc-burgundy
    
  Series 2: CPL
    Color: --sc-forest-blue (#1B3A6B)

  Bar arrangement: Within each group, two bars side by side, 4px gap between them
  Inter-group gap: 32px
  
  Group labels (below bar groups):
    "META" | "GOOGLE"
    Typeface: Söhne Medium 11px, ALL CAPS, +8 tracking, --sc-grey-warm

  Value labels:
    Lead Count bars: "34 leads" above — Caslon Pro 10px, --sc-charcoal
    CPL bars: "$31" or "$54" above — IBM Plex Mono 11px, --sc-charcoal (machine data)

  Baseline: 0.5px --sc-grey-warm

  [INLINE COLOR KEY]
    Below chart, horizontal:
    [● Burgundy swatch 8×8px] "Lead Count"   [● Navy swatch 8×8px] "Cost Per Lead"
    Typeface: Caslon Pro Small Caps 8px, --sc-grey-warm
    Note: Swatches are solid-filled 8×8px squares, no rounded corners
```

---

## PANEL 08: ALERT PANEL (Conditional)

```
Appears only when alerts exist.
Position: Below Exhibits 6+7, full content area width
X: 0
Y: [Exhibits 6+7 bottom + 32px]
Width: 1012px
Background: --sc-screen-secondary (#E8E3DC)
Border: None (status layer, not an exhibit)
Padding: 20px all sides
```

**Internal elements:**

```
[PANEL HEADING]
  Text: "ACCOUNT STATUS"
  Typeface: Söhne Medium 11px, ALL CAPS, +8 tracking, --sc-grey-warm

[ALERT ITEMS — vertical list]
  Each item:
    Left rule: 3px solid [severity color]
    Left padding: 12px from rule
    Alert text: Söhne Regular 13px, --sc-charcoal
    Action link (if present): Söhne Medium 13px, --sc-burgundy — right-aligned on same line
    Bottom rule: 0.25px --sc-grey-warm
    Padding: 12px top/bottom per item

  Example items:
    [Burgundy rule] "Payment due March 15 — Invoice #2026-03"   [VIEW INVOICE]
    [Amber rule] "Lead volume is tracking 15% below March target"   [VIEW LEADS]
```

---

## PAGE FOOTER

```
X: 0
Y: [last panel bottom + 48px]
Width: 1012px
Height: 48px
```

**Internal elements:**

```
[FOOTER RULE]
  Width: 1012px, 0.5px --sc-burgundy, at top of footer

[FOOTER TEXT — left-aligned]
  Text: "Second Chair Intelligence Platform · Dashboard data refreshes every 4 hours"
  Typeface: Caslon Pro Regular 10px, --sc-grey-warm

[FOOTER TEXT — right-aligned]
  Text: "Last updated: March 14, 2026 at 6:00 AM CT"
  Typeface: IBM Plex Mono 10px, --sc-grey-warm
  (Machine timestamp = monospace per system spec)
```

---

## DESIGN VERIFICATION CHECKLIST

Before handing off the Figma file for development, the following must be confirmed:

### Massimo's Checks (Visual System)
- [ ] True optical small caps confirmed on all exhibit labels (Caslon Pro `smcp` OpenType feature active, not CSS `font-variant: small-caps`)
- [ ] Panel borders are 2px — not 1.5px, not 2pt at wrong resolution
- [ ] All rule weights are exactly 0.5px or 0.25px per spec — not approximated
- [ ] Isometric projection is true 30-degree, not perspective
- [ ] No rounded corners anywhere in the product
- [ ] No box shadows on exhibit panels (shadow only on dimensional hero numbers)
- [ ] Color values match the exact hex values in `02_Color_System.md` — no approximations
- [ ] IBM Plex Mono is used only for machine-generated data (IDs, timestamps, codes, CPL values from systems) — not for human-entered content
- [ ] Background grain overlay is present at 3–5% opacity on all screen surfaces
- [ ] Exhibit titles state conclusions, not subjects — every title reviewed and approved

### Luke's Checks (UX Architecture)
- [ ] Every exhibit is numbered sequentially
- [ ] Exhibit 1 is the most important finding (Lead Volume)
- [ ] All five data states are built for every panel: Empty, Loading, Partial, Populated, Error
- [ ] Period selector updates all panels simultaneously
- [ ] Tab order follows visual reading order (top-to-bottom, left-to-right)
- [ ] All interactive elements have visible focus states (2px Burgundy outline)
- [ ] Navigation active state is correct (Burgundy left rule + Söhne Medium)
- [ ] Alert panel appears conditionally only when alerts exist

### Graham's Checks (Art Direction)
- [ ] The overall screen reads as "designed by someone serious" — not as a SaaS template
- [ ] The first thing the eye lands on is the hero trio (Exhibit 1, 2, 3)
- [ ] The Burgundy section separator rules provide rhythm between exhibit rows
- [ ] White space around panels feels structural, not accidental
- [ ] At distance (stand back from the screen or squint): the grid and hierarchy are legible
- [ ] The sidebar does not compete with the content — it is a map, not a feature
- [ ] The dashboard, viewed without context, reads as "analytical document on glass" — not as "web application"

---

## GRAHAM'S ART DIRECTION NOTES

*"I want to add something before this document closes. The most common failure mode I see in dashboard design is what I'd call the democracy problem: every panel gets the same visual weight, the same size, the same border, the same treatment. Everything is equal. Nothing is important.*

*Second Chair must not make this mistake. The three hero panels at the top — the lead count, the CPSC, the cases signed — must visually dominate the dashboard. They are the answer. Everything below them is the evidence. The visual hierarchy must communicate this distinction without anyone having to read it.*

*Two things achieve this: the hero number size (80px Tiempos Bold with dimensional depth — it is physically large, it has physical presence) and the vertical separation rule (the 0.5pt Burgundy rule that separates the answer from the evidence). These are not decorative choices. They are the visual argument.*

*When I look at this dashboard, I should feel the answer at the top and the evidence below. Like a well-structured brief. The attorney should be able to read the top row and know whether to be pleased or concerned before reading a single word of context.*

*That is the design standard. Hold it."*

---

## MASSIMO'S FINAL SPECIFICATION NOTE

*"One addition that belongs in this document. The screen specified above is the populated state — a client in month three with 13 weeks of data. Luke has specified the empty state and loading state in the architecture document.*

*I want to specify the empty state visual treatment here because it is the first impression for every new client, and first impressions are the visual system's most critical test.*

*On first login — no data, zero leads delivered — the dashboard should look like this:*

*The three exhibit panels at the top are present, properly bordered, properly labeled. The hero number position shows '—' (an em dash) in Tiempos Headline Bold at the same size, in Warm Grey. The context label reads as specified. The exhibit title reads: 'No leads delivered yet — your first leads typically arrive within 3 business days.'*

*The panels below are also present, bordered, labeled. Each shows the Caslon Italic message: 'No data available for this period.'*

*Above Exhibit 1, a full-width strip on the secondary surface reads: 'Welcome to Second Chair. Your dashboard will populate as leads are delivered to your account.' — Tiempos Headline Bold 22px, followed by Caslon Pro Regular 14px body copy and the account representative's name and contact.*

*The Burgundy rules are present. The sidebar is functional. The grid holds. The system does not break when empty — it holds its structure and communicates patience and credibility. This is how you know the design is principled: it works when there is nothing in it."*

---

*Screen Specifications complete.*
*Ready for Figma execution.*
*Visual system reference: `14_Visual_Identity/06_Digital_Applications.md` | `14_Visual_Identity/02_Color_System.md`*
*Architecture reference: `16_Dashboard_UX_Design/02_UX_Architecture.md`*
*Component reference: `16_Dashboard_UX_Design/03_Component_Inventory.md`*
