# Lovable Prompts: Phase-Based Implementation

**Implementation Approach:** Phase-based, organized by priority  
**Tool:** Lovable for 95% of work (structure + copy)  
**Note:** Framer only for final 5% polish (micro-interactions)

**How to Use This File:**
1. Copy the prompt for your current phase
2. Paste into Lovable
3. Review the output
4. Test on mobile
5. Move to next prompt

**Important:** All copy AND structure changes go through Lovable. Framer is finishing touches only.

---

## PHASE 1: MOBILE FOUNDATION

**Focus:** Critical mobile conversion blockers  
**Capacity:** 8-10 hours total  
**Priority:** Highest ROI changes first

### Prompt #1: Reduce Mobile H1 Size

```
Reduce the hero section H1 font size on mobile devices to improve readability 
and bring the CTA button above the fold.

Current: H1 is 102.4px on all screen sizes
Target: H1 should be 56px on mobile (max-width: 768px), 64px on tablet (769-1024px), 
and remain 102.4px on desktop (1025px+)

Make sure line-height adjusts proportionally to maintain visual balance.
```

**Expected Output:** Responsive H1 that's readable on mobile without dominating screen

**Test:** View on iPhone (375px width) - H1 should take ~25-30% of viewport, not 50%+

---

### Prompt #2: Create Sticky Bottom CTA Bar

```
Create a sticky CTA bar component that stays fixed to the bottom of the viewport 
on mobile devices as users scroll down the homepage.

Requirements:
- Fixed position at bottom of screen
- Only appears on mobile (max-width: 768px)
- Height: 72px (includes padding)
- Background: Brand green (#10B77F) with slight opacity (0.95)
- Contains button: "See if my market is available"
- Button text: 18px, white, bold
- Box shadow for elevation
- Slides in after user scrolls past hero section (50vh)
- Doesn't overlap footer when user reaches bottom

Make sure it doesn't conflict with existing CTAs on the page.
```

**Expected Output:** Persistent mobile CTA that follows scroll

**Test:** Scroll homepage on mobile - bar should appear after hero, disappear at footer

---

### Prompt #3: Simplify Proof Bar to Static Grid

```
Replace the current scrolling horizontal proof bar with a clean 2×2 static grid 
that displays 4 key statistics.

Current: Scrolling horizontal ticker with 7+ stats
Target: 2×2 grid layout with these 4 stats:

Row 1:
- Left: "92%" with label "acceptance rate"
- Right: "$1,600" with label "per signed case"

Row 2:
- Left: "47" with label "territories locked"
- Right: "ZERO" with label "shared leads"

Design specs:
- Grid layout with gap: 24px
- Each stat card: centered text, padding: 32px
- Number: 48px bold, black
- Label: 14px medium, gray (#666666)
- Light border or subtle background on each card
- Mobile: stack into single column (4 rows)
- Desktop: maintain 2×2 grid

Remove the scrolling animation completely.
```

**Expected Output:** Clean, scannable proof grid

**Test:** Check readability on mobile - stats should be clear and organized

---

### Prompt #4: Increase CTA Button Height

```
Increase the height of all primary CTA buttons to meet mobile touch target 
guidelines and improve usability.

Current: CTA buttons appear to be ~48px height
Target: 56px minimum height on all screen sizes

Changes needed:
- Height: 56px
- Padding: 16px 32px (vertical, horizontal)
- Font size: 18px (up from 16px)
- Maintain green background (#10B77F)
- Maintain border-radius: 8px
- Ensure min-width: 200px on mobile for easy tapping

Apply to:
- Hero CTA: "Apply for your market"
- Final CTA: "Apply now"
- Any other primary action buttons

Don't change secondary/text link CTAs.
```

**Expected Output:** Larger, easier-to-tap CTA buttons

**Test:** Tap buttons on iPhone - should feel comfortable, not requiring precision

---

### Prompt #5: Update CTA Copy

**Use Lovable for this copy change:**

```
Update all primary CTA button text on the homepage to lower commitment and 
increase curiosity.

Current CTA text: "Apply for your market" and "Apply now"

New CTA text:
- Hero section CTA: "See if my market is available"
- Final CTA at bottom: "Check availability"
- Sticky mobile CTA bar: "See if [City] is available" (if city detection available) 
  OR "Check if my market is open"

Rationale: "See if available" is curiosity-driven and feels lower commitment than "Apply now". 
This should increase click-through rate by reducing application anxiety.

Keep all button styling the same, only change the text content.
```

