# Second Chair — B&W Editorial Chart System
*March 2026 | Massimo Vignelli (lead) | Graham Fink (art direction)*

---

## WHY THIS SYSTEM EXISTS

Second Chair's primary chart register is monochrome. Not because of a limitation — because of a deliberate strategic choice about what seriousness looks like.

The prestige publications that constitute Second Chair's visual reference world — The Economist, the Wall Street Journal, the Harvard Business Review, Fortune Magazine in the pre-color era, Goldman Sachs annual reports through the 1990s — all developed sophisticated charting systems within monochrome or near-monochrome constraints. Those constraints produced discipline. Every differentiation had to be earned through tonal weight, pattern logic, or spatial organization rather than color shortcut. The result is charts that read as precise, authoritative, and serious in a way that color-heavy charts rarely achieve.

The monochrome system is also the correct system for the cream-paper world. Color sits differently on cream than on white — it muddles, it warms, it loses precision. Black and gray on cream is sharp. It is the relationship the prestige law publication and the quality annual report have used for a century because it is correct.

**Single color accent (Oxblood Burgundy `#6B1A1A`) is permitted and strategically important.** It is used the way The Economist uses its signature red: one element, maximum contrast, making the critical reading unavoidable. Nothing else.

**Old Gold (`#B8962E`) is permanently excluded from all chart and document contexts.** See gold exclusion section.

---

## THE RESEARCH RECORD

### Edward Tufte / *The Visual Display of Quantitative Information* (1983)

The foundational text. Tufte's own charts in this book — printed in warm charcoal on cream stock — are the direct precursor to this system. His specific contributions to Second Chair's chart grammar:

- **Data-ink ratio**: every mark on the chart must justify itself as data. No decorative fills, no borders for border's sake, no legend boxes that duplicate axis labels.
- **Small multiples**: repeated chart forms at small scale showing data variation — each panel identical in structure, data varying across panels. The preferred form for multi-series comparison.
- **Chartjunk prohibition**: heavy crosshatch, moiré patterns, unnecessary grid lines, and 3D effects all violate this. The pattern fill system below uses patterns only where functionally necessary, not decoratively.
- **The Tufte color rule**: if color is used, use it for the data, not the decoration. One color for the critical series. Grey for everything else.

### The Economist Chart Register

The Economist has maintained a consistent chart system since the 1940s. Its specific techniques, relevant to Second Chair:

- **Single red accent** on an otherwise monochrome chart — one series, one callout, one highlighted bar — rendered in the signature Economist red. All other series in grey tones.
- **Clean axes** — x and y axes in thin black rules, no box border around the chart, no top or right axis line (Tufte's recommendation). Grid lines in very light grey (10–15% tone) horizontal only.
- **Type directly on charts** — labels and callouts set in the same typeface as the publication body, not a separate "chart font." For Second Chair: Adobe Caslon Pro or Söhne, matching the document.
- **No legend boxes** — series labels placed directly at the end of lines or adjacent to bars.

### Wall Street Journal

WSJ graphics (pre-2010, the Tufte era) used:
- **Stepped tonal fills** for bar chart differentiation — solid black, 60% grey, 30% grey, open — before adopting color
- **Thin horizontal grid lines only** at labeled y-axis values, in 15% tone
- **Dot-dash hybrid accents** for specific callout elements
- **Small inline spark charts** embedded in text, pioneered by Tufte, adopted by WSJ as the "sparkline" form

### Harvard Business Review — The Exhibit Convention

HBR's editorial system (relevant to Second Chair's Exhibit Convention):
- **"EXHIBIT N:" prefix** in small caps before every chart and table — exactly as Second Chair uses
- **Chart title states the conclusion**, not the variable: "Costs declined steadily from 1988 to 1994" not "Annual costs 1988–1994"
- **Tables use horizontal rules only** — no vertical column borders, no cell shading, ruled header row in heavier weight
- **Tonal differentiation in tables**: alternating very light (5% tone) row shading for readability, not decorative

### Fortune / Goldman Sachs Annual Reports (1985–1998)

The prestige annual report tradition, directly relevant:
- **Pattern fills in multi-series bars** — when four or more series required differentiation in two-color printing (black + one Pantone color), pattern fills were used: solid, horizontal line, diagonal line, dot screen, open
- **The two-color discipline**: everything in black/pattern + one single accent Pantone (often a deep red, navy, or green). This is the direct historical precedent for Second Chair's charcoal/gray/pattern + oxblood system.
- **Generous white space** around every chart — charts never butted against body text. The exhibit occupied its own breathing zone.
- **Physical paper showing through patterns** — in letterpress/offset printing, the pattern fills show the paper color between the ink marks. On cream stock, this produces a warm, tactile tonal quality that screened fills on white never achieve.

