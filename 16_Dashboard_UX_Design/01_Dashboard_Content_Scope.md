# Second Chair — Dashboard Content Scope
*What the Client Dashboard Contains and Why*
*Luke Grabowski (lead) | Session: March 2, 2026*

---

## LUKE'S FRAMING

*"Before I list data categories, I want to establish the organizing logic. A dashboard is not a database browser — it is not 'all the data we have access to, displayed.' It is a curated analytical argument. The question before every data category is: does this belong in the dashboard, or does it belong in a drill-down report, or does it belong in a data export?*

*The framework I use: if an attorney needs this information to make a weekly operating decision, it belongs in the dashboard. If they need it to evaluate a specific case or dispute a specific lead, it belongs in a drill-down. If they need it for their own accounting or case management, it belongs in an export.*

*With that framing, here is every data category Second Chair needs, organized by the attorney's decision-making chain."*

---

## THE ATTORNEY'S DECISION CHAIN

Every data category in this document maps to one of five decisions the attorney makes at different intervals:

| Decision | Frequency | Dashboard or Report |
|---|---|---|
| **Is this working this week?** | Weekly | Dashboard (primary view) |
| **Is this on track this month?** | Monthly | Dashboard + Monthly Report |
| **Is my investment efficient?** | Ongoing, checked monthly | Dashboard (persistent metric) |
| **Should I change my territory or case mix?** | Quarterly | Dashboard + Drill-down |
| **Should I renew / expand / reduce?** | Contract renewal | Monthly Report history |

---

## DATA CATEGORY 01: LEAD VOLUME

**The primary metric. The first thing every attorney checks.**

### Core Metrics
| Metric | Definition | Display Format |
|---|---|---|
| Leads This Period | Count of leads delivered in current period (MTD, QTD, or custom range) | Hero number (Exhibit 1) |
| Leads Last Period | Same count for prior comparable period | Supporting number with delta |
| Period-Over-Period Change | % change from last period to current | Delta indicator (Success Green if positive, Burgundy if negative) |
| Leads Remaining in Subscription | If on a subscription model: leads left in current billing period | Supporting stat |

### Lead Volume by Time Dimension
| Metric | Definition | Chart Type |
|---|---|---|
| Daily Lead Volume (30-day rolling) | Leads per day, trailing 30 days | Area chart |
| Weekly Lead Volume (13-week rolling) | Leads per week, trailing 13 weeks | Isometric bar chart |
| Monthly Lead Volume (12-month) | Leads per month, trailing 12 months | Isometric bar chart |

### Lead Volume Segmentation
| Dimension | Why It Matters | Chart Type |
|---|---|---|
| By case type | Attorneys typically want specific case mixes; imbalance signals a configuration issue | Donut chart with dimensional disk |
| By source channel | Meta vs. Google vs. organic vs. referral — which sources are producing | Isometric bar chart (multi-series) |
| By geography / county | Attorneys often have specific coverage areas; lead volume by territory | Data table with inline bar |
| By time of day received | Operational: are leads coming during intake hours? | Area chart |

**Decision this serves:** "Is this working this week?" — answered at a glance by Exhibit 1 (hero number) and Exhibit 2 (area chart).

---

## DATA CATEGORY 02: LEAD QUALITY

**The second thing attorneys ask, usually within the first month.**

Lead quality is where Second Chair differentiates from commodity lead vendors. The dashboard must make quality visible — not as a vague score but as measurable conversion outcomes that the attorney can trace.

### Core Quality Metrics
| Metric | Definition | Display Format |
|---|---|---|
| Contact Rate | % of leads where attorney's intake team made contact | Hero stat (Exhibit 3 or standalone panel) |
| Consultation Rate | % of contacted leads who completed a consultation | Supporting stat |
| Sign Rate | % of consultations that resulted in a signed case | Supporting stat |
| Overall Conversion Rate | Leads → Signed (end-to-end) | Trend line |

### The Conversion Funnel
This is the single most important multi-step data visualization in the product.

```
LEADS DELIVERED
    ↓ [Contact Rate %]
LEADS CONTACTED
    ↓ [Consultation Rate %]
CONSULTATIONS COMPLETED
    ↓ [Sign Rate %]
CASES SIGNED
```

**Display:** A staged funnel visualization — each stage is a bar (isometric treatment) with the stage label in Caslon small caps and the conversion rate percentage between stages. The funnel reads top to bottom. The total case count is the hero number at the bottom.

**Why this matters:** The funnel separates Second Chair's performance (lead delivery, lead quality) from the attorney's performance (intake responsiveness, consultation quality). If the sign rate is low but the contact rate is high, the issue is the attorney's consultation process, not Second Chair's leads. This distinction matters for renewal conversations.