**Expected Output:** CTA copy that feels less like a form, more like discovery

**Test:** Do the CTAs feel more inviting and less intimidating?

---

## PHASE 2: TERRITORY MAP + SOCIAL PROOF

**Focus:** Brand signature device + testimonials  
**Capacity:** 12-16 hours total  
**Note:** Territory map is the biggest build in this phase

### Prompt #6: Territory Map Component (Requires Map Asset)

**Option A: Using Static Image Map**

```
Create a territory map component that displays a US map showing locked and available 
markets for the geo-exclusive model.

Component should:
- Display a US map image (I'll provide the SVG/image)
- Show green dots for locked territories (47 locations)
- Show gray outlines for available territories
- Include a legend: "🟢 Locked" and "⚪ Available"
- Be responsive (full width on mobile, max 800px on desktop, centered)
- Place in "Geo-Exclusive" section after the "One firm per market" text

Design specs:
- Map container: max-width 800px, centered
- Padding: 40px on desktop, 24px on mobile
- Legend below map: small text, gray
- Optional: Add hover tooltip showing city name (if SVG has city markers)

I'll need to provide the actual map image/SVG. This prompt creates the container 
and styling.
```

**Expected Output:** Map container ready for image insertion

**Test:** Check responsive sizing - map should be readable on all devices

---

**Option B: Using React Map Library**

```
Create an interactive territory map component using react-simple-maps library 
that shows locked vs available markets.

Install: react-simple-maps

Component requirements:
- Display US map with state outlines
- Add markers for 47 locked territories (green circles)
- Add markers for available territories (gray circles)
- Hover tooltip showing city name
- Legend showing "Locked" (green) vs "Available" (gray)
- Responsive sizing

Data structure:
- Array of territories with properties: city, state, lat, long, status (locked/available)

Styling:
- Green markers: #10B77F, 10px radius
- Gray markers: #CCCCCC, 8px radius
- Map background: light gray
- State borders: light gray, 1px

Place in "Geo-Exclusive" section after "One firm per market" heading.
```

**Expected Output:** Interactive map showing territory status

**Test:** Hover over markers - tooltips should show city names

---

### Prompt #7: Testimonial Card Component

```
Create a testimonial card component for displaying attorney testimonials.

Component structure:
- Circular photo (80px diameter) at top
- Quote text below photo (italic, 16px, gray)
- Name below quote (bold, 18px, black)
- Firm name and city below (14px, gray)

Design specs:
- Card padding: 32px
- Background: off-white (#F8F9FA) or white with subtle border
- Border-radius: 12px
- Centered text alignment
- Max-width: 400px per card
- Photo: circular crop, 80px × 80px, centered
- Quote: max 3 lines, then ellipsis

Layout for multiple testimonials:
- Desktop: 3 columns (if 3 testimonials)
- Tablet: 2 columns
- Mobile: 1 column (stacked)
- Gap between cards: 24px

Place in "Who We Work With" section after the criteria lists.
```

**Expected Output:** Testimonial card component ready for content

**Test:** Check photo cropping and text readability on all devices

---

### Prompt #8: Testimonial Content Insertion

**After collecting testimonials, prompt:**

```
Add testimonials to the testimonial card component in the "Who We Work With" section.

Testimonial 1:
- Photo: [upload attorney photo]
- Quote: "Second Chair's geo-exclusive model changed our practice. We went from competing 
  with 5 firms for the same leads to owning Denver. Our acceptance rate went from 40% to 91%."
- Name: "John Smith"
- Firm: "Smith & Associates, Denver, CO"

[Repeat for testimonials 2 and 3]

Layout: Display all 3 testimonials in a row on desktop, stack on mobile.

Headline above testimonials: "What attorneys say about partnering with us"
```

**Expected Output:** Testimonials displayed with proper formatting

**Test:** Read testimonials on mobile - should be clear and compelling

---

## PHASE 3: COPY TRANSLATION + COMPETITIVE POSITIONING

**Focus:** Humanize copy, add emotional depth  
**Capacity:** 6-8 hours total  
**Note:** All copy enhancements happen in this phase

### Prompt #9: "Why Switch?" Competitive Section