### Zip-a-Tone / Letraset Pattern Era (1960s–1985)

Before digital, editorial designers differentiated chart series using adhesive pattern sheets (Zip-a-Tone, Letraset, Formatt) applied by hand to artwork:
- Standard screen densities: 10%, 20%, 30%, 40%, 50%, 65%, 85% dot coverage
- Standard ruling patterns: horizontal lines, vertical lines, 45° diagonal, 60° diagonal, crosshatch, wavy, random texture
- The six patterns in Second Chair's system are derived from the most commonly used Zip-a-Tone sheets in editorial production — the ones that survived into the digital era because they were the clearest

---

## THE TONAL LADDER — 6 STOPS

All tones are warm-cast, not neutral grey. On cream stock (`#F5F0E8`), neutral grey appears cool and disconnected. Warm grey harmonizes with the paper and reads as print ink at various densities. These values are calibrated for screen display; for print, verify against press proof on Crane Lettra or equivalent cream stock.

Print black is never `#000000`. Pure black on cream stock is harsh and reads as digital, not print.

| Stop | Name | Hex | Use |
|---|---|---|---|
| 1 | Print Black | `#2C2C2C` | Primary series fill, chart borders, axis lines, all type |
| 2 | 75% Tone | `#4D4845` | Secondary solid series, heavy emphasis fills |
| 3 | 50% Tone | `#7A736E` | Tertiary series, supporting data, reference marks |
| 4 | 25% Tone | `#B5ADA8` | Background fills, non-highlighted bars, reference bands |
| 5 | 10% Tone | `#DDD8D3` | Very light backgrounds, subtle reference zones, alternating table rows |
| 6 | Paper | `#F5F0E8` | Ground. The "white" of this system. Never replaced with pure white. |

### How the Tonal Ladder Works in Practice

**Two-series chart:** Series A in Print Black `#2C2C2C` solid. Series B in 25% Tone `#B5ADA8` solid.

**Three-series chart:** Print Black / 50% Tone / 25% Tone. Or: Oxblood (featured series) / Print Black / 50% Tone.

**Four-series chart:** Introduce pattern fills at this point. Tonal differentiation alone becomes unreliable at four series. See pattern system below.

**Reference band / target line:** 10% Tone fill for reference zone. Print Black 0.5pt dashed rule for target line.

**Grid lines:** 10% Tone `#DDD8D3` horizontal only, at labeled y-axis values. No vertical grid lines. No grid lines at unlabeled intervals.

---

## THE PATTERN FILL SYSTEM — 6 PATTERNS

Used when tonal differentiation is insufficient — typically at four or more categorical series, or when a chart must be legible when photocopied or printed in pure black-and-white (removing even the tonal differentiation).

Patterns always use Print Black `#2C2C2C` ink on Paper `#F5F0E8` ground, or on the relevant tone fill as background.

| Pattern | Name | Description | SVG/CSS Reference | Zip-a-Tone Equivalent |
|---|---|---|---|---|
| P1 | Solid | 100% fill, no pattern | `fill: #2C2C2C` | 100% screen |
| P2 | Horizontal Rule | Horizontal lines, 3px spacing, 0.75px weight | SVG `pattern` — see below | Zip 62-8 |
| P3 | Diagonal Rule | 45° diagonal lines, 3px spacing, 0.75px weight | SVG `pattern` — see below | Zip 60-8 |
| P4 | Crosshatch | Horizontal + vertical, 4px spacing, 0.5px weight | SVG `pattern` — see below | Zip 64-5 |
| P5 | Dot Screen | Circular dots, ~25% coverage, 4px grid | SVG `pattern` — see below | Zip 30-25 |
| P6 | Open | Paper ground only, 1px Print Black border | `fill: #F5F0E8; stroke: #2C2C2C; stroke-width: 1` | Open |

### SVG Pattern Definitions

These can be dropped directly into SVG chart elements or referenced via CSS.

```svg
<!-- P2: Horizontal Rule -->
<pattern id="sc-p2-horizontal" patternUnits="userSpaceOnUse" width="6" height="3">
  <line x1="0" y1="1.5" x2="6" y2="1.5" stroke="#2C2C2C" stroke-width="0.75"/>
</pattern>

<!-- P3: Diagonal Rule -->
<pattern id="sc-p3-diagonal" patternUnits="userSpaceOnUse" width="4" height="4">
  <line x1="0" y1="4" x2="4" y2="0" stroke="#2C2C2C" stroke-width="0.75"/>
  <line x1="-1" y1="1" x2="1" y2="-1" stroke="#2C2C2C" stroke-width="0.75"/>
  <line x1="3" y1="5" x2="5" y2="3" stroke="#2C2C2C" stroke-width="0.75"/>
</pattern>

<!-- P4: Crosshatch -->
<pattern id="sc-p4-crosshatch" patternUnits="userSpaceOnUse" width="5" height="5">
  <line x1="0" y1="2.5" x2="5" y2="2.5" stroke="#2C2C2C" stroke-width="0.5"/>
  <line x1="2.5" y1="0" x2="2.5" y2="5" stroke="#2C2C2C" stroke-width="0.5"/>
</pattern>

<!-- P5: Dot Screen -->
<pattern id="sc-p5-dots" patternUnits="userSpaceOnUse" width="4" height="4">
  <circle cx="2" cy="2" r="0.9" fill="#2C2C2C"/>
</pattern>
```

