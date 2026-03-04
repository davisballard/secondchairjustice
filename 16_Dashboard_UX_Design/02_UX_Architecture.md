# Second Chair — UX Architecture
*Screen Map, Navigation, Panel Hierarchy, Data States*
*Luke Grabowski (lead) | Session: March 2, 2026*

---

## LUKE'S ARCHITECTURAL BRIEF

*"The architecture has one job: get the PI attorney from login to their primary question answered in under 60 seconds. Everything else — the drill-downs, the reports, the account settings — is secondary navigation. The primary experience is the Dashboard view. That is where we spend 80% of our design energy.*

*The navigation is minimal and purposeful. The attorney should never feel lost. The sidebar is a map, not a menu. The active state tells you where you are. The rest of the interface tells you what the data says."*

---

## SITE MAP

```
SECOND CHAIR CLIENT PORTAL
│
├── LOGIN
│   └── → Dashboard (default landing after auth)
│
├── [NAV: DASHBOARD]  ← Default view
│   └── Primary performance overview
│       ├── Current period selector (MTD / QTD / Custom)
│       ├── Exhibit 1: Lead Volume (hero)
│       ├── Exhibit 2: Lead Volume Trend
│       ├── Exhibit 3: Conversion Funnel
│       ├── Exhibit 4: Cost Per Signed Case (hero)
│       ├── Exhibit 5: CPSC Trend
│       ├── Exhibit 6: Channel Efficiency
│       └── Alert Panel (conditional)
│
├── [NAV: LEADS]
│   ├── Lead Summary (aggregate, current period)
│   │   ├── Volume by case type (donut)
│   │   ├── Volume by source (bar)
│   │   └── Volume by geography (table)
│   └── Lead Detail Table (individual leads, filterable)
│       ├── Filter: Date range
│       ├── Filter: Case type
│       ├── Filter: Source
│       ├── Filter: Disposition
│       └── Export (CSV)
│
├── [NAV: PERFORMANCE]
│   ├── Conversion Analysis
│   │   ├── Funnel detail (all stages, all segments)
│   │   ├── Conversion by case type (multi-series bar)
│   │   └── Conversion trend (13-week area chart)
│   └── Cost Efficiency Analysis
│       ├── CPSC history (13-month)
│       ├── CPL by channel (comparative bar)
│       └── Spend breakdown (table)
│
├── [NAV: REPORTS]
│   ├── Most recent monthly report (view / download PDF)
│   ├── Report archive (list by month, download each)
│   └── Custom date range export (Phase 2)
│
└── [NAV: ACCOUNT]
    ├── Subscription & Billing
    ├── Territory Settings
    ├── Case Type Preferences
    ├── Intake Configuration
    ├── User Management
    └── Notification Preferences
```

---

## NAVIGATION SYSTEM

### Sidebar Navigation

The primary navigation is a left sidebar — present on all screens, consistent in position and behavior.

**Visual specification:**
- Width: 220px
- Background: Secondary screen surface `#E8E3DC`
- No header bar distinguishing it from content — the surface color difference is the separator
- No sidebar border rule — the surface color contrast is sufficient per `06_Digital_Applications.md`

**Navigation items:**
- Typeface: Söhne Regular, 13px, Title Case
- Color (default): Warm Charcoal `#2C2C2C`
- Color (hover): No color change — cursor change only
- Active state: 0.5pt Burgundy `#6B1A1A` left-border rule + Söhne Medium weight
- No background color change on active or hover — the rule and weight change is sufficient

**Navigation item list:**
```
SECOND CHAIR [logotype, top of sidebar]
───────────────── [0.5pt Burgundy rule]

Dashboard
Leads
Performance
Reports

───────────────── [0.5pt Burgundy rule, pushed to bottom]

Account
```

**The logotype in the sidebar:**
- Second Chair wordmark (Direction A or B, per final logo decision) at 14px equivalent
- Sits at top of sidebar with 24px padding top/left
- The Burgundy rule below it is the 0.5pt brand rule — same rule that separates nav sections

