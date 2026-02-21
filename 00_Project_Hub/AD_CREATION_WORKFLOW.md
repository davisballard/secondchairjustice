# Second Chair Ad Creation Workflow

> **Trigger:** "Make ads for [STATE]" or "Create ads for [STATE]"
> 
> **What Happens:** The agency team loads all relevant context, runs a roundtable discussion, and works interactively with you to develop concepts and executions.

---

## How This Works

1. **You say:** "Make ads for CA" (or any active state)
2. **System:** Auto-loads all relevant context for that state
3. **Agency asks:** "What's the goal — testing new angles or scaling winners?"
4. **Roundtable:** Experts discuss and build on each other's ideas
5. **Hegarty review:** ECD filters concepts before presenting
6. **You pick:** Which concept(s) to develop
7. **FORMAT DISCUSSION:** Experts discuss content type options (static, motion still, video, etc.) with placement implications — you pick format before execution
8. **Execution:** Develop headlines, copy, prompts for the chosen format
9. **Production:** Ready for generation

> **IMPORTANT:** Do NOT jump from concept selection (step 6) directly to full execution. Step 7 (format discussion) must happen first. Different formats have different placement access, production costs, and testing implications. Get alignment on format before building out copy and prompts.

---

## The Agency Team

When triggered, load these expert agents for the roundtable:

| Expert | Role | File |
|--------|------|------|
| **Julian Cole** | Head of Strategy — Strategic frame, comms architecture | `01_Dept_The_Lab_Strategy/Julian_Cole_(Head_of_Strategy)/AGENT.md` |
| **Richard Shotton** | Behavioral Scientist — Psychological levers, biases to exploit | `01_Dept_The_Lab_Strategy/Richard_Shotton_(Behavioral_Scientist)/AGENT.md` |
| **Ed McCabe** | Senior Copywriter — Headlines, hooks, copy craft | `02_Dept_Creative_Core/Ed_McCabe_(Senior_Copywriter)/AGENT.md` |
| **Depesh Mandalia** | Meta Specialist — Format selection, platform tactics | `04_Dept_Growth_Distribution/Depesh_Mandalia_(Meta_Paid_Social)/AGENT.md` |
| **Indigo Sato** | Performance Creative — Testing structure, creative strategy | `04_Dept_Growth_Distribution/Indigo_Sato_(Performance_Creative)/AGENT.md` |
| **Giuseppe Karma** | AI Creative Director — Visual direction, image prompts | `03_Dept_Production_Studio/Giuseppe_Karma_(AI_Creative_Director)/AGENT.md` |
| **John Hegarty** | Executive Creative Director — Quality gate, pushes for stronger concepts | `02_Dept_Creative_Core/John_Hegarty_(Executive_Creative_Director)/AGENT.md` |

---

## Context Auto-Loading

### For Any State

**Brand Core:**
- `01_Identity/Brand_Essence.md` — Mission, positioning
- `01_Identity/Partner_Firms.md` — Which firm for which state
- `03_Voice/Third_Person_Rules.md` — "YOU" ban, third-person language

**Strategic Frameworks:**
- `07_Research/Strategic_Analysis/BEHAVIORAL_CONTENT_SYSTEM.md` — Psychological levers, power scores
- `07_Research/Strategic_Insights/Audience_Psychology_Insights.md` — Victim psychology, punchy lines
- `02_Visual/Video_Format_Strategy.md` — Format guidance (Motion Still, TikTok Slide)

**Restrictions:**
- `05_Restrictions/Platform_Rules.md` — Meta Special Ad Categories
- `05_Restrictions/State_Bar_Quick_Ref.md` — State-specific disclosure requirements

### State-Specific Context

| State | Partner Firm | Stats Reference | State Rules |
|-------|-------------|-----------------|-------------|
| **CA** | Larry H. Parker | `07_Research/Partner_Firms/CA_Ads_Stats_Reference.md` + `Larry_H_Parker_Reference.md` | Standard |
| **NV** | Jacoby & Meyers | `07_Research/Partner_Firms/Jacoby_Meyers_Reference.md` | `05_Restrictions/nevada/` |
| **CO** | Jacoby & Meyers | `07_Research/Partner_Firms/Jacoby_Meyers_Reference.md` | `05_Restrictions/colorado/State_Rules.md` |
| **WA** | Jacoby & Meyers | `07_Research/Partner_Firms/Jacoby_Meyers_Reference.md` | `05_Restrictions/washington/State_Rules.md` |

---

## The Golden Rule: Form Alignment

**Every ad angle MUST tie back to the form action.**

The form is a 6-question quiz that delivers a **FREE CLAIM ESTIMATE**:

> **Form Experience:** 6-question quiz (accident → timing → injury → medical care → fault → attorney) → loading screen with progress bar → lead capture (name, phone, email). The form delivers a FREE CLAIM ESTIMATE.

### The Alignment Chain

```
HOOK (emotional/behavioral lever)
    ↓
BRIDGE ("here's how to find out")
    ↓
PROMISE (what the form delivers: "your free estimate")
    ↓
CTA (matches the promise: "See my estimate" / "Check if you qualify")
```

### Angle Transformation Examples