```
Create a new section titled "Why Switch?" that addresses attorneys currently 
working with other lead gen companies.

Place this section after "How It Works" and before "Products".

Section structure:
- H2: "Already buying leads? Here's why firms are switching to Second Chair."
- Intro paragraph
- Comparison table (3 columns: "What You're Used To", "What You Get With Us", "Why It Matters")
- 4 comparison rows
- Closing paragraph with test offer
- CTA button: "Test us in your worst market"

Content (copy this text):

Intro:
"We know you're probably working with someone. Maybe it's Martindale-Avvo. Maybe it's 
Ngage. Maybe it's a regional aggregator. And you're probably frustrated."

Table:
Row 1:
- What You're Used To: "Shared leads across multiple buyers"
- What You Get: "One firm per market (contractually exclusive)"
- Why It Matters: "No bidding wars, no price erosion"

Row 2:
- What You're Used To: "Volume-first (quantity quotas)"
- What You Get: "Over-qualification beats volume"
- Why It Matters: "92% acceptance rate vs. industry 30-50%"

Row 3:
- What You're Used To: "Spin when performance drops"
- What You Get: "Bad weeks reported early"
- Why It Matters: "Operational trust, not vendor games"

Row 4:
- What You're Used To: "Just ads"
- What You Get: "Tools that pre-qualify (CaseSnapshot)"
- Why It Matters: "Better lead quality from better capture"

Closing:
"Test us in your worst-performing geography. Pick the market where your current 
vendor is weakest. Give us 90 days. If we don't beat their performance, walk away."

Table styling:
- 3 columns on desktop, stack on mobile
- Row striping (alternate light gray background)
- Bold text for column headers
- Padding: 16px per cell
```

**Expected Output:** New competitive positioning section

**Test:** Read table on mobile - should be scannable and clear

---

### Prompt #10: "What Happens Next" Section at CTA

```
Add a "What happens next?" clarification section immediately after the final CTA 
button in the "Limited Availability" section.

Content:
H3: "What happens after you apply?"

Timeline list (with icons/numbers):
1. "We review your application (24-48 hours)"
2. "Schedule 15-minute discovery call if there's a fit"
3. "Discuss your market, case volume, and exclusivity terms"
4. "If approved, lock your territory and begin onboarding"

Style:
- Display as 4-step vertical timeline on mobile
- Display as horizontal steps on desktop
- Use numbers or icons for each step
- Gray text, 16px, readable
- Spacing between steps: 16px

Place directly under CTA button, before footer.
```

**Expected Output:** Process clarity that reduces application anxiety

**Test:** Read flow on mobile - should feel reassuring and clear

---

## PHASE 4: ADVANCED FEATURES (OPTIONAL)

**Focus:** Pre-qual quiz, analytics, form optimization  
**Capacity:** 6-10 hours (as time/priority allows)  
**Note:** Only implement if time permits after Phases 1-3

### Prompt #11: Enhanced CTA Visual Weight

```
Increase the visual prominence of the primary CTA button to match the verbal 
confidence of the copy.

Current: Green (#10B77F) button with white text
Enhanced:

Option A (Darker Green for Better Contrast):
- Background: #0D9A68 (darker green)
- Text: White, 18px bold
- Height: 56px
- Add subtle hover effect: Lift shadow (0 4px 12px rgba(13, 154, 104, 0.3))
- Add press state: translateY(1px)

Option B (Bold Black for Maximum Command):
- Background: #0A0A0A (black)
- Text: White, 18px bold
- Height: 56px
- Add hover effect: Background shifts to #10B77F (green)
- Add press state: translateY(1px)

Implement Option A first (less risky). Test conversion. If needed, A/B test Option B.

Apply to all primary CTAs:
- Hero CTA
- Final CTA
- Sticky mobile CTA
```

**Expected Output:** More visually commanding CTA buttons

**Test:** Do buttons feel more prominent? Do they command action?

---

### Prompt #12: Enhanced Geo-Exclusive Copy

**Use Lovable for this copy enhancement:**

```
Enhance the "Geo-Exclusive Model" section copy to add competitive context and 
emotional ownership framing.

Current section text (keep this):
"When you partner with Second Chair, you own your geography. Every qualified case 
opportunity in your market flows exclusively to your firm. No bidding wars. No shared 
intake. Once your market is locked, it's locked."

Add this additional copy after the existing paragraph:

"**This is different from every other lead gen company.** Martindale-Avvo sells 
'exclusive' leads to multiple buyers. Ngage runs volume quotas. Lead aggregators 
auction the same case to whoever pays most.

We don't do that. You get every qualified case in Denver. No other firm gets them. That's it.

**Your territory. Your clients. Your fight.** While your competitors are bidding 
against each other for the same leads, you're signing cases."

Keep all section styling the same. This is pure copy addition to strengthen competitive 
positioning and add emotional ownership framing.
```

