# Second Chair - Ad Image Iteration Workflow

> Interactive chat-first workflow for generating, iterating, and finalizing ad images.
> 
> **Chat = Creative Workspace** | **Airtable = Review Queue**

---

## Quick Start

**To generate images:**
```
"Generate 3 variations of a David vs Goliath infographic for the settlement gap angle"
```

**To iterate:**
```
"Make image 1 more aggressive with red tones"
"Try image 2 with Nevada desert background instead"
```

**To push to Airtable:**
```
"Add image 1 and 3 to record recsJClIWKEhaD49G"
"Create new row with all images"
```

---

## Workflow Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    CHAT (Creative Workspace)                 │
│                                                              │
│   Concept → Generate → Review → Iterate → Finalize          │
│                  ↑________________↓                          │
│                     (repeat until good)                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼ (only when ready)
┌─────────────────────────────────────────────────────────────┐
│                  AIRTABLE (Review Queue)                     │
│                                                              │
│   Push selected images → Team reviews → Deploy or iterate   │
└─────────────────────────────────────────────────────────────┘
```

---

## Session Image Tracking

All generated images in a session are numbered for easy reference:

```
Image 1: David vs Goliath infographic — [url]
Image 2: Boxing ring metaphor — [url]
Image 3: Army of suits vs one person — [url]
Image 4: Image 1 refined with red tones — [url]
```

Reference images by number in commands:
- "I like 1 and 3"
- "Refine image 2"
- "Add images 1, 3, 4 to Airtable"

---

## Generation Commands

### Basic Generation

```
"Generate an image of [description]"
"Create 3 variations of [concept]"
"Make me an infographic showing [idea]"
```

### With Specific Angle

```
"Generate a David vs Goliath visual for the settlement gap angle"
"Create a POV shot for the deadline urgency angle"
"Make a before/after transformation for the counterfactual angle"
```

### With Platform Specs

```
"Generate a 4:5 Meta feed image of [description]"
"Create a 9:16 vertical for TikTok showing [concept]"
```

---

## Iteration Commands

### Refinement

```
"Make image 1 more [aggressive/warm/dramatic/etc.]"
"Add [element] to image 2"
"Remove [element] from image 3"
"Try image 1 with [different setting/lighting/mood]"
```

### Variations

```
"Give me 2 more variations of image 1"
"Try the same concept but with [different approach]"
"Same idea, but more [UGC/cinematic/editorial] style"
```

### Comparison

```
"Which of these works better for the settlement gap angle?"
"Compare image 1 and 3 for the Meta feed"
```

---

## Airtable Commands

### Update Existing Record

```
"Add image 1 and 3 to record recXXXXXXXXXXXXXX"
"Push images 1, 2, 4 to recXXXXXXXXXXXXXX"
"Update the settlement gap ad with image 2"
```

**Finding the record ID:**
1. Open the record in Airtable (expand the row)
2. Look at the URL: `airtable.com/appXXX/tblXXX/viwXXX/recXXXXXXXXXXXXXX`
3. The `recXXXXXXXXXXXXXX` part is your record ID

### Create New Record

```
"Create new row with images 1, 2, 3"
"Add all images to a new Airtable row"
"Create new ad row titled 'Settlement Gap: Fighter' with images 1 and 3"
```

### With Additional Fields

```
"Create new row with:
- Title: Settlement Gap: The Fighter
- Images: 1, 3, 4
- State: NV
- Client: Jacoby & Meyers
- Strategy: David vs Goliath, fighting back narrative"
```

---

## Image Field Mapping

When pushing to Airtable:

| Image Selection | Airtable Fields |
|-----------------|-----------------|
| 1 image | IMG |
| 2 images | IMG, IMG 2 |
| 3 images | IMG, IMG 2, IMG 3 |

Images are assigned in order of selection:
- "Add images 3, 1, 4" → IMG=3, IMG 2=1, IMG 3=4

---

## Second Chair Specific Angles

Reference these when generating:

| Angle | Visual Direction |
|-------|------------------|
| **David vs Goliath** | Corporate tower vs single fighter, boxing ring, army vs one |
| **Settlement Gap** | Before/after numbers, low offer vs actual value |
| **Counterfactual** | Split screen paths, "what if" scenarios |
| **Insider Exposé** | Documents (blurred), behind-the-scenes |
| **Deadline Urgency** | Clocks, calendars, time pressure |
| **POV/Self-Reference** | Driver seat perspective, hands on wheel |

---

## Aspect Ratios

| Platform | Ratio | Use For |
|----------|-------|---------|
| Meta Feed | 1:1 or 4:5 | Primary feed ads |
| Meta Stories/Reels | 9:16 | Vertical full-screen |
| TikTok | 9:16 | Vertical only |
| Google Display | 16:9 or 1:1 | Banner/square placements |

Default: `4:5` for Meta feed (more real estate)

---

## Example Session

```
User: Generate 3 variations of a David vs Goliath infographic 
      for the settlement gap angle, 4:5 for Meta

Claude: [Generates 3 images]
  - Image 1: Corporate tower vs single fighter
  - Image 2: Boxing ring metaphor  
  - Image 3: Army of suits vs one person

User: I like 1 and 3. Make image 1 more aggressive with red tones

Claude: [Regenerates image 1]
  - Image 4: Corporate tower vs single fighter (aggressive, red accents)

User: Perfect. Add images 4 and 3 to record recsJClIWKEhaD49G

Claude: [Pushes to Airtable]
  - Updated record recsJClIWKEhaD49G
  - IMG: Image 4 (aggressive red)
  - IMG 2: Image 3 (army of suits)
```

---

## Best Practices

1. **Start broad** — Generate variations before narrowing
2. **Iterate fast** — Quick feedback loops are better than long prompts
3. **Reference by number** — "Image 2" is faster than describing it
4. **Only push when ready** — Airtable is for team review, not WIP
5. **Track your favorites** — Note which images worked for future reference

---

## Cross-References

- `IDEATION.md` — Angle frameworks, behavioral triggers
- `IMAGE_STYLE_GUIDE.md` — Visual style direction
- `AI_IMAGE_GUIDELINES.md` — Behavioral science image prompting
- `../../08_Ad_Factory/SKILL.md` — Full ad factory workflow