**Period selector:**
- Persistent control below the navigation items, above the bottom rule
- Options: MTD (month-to-date) | QTD (quarter-to-date) | Last 30 Days | Last 90 Days | Custom
- Typeface: Söhne Regular 11px, ALL CAPS, +8 tracking (matches table header convention)
- Active option: Söhne Medium, Burgundy `#6B1A1A`
- Inactive options: Warm Grey `#8C8680`
- This control persists across Dashboard, Leads, and Performance views — changing the period updates all three simultaneously

---

## PRIMARY VIEW: DASHBOARD

**Question this screen answers:** "How is my account performing right now, and is my investment working?"

**Viewport:** 1280px container, 12-column grid, 24px gutters, 48px outer margins. The sidebar occupies 220px + 48px left margin = 268px. The content area is 1280 - 268 = 1012px, using a 12-column grid within that content area.

---

### PANEL HIERARCHY (Primary Dashboard)

Panel order is analytical priority order. The attorney reads top to bottom and builds understanding.

**TOP TIER: Page Header (always visible, not an exhibit)**
Full 12-column width
- Page title: "Dashboard" in Tiempos Headline Bold, 36px, Warm Charcoal
- Client name + account ID: Söhne Regular 13px, Warm Grey
- Period indicator: Current period label (e.g., "March 2026, Month-to-Date") in Söhne Regular 13px, Warm Grey
- If alerts exist: Alert banner appears between page header and Exhibit 1 (full width, Warm Charcoal background, Cream text, Söhne Regular 13px)

---

**EXHIBIT 1: LEAD VOLUME — THE PRIMARY FINDING**
Position: Top-left, columns 1–4 (of 12) in content area
Panel width: 4 columns = approximately 310px

*Question: How many leads did I receive this period?*

Contents:
- Exhibit label: "EXHIBIT 1:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "[N] leads delivered in [period] — [direction] from [prior period]" — Caslon Pro Regular Italic, 14px, Warm Charcoal
- Hero number: Lead count (e.g., "47") — Tiempos Headline Bold, 80px, with dimensional depth treatment per `06_Digital_Applications.md`
- Supporting stats (below hero):
  - Prior period count with delta: Söhne Regular 13px
  - Period-over-period % change: Success Green if positive, Burgundy if negative, Söhne Medium 13px

---

**EXHIBIT 2: COST PER SIGNED CASE — THE SECOND PRIMARY FINDING**
Position: Top-center, columns 5–8 (of 12)
Panel width: 4 columns

*Question: What am I paying per case I signed?*

Contents:
- Exhibit label: "EXHIBIT 2:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "Cost per signed case [period] — [direction] from [prior period]" — Caslon Pro Regular Italic, 14px
- Hero number: CPSC (e.g., "$847") — Tiempos Headline Bold, 80px, dimensional depth treatment
- Supporting stats:
  - Prior period CPSC with delta
  - CPSC vs. target (if target set): color-coded

*Note: CPSC requires signed case data from the attorney's intake system. If that integration isn't live, this panel shows CPL (cost per lead) with a label explaining the distinction and a CTA to connect intake data.*

---

**EXHIBIT 3: CASES SIGNED**
Position: Top-right, columns 9–12 (of 12)
Panel width: 4 columns

*Question: How many cases did my leads produce?*

Contents:
- Exhibit label: "EXHIBIT 3:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "Cases signed from Second Chair leads this [period]" — Caslon Pro Regular Italic, 14px
- Hero number: Signed case count — Tiempos Headline Bold, 80px, Success Green `#2A6B3C` dimensional treatment
- Supporting stats:
  - Sign rate (% of leads → signed)
  - By case type breakdown (Söhne Regular 12px, with mini categorical color dots)

---

**0.5pt BURGUNDY RULE (section separator)**
Full 12-column width, 32px below the top trio, 32px above the next row

---

**EXHIBIT 4: LEAD VOLUME TREND**
Position: Columns 1–8 (of 12) — wide panel
Panel width: 8 columns

*Question: Is my lead volume growing, stable, or declining?*

Contents:
- Exhibit label: "EXHIBIT 4:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "Lead volume has [trended direction] over the past 13 weeks" — Caslon Pro Regular Italic, 14px
- Chart: Isometric bar chart, weekly intervals, 13 bars
  - Bars in Burgundy `#6B1A1A` (single series, no legend needed)
  - Current period bar in Success Green `#2A6B3C` if on pace, Amber `#C9943A` if below pace
  - Baseline: Single 0.5px Warm Grey rule
  - Labels: Week labels in Söhne Regular 10px, ALL CAPS below bars
  - Values: Direct labels above each bar, Caslon Pro 10px Warm Charcoal
