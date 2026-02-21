# Implementation Guide: Phase-Based Workflow

**For:** Davis + Danny  
**Tools:** Lovable (AI coding for structure + copy 95%), Framer (final polish 5%)  
**Capacity:** 10-12+ hours/day working together (potentially 16 hrs combined in first few days)  
**Approach:** Alignment call → Decide approach together → Implement → QA together  
**Goal:** Transform website from 7.4/10 to 9.0/10

---

## How This Works: Collaborative Workflow

### Key Context

**Danny's Expertise:**
- Lovable/Framer expert (has been doing all the work with these tools)
- Deep knowledge of both platforms

**Workflow Philosophy:**
- **Davis and Danny will decide approach together during alignment call for each phase**
- Workflow assignments (who does what) will be determined collaboratively
- Both can use Lovable, both can test, both can implement
- Decisions made together based on what makes sense for each task

**Time Commitment:**
- Phase 1: 10-12+ hours (potentially 16 hrs combined first few days)
- Phase 2: 12-16+ hours
- Phase 3: 6-10+ hours
- Phase 4: 6-12+ hours (if doing analytics/advanced features)

---

### Alignment Call Structure (Each Phase)

**Before Implementation:**
1. Review audit sections together
2. Discuss what needs to be built
3. Decide approach: Who tackles what? Work together or split up?
4. Set quality standards and success criteria
5. Review relevant prompts in `08_Lovable_Prompts.md`

**During Implementation:**
- Work together or split tasks as decided
- Test constantly
- Make decisions together in real-time
- Iterate based on feedback

**After Implementation:**
- QA together on all devices
- Review what was accomplished
- Capture any issues
- Plan next phase

---

## Lovable vs. Framer: When to Use What

### Use Lovable For (95% of Work):

✅ **Structural Changes:**
- Mobile H1 scaling (CSS media queries)
- CTA button sizing and positioning
- Sticky CTA bar component
- Proof bar redesign (grid layout)
- New sections/components

✅ **Component Creation:**
- Testimonial cards
- Territory map container
- Pre-qualification quiz
- "What happens next" section
- FAQ accordions

✅ **Layout Adjustments:**
- Responsive breakpoints
- Section spacing on mobile
- Grid systems
- Flexbox layouts

✅ **COPY CHANGES TOO:**
- Headline rewrites
- Body text refinements
- CTA copy changes
- Translating positioning language
- New section content

**Why Lovable for everything?** Danny can make copy AND structure changes at the same time. Faster iteration, one tool, immediate testing.

---

### Use Framer For (Final 5% Polish):

✅ **Visual Micro-Polish ONLY:**
- Subtle micro-interactions
- Fine-tuning hover state transitions
- Animation easing curves
- Typography kerning adjustments

**When to use Framer:** Only AFTER Lovable has built everything and it's working. Framer is for the final 5% of refinement, not primary implementation.

**New rule:** If it's copy OR structure, do it in Lovable. Framer is finishing touches only.

---

## Phase-by-Phase Implementation

### Phase 1: Mobile Foundation

**Capacity:** 10-12+ hours total (potentially 16 hrs combined first few days)  
**Workflow:** Alignment call → Decide approach → Implement → QA together

#### Alignment Call (Start of Phase)

**Read together:**
- [ ] `02_Design_Visual_Audit.md` mobile section
- [ ] `03_UX_UI_Conversion_Audit.md` friction points  
- [ ] `08_Lovable_Prompts.md` Prompts #1-5

**Decide together on alignment call:**
- Mobile H1 target size (56px or 64px?)
- Sticky CTA approach (bottom bar or floating button?)
- Proof bar layout (2×2 grid or 1×4?)
- Quality standards for this phase
- **Who tackles what? Work together or split up?**
- **How to divide the work (if splitting)?**

---

#### Implementation (8-10+ hours)

**Changes to implement (approach decided on alignment call):**

1. **Mobile H1 Scaling** (30-45 min)
   - Use Prompt #1 as reference
   - Test on mobile device
   - Iterate as needed

2. **Sticky CTA Bar** (1-2 hours)
   - Use Prompt #2 as reference
   - Test scroll behavior on mobile
   - Verify sticky positioning
   - Ensure no overlap with footer

3. **Proof Bar Simplification** (1-2 hours)
   - Use Prompt #3 as reference
   - Test readability on mobile
   - Adjust spacing as needed

4. **CTA Button Sizing** (30-45 min)
   - Use Prompt #4 as reference
   - Verify tap target sizing on phone
   - Test thumb reach