### Quality Segmentation
| Dimension | Why It Matters |
|---|---|
| Quality by case type | Some case types have structurally higher or lower sign rates; segmentation separates product quality from case mix selection |
| Quality by source channel | Meta leads vs. Google leads convert at different rates; visibility prevents misattribution |
| Quality trend (13-week) | Is lead quality improving or degrading over time? The trend matters more than a single period's number |

### Lead-Level Quality Data (Drill-Down Only)
Individual lead records belong in a drill-down, not the primary dashboard. Each lead shows:
- Lead ID (IBM Plex Mono)
- Case type
- Source channel
- Date/time received
- Intake disposition (contacted / not reached / consultation / signed / declined)
- Attorney notes (free text)

The primary dashboard shows aggregate quality metrics. The lead-level table is accessible via a navigation action ("View Leads" or "Lead Detail") from the quality panel.

---

## DATA CATEGORY 03: COST EFFICIENCY

**The ROI question. The most important metric for retention.**

If an attorney is convinced that Second Chair produces signed cases at a cost below their target, they renew. If they are not convinced, they do not. This data category must make the business case clearly, without the attorney having to calculate anything.

### Core Efficiency Metrics
| Metric | Definition | Display Format |
|---|---|---|
| Cost Per Lead (CPL) | Total spend ÷ leads delivered, current period | Persistent stat in header or Exhibit |
| Cost Per Signed Case (CPSC) | Total spend ÷ cases signed, current period | Hero stat — the most important efficiency metric |
| CPSC Trend (13-week) | CPSC by week, trailing 13 weeks | Area chart (single series, Burgundy) |
| CPSC vs. Target | Current CPSC vs. the attorney's target or industry benchmark | Delta indicator |
| CPSC vs. Category Average | Current CPSC vs. Second Chair's median CPSC across comparable accounts | Comparative bar |

**The CPSC is the single most important number in the entire dashboard.** It is the number the attorney photographs and shows their partner. It is the number that determines renewal. Design priority: CPSC should be the largest displayed number after the lead volume hero.

### Efficiency by Segment
| Dimension | Why It Matters |
|---|---|
| CPSC by case type | Mass tort cases cost more to sign than auto accidents; segmentation prevents apples-to-oranges comparison |
| CPSC trend vs. prior period | Is efficiency improving? Month-over-month CPSC trend is the most predictive retention signal |
| CPSC vs. stated case value | If average case value is known, CPSC as % of case value is the clearest ROI metric |

### Revenue Projection (Optional, Phase 2)
If Second Chair has data on average case settlement values by type, a simple projected ROI panel can be calculated:
- Average case value × signed cases = projected gross revenue from Second Chair leads
- Projected gross revenue ÷ total spend = projected ROI multiple

This panel should be labeled clearly as a projection and carry a methodology footnote. It is powerful for retention and dangerous if oversimplified. Phase 2.

---

## DATA CATEGORY 04: CAMPAIGN PERFORMANCE

**The operational layer. Answers "how is Second Chair generating these leads?"**

Most PI lead gen vendors show only the output (leads delivered) without any transparency into the inputs (how leads were generated). Second Chair's transparency here is a differentiator — it signals that the company understands its own operation and is not hiding underperformance behind a black box.

### Core Campaign Metrics
| Metric | Definition | Display Format |
|---|---|---|
| Total Media Spend | Actual media spend on behalf of this client's territory/case types in the period | Supporting stat |
| Cost Per Click (CPC) | Average CPC across active campaigns | Supporting stat |
| Click-Through Rate (CTR) | Average CTR across active campaigns | Supporting stat |
| Lead Conversion Rate | Leads generated ÷ total clicks (how efficiently Second Chair converts clicks to leads) | Supporting stat |
| Active Campaigns | Count of currently active campaigns for this account | Supporting stat |

### Channel Breakdown
| Channel | Display |
|---|---|
| Meta (Facebook/Instagram) | Share of spend, lead volume, CPL |
| Google Search | Share of spend, lead volume, CPL |
| Other (if applicable) | Share of spend, lead volume, CPL |

**Chart type:** Multi-series isometric bar chart showing CPL by channel, period over period. The attorney sees which channel is producing efficiently and which is not.

### Campaign Transparency Note
The level of campaign detail exposed depends on Second Chair's business model:
- **If accounts are managed collectively** (Second Chair runs campaigns for a territory and allocates leads across multiple clients): show aggregated territory performance, not client-specific campaign data
- **If accounts are managed individually** (dedicated campaigns per client): show full campaign detail

This document assumes the more common collective/territory model. Individual campaign exposure is Phase 2.

---

## DATA CATEGORY 05: ACCOUNT STATUS AND ALERTS

**The operational overview. Answers "is there anything I need to deal with right now?"**

This is not a primary analytical exhibit. It is a status layer — a persistent panel that surfaces anything requiring attorney attention without requiring the attorney to go looking for it.

