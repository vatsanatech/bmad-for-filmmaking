# Screenplay Workflow Guide

**BMAD-FILM Screenplay Development System**
**Version**: 2.0.0
**Date**: 2026-02-17

---

## Overview

The BMAD-FILM screenplay workflow transforms story synopsis into **complete, production-ready, Bollywood-level screenplays** with full scene choreography, technical specifications, and AI-generation ready detail.

**This is NOT basic screenplay writing. This is complete cinematic blueprints.**

---

## What You Get

### Complete Screenplay Includes:

**For EVERY Scene**:
1. ✅ **Proper scene heading** (INT/EXT, location, time)
2. ✅ **Visual action lines** (what camera sees, character blocking)
3. ✅ **Hindi-English dialogue** (60-70% / 30-40%, character-appropriate)
4. ✅ **Scene choreography** (camera positions, movements, shot sizes)
5. ✅ **Technical notes**:
   - Camera (angles, movements, lens choices)
   - Lighting (sources, mood, practicals)
   - Sound (ambient, diegetic, music cues)
   - Editing (pace, transitions, rhythm)
   - Production Design (props, set dressing, continuity)
   - AI Generation (detailed descriptions for image/video generation)
6. ✅ **Shot-by-shot breakdowns** (for complex/action scenes)

### Plus Production Documents:
- Complete formatted screenplay
- Technical summary for production planning
- Location breakdown
- Cast requirements
- Special equipment/VFX needs
- Budget and schedule considerations

---

## How It Works

### Step 1: Create Story First

**Before screenplay, you need story synopsis**.

Use the story workflow:
```
/story-synopsis [concept]
```

This creates:
- `project/development/[project-name]/genre-analysis.md`
- `project/development/[project-name]/story-synopsis.md`

### Step 2: Generate Screenplay

**After story exists, run screenplay**:
```
/screenplay [project-name]
```

**Example**:
```
/screenplay last-selfie
```

This creates:
- `project/development/last-selfie/detailed-screenplay.md` (complete screenplay)
- `project/development/last-selfie/screenplay-technical-notes.md` (production summary)

---

## The 8-Step Screenplay Process

### Step 1: Read Project Context
- Loads genre-analysis.md (genre, style, agent selection)
- Loads story-synopsis.md (complete story with beats)
- Extracts characters, locations, visual style
- Understands language standards and technical requirements

### Step 2: Screenplay Structure Planning
- Breaks story into individual scenes
- Marks act structure (act breaks, midpoint, climax)
- Creates pacing map (fast/slow rhythm)
- Tracks character transformations

### Step 3: Scene-by-Scene Writing
**THE CORE WORK**

For EACH scene, writes:

**Scene Heading**:
```
INT. ISHITA'S BEDROOM - LATE NIGHT (2:47 AM)
```

**Establishment** (visual description):
```
ESTABLISHING SHOT - The modern bedroom, dimly lit by ring light
and laptop glow. ISHITA (26, casual tank top and shorts, hair
messy) sits on her bed, phone in hand. Influencer mid-content
creation.
```

**Action Lines** (present tense, visual):
```
She holds phone up, adjusts angle. Checks frame in screen.
Smile, peace sign. Natural influencer rhythm.

SHUTTER SOUND - Digital click.
```

**Dialogue** (Hindi-English mix):
```
                    ISHITA
              (to phone camera, casual)
          12 am के बाद का light sabse accha
          hota hai. Soft. Real.
```

**Technical Notes**:
```
TECHNICAL NOTES:

CAMERA:
- Opening: Wide establishing (24mm)
- Mid-scene: Medium shots (50mm)
- Climax: Close-ups (85mm)
- Movement: Static building to handheld (tension)

LIGHTING:
- Ring light: Warm white (left of frame)
- Laptop glow: Blue (right, on desk)
- Mood: Late night isolation, familiar becoming threatening

SOUND:
- Ambient: City quiet, clock ticking
- Diegetic: Phone shutter clicks, screen taps
- Her breathing: Calm → shallow (tension build)

EDITING:
- Pace: Slow build, increasing cut frequency
- Hold on photo reveals (3-4 seconds each)
- Rhythm: Letting dread breathe

PRODUCTION DESIGN:
- Phone: iPhone 15 Pro (screen must be visible)
- Ring light: 12-inch model (specific for realism)
- Set: Lived-in bedroom (scattered clothes, open laptop)

AI GENERATION NOTES:
- Character: Indian woman, 26, casual home clothes
- Environment: Modern bedroom, warm artificial light
- Key Prop: Smartphone screen with selfie showing anomaly
- Mood: Comfort transitioning to unease
- Color: Warm foreground, dark cool background
```