5. **CTA Copy Updates** (30-45 min)
   - Use Prompt #5 as reference
   - Review copy consistency
   - Verify all CTAs updated

**Note:** Davis and Danny will decide during alignment call how to tackle each change (together, split up, parallel work, etc.)

---

#### QA Session (1-2 hours - Together)

**Test together on:**
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] Chrome DevTools mobile view
- [ ] Check all prompts implemented correctly
- [ ] Verify sticky CTA behavior
- [ ] Confirm H1 looks good on mobile

**Phase 1 Result:** Mobile-optimized hero, +35-50% expected mobile conversion

---

### Phase 2: Territory Map + Social Proof

**Capacity:** 12-16+ hours total  
**Workflow:** Alignment call → Decide approach → Implement → QA together

#### Alignment Call (Start of Phase)

**Read together:**
- [ ] `06_Consolidated_Recommendations.md` territory map section
- [ ] `08_Lovable_Prompts.md` Prompts #6-12

**Decide together on alignment call:**
- Territory map approach: React library vs. custom design?
- Testimonial collection status
- Priority order for this phase
- **Territory map: Who builds it? Work together or one person leads?**
- **Other features: Split up or tackle together?**
- **How to divide the work effectively?**

---

#### Implementation (10-14+ hours)

**Major features to build (approach decided on alignment call):**

**Territory Map (6-8 hours):**
- Research react-simple-maps or similar library
- Design locked (green dots) vs. available (gray) states
- Implement interactive or static map
- Test responsive behavior
- Deploy in geo-exclusive section
- Use Prompt #6 as reference

**Other Features (4-6 hours):**
1. **Testimonial Card Component**
   - Use Prompt #7 as reference
   - Test layout on mobile

2. **Add Testimonials**
   - Use Prompt #8 to add content

3. **"Why Switch?" Section**
   - Use Prompt #9 as reference
   - Build competitive comparison section

4. **"What Happens Next" Section**
   - Use Prompt #10 as reference
   - Add clarity section after CTA

5. **Enhanced CTA Visual Weight**
   - Use Prompt #11 as reference
   - Review color/contrast impact

6. **Enhanced Geo-Exclusive Copy**
   - Use Prompt #12 as reference
   - Verify flow and tone

**Note:** Davis and Danny will decide during alignment call how to tackle these features (work together, split tasks, parallel work, sequential, etc.)

---

#### QA Session (1-2 hours - Together)

**Test together:**
- [ ] Territory map works on all devices
- [ ] Testimonials look authentic
- [ ] Competitive sections add value
- [ ] CTAs feel more commanding
- [ ] Overall visual impact increased

**Phase 2 Result:** Territory map live (brand signature!), +25-35% engagement

---

### Phase 3: Copy Translation + Competitive Positioning

**Capacity:** 6-10+ hours total  
**Workflow:** Alignment call → Decide approach → Implement → QA together

#### Alignment Call (Start of Phase)

**Read together:**
- [ ] `01_Copy_Audit_Summary.md` copy principles
- [ ] Copy translation examples in `08_Lovable_Prompts.md`

**Decide together on alignment call:**
- Which sections to translate first
- Tone/voice standards
- How human vs. how professional
- **Who tackles which copy sections?**
- **Work together or divide and conquer?**

---

#### Implementation (5-8+ hours)

**Copy changes to implement (approach decided on alignment call):**

1. **Hero Copy Translation** (1 hour)
   - Translate "demand infrastructure" → "You own your market"
   - Add emotional close
   - Test readability on mobile
   - Adjust as needed

2. **Four-Phase Emotional Closes** (1 hour)
   - Add emotional context to each phase
   - Read aloud to test flow
   - Adjust tone as needed

3. **"Who We Work With" Identity Layer** (1 hour)
   - Add "advocates not lead buyers" framing
   - Review selection criteria
   - Test self-selection effect

4. **Final CTA Competitive Urgency** (1 hour)
   - Add "while reading this..." loss framing
   - Add mission connection
   - Test emotional impact

5. **Optional Additions** (1-2 hours if time)
   - FAQ section (accordion component)
   - Founder story section
   - Any other copy polish

**Note:** Davis and Danny will decide during alignment call how to tackle copy changes (work together, divide sections, parallel work, etc.)

---

#### QA Session (1 hour - Together)

