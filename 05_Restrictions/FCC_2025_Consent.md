# FCC 2025 Consent Rules

> **Source:** Saul.md Section 0.2
> 
> **Effective Date:** January 27, 2025
> 
> **This is not optional.** Non-compliance = class action lawsuit territory.

---

## What Changed

The FCC closed the "lead generator loophole." The old way is now ILLEGAL.

### ❌ OLD WAY (Now Illegal)
- Static "Marketing Partners" hyperlink
- Single checkbox for multiple buyers
- Blanket consent to unknown entities
- Ping-post auction decided AFTER form submission
- "See our 500 marketing partners" lists

### ✅ NEW WAY (Required)
- Specific named entity disclosed BEFORE consent
- Individual checkbox for EACH buyer
- Checkboxes unchecked by default
- Buyers determined BEFORE final submission
- One buyer, one checkbox, one consent

> **Saul says:** "The old way? You had a hyperlink that said 'see our 500 marketing partners' and prayed nobody clicked it. That's dead. Now, if Morgan & Morgan is going to call this lead, the form has to SAY 'Morgan & Morgan' before they check the box."

---

## The Dynamic Consent Flow

### Required Process
1. User enters zip code + injury type
2. System pings buyer network (real-time, BEFORE submission)
3. Form displays actual firm names bidding on this lead
4. User sees unchecked checkboxes for each firm
5. User selects which firms may contact them
6. Submission = consent ONLY to selected entities

### Technical Requirements
| Requirement | Status | Notes |
|-------------|--------|-------|
| **TrustedForm** | MANDATORY | Video replay of consent moment |
| **Jornaya LeadiD** | MANDATORY | Audit trail + bot detection |
| **Certificate Retention** | 5 years minimum | Keep all consent proof |

---

## Consent Language Template

### Single Firm
```
By submitting this form, I provide my express written consent to receive 
calls and/or text messages from [SPECIFIC NAMED FIRM] at the phone number 
provided, including via automated telephone dialing system or prerecorded 
voice. I understand that consent is not a condition of purchase. 
Message and data rates may apply.
```

### Multiple Firms (Dynamic)
```
I consent to receive calls and/or text messages from the following firms 
at the phone number provided:

☐ [Firm Name 1]
☐ [Firm Name 2]
☐ [Firm Name 3]

By checking the box(es) above, I provide my express written consent to be 
contacted by the selected firm(s), including via automated telephone 
dialing system or prerecorded voice. I understand that consent is not a 
condition of purchase. Message and data rates may apply.
```

---

## Form Requirements

| Requirement | Compliant | Non-Compliant |
|-------------|-----------|---------------|
| Buyer names | Actual firm names shown | "Marketing partners" link |
| Checkboxes | Individual per buyer | Single checkbox for all |
| Default state | Unchecked | Pre-checked |
| Placement | Above submit button | Below or in modal |
| TrustedForm | Active, capturing screen | Inactive or misconfigured |
| Firm selection | Before submission | After submission (ping-post) |

---

## The Math (Why This Matters)

| Violation Type | Per Call | 1,000 Leads | 10,000 Leads |
|----------------|----------|-------------|--------------|
| Negligent | $500 | $500,000 | $5,000,000 |
| **Willful** | $1,500 | $1,500,000 | **$15,000,000** |

> **Saul says:** "Ten thousand leads at $1,500 per willful violation. That's $15 million. Fifteen. Million. Dollars. Still think the consent checkbox is optional?"

---

## TrustedForm Requirements

### What It Must Capture
- Video replay of the consent moment
- Screen showing specific firm name at time of consent
- User action (checking box, clicking submit)
- Timestamp

### What Invalidates a Certificate
- "Marketing Partners" visible instead of firm name
- Pre-checked box visible
- Consent below fold/not visible
- Technical malfunction

> **Saul says:** "A lead without a TrustedForm certificate is a lead you can't defend in court. Period. If the certificate shows 'Marketing Partners' on the screen instead of the actual firm name? Congratulations, you just provided evidence against yourself."

---

## Compliance Checklist

Before launching any landing page:

### Consent Setup
- [ ] Individual checkboxes for each firm
- [ ] Checkboxes unchecked by default
- [ ] Actual firm names displayed (not "partners")
- [ ] Consent visible above submit button
- [ ] Consent language includes all required elements

### Technical Integration
- [ ] TrustedForm active and configured
- [ ] Jornaya LeadiD integrated
- [ ] Certificate storage set up (5+ years)
- [ ] Dynamic firm display working

### Testing
- [ ] Test submission captures correct certificate
- [ ] Certificate shows firm names on screen
- [ ] Checkbox states recorded correctly
- [ ] All required fields captured

---

## Deep Dive Reference

For complete TCPA consent details, see:
`05_Dept_Compliance/Rulebook/01_TCPA_Consent_2025.md`
