# Video Format Strategy: Second Chair

> **The 6-15 Second Playbook for Meta Ads Video**
> 
> Why shorter is better, and the two formats that unlock cheap traffic.
> 
> **Last Updated:** January 2026

---

## ⚠️ CRITICAL: Image Quality = Video Quality

**Video clips start as images. If the image is bland, the video will be bland.**

Before generating ANY clip image:
1. **Follow the IMAGE_STYLE_GUIDE.md** — not optional
2. **Nevada-specific details** — tan stucco, desert, harsh sunlight, NOT generic
3. **3-5 Easter eggs in every shot** — absurd background details
4. **Amateur iPhone quality** — NOT DSLR, NOT stock photo
5. **Match the specific ad angle** — Settlement Gap = show the GAP, Fighter = show the FIGHT

**See:** `10_Ad_Factory/IMAGE_STYLE_GUIDE.md` for full prompt examples

---

## The Core Insight: Why 6-15 Seconds?

### The "Video" Placement Hack

Meta's algorithm treats files differently:

| Format | Placements Unlocked |
|--------|---------------------|
| Static Image (JPG) | Feed only |
| Video (MP4, even 5 seconds) | Feed + **Reels** + **Stories** |

**Result:** Reels and Stories are where 80% of cheap traffic lives right now. A 5-second video unlocks placements that a static image cannot.

### Looping Psychology

| Duration | User Behavior |
|----------|---------------|
| 6-second loop | Hypnotic, rewatches 3-4x without realizing |
| 15-second video | Quick consumption, high completion rate |
| 30-second video | Requires commitment → drop-off |

For a "blind" offer (check eligibility), we want them to **click**, not watch a movie.

> **Rule:** Don't make them wait to understand the offer. They should get it instantly.

---

## Format A: The "Motion Still" (5-6 Seconds)

### Best For
- POV Dashboard / Steering Wheel visuals
- Car Dent / Bumper damage visuals
- Any single powerful image that just needs life

### What It Is
Take a static Flux/AI image and add **one subtle movement** so it qualifies as a video file.

### Production Process

| Step | Action | Tool |
|------|--------|------|
| 1. Image Generation | Create static image | Fal.ai (Nano Banana, Flux) |
| 2. Image Approval | Review in Airtable | Human approval |
| 3. Video Animation | Add subtle motion | Fal.ai (Kling Pro) |
| 4. Audio (Optional) | Add environment sound | Fal.ai (MMAudio v2) |
| 5. Text Overlay | Add hook text | CapCut / Meta native |

### Motion Options (Pick One)

| Motion Type | Prompt Keywords | Best For |
|-------------|-----------------|----------|
| **Handheld Shake** | "handheld camera movement, slight shake" | Most versatile, works on everything |
| **Rain on Windshield** | "rain hitting windshield, wipers moving" | Dashboard POV, accident scenes |
| **Traffic Movement** | "passing traffic, headlights moving" | Night scenes, roadside |
| **Breathing/Subtle** | "natural breathing, subtle movement" | People holding objects |
| **Slow Zoom** | "slow push in, cinematic" | Documents, evidence shots |

### Motion Prompt Template
```
Handheld camera movement, slight shake, realistic, raw footage,
iPhone video quality, authentic, NOT smooth, natural imperfections
```

### Audio Strategy (Optional but Recommended)
- **Car scenes:** Traffic hum, rain, wind noise
- **Document scenes:** Fluorescent hum, paper rustle
- **NO TALKING** — this is a silent scroll-stopper
- Use MMAudio v2 to auto-generate synced environment sound

### Text Overlay (Add in CapCut or Meta)
Position: Center or bottom third
Example: *"If you don't have a lawyer yet, read this."*

### Why It Works
- Moves = unlocks Reels/Stories placements
- User can read the text instantly (no waiting for script)
- Low production cost, high ROI
- Looks native to feed

---

## Format B: The "Story Slide" (15 Seconds)

> **Note:** This format was originally called "TikTok Slide" but works on ALL short-form platforms: Meta Reels, IG Stories, FB Feed, and TikTok. Renamed to "Story Slide" to be platform-agnostic.

### Best For
- Settlement angle ads
- News/Alert angle ads
- Story-based ads (problem → action → solution)
- Any angle that needs a sequence
- **Works on:** Meta (Reels, Stories, Feed), TikTok, YouTube Shorts