**Test together:**
- [ ] Copy sounds natural when read aloud
- [ ] Copy connects emotionally (not just rationally)
- [ ] Identity layer feels authentic
- [ ] Mission connection is clear
- [ ] All sections flow well on mobile

**Phase 3 Result:** Humanized copy throughout, +20-30% emotional connection

---

### Phase 4: Advanced Features (Optional)

**Capacity:** 6-12+ hours (as time/priority allows)  
**Workflow:** Alignment call → Decide approach → Implement → QA together

#### Alignment Call (Start of Phase)

**Decide together on alignment call:**
- [ ] Do we need pre-qual quiz now or later?
- [ ] Analytics setup priorities
- [ ] Form optimization approach
- **Who tackles analytics? Who handles quiz/forms?**
- **Work together or split tasks?**

---

#### Implementation Work (if time/priority allows)

**Features to build (approach decided on alignment call):**

**Analytics Setup (4-6 hours if prioritized):**
- Google Analytics 4 event tracking
- CTA click tracking
- Scroll depth tracking
- Form abandonment tracking
- A/B testing tool setup (Google Optimize)

**Pre-Qualification Quiz (2-4 hours if prioritized):**
- Use Prompt #13 as reference
- Build 5-question quiz
- Test logic flow
- Ensure mobile-friendly

**Form Optimization (2-4 hours if prioritized):**
- Use Prompt #14 as reference
- Multi-step form
- Progress indicators
- Inline validation

**Note:** Davis and Danny will decide during alignment call which features to prioritize and how to divide the work.

---

#### QA Session (1-2 hours - Together)

**Test together:**
- [ ] Analytics tracking all events
- [ ] Optional features work well (or excluded)
- [ ] No bugs across devices
- [ ] Performance still good

**Phase 4 Result:** Analytics ready, +20-30% additional if features built

---

### Phase 5: Deploy + Monitor

**Capacity:** 3-5 hours  
**Workflow:** All Tandem

#### Final QA Checklist (2-3 hours - Together)

**Device Testing:**
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] iPad (Safari)
- [ ] Desktop (Chrome, Safari, Firefox)

**Functionality Testing:**
- [ ] All CTAs click correctly
- [ ] Sticky CTA bar works
- [ ] Territory map renders
- [ ] Testimonials display
- [ ] Forms submit (if applicable)
- [ ] Analytics tracking fires

**Content Testing:**
- [ ] All copy sounds natural
- [ ] No typos or formatting issues
- [ ] Images load correctly
- [ ] Mobile readability excellent

---

#### Baseline Capture (30 min - Together)

**Before deploying, capture:**
- [ ] Screenshot current analytics
- [ ] Note baseline bounce rate
- [ ] Note baseline CTA click-through rate
- [ ] Note baseline time on page
- [ ] Note baseline conversion rate

---

#### Deploy (30 min - Together)

**Deployment steps:**
1. Final code review
2. Push to production
3. Smoke test live site
4. Verify all changes live

---

#### Monitor (1-2 hours - Together)

**Post-launch monitoring:**
- Check analytics every 30 min for first 2-3 hours
- Watch for any bugs or issues
- Fix immediately if needed
- Celebrate when stable! 🎉

**Phase 5 Result:** Complete 7.4/10 → 9.0/10 transformation live

---

## Testing Protocols

### After Each Phase:

**Mobile Testing (always):**
- View on mobile device
- Test in Chrome DevTools mobile view
- Check 375px, 414px, 768px viewports
- Verify touch targets meet 56px minimum

**Cross-Browser Testing (Phase 5):**
- Chrome (primary)
- Safari (iOS/macOS)
- Firefox
- Edge (if time)

**Performance Testing:**
- PageSpeed Insights
- Load time under 3 seconds
- Core Web Vitals green

---

## Common Issues + Solutions

### Issue: Lovable output doesn't match prompt

**Solution:**
1. Re-read prompt for clarity
2. Try more specific instructions
3. Danny and Davis review output together, iterate
4. Danny can code it manually if needed

---

### Issue: Territory map too complex to build

**Solution:**
1. Fallback to static image map
2. Design in Figma with green/gray dots
3. Export as SVG or PNG
4. Still achieve visual impact

---

### Issue: Copy sounds too corporate after translation

**Solution:**
1. Read aloud together
2. Remove jargon
3. Shorten sentences
4. Add conversational tone
5. Test on mobile readability

---

### Issue: Mobile testing shows bugs