### Alert Types
| Alert | Trigger | Severity |
|---|---|---|
| Lead volume below threshold | Period-to-date leads are tracking below target by >15% | Medium |
| Billing event | Invoice generated, payment due, payment failed | High |
| Lead quality dispute | Attorney has flagged a lead; resolution pending | Low |
| Coverage gap | Attorney's territory has no active campaign in a specified case type | Medium |
| Subscription milestone | Approaching or exceeded subscription lead count | Informational |
| New report available | Monthly performance report has been generated | Informational |

### Display Logic
- Alerts appear in a persistent banner or sidebar panel, never as popups or modals that interrupt the analytical view
- High-severity alerts (billing failure, payment issue) appear at top of the primary view, above Exhibit 1
- Medium and low alerts appear in a collapsible alert panel in the sidebar
- Informational alerts (new report available) appear as a subtle badge on the relevant navigation item

---

## DATA CATEGORY 06: MONTHLY PERFORMANCE REPORT

**The formal analytical document. The exhibit-format document that goes to the attorney and can be shared with their firm.**

The monthly report is not a screen — it is a generated PDF document that follows the same exhibit conventions as the dashboard but in print register. It is referenced here because the dashboard must surface:
- That a report has been generated (notification)
- The most recent report (accessible from the dashboard)
- Archive of prior reports (accessible from the Reports section)

### Report Contents (What the Generated Document Contains)
| Section | Description |
|---|---|
| Cover | Second Chair identity (Direction A/B/C), client name, reporting period, date |
| Executive Summary | 3–5 bullet findings in S-O-S format (Situation, Complication, Resolution) |
| Exhibit 1: Lead Volume | Volume trend, period comparison, segmentation |
| Exhibit 2: Conversion Funnel | Full funnel with rates at each stage |
| Exhibit 3: Cost Efficiency | CPSC trend, current period vs. target |
| Exhibit 4: Channel Performance | By-channel breakdown of spend and CPL |
| Exhibit 5: Cases Signed | Count, by case type, with CPSC |
| Appendix: Lead Detail | Full lead-level data table for the period |

The report is a designed object — not an exported CSV, not a generic PDF. It uses the same typefaces, the same exhibit convention, the same rule weights as the dashboard. An attorney who opens the report after using the dashboard should feel they are in the same system.

---

## DATA CATEGORY 07: ACCOUNT SETTINGS AND CONFIGURATION

**Operational — not analytical. The attorney manages their account here.**

This section is outside the analytical dashboard scope. It exists for completeness and to confirm that account management functions do not contaminate the analytical view.

### What Belongs Here
- Subscription plan and billing information
- Territory and geography settings (what counties/DMAs are covered)
- Case type preferences (what types of leads to receive)
- Intake contact information (phone numbers, CRM integration settings)
- User management (who has access to this account)
- Notification preferences

**Design principle:** Account settings live in a separate section, accessible via navigation, not embedded in the analytical dashboard. The attorney who opens the dashboard to check performance is not confronted with account management UI — those are separate jobs.

---

## CONTENT SCOPE SUMMARY

| Category | Primary Dashboard | Drill-Down | Report |
|---|---|---|---|
| Lead Volume (totals + trend) | ✓ | — | ✓ |
| Lead Volume (segmentation) | Summary | Full | ✓ |
| Lead Quality (funnel, rates) | ✓ | — | ✓ |
| Lead Quality (individual leads) | — | ✓ | Appendix |
| Cost Per Lead | ✓ | — | ✓ |
| Cost Per Signed Case | ✓ | — | ✓ |
| CPSC Trend | ✓ | — | ✓ |
| Campaign Performance | Summary | Full | ✓ |
| Account Alerts | ✓ | — | — |
| Monthly Report Access | Notification + Link | — | ✓ |
| Account Settings | — | ✓ | — |

---

## WHAT IS OUT OF SCOPE (VERSION 1)

The following are real data points Second Chair may eventually expose. They are explicitly out of scope for V1 to prevent dashboard complexity from exceeding what the data infrastructure can support at launch:

- **Competitive benchmarks** — "Your CPSC vs. the category average." Requires normalized comparison data across client base. Phase 2 when client base is large enough.
- **Predictive / projected ROI** — Revenue projection based on case values. Requires settlement value data, which Second Chair may not have. Phase 2.
- **Real-time lead notifications** — Push notification when a lead is delivered. Mobile app feature, not dashboard. Phase 2.
- **A/B test performance** — Internal campaign optimization data. Not client-facing in V1.
- **Attorney intake performance scoring** — Ranking how well the attorney's intake compares to other Second Chair clients. Potentially useful for retention, politically sensitive. Phase 2.

---

*Next: `02_UX_Architecture.md` — how this content organizes into screens, navigation, and exhibit sequences.*