### What It Is
Three 5-second clips stitched together with hard cuts.

**Structure:**
```
┌─────────────────┬─────────────────┬─────────────────┐
│  CLIP 1: HOOK   │  CLIP 2: ACTION │  CLIP 3: CTA    │
│   (0:00-0:05)   │   (0:05-0:10)   │   (0:10-0:15)   │
└─────────────────┴─────────────────┴─────────────────┘
```

### The 3-Clip Framework

| Clip | Duration | Purpose | Visual Example | Text Overlay |
|------|----------|---------|----------------|--------------|
| **1: HOOK** | 0:00-0:05 | Stop the scroll, create curiosity | POV dashboard with airbag deployed | "Car accident in 2024?" |
| **2: ACTION** | 0:05-0:10 | Show the situation/problem | Hands looking at settlement letter | "Drivers are checking eligibility here" |
| **3: CTA** | 0:10-0:15 | Direct to next step | Green screen map or "Check Now" button | "Link below" |

### Production Process

| Step | Action | Tool |
|------|--------|------|
| 1. Script/Concept | Define 3-clip story | Human (Airtable record) |
| 2. Image Generation | Create 3 static images | Fal.ai (Nano Banana) |
| 3. Image Approval | Review in Airtable | Human approval |
| 4. Video Animation | Animate each image | Fal.ai (Kling Pro, 5s each) |
| 5. Assembly | Stitch 3 clips | FFmpeg / MoviePy |
| 6. Audio - SFX | Generate environment audio | Fal.ai (MMAudio v2) |
| 7. Audio - VO | Generate voiceover (optional) | Fal.ai (ElevenLabs) |
| 8. Mix | Layer VO at 100%, SFX at 40% | FFmpeg |
| 9. Subtitles | Hardcode text overlays | MoviePy / FFmpeg |

### Transition Style
- **HARD CUTS ONLY** — no fades, no transitions
- Abrupt cuts feel more authentic/amateur
- Smooth transitions = "this is an ad" signal

### Audio Strategy

| Layer | Source | Volume | Duration | Start | Airtable |
|-------|--------|--------|----------|-------|----------|
| **Voiceover** | ElevenLabs TTS | 100% (full) | ~12 seconds | **0.2 sec delay** | ✅ Upload |
| **Environment/SFX** | MMAudio v2 (synced to video) | **50%** (LOUD) | **Full video length** | 0:00 | ❌ In-process only |
| **Background Music** | Stable Audio 2.5 | **30%** (underscore) | **Full video length** | 0:00 | ✅ Upload |

> **Note:** Environment audio is generated during assembly but NOT uploaded to Airtable — it's an invisible part of the process.

**Mixing Rules:** 
1. **Voiceover is KING** — always clear and dominant
2. **VO starts at 0.2 seconds** — small delay feels more natural, less jarring
3. **Environment at 50%** — paper rustling, room sounds, car noises should be CLEARLY AUDIBLE
4. **Music at 30%** — audible underscore, never competing with VO
5. **Music + Environment run FULL VIDEO LENGTH** — starts at 0:00, continues after VO ends

**FFmpeg Mixing Command:**
```bash
# Add 0.2 second delay to VO, pad to full duration
ffmpeg -y -i voiceover.mp3 -af "adelay=200|200,apad=whole_dur=15" -ar 44100 padded_vo.mp3

# Mix all 3 tracks - music/env run full duration
ffmpeg -y -i padded_vo.mp3 -i music.mp3 -i environment.mp3 \
  -filter_complex "[0:a]volume=1.0[vo];[1:a]volume=0.30[music];[2:a]volume=0.50[env];[vo][music][env]amix=inputs=3:duration=longest[aout]" \
  -map "[aout]" -t 15 mixed.mp3

# CRITICAL: Normalize to -14 LUFS for TikTok/Meta loudness matching
ffmpeg -y -i mixed.mp3 -af "loudnorm=I=-14:TP=-1:LRA=11" -ar 44100 normalized.mp3
```

**⚠️ LOUDNESS NORMALIZATION (Required for Social)**

Social platforms target **-14 LUFS** integrated loudness. Without normalization, your video will sound quiet compared to others.

```bash
# Final step before muxing with video:
ffmpeg -y -i mixed_audio.mp3 -af "loudnorm=I=-14:TP=-1:LRA=11" normalized.mp3
```