**Solution:**
1. Fix immediately before moving forward
2. Decide together who debugs vs. continues (if working in parallel)
3. Re-test after each fix
4. Don't deploy with known bugs

---

## Vibe Coding Best Practices (Lovable)

### Writing Good Prompts:

**Be specific:**
❌ "Make the button bigger"  
✅ "Increase CTA button height to 56px and text to 18px for better thumb targeting"

**Include context:**
❌ "Add testimonials"  
✅ "Create a testimonial card component with photo (circular, 80px), quote (2-3 sentences), name, firm name, and city"

**Specify breakpoints:**
❌ "Make it mobile-friendly"  
✅ "On mobile (max-width: 768px), reduce H1 from 102.4px to 56px"

**Reference existing styles:**
❌ "Style the button"  
✅ "Use existing brand green (#10B77F) or darker (#0D9A68) for better contrast"

---

### Testing After Each Prompt:

1. View output immediately
2. Test on mobile first (where issues show up)
3. Check responsive behavior
4. Verify copy renders correctly
5. Confirm no layout breaks

---

### Iterating Together:

1. Review what was generated
2. Discuss what needs adjustment
3. Make refinements in Lovable or code
4. Test together
5. Move to next change

**Note:** Davis and Danny decide who implements based on what makes sense for each task.

---

## Capacity Planning: 10-12+ Hours/Day

### Realistic Timeline

**With 10-12+ hours/day working together (potentially 16 hrs combined first few days):**

| Phase | Hours | Pace |
|-------|-------|------|
| Phase 1: Mobile | 8-10 hrs | 1 full session |
| Phase 2: Territory Map | 12-16 hrs | 1.5-2 sessions |
| Phase 3: Copy | 6-8 hrs | 1 session |
| Phase 4: Advanced (optional) | 6-10 hrs | 1 session |
| Phase 5: Deploy | 3-5 hrs | Half session |
| **Total** | **35-49 hrs** | **4-6 sessions** |

**Translation:** Complete Phases 1-3 (core transformation) in 3-4 work sessions = 3-4 days if working daily

---

## Success Metrics

### Track After Each Phase:

**Immediately After Deploy:**
- Bounce rate (should decrease)
- Time on page (should increase)
- Scroll depth (should increase)

**Week 1:**
- CTA click-through rate (should increase 30-50%)
- Application starts (should increase 35-50%)
- Mobile conversion rate (should increase 40-55%)

**Week 2-4:**
- Qualified applicant rate (should increase 20-30%)
- Overall conversion (should 2x or more)
- Brand memorability (qualitative - feedback)

---

## Collaboration Checkpoints

### Start of Each Phase (Alignment Call):
- [ ] Davis and Danny read relevant audit sections together
- [ ] Discuss what needs to be built
- [ ] Decide approach: Who tackles what? Work together or split up?
- [ ] Review prompts together as references
- [ ] Set quality standards and success criteria

### During Implementation:
- [ ] Work according to approach decided on alignment call
- [ ] Test constantly (mobile-first)
- [ ] Make decisions together in real-time
- [ ] Iterate based on feedback
- [ ] Stay flexible - adjust approach if needed

### End of Each Phase:
- [ ] QA together on all devices
- [ ] Review what was accomplished
- [ ] Capture any bugs to fix
- [ ] Plan next phase focus

---

## Final Notes

### What Makes This Work:

1. **Alignment → Decide → Implement workflow**
   - Start each phase with alignment call
   - Decide approach together (who does what, work together vs. split)
   - Stay flexible during implementation
   - Make decisions collaboratively

2. **10-12+ hours/day capacity**
   - Potentially 16 hrs combined in first few days
   - Can work weekends if needed
   - Sustained focus yields results
   - Number 1 priority

3. **Danny's Lovable/Framer expertise**
   - Danny has been doing all the work with these tools
   - Danny is the expert on Lovable/Framer
   - Both Davis and Danny can use Lovable
   - Workflow decided together on alignment calls

4. **Constant testing**
   - Test after every change
   - Mobile-first approach
   - Fix bugs immediately
   - QA together regularly

5. **Phase-based, not time-based**
   - Focus on outcomes, not schedule
   - Complete each phase fully
   - Don't rush to arbitrary deadlines
   - Flexible approach based on what works

---

**The audit is complete. The phases are clear. The prompts are ready. Davis and Danny have 10-12+ hours/day to work together (potentially 16 hrs combined in first few days). Workflow will be decided during alignment calls for each phase. Transform the website from 7.4/10 to 9.0/10.**