**Bad (angle doesn't connect to form):**
> "Dashcams delete in 48hrs"
> 
> Problem: Talks about evidence, but form delivers an estimate

**Good (same insight, ties to form):**
> "Evidence disappears fast. Find out what your case is worth before it's too late."
> 
> Solution: Same urgency, bridges to estimate

**Bad:**
> "Insurance companies lowball you"
> 
> Problem: Talks about fighting insurance, no form connection

**Good:**
> "Insurance offered you a number. See what similar cases actually received."
> 
> Solution: Same villain, bridges to comparison/estimate

**The principle:** Hooks like "fighting insurance" are fine, but they must bridge to "find out what you're owed" / "check if you qualify" / "get your free estimate."

---

## Platform Focus

| Priority | Platform | Formats |
|----------|----------|---------|
| **Primary** | Meta (Instagram Feed, Reels, Stories + Facebook) | Static images (4:5), Motion Stills (9:16 for Reels/Stories) |
| **Future** | TikTok | Explore once Meta is performing |

### Format Selection Guide

| Format | When to Use | Production Effort |
|--------|-------------|-------------------|
| **Static Image** | Testing new concepts fast, A/B testing copy | Low |
| **Motion Still (5-6s)** | Proven static that needs Reels/Stories placement | Low-Medium |
| **Story Slide (15s)** | Story-based concepts needing sequence (problem → action → solution) — works on Meta Reels/Stories/Feed | Medium |
| **Full VO Video** | Retargeting, authority content, testimonials | High |

**Start with:** Static + Motion Stills for testing velocity. Graduate to slides for winning concepts.

---

## The Roundtable Format

Experts speak together, building on each other's ideas:

```
JULIAN (Strategy): "The strategic problem we're solving is [X]. The barrier 
is [Y]. We need different messages for different moments, but the core 
unlock is..."

RICHARD (Behavioral): "Building on that, the bias to exploit here is [X]. 
Research shows [study] — we can apply this by..."

ED (Copy): "If we're using that lever, the headline structure should be 
[formula]. Something like: '[headline option]' — direct, specific, 
form-aligned."

DEPESH (Media): "For Meta cold traffic in Special Ad Categories, that 
angle works best as [format] because [reason]. The algorithm will respond 
to..."

INDIGO (Performance): "To test this properly, we need [X] variations. I'd 
structure it as 3 hooks × 2 bodies × 2 CTAs = 12 variations. Winners get 
iterated into..."

GIUSEPPE (Visual): "Visually, I'd execute this as [description]. iPhone 
quality, documentary feel. The prompt direction: [brief prompt idea]..."

HEGARTY (ECD): "Hold on. Is this in the 10%? Does it give you goosebumps? 
[Either approves or pushes for stronger work before presenting]"
```

---

## Intake Question

After loading context, always ask:

> **"What's the goal — testing new angles or scaling winners?"**
> 
> - **Testing new angles:** We'll develop 3-5 fresh concepts across different behavioral levers
> - **Scaling winners:** Tell me what's working and we'll create variations/iterations

---

## Concept Presentation Format

After the roundtable and Hegarty's quality gate, present concepts like this:

```
────────────────────────────────────────────────────────
CONCEPT A: [Name]
────────────────────────────────────────────────────────

Strategic Insight: [One sentence — the human truth we're tapping into]

Behavioral Lever: [Primary bias + any amplifiers]

Form Alignment: [How it ties to the estimate/qualification]

Headline Direction: "[Example hook]"

Visual Direction: [Brief description of the image/video approach]

Format: [Static / Motion Still / TikTok Slide]

Why It Should Work: [1-2 sentences grounded in research or psychology]

────────────────────────────────────────────────────────
```

Then ask: **"Which concepts do you want to develop?"**

---

## Execution Development

Once you pick concepts, we develop:

| Element | What We Create |
|---------|----------------|
| **Headlines** | 3-5 variations per concept |
| **Post Copy** | Primary text (under 125 characters + extended body) |
| **Image Prompts** | Production-ready for Fal.ai |
| **Format Specs** | Aspect ratio, placement, variations needed |
| **Testing Matrix** | Which hooks to test against each other |

---

## Output Format (Production-Ready)

Final concepts formatted for the Ad Factory:

```python
{
    "type": "image",
    "ad_title": "Concept Name - Variation",
    "post_copy": "The post copy here...",
    "headline": "The headline",
    "description": "The description",
    "cta": "Learn More",
    "display_link": "claimjusticenow.com",
    "image_prompt": "Detailed image prompt here...",
    "strategy": "Brief behavioral rationale",
    "state": "CA",
    "client": "Larry H. Parker",
    "channel": "Meta",
    "variations": 3,
    "aspect_ratio": "4:5",
}
```

---

## Quick Reference: California Stats

For CA campaigns, these stats are approved for use:

| Stat | Value | Use In |
|------|-------|--------|
| **Total Recovered** | $2.2 Billion+ | Headlines, hero sections, ads |
| **Success Rate** | 95% | Trust badges, ads |
| **Years Experience** | 45+ | Trust badges |
| **Clients Served** | 100,000+ | Social proof |

**Remember:** Stats can be used in ads, but the firm name (Larry H. Parker) can ONLY appear in form fine print, consent checkbox, and thank you page header — never in ads.

---

## Compliance Reminders

Before finalizing any ad:

- [ ] Third-person language only (no "you were injured")
- [ ] "This is an advertisement. Statutes of limitations apply."
- [ ] No specific dollar guarantees
- [ ] No firm name in ad creative (stats are OK)
- [ ] Form-aligned CTA (estimate/qualify language)

---

## Related Files

| File | Purpose |
|------|---------|
| `BRAND_MASTER.md` | Full brand hub and file index |
| `10_Ad_Factory/Production_Guidelines/IDEATION.md` | Image prompt templates, angle categories |
| `10_Ad_Factory/Production_Guidelines/Image_Style_Guide.md` | Visual style direction |
| `02_Visual/Video_Format_Strategy.md` | Motion Still + TikTok Slide specs |

---

*Last Updated: January 2026*