**Shot Breakdown** (complex scenes):
```
SHOT-BY-SHOT:

SHOT 1: WIDE - Establishing bedroom
[Duration: 3 sec]

SHOT 2: MEDIUM - Ishita on bed with phone
[Duration: 4 sec]

SHOT 3: CLOSE-UP - Phone screen (photo visible)
[Duration: 5 sec - hold for audience to see anomaly]
```

### Step 4: Dialogue Polish
- Verifies Hindi-English balance (60-70% / 30-40%)
- Checks character voice consistency
- Ensures subtext and authenticity
- Confirms "rickshaw driver would understand" standard

### Step 5: Technical Specification Completion
- Verifies every scene has complete technical notes
- Creates technical summary document
- Lists all locations, characters, props
- Notes VFX/special requirements

### Step 6: Runtime Verification
- Calculates total runtime (1 page ≈ 1 minute)
- Estimates each scene duration
- Verifies matches target (e.g., 5 min for shorts)
- Adjusts pacing if needed

### Step 7: Quality Assurance
**Master Story Director reviews**:
- Story beats all present
- Act structure effective
- Genre conventions honored
- Bollywood standards met
- Production readiness verified

**Approval gate**: Must pass before finalization.

### Step 8: Finalization
Creates final documents:
- Formatted screenplay with title page, character list, all scenes
- Technical notes document
- Production summary

---

## Output Format Example

### detailed-screenplay.md Structure:

```
=====================================
आख़िरी SELFIE (The Last Selfie)
5 Minute Horror Film

Story Synopsis by: Horror Architect (RGV/Bhatt Training)
Screenplay by: BMAD-FILM Bollywood Screenplay Writer

Date: 2026-02-17
Version: 1.0
=====================================

CHARACTERS:

ISHITA (26)
Lifestyle influencer, 120K followers. Modern, independent,
lives alone. Comfortable with technology. Late night content
creator. Tank top and shorts, messy bun, minimal makeup.

[Additional characters if any...]

---

LOCATIONS:

INT. ISHITA'S BEDROOM
Modern Mumbai apartment. Ring light setup, laptop on desk,
lived-in but organized. Window with curtains, cupboard along
wall. Warm artificial lighting, contemporary aesthetic.

INT. ISHITA'S LIVING ROOM
[If applicable...]

---

=====================================

FADE IN:

INT. ISHITA'S BEDROOM - LATE NIGHT (2:47 AM)

[Complete scene with all elements as shown above...]

[Additional scenes...]

FADE OUT.

=====================================
END OF SCREENPLAY
=====================================

PRODUCTION NOTES:

Runtime Estimate: 5 minutes
Total Scenes: 6
Scene Breakdown:
  - Interior: 6
  - Exterior: 0
  - Night: 6
  - Day: 0

Cast Requirements: 1 principal

Locations: 1 (Apartment - bedroom + living room zones)

Special Requirements:
- VFX: Entity design (practical + digital enhancement)
- Phone screen compositing
- Sound design critical (diegetic only)

Budget Considerations: Low-medium
- Single location
- One actor
- Entity VFX main expense
- Sound design investment needed

Schedule Considerations: 2-3 night shoots
```

### screenplay-technical-notes.md Structure:

```
# Technical Notes: आख़िरी Selfie

## Camera Requirements

**Shots Summary**:
- Wide shots: 8
- Medium shots: 12
- Close-ups: 15
- POV shots: 6
- Phone screen shots: 10

**Movement**:
- Static: 60%
- Handheld: 30%
- Push-ins: 10%

**Lenses**:
- 24mm: Wide establishing
- 50mm: Medium dialogue/action
- 85mm: Close-ups emotional

## Lighting Plan

**Primary Sources**:
- Ring light (practical, in scene)
- Laptop glow (practical)
- Motivated darkness (window, corners)

**Mood**: Warm foreground (false safety) → Cool shadows (threat)

## Sound Design

**Critical Elements**:
- Diegetic ONLY (no score)
- Phone sounds (shutter, notifications)
- Breathing (escalating from calm to panicked)
- Silence (deliberate, creates tension)
- Touch moment (wet, cold, wrong)

## Post-Production

**VFX**:
- Entity in phone photos (practical + enhancement)
- Phone screen composites
- Void-face digital (subtle, not overworked)

**Color Grade**:
- Warm artificial lights (amber)
- Cool shadows (blue-green)
- Phone screen (blue-white)
- Progressive desaturation (comfort → horror)

**Edit Notes**:
- Photo reveal holds: 3-5 seconds each
- Cut frequency increases with tension
- Final attack: Off-screen (sound + shadows)

## Production Schedule

**Night 1**: Bedroom scenes 1-3 (selfie taking, discoveries)
**Night 2**: Bedroom scenes 4-5 (testing, panic, climax)
**Night 3**: Pickups, phone screen details, floor POV

**Total**: 2-3 nights + 1 pickup day

## Budget Breakdown

**Low-Medium Budget**:
- Location: ₹10,000 (apartment rental 3 nights)
- Cast: ₹50,000 (1 principal)
- Crew: ₹1,50,000 (minimal crew, 3 nights)
- Equipment: ₹75,000 (camera, lighting, sound)
- VFX: ₹1,00,000 (entity design, composites)
- Post: ₹50,000 (edit, color, sound design)
- Contingency: ₹15,000

**Total Estimate**: ₹4,50,000 (approx)
```

---

## Quality Standards

Every screenplay meets these Bollywood production standards:

### Visual Storytelling
- ✅ Action lines SHOW, don't tell
- ✅ Character emotions through behavior, not description
- ✅ Camera language supports story emotionally
- ✅ Blocking reveals relationships spatially

