# Second Chair — Typography System
*Session: March 1, 2026 | Massimo Vignelli (lead) + Graham Fink*

---

## MASSIMO ON TYPOGRAPHY

*"Before I present the three options, one principle that applies to all of them and cannot be negotiated:*

*Typography IS the identity. Before anyone reads a single word of Second Chair's copy, the typeface has already communicated. Century Schoolbook small caps communicates: Supreme Court, law review, federal brief — the highest courts in the land. Adobe Caslon Pro communicates: founding document, The New Yorker, federal preference — the voice of serious American prose. Neither of these facts is visible to most readers. Both are felt by every legally-trained reader.*

*The second principle: hierarchy through typography, not color. The system is legible in black-and-white. Color is an accent. Typography is the hierarchy. If we remove all color from a Second Chair document, the hierarchy must still be completely clear. If it isn't, the typography isn't working.*

*The third principle, which the visual research states explicitly and I will repeat: true optical small caps only. The difference between true small caps (designed specifically by the type designer) and CSS faux small caps (scaled-down capitals) is visible to trained eyes. Every attorney who went to a federal clerkship submitted briefs in true small caps per FRAP. They will notice. We will not use faux small caps. Ever.*

*Three system options. Each is named for the institutional register it references. All three are valid. The selection should be based on which direction wins in the logo decision — because the logo typeface and the typographic system should share DNA.*"

---

## SHARED PRINCIPLES ACROSS ALL THREE OPTIONS

Regardless of which option is selected, these rules apply universally:

**Hierarchy construction:**
1. Small caps → Full caps → Italic → Roman (descending emphasis)
2. Scale differential: Display should be visually 2–3x larger than body — substantial, not subtle
3. Weight differential: Bold display + Regular body — or Regular display + no bold (let size carry the hierarchy)
4. No color in the hierarchy — black/charcoal only for type hierarchy; color (Burgundy) for structural elements (rules) only

**Spacing:**
- Leading: 140–150% of point size for body text (120pt leading on 10pt body = 12pt leading; this is tighter than ideal; use 14pt leading on 10pt body)
- Tracking for small caps: +25–35 units (generous — small caps at tight tracking lose their institutional quality)
- Column width: 60–75 characters per line for body text (the Bringhurst optimum)
- Margins: Generous — minimum 1.5" on print, minimum 40px on digital

**Type classes and when to use each:**
- **Display/Heading:** The typeface that sets the institutional register of each document
- **Body:** The typeface that carries the primary reading experience
- **Caption/Label:** Small supporting text — 8–9pt, often in small caps
- **Monospace/Technical:** For data labels, legal citations, code references

---

## OPTION A: THE SUPREME COURT
*Century Schoolbook Pro (Display + Headings) + Adobe Caslon Pro (Body)*

### The Register

The federal circuit. The Supreme Court brief. The Solicitor General's office. SCOTUS Rule 33 mandates Century family at 12pt with 2pt leading for Supreme Court briefs. When the Solicitor General of the United States files a brief, it is set in Century Schoolbook. This is the highest institutional authority in American law.

**Who this speaks to:** The attorney who clerked in a federal circuit. The attorney who has argued or dreamed of arguing in federal court. The attorney who owns every West Reporter volume for their circuits.

### The Typefaces

**Display / Heading: Century Schoolbook Pro**
- Developed by: Linn Boyd Benton for American Type Founders, 1895 (Schoolbook variant)
- Character: Wide proportions, ball terminals, sturdy serifs, high legibility at all sizes
- The visual anatomy: Heavy serifs. Ball terminals at the ends of strokes. Large x-height. Wide letterforms that breathe on the page.
- Why it's authentic: SCOTUS Rule 33 by name. West Publishing chose it for their casebooks. Federal courts cite it. It is not a stylistic choice — it is the typeface of legal authority.
- Modern source: Century Schoolbook Pro from URW Type Foundry (includes true small caps). Alternative: Monotype Century Schoolbook with OpenType small caps feature.

**Body: Adobe Caslon Pro**
- Developed by: William Caslon I, 1720s; digitized by Carol Twombly for Adobe, 1990
- Character: Slightly irregular, humanist warmth, excellent readability at text sizes, beautiful italic
- The visual anatomy: Moderate x-height, slight calligraphic variation in stroke weight, warm serifs
- Why it's authentic: Declaration of Independence face. Seventh Circuit brief guidelines recommend Caslon. "When in doubt, use Caslon." The New Yorker uses it for body text.
- Key: Must be the Pro version (Adobe Caslon Pro) — it includes genuine small cap glyphs, old-style figures, and proper ligatures. ITC Caslon is not acceptable.