**Expected Output:** Geo-exclusive section with competitive context and emotional close

**Test:** Read the section on mobile - does it feel more competitive and personal?

---


### Prompt #13: Pre-Qualification Quiz

```
Create a multi-step pre-qualification quiz that assesses whether an attorney is 
a good fit before showing the full application.

Quiz structure (5 questions, one per screen):

Question 1:
- Text: "What's your primary practice area?"
- Options: Personal Injury, Immigration, Mass Tort, Other
- Required: Yes

Question 2:
- Text: "Which market are you in?"
- Input type: Dropdown with major US cities (or open text input)
- Required: Yes

Question 3:
- Text: "What's your current monthly case volume?"
- Options: 1-5 cases, 6-10, 11-20, 20+ cases
- Required: Yes

Question 4:
- Text: "Do you have intake infrastructure in place?"
- Options: Yes (dedicated intake team), Yes (attorney handles), No (need to build)
- Required: Yes

Question 5:
- Text: "Are you ready to commit to geo-exclusivity?"
- Options: Yes, Not sure (want to learn more), No
- Required: Yes

Quiz logic:
- If answers meet criteria (PI/Immigration, major market, 6+ cases/month, intake yes, 
  exclusivity yes) → Show message: "Great fit! Continue to application"
- If answers don't meet criteria → Show message: "Thanks for your interest. We'll 
  keep your information and reach out when we expand to your area."

Design:
- One question per screen
- Progress bar at top (1/5, 2/5, etc.)
- Large buttons for options (easy tapping)
- Previous/Next buttons at bottom
- Results page with appropriate CTA

Place quiz before full application form. Button text: "See if you qualify" (instead 
of "Apply now")
```

**Expected Output:** Multi-step qualification quiz

**Test:** Complete quiz on mobile - should feel fast and frictionless

---

### Prompt #14: Multi-Step Application Form

**Note:** This requires more complex implementation. Alex should lead this.

```
Convert the current single-page application form into a multi-step form with 
progress tracking to reduce abandonment.

Step 1: Basic Information
- First name, Last name, Email, Phone

Step 2: Practice Details
- Firm name
- Practice area (dropdown)
- Market/City
- Current lead gen spend (monthly)
- Current case volume

Step 3: Review & Submit
- Summary of all entered information
- Checkbox: "I accept geo-exclusivity terms"
- Checkbox: "I understand this is not an instant approval"
- Submit button

Form features:
- Progress indicator at top (Step 1 of 3, Step 2 of 3, etc.)
- "Previous" and "Next" buttons (not "Submit" until final step)
- Inline validation (show errors immediately, not on submit)
- Save progress to localStorage (if user leaves and returns)
- Clear indication of required vs optional fields
- Mobile-optimized (one field per row, large inputs)

After submit:
- Confirmation page: "Application received! We'll review within 24-48 hours."
- Email confirmation sent to applicant
```

**Expected Output:** Professional multi-step form

**Test:** Complete form on mobile - should feel manageable, not overwhelming

---

## ADDITIONAL PROMPTS (As Needed)

### Prompt: FAQ Accordion Section

```
Create an FAQ section with accordion-style expandable questions/answers.

Add new section titled "Frequently Asked Questions" before the final CTA.

Questions:
1. "How does geo-exclusivity actually work?"
2. "What's the average cost per signed case?"
3. "Can I test Second Chair in one market before expanding?"
4. "What happens if performance drops?"
5. "Do you work with firms outside Personal Injury?"
6. "How long does approval take?"

[Provide answers for each]

Design:
- Questions are clickable headers (18px bold, black)
- Answers are hidden by default, expand on click
- Smooth animation (200ms)
- Plus/minus icon indicating expanded state
- Mobile: full-width, stack vertically
- Desktop: max-width 800px, centered
```

---

### Prompt: Founder/Mission Story Section

```
Create a new "Why We Built This" section featuring founder story and mission.

Place after "How It Works" or "Who We Work With".

Structure:
- H2: "Why we built Second Chair"
- Founder photo (left side on desktop, top on mobile)
- Story text (right side on desktop, below photo on mobile)
- Quote callout in larger text

Content:
[Photo placeholder: 400x400px square photo]

Text:
"I spent three years in legal marketing watching great PI firms waste money on lead 
gen companies that promised exclusivity and delivered shared leads. Attorneys were 
paying for the same case multiple times, competing against each other, and blaming 
their intake when leads didn't convert.

Second Chair exists because attorneys deserve better. True geo-exclusivity. 
Transparent reporting. A partner, not a vendor.

We only work with one firm per market because that's the only way exclusivity is real."

— [Founder Name], Founder

Design:
- Two-column layout on desktop (40% photo, 60% text)
- Single column on mobile (photo stacked above)
- Quote callout: larger text, italic, with quotation marks
- Professional styling, matches brand voice
```