### Pattern Usage Rules

1. **Never use pattern fills decoratively.** Patterns exist for categorical differentiation only. If three tonal stops are sufficient, use tones — no patterns.
2. **Patterns and tones can combine.** A P3 diagonal fill at 75% Tone density is a legitimate differentiated series.
3. **Accessibility**: when designing for WCAG or print-only contexts, pattern fills are the correct solution for colorblind accessibility, not color substitution.
4. **Pattern scale matters.** At small chart sizes (sparklines, inline exhibits), patterns become illegible. Use tones only at small scale; patterns at full exhibit scale.
5. **Moiré prohibition.** Never use two similar patterns adjacently (e.g., P2 horizontal and P4 crosshatch adjacently can produce moiré at certain screen densities). Test at intended output size.

---

## OXBLOOD ACCENT — RULES OF USE

`#6B1A1A` is the single permitted color accent in the B&W editorial chart system. It functions identically to The Economist's red: one element per chart, maximum intentionality, the critical reading made unavoidable.

### Permitted Uses

| Use | Description | Example |
|---|---|---|
| **Highlighted series** | One series in a multi-series chart in oxblood solid; all others in tonal grays | "Our clients" bar in oxblood vs. "category average" bars in grey |
| **Bar cap rule** | Thin 1pt oxblood horizontal rule at the top edge of a featured bar or column | Calling out the record month in a trend bar chart |
| **Key data point** | Oxblood filled dot on a line chart for the single most important data point | "This is where costs dropped below target" |
| **Callout statistic** | The hero number in an exhibit — the one figure the attorney must remember — set in oxblood | "40% lower CPSC" in oxblood; surrounding context in charcoal |
| **Section rule** | 0.5pt oxblood horizontal rule separating sections in a document or exhibit | The brand signature rule — appears in every Second Chair document |
| **Citation/source line** | Small-caps source attribution in oxblood at base of exhibit | "SOURCE: Second Chair Platform Data, Q4 2025" |

### Prohibited Uses

- **Never as a fill for large areas** — background color, panel fill, sidebar
- **Never on two elements in the same chart** — one use per exhibit, maximum
- **Never for decorative rules** — only structural rules that separate actual sections
- **Never at reduced opacity** — no oxblood at 30% or 50% transparency. Use a tone from the tonal ladder instead.
- **Never on a colored background** — oxblood only appears against Cream `#F5F0E8` or Print Black `#2C2C2C` reversal

---

## GOLD EXCLUSION — PERMANENT, WITH RATIONALE

**Old Gold `#B8962E` is excluded from all chart, document, screen, and exhibit contexts. This is not a preference — it is a contrast and authenticity failure.**

### Contrast Failure

`#B8962E` on `#F5F0E8` (cream background) produces a contrast ratio of approximately **1.6:1**. WCAG AA requires 4.5:1 for normal text, 3:1 for large text. At 1.6:1, gold on cream is nearly invisible — a thin rule or small label in gold on cream disappears. The colors are too close in lightness.

### Authenticity Failure

Gold never appeared on the interior pages of any of the prestige publications Second Chair draws from. Open any volume of the West Federal Reporter: oxblood cloth cover, gold lettering on the spine — but inside, every page is warm charcoal ink on cream. Open a Harvard Law Review: the cover may have embossed gold, but inside, every page is black type on cream paper. Open a Goldman Sachs annual report from 1990: the cover has gold foil, but inside, charcoal type on cream or white stock, with possibly one Pantone accent color.

Gold is a **physical material color** — it communicates through the properties of physical gold: reflectivity, warmth, permanence, the sense that something has been pressed into a surface. Reproduced as a flat hex value on a screen or laser-printed page, it has none of those properties. It is simply a medium-dark yellow. It does not read as "gold." It reads as a dull mustard.

**Gold lives in the physical world:** foil stamping on book covers, embossing on business cards, engraving on brass nameplates. It does not live in documents or on screens.

---

## COMBINATION RULES — HOW THE SYSTEM WORKS TOGETHER

### The Decision Tree

