# Disclosure Library

> **Source:** Saul.md Mode C (Landing Page Auditor) + FCC 2025 Requirements
> 
> Required legal language for ads and landing pages. Non-negotiable.

---

## Required Disclosures (Non-Negotiable)

These MUST appear on all landing pages:

### 1. Advertising Disclosure
```
This is an advertisement for legal services.
```
**Placement:** Header or above the form
**Visibility:** Must be readable, not hidden

---

### 2. Lead Gen Disclosure
```
You are not contacting an attorney directly. Your information will be 
shared with a participating law firm.
```
**Placement:** Near the form, visible before submission
**Visibility:** Readable font size, decent contrast

---

### 3. Outcome Disclaimer
```
Past results do not guarantee future outcomes.
```
**Placement:** Footer or near any settlement/dollar mentions
**Use when:** Any mention of settlement amounts or case results

---

## TCPA Consent Language (2025 Compliant)

### Standard Consent (REQUIRED)
```
By submitting this form, I provide my express written consent to receive 
calls and/or text messages from [SPECIFIC NAMED FIRM] at the phone number 
provided, including via automated telephone dialing system or prerecorded 
voice. I understand that consent is not a condition of purchase. 
Message and data rates may apply.
```

**CRITICAL:** `[SPECIFIC NAMED FIRM]` must be the actual firm name displayed on the form. No "marketing partners" lists. One firm, one checkbox, one consent.

---

### Multi-Firm Dynamic Consent
When multiple firms may contact the lead:
```
I consent to receive calls and/or text messages from the following firms 
at the phone number provided:

☐ Jacoby & Meyers
☐ Sink Law  
☐ [Firm 3]

By checking the box(es) above, I provide my express written consent to be 
contacted by the selected firm(s), including via automated telephone 
dialing system or prerecorded voice. I understand that consent is not a 
condition of purchase. Message and data rates may apply.
```

**Requirements:**
- Checkboxes must be UNCHECKED by default
- Each firm is a separate checkbox
- Firm names must be the actual bidding entities
- Consent visible ABOVE the submit button

---

## Placement Rules

### Above the Fold / Visible
- "This is an advertisement" → Header or above form
- TCPA consent checkbox → ABOVE submit button
- Privacy policy link → Near form, accessible

### Footer Acceptable
- "Past results do not guarantee future outcomes"
- Full privacy policy link
- Additional legal disclosures

### NOT Acceptable
- Consent below submit button
- Disclosures in modal/popup only
- Hidden in terms nobody reads
- Gray text on light gray background
- Font smaller than 8pt

> **Saul says:** "I know you want a clean flow. Minimal friction. I get it. But that TCPA consent checkbox? It needs to be ABOVE the submit button. Not below. Not in a modal. Not in a terms page nobody reads. Above. Visible. Checkable."

---

## State-Specific Disclosures

Some states require additional disclosures. Reference `State_Bar_Quick_Ref.md` for:
- California (Rules 7.1-7.5)
- Texas (high enforcement)
- Florida (high enforcement)
- New York (specific requirements)

---

## Consultation Clarifications

### Free Consultation
```
No upfront cost to speak with an attorney.
```
Do NOT use: "100% free" or "completely free"

### No Guarantee of Representation
```
A free consultation does not guarantee representation.
```
Use when offering "free case evaluation"

---

## Technical Requirements

### TrustedForm
- MANDATORY on all lead forms
- Must capture video replay of consent moment
- Certificate must show specific firm name visible at consent
- Retain certificates for 5+ years

### Jornaya LeadiD
- MANDATORY for audit trail
- Bot detection
- Consent verification

> **Saul says:** "A lead without a TrustedForm certificate is a lead you can't defend in court. Period."

---

## Quick Checklist

Before launching any landing page:

- [ ] "This is an advertisement" visible
- [ ] Lead gen disclosure present
- [ ] TCPA consent above submit button
- [ ] Checkboxes unchecked by default
- [ ] Specific firm names shown (not "partners")
- [ ] Privacy policy link visible
- [ ] TrustedForm active
- [ ] Jornaya LeadiD active
- [ ] All text readable (8pt minimum, good contrast)