### Type Scale — Option A

| Role | Typeface | Weight | Size | Leading | Tracking | Case |
|---|---|---|---|---|---|---|
| Display (cover, hero) | Century Schoolbook | Regular | 48–72pt | 110% | 0 | Title case |
| H1 (section title) | Century Schoolbook | Regular | 24–32pt | 120% | 0 | Title case |
| H2 (subsection) | Century Schoolbook | Regular, small caps | 14–16pt | 130% | +25 | ALL SMALL CAPS |
| H3 (sub-subsection) | Adobe Caslon Pro | Italic | 11–12pt | 140% | 0 | Title case |
| Body | Adobe Caslon Pro | Regular | 10–11pt | 150% | 0 | Sentence case |
| Caption | Adobe Caslon Pro | Regular, small caps | 8–9pt | 130% | +20 | ALL SMALL CAPS |
| Exhibit label | Century Schoolbook | Regular, small caps | 7–8pt | 120% | +15 | "EXHIBIT N:" |
| Running head/folio | Adobe Caslon Pro | Regular, small caps | 7–8pt | 120% | +15 | ALL SMALL CAPS |
| Footnote | Adobe Caslon Pro | Regular | 8–9pt | 130% | 0 | Sentence case |

### Figma Style Setup — Option A

**Text Styles to create:**

```
A / Display — Century Schoolbook / Regular / 60pt / 66pt leading / 0 tracking
A / H1 — Century Schoolbook / Regular / 28pt / 34pt leading / 0 tracking
A / H2 — Century Schoolbook / Regular / 15pt / 20pt leading / +25 tracking / OpenType small caps
A / H3 — Caslon Pro / Italic / 12pt / 17pt leading / 0 tracking
A / Body — Caslon Pro / Regular / 10.5pt / 16pt leading / 0 tracking
A / Caption — Caslon Pro / Regular / 8.5pt / 12pt leading / +20 tracking / OpenType small caps
A / Exhibit Label — Century Schoolbook / Regular / 7.5pt / 10pt leading / +15 tracking / OpenType small caps
A / Running Head — Caslon Pro / Regular / 7.5pt / 10pt leading / +15 tracking / OpenType small caps
A / Footnote — Caslon Pro / Regular / 8.5pt / 12pt leading / 0 tracking
```

**Font sourcing:**
- Century Schoolbook Pro: URW Type Foundry (available via Adobe Fonts or direct license); OR MyFonts. Look for: Century Schoolbook Pro with "small caps" or OpenType features listed.
- Adobe Caslon Pro: Adobe Fonts (Typekit subscription) — included in Creative Cloud. Pro version essential.

**OpenType feature settings (Figma: Advanced typography panel):**
- Small caps: Enable "Small Caps" (smcp) feature — NOT "All Caps" styling
- Old-style figures: Enable "Oldstyle" (onum) — for numerals in body text (they sit on the baseline like lowercase letters, not capitals)
- Ligatures: Enable standard ligatures (liga) — fi, fl, etc.

---

## OPTION B: THE GOLDMAN SACHS
*Century Schoolbook (Display) + Palatino (Body)*

### The Register

The Goldman Sachs annual report under Arnold Saks Associates, 1982–1994. Palatino at 10.5pt/14pt leading. Burt Glinn photography. Cover = single large typographic element. No decorative illustration. The boardroom. The institutional investor letter. The professional service firm that communicates exclusively through quality, not volume.

**Who this speaks to:** The attorney who followed the money — who reads Goldman research reports, understands institutional capital, and sees their law practice as a professional services business. The attorney who went to law school with the associates who went to Goldman.

### The Typefaces

**Display: Century Schoolbook (same as Option A)**
- At display sizes, Century Schoolbook carries the same institutional weight
- The difference from Option A: at body text, the switch to Palatino creates a different reading experience — slightly more calligraphic, slightly warmer

**Body: Palatino (Hermann Zapf, 1948)**
- Developed by: Hermann Zapf for Stempel, 1948; widely available
- Character: Slightly larger x-height than Caslon, calligraphic influences, beautiful in large format
- The visual anatomy: Wide lowercase, tall ascenders, generous proportions, pen-influenced strokes
- Why it's authentic: Confirmed Goldman Sachs typeface (Arnold Saks Associates). Federal courts recommend it. The design community considers it among the great readable serifs.
- Source note: Use Palatino Linotype (Windows) or Book Antiqua — but ideally source Palatino Nova (Linotype) for improved digital rendering. Do NOT use Palatino-clone faces that lack proper small caps.
- Key distinction from Caslon: Palatino reads slightly more architectural than Caslon's editorial quality. Caslon = New Yorker; Palatino = annual report.