| Parameter | Value | Meaning |
|-----------|-------|---------|
| `I=-14` | -14 LUFS | Target integrated loudness (TikTok/Meta standard) |
| `TP=-1` | -1 dBTP | True peak limit (prevents clipping) |
| `LRA=11` | 11 LU | Loudness range (dynamic range) |

**Music Presets Available:**
- `urgent_tense` — Hook clips, problem awareness
- `fighting_spirit` — Fighter/defiant clips
- `victory_resolution` — CTA/victory clips
- `emotional_piano` — Testimonial-style
- `news_underscore` — Alert/news-style ads

### ⚠️ CRITICAL: Script Timing Rule

**Target: 1.5 - 2.1 words per second of video.**

This leaves ~2-3 seconds of music outro at the end.

| Video Duration | Word Count Target | Calculation |
|----------------|-------------------|-------------|
| 6 seconds | **9-13 words** | 6 × (1.5 to 2.1) |
| 10 seconds | **15-21 words** | 10 × (1.5 to 2.1) |
| 15 seconds | **23-31 words** | 15 × (1.5 to 2.1) |
| 20 seconds | **30-42 words** | 20 × (1.5 to 2.1) |

**Why:** ElevenLabs TTS pacing varies. Music/ambiance should continue after VO ends — this creates a professional "outro" feel.

**Voice Settings (Bill - Primary Working-Class Nevada):**
- Voice: `Bill` (gruff, working-class American — sounds like a real Nevada guy)
- Stability: `0.75` (smooth, not choppy)
- Similarity Boost: `0.70`
- Style: `0.15` (natural, not theatrical)
- Model: `eleven_turbo_v2_5`

**Alternative Voice (Adam - Deep & Mature):**
- Voice: `Adam` (deep, mature American — authoritative but relatable)
- Stability: `0.75`
- Similarity Boost: `0.75`
- Style: `0.15`

**Number Formatting:**
- Say full amounts: "a hundred seventy-five K" NOT "one seventy-five"
- Say "thirty-two hundred bucks" NOT "$3,200"
- Natural speech patterns, not reading numbers