### Dialogue
- ✅ 60-70% Hindi, 30-40% English (measured)
- ✅ Tech terms in English, emotional words in Hindi
- ✅ Characters have distinct voices
- ✅ Subtext present (what's unsaid matters)
- ✅ Actable (sounds like real speech)

### Technical Completeness
- ✅ Every scene has camera notes
- ✅ Lighting specified for mood
- ✅ Sound design indicated
- ✅ Editing rhythm noted
- ✅ Production design details present
- ✅ AI generation descriptions complete

### Production Readiness
- ✅ Director knows what to shoot
- ✅ Actors know what to perform
- ✅ Editor can visualize the cut
- ✅ All departments have guidance
- ✅ Budget and schedule feasible

### Bollywood Cinema Standards
- ✅ Cinematic, not TV-flat (scale, scope, visual richness)
- ✅ Emotional beats are strong (not subtle)
- ✅ Language feels authentic (culturally accurate)
- ✅ Rewatch value (layered, detailed)

---

## Usage Examples

### Example 1: Horror Short

```bash
# Step 1: Create story
/story-synopsis "5 min horror"

# User refines concept, story is created as "last-selfie"

# Step 2: Generate screenplay
/screenplay last-selfie

# Result:
# project/development/last-selfie/
# ├── genre-analysis.md
# ├── story-synopsis.md
# ├── detailed-screenplay.md ← NEW
# └── screenplay-technical-notes.md ← NEW
```

### Example 2: Comedy Short

```bash
# Story already exists as "sharma-ji-ka-beta"

/screenplay sharma-ji-ka-beta

# Creates complete screenplay with:
# - All colony party scenes choreographed
# - Escalating disaster moments detailed
# - Parent reaction shots specified
# - Comedy timing and pacing notes
# - Physical comedy choreography
```

### Example 3: Romance Short

```bash
# Story exists as "awaaz-ka-chehra"

/screenplay awaaz-ka-chehra

# Creates screenplay with:
# - Split screen notation for parallel worlds
# - Voice message audio intimacy notes
# - Meeting/recognition choreography
# - Emotional confrontation blocking
# - Mumbai monsoon atmosphere detail
```

---

## Tips for Best Results

### 1. Start with Good Story
**Screenplay quality depends on story quality**.

Good story synopsis has:
- Clear structure (beginning, middle, end)
- Defined characters (who they are, what they want)
- Visual moments (not just dialogue/talking heads)
- Emotional beats (audience should feel something)
- Genre conventions (thriller has suspense, comedy has escalation)

### 2. Trust the Process
The 8-step workflow ensures:
- Nothing is missed (structure → writing → polish → verification)
- Technical completeness (every scene gets full choreography)
- Quality standards (Master Story Director approval gate)

Let the system work. Don't skip steps.

### 3. Review Output Carefully
After screenplay is generated:
- **Read it like a film** (can you see it in your mind?)
- **Check dialogue out loud** (does it sound natural?)
- **Verify technical notes** (are they specific enough?)
- **Confirm runtime** (does it match target?)

### 4. Iterate If Needed
If something doesn't feel right:
- Identify specific issue (pacing? dialogue? technical detail?)
- Request revision (be specific about what needs adjustment)
- Re-run quality check

---

## Frequently Asked Questions

### Q: Can I write screenplay without story synopsis first?
**A**: No. Screenplay workflow requires existing story synopsis. The story defines structure, characters, beats, visual style. Screenplay translates that into shootable format.

### Q: How detailed are the technical notes?
**A**: Very detailed. Every scene gets camera, lighting, sound, editing, production design notes. Enough for director, DP, editor, sound designer to work from. Enough for AI to generate images/videos.

### Q: What if my story is longer than 5 minutes?
**A**: Workflow adapts to story length. 5-minute = ~5-7 pages. 15-minute = ~15-20 pages. Process is same, just more scenes.

### Q: Can I get screenplay in industry-standard format (Final Draft)?
**A**: Current output is markdown with proper formatting. Can be exported to PDF or converted to Final Draft format. Core content (scenes, dialogue, technical notes) is all there.

### Q: What's the difference between this and regular screenplay?
**A**: Regular screenplay = scene heading + action + dialogue.
BMAD-FILM screenplay = all that PLUS complete choreography (camera, lighting, sound, editing) + technical specs + AI-generation detail. It's a complete production blueprint, not just a story document.

### Q: How long does it take?
**A**: For 5-minute short: 2-4 hours depending on complexity. The system works through all 8 steps methodically. Quality over speed.

### Q: Can I request specific changes?
**A**: Yes. After screenplay is generated, you can request:
- Scene revisions (specific scenes)
- Dialogue adjustments (character voices, language balance)
- Technical detail additions (more specific camera notes)
- Pacing changes (faster/slower scenes)

Be specific about what you want changed.

---

## Workflow Integration

### Current Position in BMAD-FILM:

```
DEVELOPMENT PHASE:

1. ✅ Story Synopsis (DONE - existing 5 stories)
   ↓
2. ➡️ SCREENPLAY (THIS WORKFLOW - now available)
   ↓
3. ⏸️ Story Architecture (future)
   ↓
4. ⏸️ Character Profiles (future)
   ↓
5. ⏸️ Shot Breakdown (future)
```

**Next Steps After Screenplay**:
- Shot breakdown (shot-by-shot with AI generation prompts)
- Production planning (schedule, budget, crew)
- Pre-visualization (storyboards, animatics)

---

## Success Metrics

Screenplay is successful when:

✅ **Complete**: Every scene from story is present and detailed
✅ **Shootable**: Director can film directly from screenplay
✅ **Actable**: Actors have clear performance guidance
✅ **Cuttable**: Editor can visualize the edit
✅ **AI-Ready**: Every visual has generation-ready description
✅ **Runtime Accurate**: Matches target duration (±30 seconds)
✅ **Language Authentic**: Hindi-English balance feels natural
✅ **Technically Complete**: All departments have specifications
✅ **Bollywood Quality**: Cinematic, emotionally resonant, culturally accurate
✅ **Production Feasible**: Budget and schedule are realistic

---

## Support and Issues

If screenplay output has issues:
1. Check that story synopsis exists and is complete
2. Verify genre-analysis.md has proper genre identification
3. Review generated screenplay for specific problems
4. Request targeted revisions (be specific)

For system issues:
- File not found: Check project directory structure
- Incomplete technical notes: Request enhancement for specific scenes
- Language balance off: Request dialogue polish pass
- Runtime mismatch: Request pacing adjustment

---

**Ready to transform stories into production-ready screenplays.**

*BMAD-FILM: Building cinematic blueprints, not just scripts.*