**Accent/Display variant: Bodoni (display only)**
- For very large display applications (hero text on deck covers, large format print), Bodoni's extreme thick/thin contrast references the gold-lettered West Reporter spine
- Never at body text sizes — the hairline strokes disappear
- Bodoni Poster or Bodoni 72 Book are the correct weights to evaluate
- Use Bodoni no more than once per document — at a scale where the thick/thin contrast is visible

### Type Scale — Option B

| Role | Typeface | Weight | Size | Leading | Tracking | Case |
|---|---|---|---|---|---|---|
| Display (cover, hero) | Century Schoolbook | Regular | 48–72pt | 110% | 0 | Title case |
| H1 (section title) | Century Schoolbook | Regular | 24–32pt | 120% | 0 | Title case |
| H2 (subsection) | Century Schoolbook | Regular, small caps | 14–16pt | 130% | +25 | ALL SMALL CAPS |
| H3 (sub-subsection) | Palatino | Italic | 11–12pt | 140% | 0 | Title case |
| Body | Palatino | Regular | 10–11pt | 150% | 0 | Sentence case |
| Caption | Palatino | Regular, small caps | 8–9pt | 130% | +20 | ALL SMALL CAPS |
| Exhibit label | Century Schoolbook | Regular, small caps | 7–8pt | 120% | +15 | "EXHIBIT N:" |
| Running head/folio | Palatino | Regular, small caps | 7–8pt | 120% | +15 | ALL SMALL CAPS |
| Footnote | Palatino | Regular | 8–9pt | 130% | 0 | Sentence case |

**Key difference from Option A:** The body text in Palatino reads slightly more architecturally formal than Caslon. For financial-adjacent communications and sales decks, Palatino may be the stronger choice. For editorial content (blog, law review-style articles), Caslon is warmer.

### Figma Style Setup — Option B

```
B / Display — Century Schoolbook / Regular / 60pt / 66pt leading / 0 tracking
B / H1 — Century Schoolbook / Regular / 28pt / 34pt leading / 0 tracking
B / H2 — Century Schoolbook / Regular / 15pt / 20pt leading / +25 tracking / OpenType small caps
B / H3 — Palatino / Italic / 12pt / 17pt leading / 0 tracking
B / Body — Palatino / Regular / 10.5pt / 16pt leading / 0 tracking
B / Caption — Palatino / Regular / 8.5pt / 12pt leading / +20 tracking / OpenType small caps
B / Exhibit Label — Century Schoolbook / Regular / 7.5pt / 10pt leading / +15 tracking / OpenType small caps
B / Footnote — Palatino / Regular / 8.5pt / 12pt leading / 0 tracking
```

**Font sourcing:**
- Century Schoolbook: As above (Option A)
- Palatino Nova: Linotype (Adobe Fonts or direct). Pro weights include proper small caps. Do not use Palatino-clone faces.

---

## OPTION C: THE LAW REVIEW
*Tiempos Headline + Hoefler Text (or Chronicle Display) + Söhne*

### The Register

The Harvard Law Review as redesigned by Upstatement (2024). The American Lawyer at its peak design period. The modern legal editorial publication that looks like it belongs in 2026 while carrying the institutional authority of 150 years of case law. This is the "new classic" synthesis the research identified in the Modern Elevated section — Century grounding, 2026 precision.

**Who this speaks to:** The attorney who reads Bloomberg Law and wishes it were better designed. The attorney who came from BigLaw and chose PI. The attorney who looks at the American Lawyer's current redesign and feels something was lost. The attorney who notices when a publication is well-designed and appreciates it.

### The Typefaces

**Display: Tiempos Headline (Klim Type Foundry, Kris Sowersby)**
- Available at: klim.co.nz — purchase commercial license
- Character: Warm curves + sharp details. Designed to feel simultaneously historical (derives from the 18th-century serif tradition) and unmistakably contemporary. Used by legal brand Prāvo and Université Catholique de Lille.
- Weight to use: Bold for major display; Regular for display at large sizes
- The visual anatomy: Slightly condensed proportions, pronounced contrast between thick and thin, generous x-height, distinctive angled stress
- Why it works for Second Chair: "Could have appeared on a 1989 AmLaw 100 masthead, executed with the precision of a 2026 B2B product" — the exact formula identified in the research

