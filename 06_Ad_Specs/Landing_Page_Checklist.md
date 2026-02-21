# Landing Page Checklist: Second Chair

> **Source:** Saul.md Mode C (Landing Page Auditor) + FCC 2025 Requirements
> 
> Run through this checklist before launching any landing page.

---

## Pre-Launch Checklist

### Required Disclosures

- [ ] **"This is an advertisement"** — Visible in header or above form
- [ ] **Lead gen disclosure** — "You are not contacting an attorney directly. Your information will be shared with a participating law firm."
- [ ] **Privacy policy link** — Clearly visible and accessible
- [ ] **"Past results do not guarantee future outcomes"** — If any settlement amounts mentioned

---

### TCPA Consent (FCC 2025 Compliant)

- [ ] **Specific firm names displayed** — Not "marketing partners"
- [ ] **Individual checkboxes** — One per firm
- [ ] **Unchecked by default** — No pre-checked boxes
- [ ] **Above submit button** — Visible before user submits
- [ ] **Proper consent language** — Includes all required elements:
  - Express written consent
  - Automated dialing system mention
  - Not condition of purchase
  - Message and data rates

---

### Technical Integration

- [ ] **TrustedForm active** — Capturing video replay
- [ ] **TrustedForm configured correctly** — Shows firm names on screen
- [ ] **Jornaya LeadiD integrated** — Audit trail active
- [ ] **Certificate storage** — Set up for 5+ year retention
- [ ] **Form submission working** — Test submissions going through

---

### Dynamic Consent (If Multi-Firm)

- [ ] **Ping-post architecture** — Firms determined BEFORE submission
- [ ] **Real-time display** — Actual bidding firms shown
- [ ] **User selection** — User chooses which firms can contact
- [ ] **Consent limited** — Only selected firms get consent

---

### Copy Compliance

- [ ] **Third-person language** — No "you" + injury/condition
- [ ] **No banned phrases** — Check against `Banned_Phrases.md`
- [ ] **Qualified claims** — "Settlements in similar cases..." not guarantees
- [ ] **No "recommend" language** — We connect, we don't recommend

---

### Visual Compliance

- [ ] **No banned imagery** — Check against `Banned_Imagery.md`
- [ ] **Recovery/hope focus** — Not trauma/injury
- [ ] **Readable disclosures** — 8pt minimum, good contrast
- [ ] **Professional appearance** — Not "ambulance chaser" vibes

---

### Mobile Experience

- [ ] **Form works on mobile** — Test on actual device
- [ ] **Disclosures visible mobile** — Not hidden by viewport
- [ ] **Consent checkboxes accessible** — Easy to tap
- [ ] **Page speed acceptable** — Under 3 seconds

---

## Compliance Scoring

Rate each section:

| Section | Score (1-5) | Notes |
|---------|-------------|-------|
| Disclosures | | |
| TCPA Consent | | |
| Technical | | |
| Copy | | |
| Visual | | |
| Mobile | | |
| **TOTAL** | /30 | |

**Minimum to launch:** 25/30 (no section below 4)

---

## Common Failures

### Instant Fails (Do Not Launch)

| Issue | Why It Fails |
|-------|--------------|
| Pre-checked consent boxes | FCC 2025 violation |
| "Marketing partners" instead of firm names | FCC 2025 violation |
| Consent below submit button | Not visible = not valid |
| No TrustedForm | No defense in court |
| "You" + injury in headlines | Meta rejection |
| Blood/injury imagery | Meta rejection |

---

### Saul's Quick Audit

> **Saul says:** "Here's what I check first:
> 1. Is the consent above the button? 
> 2. Do I see actual firm names or 'partners'?
> 3. Are the boxes pre-checked?
> 4. Can I actually read the disclosures?
> 
> If any of those fail, we're not launching. Fix it."

---

## Post-Launch Monitoring

### First 24 Hours
- [ ] Check TrustedForm certificates generating
- [ ] Verify form submissions reaching CRM
- [ ] Monitor for ad rejections
- [ ] Watch CPMs for anomalies

### Ongoing
- [ ] Weekly TrustedForm audit
- [ ] Monthly consent language review
- [ ] Quarterly full compliance check

---

## Resources

| File | Use For |
|------|---------|
| `Disclosure_Library.md` | Copy-paste disclosure text |
| `FCC_2025_Consent.md` | Consent requirements deep dive |
| `Banned_Phrases.md` | Copy QA |
| `Banned_Imagery.md` | Visual QA |
| `Platform_Rules.md` | Platform-specific rules |