---

## TESTING + ANALYTICS PROMPTS

### Prompt: Analytics Event Tracking

**Note:** Alex should implement this with Google Analytics or similar.

```
Add event tracking to key user interactions for conversion analysis.

Events to track:
1. CTA button clicks (Hero CTA, Final CTA, Sticky CTA)
2. Scroll depth (25%, 50%, 75%, 100% of page)
3. Section visibility (Geo-Exclusive, How It Works, Who We Work With reached)
4. Territory map interactions (if interactive)
5. Application form starts
6. Application form completions
7. Application form abandonment (which step?)
8. Quiz starts and completions

Use Google Analytics 4 or similar analytics platform.

Label events clearly:
- "cta_hero_click"
- "scroll_depth_50"
- "section_view_geo_exclusive"
- etc.

This data will inform A/B testing and optimization priorities.
```

---

## EMAIL TEMPLATE: Requesting Testimonials

**Use this to collect attorney testimonials (Phase 2):**

```
Subject: Quick request — 2-minute testimonial for Second Chair website?

Hi [Attorney Name],

We're updating the Second Chair website and would love to feature a quick testimonial 
from you about your experience with the geo-exclusive model.

Would you be willing to share 2-3 sentences about:
- What made you choose Second Chair?
- How has it impacted your practice?
- What's different from other lead gen companies you've worked with?

We'd also love to include:
- Your professional headshot (high-res photo)
- Your name, firm name, and city

Example format:
"Second Chair's geo-exclusive model changed our practice. We went from competing with 
5 firms for the same leads to owning [City]. Our acceptance rate went from 40% to 91%."
— [Your Name], [Firm Name], [City]

This would appear on our "Who We Work With" section and help other attorneys understand 
the value of true exclusivity.

Any concerns or questions? Let me know. And if this doesn't work for you right now, 
no problem at all.

Thanks,
[Your Name]
```

---

## IMPLEMENTATION SUMMARY: Phase-by-Phase Prompt Schedule

### PHASE 1: MOBILE FOUNDATION (8-10 hours)
**Critical mobile conversion blockers:**
1. ✅ Prompt #1: Mobile H1 scaling
2. ✅ Prompt #2: Sticky CTA bar
3. ✅ Prompt #3: Proof bar simplification
4. ✅ Prompt #4: CTA button height
5. ✅ Prompt #5: CTA copy update

**Expected Impact:** +35-50% mobile conversion rate

---

### PHASE 2: TERRITORY MAP + SOCIAL PROOF (12-16 hours)
**Brand signature device + testimonials:**
6. ✅ Prompt #6: Territory map (complex build)
7. ✅ Prompt #7: Testimonial cards
8. ✅ Prompt #8: Testimonial content
9. ✅ Prompt #9: "Why Switch?" section
10. ✅ Prompt #10: "What Happens Next"
11. ✅ Prompt #11: Enhanced CTA visual weight
12. ✅ Prompt #12: Enhanced geo-exclusive copy

**Expected Impact:** +25-35% engagement + brand memorability

---

### PHASE 3: COPY TRANSLATION (6-8 hours)
**Humanize copy, add emotional depth:**
- Copy translation across all sections (use Lovable for all copy changes)
- Hero, phases, identity layer, competitive urgency
- FAQ section (if time)
- Founder story (if time)

**Expected Impact:** +20-30% emotional connection

---

### PHASE 4: ADVANCED FEATURES (6-10 hours - OPTIONAL)
**Only if time/priority permits:**
13. ⚠️ Prompt #13: Pre-qualification quiz
14. ⚠️ Prompt #14: Multi-step form
- Analytics setup (priority if time limited)
- A/B testing infrastructure

**Expected Impact:** +20-30% additional lift

---

## Implementation Approach

**Complete Phases 1-3 for core transformation:**
- ✅ Mobile-optimized hero (+35-50%)
- ✅ Territory map live (brand signature!)
- ✅ Testimonials + competitive positioning (+25-35%)
- ✅ Humanized copy throughout (+20-30%)

**Result:** +80-115% cumulative improvement (2x+ conversion rate)

**Phase 4 is optional:** Only add if time and priorities allow. Phases 1-3 deliver the core transformation.