**Body: Hoefler Text (Hoefler&Co)**
- Available at: typography.com (Hoefler&Co) — subscription required
- Character: Simultaneously classical and contemporary. Hoefler Text has extensive OpenType features, genuine small caps, old-style figures, discretionary ligatures.
- Why it's authentic: Used by the Harvard Law Review (Upstatement chose Hoefler Text for the digital redesign of HLR — if Second Chair uses Hoefler Text, it directly inherits the Harvard Law Review association). *This is a specific and significant distinctive asset.*
- Alternative: Chronicle Display at smaller body sizes if Hoefler Text is not available; or Adobe Caslon Pro from Option A as a fallback (maintains institutional quality)

**Display variant: Chronicle Display (Hoefler&Co)**
- The larger display sibling of Hoefler Text — for hero text on covers and large-format applications
- "Simultaneously 18th-century and unmistakably 21st-century" — the Hoefler&Co description is apt
- Use at 48pt+ where the Chronicle proportions read at their intended scale

**UI / Metadata: Söhne (Klim Type Foundry)**
- Available at: klim.co.nz (same foundry as Tiempos — single license relationship)
- Character: Refined Akzidenz Grotesk with warmth — institutional without coldness. The grotesque that doesn't feel corporate.
- Usage: UI labels, navigation, metadata text, captions where small caps serifs don't work
- Why this instead of Inter: Inter is the category convention. Söhne is outside the category. It is a grotesque with a different character — warmer, less tech-adjacent.
- Weight to use: Regular and Medium only. Not Bold (Hoefler Text handles the bold register).

### Type Scale — Option C

| Role | Typeface | Weight | Size | Leading | Tracking | Case |
|---|---|---|---|---|---|---|
| Display (cover, hero) | Chronicle Display / Tiempos | Bold | 48–72pt | 110% | 0 | Title case |
| H1 (section title) | Tiempos Headline | Bold | 24–32pt | 120% | 0 | Title case |
| H2 (subsection) | Hoefler Text | Regular, small caps | 14–16pt | 130% | +25 | ALL SMALL CAPS |
| H3 (sub-subsection) | Hoefler Text | Italic | 11–12pt | 140% | 0 | Title case |
| Body | Hoefler Text | Regular | 10–11pt | 150% | 0 | Sentence case |
| Caption | Söhne | Regular | 8–9pt | 130% | +5 | ALL CAPS |
| Exhibit label | Hoefler Text | Regular, small caps | 7–8pt | 120% | +15 | "EXHIBIT N:" |
| Running head/folio | Söhne | Regular | 7–8pt | 120% | +5 | ALL CAPS |
| Footnote | Hoefler Text | Regular | 8–9pt | 130% | 0 | Sentence case |
| UI label | Söhne | Regular | 11–13pt | 130% | +5 | Title case |

### Figma Style Setup — Option C

```
C / Display — Chronicle Display Bold / 60pt / 66pt leading / 0 tracking
C / H1 — Tiempos Headline / Bold / 28pt / 34pt leading / 0 tracking
C / H2 — Hoefler Text / Regular / 15pt / 20pt leading / +25 tracking / OpenType small caps
C / H3 — Hoefler Text / Italic / 12pt / 17pt leading / 0 tracking
C / Body — Hoefler Text / Regular / 10.5pt / 16pt leading / 0 tracking
C / Caption — Söhne / Regular / 8.5pt / 12pt leading / +5 tracking / All caps
C / Exhibit Label — Hoefler Text / Regular / 7.5pt / 10pt leading / +15 tracking / OpenType small caps
C / Running Head — Söhne / Regular / 7.5pt / 10pt leading / +5 tracking / All caps
C / Footnote — Hoefler Text / Regular / 8.5pt / 12pt leading / 0 tracking
C / UI Label — Söhne / Regular / 12pt / 16pt leading / +5 tracking
```

**Font sourcing:**
- Tiempos Headline: klim.co.nz — Commercial license. Weights: Regular, Bold. Expect $200–400 per weight for web+desktop.
- Chronicle Display: typography.com (Hoefler&Co) — Cloud.typography subscription. Or retail license.
- Hoefler Text: typography.com — Available as a local desktop license or Cloud.typography web font.
- Söhne: klim.co.nz — Same foundry as Tiempos. Commercial license. Weights: Regular, Medium.

---

## TYPE SYSTEM — OPTION COMPARISON