- Period trend annotation: "13-week average: [N] leads/week" — Caslon Pro Regular Italic 12px, Warm Grey, positioned inside panel below chart

---

**EXHIBIT 5: CONVERSION FUNNEL**
Position: Columns 9–12 (of 12) — right column alongside Exhibit 4
Panel width: 4 columns

*Question: How well do my leads convert at each stage?*

Contents:
- Exhibit label: "EXHIBIT 5:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "[N]% of leads become signed cases — [direction] from last period" — Caslon Pro Regular Italic, 14px
- Chart: Staged funnel
  - Stage bars are horizontal, stacked vertically (top = leads, bottom = signed)
  - Each bar width is proportional to that stage's count (bar narrows as funnel narrows)
  - Bar height: 20px each, with 24px gap between stages
  - Bar color: Burgundy primary, each stage same color (the narrowing is the visual — no color variation)
  - Stage labels: Caslon Pro Small Caps 9px, left of each bar
  - Stage counts: Söhne Medium 12px, inside or right of each bar
  - Conversion rates: Between stages, Söhne Regular 11px, Warm Grey (e.g., "↓ 68% contacted")
  - Bottom: "CASES SIGNED: [N]" in Caslon Pro Small Caps 9px, Success Green

---

**0.5pt BURGUNDY RULE (section separator)**
Full 12-column width

---

**EXHIBIT 6: CPSC TREND**
Position: Columns 1–6 (of 12)
Panel width: 6 columns

*Question: Is my cost per case improving over time?*

Contents:
- Exhibit label: "EXHIBIT 6:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "Cost per signed case has [direction] [%] over 13 weeks" — Caslon Pro Regular Italic, 14px
- Chart: Area chart, 13-week rolling
  - Single series, Burgundy `#6B1A1A` at 25% opacity fill, 1.5px solid line
  - Baseline rule: 0.5px Warm Grey
  - No gridlines
  - Direct value labels at week intervals (every 4th week labeled, current week always labeled)
  - If CPSC improves over time, trend direction annotation: "↓ 18% over 13 weeks" in Success Green, Caslon Pro Italic 12px

---

**EXHIBIT 7: CHANNEL EFFICIENCY**
Position: Columns 7–12 (of 12)
Panel width: 6 columns

*Question: Which channel is producing my leads most efficiently?*

Contents:
- Exhibit label: "EXHIBIT 7:" — Caslon Pro Small Caps, 8px, Warm Grey
- Exhibit title: "Meta delivers [N]% more leads per dollar than Google this period" — or whichever is true
- Chart: Isometric bar chart, two groups (Meta, Google), two metrics per group (Lead Count, CPL)
  - Two-series chart: Lead Count in Burgundy, CPL in Forest Blue `#1B3A6B`
  - Bars grouped by channel (Meta | Google), with inter-group gap
  - Baseline rule: 0.5px Warm Grey
  - Inline color key (Caslon small caps 8px) below chart, no floating legend
  - CPL values in IBM Plex Mono 11px (machine data) directly on bar tops

---

**ALERT PANEL (conditional — only appears when alerts exist)**
Position: Below all exhibits, full 12-column width, or as right sidebar panel if space permits
Background: Secondary screen surface `#E8E3DC` — the only panel without a thick rule border (it is a status layer, not an analytical exhibit)
Contents:
- Panel heading: "ACCOUNT STATUS" — Söhne Medium 11px, ALL CAPS, +8 tracking, Warm Grey
- Alert items: Listed vertically, each with severity indicator (1px left rule: Burgundy for High, Amber for Medium, Warm Grey for Low)
- Alert text: Söhne Regular 13px, Warm Charcoal
- Alert action link (if applicable): Söhne Medium 13px, Burgundy (hover: underline)

---

## LEADS VIEW

**Question this screen answers:** "What leads did I receive, in what volume and mix, and what happened to them?"