```
HOW MANY CATEGORICAL SERIES?

1 series
  → Use Print Black solid. Consider oxblood for key data point.

2 series
  → Print Black + 25% Tone.
  → Or: Oxblood (featured) + Print Black (comparison).

3 series
  → Print Black + 50% Tone + 25% Tone.
  → Or: Oxblood + Print Black + 25% Tone (when one series is the point).

4 series
  → Introduce patterns. Print Black solid + P3 diagonal + 25% Tone + P5 dots.
  → Or: Oxblood + P2 horizontal (black) + 50% Tone + P5 dots.

5–6 series
  → Full pattern system. Assign by visual weight, not arbitrary order.
  → Test legibility at intended output size. Consider small multiples instead.

6+ series
  → Do not use one chart. Use small multiples (Tufte).
  → Each panel: single series in Print Black. Same scale across all panels.
```

### Axis and Grid Grammar

| Element | Spec |
|---|---|
| X-axis rule | Print Black `#2C2C2C`, 0.75pt |
| Y-axis rule | Print Black `#2C2C2C`, 0.75pt |
| Top / right axis | None (open chart, Tufte convention) |
| Horizontal grid lines | 10% Tone `#DDD8D3`, 0.5pt, at labeled y-values only |
| Vertical grid lines | None (except time-series with meaningful interval marks) |
| Axis labels | Söhne Regular, 8pt, Warm Grey `#8C8680`, aligned to axis |
| Chart title | Tiempos Headline Bold or Caslon Pro Bold — states the conclusion |
| Exhibit label | "EXHIBIT N:" Caslon Pro small caps, 8pt, Warm Grey, above title |
| Source line | Caslon Pro small caps or Söhne, 7pt, Warm Grey OR oxblood `#6B1A1A` |
| Data labels | Direct on bars/points — Söhne Regular 7–8pt. No floating legend. |

### Table Grammar

| Element | Spec |
|---|---|
| Header rule | Print Black `#2C2C2C`, 1pt, full width |
| Header type | Caslon Pro small caps or Söhne, 8pt, Print Black, centered or left-aligned |
| Row rules | 10% Tone `#DDD8D3`, 0.5pt, between all rows |
| Column rules | None |
| Alternating rows | Optional: 10% Tone `#DDD8D3` fill on alternate rows for wide tables |
| Body type | Caslon Pro Regular 9pt or Söhne Regular 8pt |
| Emphasized cell | Oxblood type `#6B1A1A` — one cell per table maximum |
| Footer / source | Caslon Pro small caps, 7pt, Warm Grey |

---

## FIGMA BUILD NOTES

### Color Styles to Create

```
SC/Chart/PrintBlack      #2C2C2C
SC/Chart/Tone75          #4D4845
SC/Chart/Tone50          #7A736E
SC/Chart/Tone25          #B5ADA8
SC/Chart/Tone10          #DDD8D3
SC/Chart/Paper           #F5F0E8
SC/Chart/OxbloodAccent   #6B1A1A
```

### Pattern Components

Create a Figma component for each pattern fill as a repeating frame with the SVG pattern embedded. Name them:
```
SC/Pattern/Solid
SC/Pattern/HorizontalRule
SC/Pattern/DiagonalRule
SC/Pattern/Crosshatch
SC/Pattern/DotScreen
SC/Pattern/Open
```

Use these as fill overrides on chart bar/area components.

### Chart Component Library Sequence

1. Base chart frame (cream background, no border)
2. Axis component (x + y rules at Print Black 0.75pt)
3. Grid line component (10% Tone 0.5pt horizontal)
4. Bar component (accepts fill: solid, pattern, or oxblood)
5. Exhibit label component (small caps prefix)
6. Chart title component (conclusion-first copy)
7. Data label component (direct placement, no legend)
8. Source line component (small caps, Warm Grey or oxblood)

---

## QUICK REFERENCE CARD

```
SECOND CHAIR B&W CHART SYSTEM — QUICK REFERENCE

TONES (warm-cast, all on cream #F5F0E8):
  Print Black  #2C2C2C   Primary series, type, axes
  75% Tone     #4D4845   Secondary solid series
  50% Tone     #7A736E   Tertiary series
  25% Tone     #B5ADA8   Supporting/background fills
  10% Tone     #DDD8D3   Grid lines, subtle reference zones
  Paper        #F5F0E8   Ground color — the cream

PATTERNS (use at 4+ series, for accessibility):
  P1  Solid             Primary
  P2  Horizontal rule   Secondary
  P3  Diagonal 45°      Tertiary
  P4  Crosshatch        Quaternary
  P5  Dot screen        Quinary
  P6  Open (paper)      Senary / reference

ACCENT (one use per chart, maximum):
  Oxblood  #6B1A1A    Bar cap / featured series / key callout / section rule

EXCLUDED PERMANENTLY:
  Gold  #B8962E   Contrast failure on cream + authenticity failure — physical material only
  Any other color from the brand palette or data palette in this context
```