| Dimension | Option A (Supreme Court) | Option B (Goldman Sachs) | Option C (Law Review) |
|---|---|---|---|
| **Heading voice** | Supreme Court, federal brief | Annual report, boardroom | Law journal, editorial |
| **Body voice** | New Yorker, federal court | Goldman investor letter | HLR, modern editorial |
| **Era reference** | 1986–1995 federal courts | 1982–1994 finance | 1990–1995 law journal |
| **Audience recognition** | Federal clerks, brief-filers | Finance-adjacent attorneys | BigLaw alums, editorial-aware |
| **System complexity** | Low (2 typefaces) | Low (2–3 typefaces) | Medium (3–4 typefaces) |
| **Font cost** | Medium (Adobe Fonts subscription + URW license) | Medium (Linotype + URW) | Higher (Klim license + Hoefler subscription) |
| **Logo alignment** | Perfect for Direction A and B | Good for Direction B | Perfect for Direction C |
| **Recommended for** | Maximum institutional authority | Finance-prestige register | Modern editorial authority |

---

## THE HIERARCHY IN PRACTICE

**How a Second Chair document header works (all options):**

```
[RUNNING HEAD in small caps, 7.5pt, Warm Grey — above a 0.5pt Burgundy rule]

[SECTION TITLE in small caps, 15pt, Charcoal]

[HEADLINE in Display, 28–32pt, Charcoal]

[Body paragraph in body face, 10.5pt, Charcoal, 16pt leading]

[Caption or exhibit label in small caps, 8pt, Warm Grey — below a 0.5pt Burgundy rule]
```

This structure is legible in black-and-white. The only color additions are:
- Burgundy rules (horizontal, 0.5pt) as structural dividers
- Burgundy accent color in data exhibits (highlight bar/line)

Everything else is Charcoal on Cream. This is intentional. The typographic system carries the hierarchy; color carries the brand.

---

## DATA VISUALIZATION TYPOGRAPHY

Regardless of which option is selected, data visualization uses a specific typographic convention:

**Exhibit label:** "EXHIBIT N:" in display typeface small caps, 7–8pt, Warm Grey `#8C8680`, left-aligned, above the chart title
**Chart title:** Body typeface bold or display face at slightly larger size, states the conclusion in the title ("Signed cases cost 40% less at CPSC-aligned vendors")
**Data labels:** Body typeface regular, 7–9pt, directly on the data point — no legend boxes
**Axis labels:** Body typeface regular, 8pt, Warm Grey
**Source attribution:** "Source:" in italic, 7pt, Warm Grey, bottom-right

**The Exhibit convention (from the research) is the highest-priority Track 2 candidate in data visualization.** "Exhibit n:" in small caps is:
1. The McKinsey convention for analytical rigor
2. The legal convention for formally introduced evidence
3. Completely unused by every competitor in the category

Once established, this convention should appear on every chart, every table, every data point Second Chair publishes. It compounds.

---

## MASSIMO'S RECOMMENDATION

*"If Direction A (The Registry) or Direction B (The Plaque) wins in the logo decision: choose Option A or B for the typographic system. Century Schoolbook as the mark typeface should be Century Schoolbook as the heading typeface — system unity.*

*If Direction C (The Masthead) wins: choose Option C for the typographic system. Tiempos Headline in the wordmark should be Tiempos Headline in the headings. Caslon Pro bridges the masthead wordmark to the body.*

*My personal recommendation — and I am consistent in this: Option A, because it ties the wordmark, the typographic hierarchy, and the historical reference to a single source. Century Schoolbook Pro + Adobe Caslon Pro. The Supreme Court and The New Yorker. The federal court brief and the long-form article. The highest institutional authority and the most refined American prose voice. Together they cover every communication mode Second Chair will ever need.*

*But I will execute whichever direction Davis chooses. The system is designed to work. The execution will be impeccable regardless.*"

---

## GRAHAM'S TYPOGRAPHY READ

*"Massimo's right that system unity matters. But I want to add one art direction note about all three options:*

*The small caps are the voice. Before anyone reads the words in a Second Chair document, the small caps section headers communicate: this is a serious document, prepared by serious people who know how documents are made. The small caps are the visual signal of institutional discipline.*

*The choice between Options A, B, and C is largely a choice about which body typeface feels most right for the content Davis is actually writing. Caslon is warmer and editorial — better for case study content and long-form persuasion. Palatino is slightly more architectural — better for financial tables and formal presentations. Hoefler Text splits the difference — warm enough for editorial, precise enough for financial.*

*Pick the one that matches the writing mode Second Chair will be in most. And then set the exhibit convention regardless of which you choose — because that convention is the thing that no one else is doing, and it will become the most recognizable typographic signal Second Chair has.*"

---

*Typography system complete. See `02_Color_System.md` for color specifications.*
*Session documents: `00_Session_Brief.md`, `01_Logo_Directions.md`, `02_Color_System.md`, `03_Typography_System.md`*