This view has two sub-sections: Lead Summary (aggregate analytics, same visual system as Dashboard) and Lead Detail Table (individual leads).

### Lead Summary Panel

Position: Full width, above the Lead Detail Table

Contains:
- **Exhibit 1 (Leads View): Volume by Case Type** — Dimensional donut chart, 6-category palette, columns 1–4
- **Exhibit 2 (Leads View): Volume by Source** — Isometric bar, columns 5–8
- **Exhibit 3 (Leads View): Volume by Geography** — Data table with inline bar (county | lead count | inline Burgundy bar proportional to count), columns 9–12

### Lead Detail Table

Full 12-column width
- Table heading: "LEAD DETAIL" — Söhne Medium 11px, ALL CAPS, +8 tracking
- Column headers: Söhne Medium, 11px, ALL CAPS, +8 tracking, Warm Grey
- Filter controls: Inline above the table — date range, case type, source, disposition (Söhne Regular 12px)
- Columns: Lead ID (IBM Plex Mono) | Date Received (IBM Plex Mono) | Case Type | Source | Status | Action
- Row styling: 0.25pt Warm Grey horizontal rules between rows; Amber Pale `#F2E4C0` on hover
- Export button: "EXPORT CSV" — Söhne Medium 13px, Burgundy — right-aligned above table

---

## PERFORMANCE VIEW

**Question this screen answers:** "How is conversion and efficiency trending in detail, and where should I focus?"

This view goes deeper than the Dashboard — it is for the attorney who wants to investigate beyond the headline metrics.

### Sub-section: Conversion Analysis

- **Exhibit 1 (Perf): Conversion Funnel (Full)** — Full funnel with all segment breakdowns. 12 columns wide. Each stage segmented by case type (stacked bar within each funnel stage).
- **Exhibit 2 (Perf): Sign Rate by Case Type** — Multi-series isometric bar. 6 columns. Case types on X-axis, sign rate on Y-axis. Up to 6 case types, using categorical palette.
- **Exhibit 3 (Perf): Conversion Trend (13-week)** — Multi-series area chart. 6 columns. Contact rate, consultation rate, sign rate as three overlapping series (Burgundy, Forest Blue, Success Green).

### Sub-section: Cost Efficiency Analysis

- **Exhibit 4 (Perf): CPSC — 13-Month History** — Isometric bar chart, 13 bars. One bar per month. Shows full year-plus context. 8 columns.
- **Exhibit 5 (Perf): CPL by Channel (This Period)** — Simple comparative bar. 4 columns.
- **Exhibit 6 (Perf): Spend Breakdown** — Data table. Full 12 columns. Channel | Spend | Leads | CPL | % of Total. Totals row separated by double 0.25pt rules.

---

## REPORTS VIEW

**Question this screen answers:** "Where are my monthly reports, and how do I get them?"

Simple list view — no complex analytics. The visual system applies to the list itself.

Layout:
- Page title: "Reports" — Tiempos Headline Bold 36px
- Subtitle: "Monthly performance reports — [current year]" — Caslon Pro Regular Italic 16px, Warm Grey
- Report list: Vertical list of report cards, each with:
  - Report period (e.g., "February 2026") — Tiempos Headline Bold 18px
  - Date generated — Söhne Regular 12px, Warm Grey
  - 0.5pt Burgundy rule below each item
  - "VIEW REPORT" link — Söhne Medium 13px, Burgundy
  - "DOWNLOAD PDF" link — Söhne Medium 13px, Warm Charcoal
- Most recent report is highlighted: subtle `#E8E3DC` background strip, no border (the surface is the signal)

---

## DATA STATES — FULL SPECIFICATION

Every view and every panel must be designed for all five states. These are not afterthoughts — they are part of the product.

### STATE 1: EMPTY (No data — new account)

**When:** First login, or period with no leads delivered.

**Per panel behavior:**
- Exhibit panels show the exhibit label and title as normal
- Chart area shows a placeholder: a single centered message in Caslon Pro Regular Italic 14px, Warm Grey: "No leads delivered in this period."
- The thick-bordered panel remains — the exhibit structure is intact even when empty
- Hero numbers show "—" (em dash) in Tiempos Headline Bold at normal size, Warm Grey