### Text Overlay Specs
- **Font:** Arial Bold (Instagram native look)
- **Color:** Yellow (#FFD700) with Black Stroke (3px)
- **Position:** Bottom Center (padding-bottom: 250px to clear TikTok/Reels UI)
- **Animation:** None (static per phrase) — NO fancy effects

---

## Modular Clip-Based Production System

### How We Think About Videos

Videos are **not** conceived as single units. They are **assembled from modular clips**.

Each clip goes through its own approval cycle:
```
Image Prompt → Image Generated → Image Approved → Video Generated → Video Approved
                                      ↓
                              (Reject: Re-prompt)
```

Only after all clips are approved do we assemble.

### Clip Types

| Clip Type | Duration | Use |
|-----------|----------|-----|
| **Hook Clip** | 5 seconds | Opens video, stops scroll |
| **Story Clip** | 5 seconds | Middle of sequence |
| **CTA Clip** | 5 seconds | Closes video, directs action |
| **Motion Still** | 5-6 seconds | Standalone video (Format A) |

### Typical Video Structures

| Structure | Total Duration | Clips | When to Use |
|-----------|----------------|-------|-------------|
| **Motion Still** | 5-6s | 1 clip | Simple scroll-stopper, single image |
| **Story Slide** | 15s | 3 clips | Story sequence, most ads |
| **Extended Slide** | 20s | 4 clips | Longer story (rare) |
| **Deep Dive** | 25s | 5 clips | Complex angle (very rare) |

### Assembly Rules

| Rule | Implementation |
|------|----------------|
| Hard cuts only | No fades, wipes, or transitions |
| 5-second base unit | All clips are ~5 seconds |
| Voiceover pacing | Script must match clip duration |
| SFX auto-sync | MMAudio generates per-clip, mixed post-assembly |

---

## Image → Video Model Selection

> See: `08_Ad_Factory/video_models/` for full implementation

### Default Model: Kling Pro (95% of use)
- Best for humans, faces, hands, cinematic shots
- $0.35 per 5-second clip
- High realism, excellent prompt adherence

### Specialty Models (Explicit Call Only)

| Model | Use Case | When to Call |
|-------|----------|--------------|
| `hunyuan` | POV driving, rain, vehicle environments | `model="hunyuan"` in prompt |
| `hailuo_standard` | Simple object motion, no people | `model="hailuo_standard"` in prompt |

### Prompt Template for Video Animation
```python
# For Kling Pro (default)
motion_prompt = "Handheld camera movement, slight shake, realistic, raw footage"

# For POV driving (Hunyuan)
motion_prompt = "Driving POV, rain on windshield, slight camera movement, dash visible"

# For simple motion (Hailuo)
motion_prompt = "Subtle movement, gentle breathing, ambient motion"
```

---

## The "Nana Banana Rule" (Lo-Fi Aesthetic)

> **CRITICAL:** All outputs must avoid the "AI Gloss" or "Cinematic" look.

### Goal: High Trust, Low Polish

| Element | Do This | Not This |
|---------|---------|----------|
| Visuals | iPhone 11, Dashcam, cheap Android | 4K cinematic, DSLR quality |
| Lighting | Harsh, blown out, low-light grainy | Studio lighting, perfect exposure |
| Framing | Imperfect, handheld, off-center | Rule of thirds, stabilized |
| Motion | Shake, jitter, raw | Smooth, gimbal, cinematic |

### Negative Prompt Keywords
Always avoid: `cinematic, hollywood, 8k, perfect lighting, studio quality, bokeh, smooth motion`

### Style Modifiers to Append
Always include: `...taken on iPhone 14, harsh flash photography, posted on twitter, slight motion blur, raw photo, realistic texture, unpolished, f/1.8 aperture`

---

## Quick Reference: Production Costs

| Format | Clips | Image Cost | Video Cost | Audio Cost | Total |
|--------|-------|------------|------------|------------|-------|
| Motion Still | 1 | ~$0.01 | ~$0.35 | ~$0.08 | **~$0.44** |
| Story Slide | 3 | ~$0.03 | ~$1.05 | ~$0.08 | **~$1.16** |
| Extended (4) | 4 | ~$0.04 | ~$1.40 | ~$0.08 | **~$1.52** |

*Costs are estimates based on Fal.ai pricing*

---

## Compliance Reminders

### ⚠️ AI Video for Legal Ads

| Allowed | Banned |
|---------|--------|
| ✅ AI-generated scenes, cars, documents | 🔴 AI lip-sync testimonials |
| ✅ Voiceover narrating OVER video | 🔴 AI person "speaking" results |
| ✅ Text overlay making claims | 🔴 Deepfake client statements |

**Rule:** Use AI for the VISUALS, not the EVIDENCE.

See: `02_Visual/Banned_Imagery.md` — AI Lip-Sync section

---

## Related Files

| File | Contains |
|------|----------|
| `02_Visual/Approved_Imagery.md` | What visuals work (static + video) |
| `02_Visual/Banned_Imagery.md` | What gets rejected |
| `02_Visual/Luca_Maxim_Format.md` | **Premium cinematic format (15-20s)** — Luca Maxim satirical style |
| `07_Research/Creative_Resources/Video_Hook_Templates.md` | 200 hook formulas |
| `08_Ad_Factory/video_models/` | Video generation code |
| `08_Ad_Factory/audio_models/` | Audio generation code |
| `10_Ad_Factory/IMAGE_STYLE_GUIDE.md` | Detailed image prompting |

---

## Format C: The "Luca Maxim Cinematic" (15-20 Seconds)

> **Premium satirical format for hero content and pattern interrupts.**

See: `Luca_Maxim_Format.md` for full specification.

### Quick Summary

| Attribute | Value |
|-----------|-------|
| Duration | 15-20 seconds |
| Shots | 4-5 beats |
| Style | Movie-trailer execution, satirical commentary |
| Cost | ~$2-3 per video (premium) |
| Use For | Brand-building, settlement gap angles, pattern interrupts |

### The Core Rule: No Boring Shots

Every frame must pass the drama checklist:
- Does this frame have emotional tension?
- Would someone screenshot this?
- Is there visual contrast (power dynamics, scale, lighting)?
- Does the camera movement add meaning?

### When to Use

| Luca Maxim Format | Motion Still / Story Slide |
|-------------------|---------------------------|
| Hero content | Quick-turn testing |
| Emotional angles | Direct response |
| Pattern interrupts | UGC aesthetic |
| Premium placements | Standard Reels/Stories |
