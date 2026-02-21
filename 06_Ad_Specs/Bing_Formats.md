# Bing (Microsoft Ads) Formats: Second Chair

> **Platform Focus:** Search and display ads through Microsoft Advertising network.
> 
> **Key Insight:** Bing users skew older and more affluent. Lower competition than Google, often better CPL.

---

## Ad Copy Fields (Search)

| Field | Character Limit | Notes |
|-------|-----------------|-------|
| **Headlines** | Up to 15 | 30 characters each |
| **Descriptions** | Up to 4 | 90 characters each |
| **Display Path** | 2 fields | 15 characters each |
| **Final URL** | 1 | Landing page URL |

---

## Responsive Search Ads

| Element | Limit | Notes |
|---------|-------|-------|
| **Headlines** | 3-15 | 30 characters each, min 3 required |
| **Descriptions** | 2-4 | 90 characters each, min 2 required |
| **Display Path** | 2 fields | 15 characters each |

### Recommended Headlines (from approved phrases)
- "Car Accident Cases Being Accepted"
- "Speak With an Attorney Today"
- "Free Case Evaluation"
- "No Upfront Cost"
- "Legal Help Available Now"

---

## Microsoft Audience Network (Display)

### Image Ads
| Attribute | Specification |
|-----------|---------------|
| **Dimensions** | 1200 x 628px (1.91:1) |
| **Alternative** | 1200 x 1200px (1:1) |
| **File Size** | Max 5MB |
| **Format** | JPG, PNG, GIF |

### Responsive Ads
| Asset | Dimensions | Notes |
|-------|------------|-------|
| **Landscape Image** | 1200 x 628px (1.91:1) | Required |
| **Square Image** | 1200 x 1200px (1:1) | Recommended |
| **Logo** | 1200 x 1200px (1:1) | Square logo |
| **Headlines** | Up to 15 | 30 characters each |
| **Long Headline** | 1 | 90 characters |
| **Descriptions** | Up to 5 | 90 characters each |

---

## Multimedia Ads

| Attribute | Specification |
|-----------|---------------|
| **Video** | Up to 120 seconds |
| **Format** | MP4 |
| **Dimensions** | 16:9 preferred |

---

## Second Chair Specific Requirements

### Audience Advantage
Bing/Microsoft users:
- Skew older (35-65)
- Higher household income
- More likely to be in decision-making roles
- Lower ad competition = better CPL

### Compliance
- Same as Google requirements
- Third-person language
- No injury imagery
- Clear disclaimers

### Targeting
- Geographic: State-based
- Age: 35-65 optimal for Bing
- Device: Desktop users more common
- LinkedIn Profile Targeting available (Microsoft owns LinkedIn)

---

## Import from Google Ads

Microsoft Ads allows direct import from Google Ads:
1. Campaigns
2. Ad groups
3. Keywords
4. Ads

**Recommendation:** Build for Google first, import to Bing, then optimize for Bing's audience.

---

## Template Dimensions Quick Reference

```
Search:            Text only
Display Landscape: 1200 x 628px (1.91:1)
Display Square:    1200 x 1200px (1:1)
Video:             16:9 aspect
```

---

## Aspect Ratio for Ad Factory

Use `"aspect_ratio": "16:9"` or `"aspect_ratio": "1:1"` for Bing display ads.