**Full dashboard empty state (first login):**
All exhibit panels show placeholder content. Above Exhibit 1, a full-width information strip (Secondary surface `#E8E3DC`):
- Title: "Welcome to Second Chair." — Tiempos Headline Bold 22px
- Body: "Your dashboard will populate as leads are delivered to your account. Your first leads typically arrive within [N] business days of account activation." — Caslon Pro Regular 14px
- Account representative contact line — Söhne Regular 13px

### STATE 2: LOADING

**When:** Data is being fetched (initial page load, period change, filter update).

**Per panel behavior:**
- Exhibit label and title remain visible (they are static, from configuration)
- Chart area shows: A 1px Burgundy `#6B1A1A` horizontal progress line animating from left to right across the panel width — per `06_Digital_Applications.md` specification
- Animation: 200ms ease-out
- No skeleton placeholders with colored elements — only the Burgundy progress line

### STATE 3: PARTIAL (Current period incomplete)

**When:** Mid-month data — some of the period has data, but the period is ongoing.

**Per panel behavior:**
- Data displays normally for the completed portion of the period
- Period label gains a contextual note: "(MTD through March 14)" — Söhne Regular 11px, Warm Grey
- Hero numbers display current accumulated total, not a projection
- Trend charts show completed bars at full opacity; current in-progress bar at 60% opacity with an "In progress" annotation

### STATE 4: POPULATED (Normal operational state)

**When:** Full data available for the selected period.

This is the primary designed state — all exhibit specifications in this document describe the populated state.

### STATE 5: ERROR

**When:** Data fetch failed, API timeout, data quality issue.

**Per panel behavior:**
- Exhibit label and title remain
- Chart area: "Data unavailable" — Caslon Pro Regular Italic 13px, Burgundy `#6B1A1A`, centered in the panel
- Below: "Please refresh the page or contact your account representative." — Söhne Regular 12px, Warm Grey
- The thick rule border remains — the structure is maintained even when the content fails
- No error icons, no warning symbols — text only

**Full-page error (total data failure):**
Minimal centered message, page surface `#F0EBE3`:
- "Data temporarily unavailable." — Tiempos Headline Bold 28px
- "Please refresh the page. If this issue persists, contact [name] at [email]." — Caslon Pro Regular 16px
- Second Chair wordmark at top of page, per navigation spec

---

## NAVIGATION BEHAVIOR SPECIFICATIONS

**Active state:** Left 0.5pt Burgundy rule + Söhne Medium. No background change.

**Hover state:** Cursor changes to pointer. No color or weight change — the sidebar does not animate on hover. It is a document, not an interactive menu.

**Period selector change:** Selecting a new period triggers a loading state (burgundy progress line) across all exhibit panels simultaneously. The period selector control shows the new selection immediately — the data follows asynchronously.

**Cross-view period persistence:** The period selected in the Dashboard view persists when navigating to Leads and Performance views. The attorney does not have to re-select the period on each screen.

**Drill-down navigation:** Lead-level detail (from Leads view), individual lead modal (from Lead Detail Table), and report viewer (from Reports view) open as full-screen overlays — not new pages, not new browser tabs. The sidebar navigation remains visible and functional behind the overlay. The overlay closes with an "×" (Söhne Regular 16px, top-right) or an "CLOSE" text link (Söhne Medium 13px, Burgundy).

---

## BREAKPOINT BEHAVIOR

The dashboard is primarily designed for desktop (1280px+). Tablet and mobile are not primary attorney use cases but must not produce broken layouts.

| Breakpoint | Grid | Sidebar | Panels |
|---|---|---|---|
| Desktop (1280px+) | 12-column, 24px gutter | 220px fixed left | Side-by-side as specified |
| Tablet (768–1279px) | 8-column, 16px gutter | Collapsed to icon bar (48px) | Panels reflow to full-width |
| Mobile (below 768px) | 4-column | Hidden; accessible via hamburger | All panels full-width, stacked |

**Mobile priority order (for stacking):** Exhibit 1 (Lead Volume) → Exhibit 2 (CPSC) → Exhibit 3 (Cases Signed) → Exhibit 4 (Trend) → remaining exhibits.

---

*Next: `03_Component_Inventory.md` — every UI component, mapped to the visual spec.*
