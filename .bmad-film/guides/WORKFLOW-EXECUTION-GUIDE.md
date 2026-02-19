# BMAD-FILM Workflow Execution Guide

**Complete Step-by-Step Guide with Feedback Loops**

Version: 1.0.0
Date: 2025-02-17

---

## 🎯 Overview

This guide shows you how to execute the complete Bollywood filmmaking workflow from concept to shot breakdown, with feedback and approval at each step.

**4-Step Workflow**:
```
STEP 1: Story Synopsis (Concept → Story)
   ↓ (Review & Approve)
STEP 2: Character Bible (Story → Characters)
   ↓ (Review & Approve)
STEP 3: Screenplay (Story + Characters → Screenplay)
   ↓ (Review & Approve)
STEP 4: Shot Breakdown (Screenplay → Production Plan)
   ✓ (Production Ready!)
```

Each step:
- Uses outputs from previous steps automatically
- Allows you to review and give feedback
- Only proceeds when you approve
- Creates files in `project/{project-name}/`

---

## 📋 Complete Workflow Example

Let's create a 5-minute thriller called "band-darwaza":

### **STEP 1: Story Synopsis** 📝

**What This Creates**:
- `genre-analysis.md` - Genre identification and agent selection
- `story-synopsis.md` - Complete story with multi-layered twists

**Command**:
```
"Create a 5-minute thriller about a locked room murder in a smart apartment. The story should be about technology backfiring. Call it band-darwaza."
```

**What Happens**:
1. Master Story Director analyzes your concept
2. Identifies genre (Thriller → 90%)
3. Selects Suspense Architect (trained on Anurag Kashyap/Sriram Raghavan)
4. Genre agent creates story synopsis with multi-layered twists
5. Outputs both structured (paragraph) and narrative (flowing) versions

**Output Location**: `project/band-darwaza/`
- `genre-analysis.md` - Shows genre identification and agent selection
- `story-synopsis.md` - Complete story (two versions)

**Review & Feedback**:
```
Option A: "Approved, proceed to character bible"
Option B: "Change the twist to [your idea]" (system regenerates)
Option C: "Make it darker/lighter in tone" (system adjusts)
Option D: "Start over with different concept"
```

**When Approved, Proceed to Step 2** ✓

---

### **STEP 2: Character Bible** 👥

**What This Creates**:
- `character-bible.md` - Comprehensive character profiles

**Prerequisite**: Story synopsis must be approved ✓

**Command**:
```
"band-darwaza"
```
(Just project name - system reads story-synopsis.md automatically)

**What Happens**:
1. Character Developer reads `genre-analysis.md` + `story-synopsis.md`
2. Extracts all characters from story
3. Creates detailed profiles:
   - **Principals**: Full depth (psychology, backstory, arc, voice)
   - **Supporting**: Moderate detail (key traits, role)
   - **Minor**: Brief profiles
4. Maps relationships between characters
5. Defines distinct voices (Hindi-English balance per character)

**Output Location**: `project/band-darwaza/character-bible.md`

**Review & Feedback**:
```
Option A: "Approved, proceed to screenplay"
Option B: "Make Ananya's backstory more detailed"
Option C: "Change Inspector Sharma's personality to more aggressive"
Option D: "Add a new character: [description]"
```

**When Approved, Proceed to Step 3** ✓

---

### **STEP 3: Screenplay** 🎬

**What This Creates**:
- `screenplay-structure.md` - Structure with placeholder dialogue (reference)
- `screenplay.md` - Final screenplay with impactful dialogue

**Prerequisite**: Character bible must be approved ✓

**Command (Default Hindi)**:
```
"band-darwaza"
```

**Command (With Dialect)**:
```
"band-darwaza in Haryanvi"
"band-darwaza in Hinglish"
"band-darwaza in Pure Hindi"
```

**What Happens**:

**Phase A: Structure Writing** (Screenplay Structure Writer)
1. Reads `genre-analysis.md` + `story-synopsis.md` + `character-bible.md`
2. Applies genre-specific visual style (Thriller → tension, clinical descriptions)
3. Creates screenplay structure:
   - Scene headings (INT/EXT, location, time)
   - Scene establishment (atmosphere, mood)
   - Action lines (visual storytelling)
   - Character behavior and movement
   - Placeholder dialogue (shows flow and information)
4. Outputs `screenplay-structure.md`

**Phase B: Dialogue Writing** (Dialogue Writer - Samvad Lekhak)
1. Reads screenplay structure
2. Reads character bible (for distinct voices)
3. Applies genre dialogue style (Thriller → terse, subtext-heavy)
4. Applies language/dialect (Hindi default or specified)
5. Replaces ALL placeholders with final impactful dialogue:
   - Character-specific voices (distinct per character)
   - Natural, actable speech
   - Memorable, quotable lines
   - Subtext and layered meaning
6. Outputs `screenplay.md` (FINAL)

**Output Location**: `project/band-darwaza/`
- `screenplay-structure.md` - Structure draft (reference)
- `screenplay.md` - Final screenplay (THIS IS THE ONE!) ⭐

**Review & Feedback**:
```
Option A: "Approved, proceed to shot breakdown"
Option B: "Scene 3 dialogue feels too formal, make it more conversational"
Option C: "Ananya's voice doesn't match her character, make her more measured"
Option D: "Add more Hinglish to Vikram's dialogue (he's urban elite)"
Option E: "The twist reveal dialogue is weak, make it more impactful"
```

**When Approved, Proceed to Step 4** ✓

---

### **STEP 4: Shot Breakdown** 📹

**What This Creates**:
- `shot-breakdown.md` - Complete shot-by-shot production plan

**Prerequisite**: Screenplay must be approved ✓

**Command**:
```
"band-darwaza"
```

**What Happens**:
1. Shot Breakdown Specialist reads:
   - `genre-analysis.md` (for visual style)
   - `character-bible.md` (for character beats)
   - `screenplay.md` (for scenes)
2. Applies genre-specific cinematography (Thriller → close-ups, tension)
3. Creates detailed shot breakdown for EACH shot:

**Shot Specification** (12-point detail):
```
SHOT 5C - CRIME SCENE REVEAL

CAMERA:
  Shot Size: Wide Shot (WS)
  Angle: High angle (god's view)
  Movement: Slow dolly in
  Lens: Wide 24mm

FRAMING:
  Body center floor, blood pool
  Smart home devices blinking

BLOCKING:
  Static (corpse)
  Sharma enters frame left

LIGHTING MOOD:
  Underlit crime scene (noir)
  LED glows (cold technology)

DIALOGUE:
  [Scene dialogue lines]

PERFORMANCE:
  Sharma: Controlled shock

CONTINUITY:
  Blood pattern consistent
  Smart devices active

PRODUCTION NOTES:
  Duration: 5 seconds
  Priority: MUST HAVE
  Difficulty: Complex
  Equipment: Dolly + 4ft track
  Special: Blood FX required

STORY PURPOSE:
  Establish crime scene horror

VISUAL REFERENCE:
  Memories of Murder (2003)

EDIT NOTES:
  Cut to close-up next
```

4. Provides TWO orderings:
   - **Story Order**: How shots appear in film
   - **Shooting Order**: Optimized for production (by location/setup)

5. Lists equipment requirements and production estimates

**Output Location**: `project/band-darwaza/shot-breakdown.md`

**Typical Output**: 40-60 shots for 5-minute film

**Review & Feedback**:
```
Option A: "Approved, ready for production"
Option B: "Shot 5C needs closer framing for tension"
Option C: "Add more close-ups of Ananya's face in Scene 7"
Option D: "The lighting for night scenes should be darker"
Option E: "Need more coverage for editing flexibility in Scene 9"
```

**When Approved: PRODUCTION READY!** 🎬✓

---

## 🎮 Commands Reference

### **Basic Execution Commands**

**Step 1: Story Synopsis**
```bash
# Tell your concept directly
"Create a 5-minute thriller about [concept]. Call it [project-name]."

# Or be more specific
"15-minute romantic drama about two strangers meeting on a train.
Set in Mumbai. Called train-se-pyaar. Should have a bittersweet ending."
```

**Step 2: Character Bible**
```bash
# Just project name
"[project-name]"

# Example
"band-darwaza"
```

**Step 3: Screenplay**
```bash
# Default (Simple Bollywood Hindi)
"[project-name]"

# With specific dialect
"[project-name] in Haryanvi"
"[project-name] in Hinglish"
"[project-name] in Pure Hindi"
"[project-name] in Punjabi-influenced style"

# Examples
"band-darwaza"
"band-darwaza in Haryanvi"
```

**Step 4: Shot Breakdown**
```bash
# Just project name
"[project-name]"

# Example
"band-darwaza"
```

### **Feedback Commands**

**To Approve and Continue**:
```bash
"Approved, proceed to next step"
"Looks good, continue"
"Yes, move forward"
```

**To Request Changes**:
```bash
# Specific change
"Change [element] to [desired change]"
"Make [character] more [trait]"
"Add [new element]"

# Examples
"Make the twist darker"
"Change Ananya's backstory to show more trauma"
"The dialogue in Scene 5 is too formal, make it conversational"
"Add 3 more close-ups in the interrogation scene"
```

**To Regenerate Completely**:
```bash
"Regenerate story synopsis"
"Rewrite the screenplay dialogue"
"Redo shot breakdown with different visual style"
```

**To Start Over**:
```bash
"Start over with new concept"
"Different approach"
```

---

## 📁 File Flow & Dependencies

Each workflow reads previous outputs automatically:

```
STEP 1: Story Synopsis
  Input: Your concept (verbal)
  Output:
    ├─ genre-analysis.md
    └─ story-synopsis.md

STEP 2: Character Bible
  Input:
    ├─ genre-analysis.md ← (reads automatically)
    └─ story-synopsis.md ← (reads automatically)
  Output:
    └─ character-bible.md

STEP 3: Screenplay
  Input:
    ├─ genre-analysis.md ← (reads automatically)
    ├─ story-synopsis.md ← (reads automatically)
    └─ character-bible.md ← (reads automatically)
  Output:
    ├─ screenplay-structure.md (reference)
    └─ screenplay.md ⭐ (FINAL)

STEP 4: Shot Breakdown
  Input:
    ├─ genre-analysis.md ← (reads automatically)
    ├─ character-bible.md ← (reads automatically)
    └─ screenplay.md ← (reads automatically)
  Output:
    └─ shot-breakdown.md
```

**You NEVER need to specify input files** - the system reads them automatically based on project name.

---

## 🔄 Feedback Loop Workflow

### **Standard Iteration Pattern**:

```
1. Execute Workflow
   ↓
2. System Creates Output
   ↓
3. YOU REVIEW
   ↓
4. Decision Point:
   ├─ Option A: APPROVE → Proceed to next step
   ├─ Option B: ADJUST → Give specific feedback → System regenerates
   └─ Option C: START OVER → Try different approach

5. Repeat until approved
   ↓
6. Move to next workflow step
```

### **Example Feedback Loop (Screenplay)**:

```
Iteration 1:
You: "band-darwaza"
System: Creates screenplay.md
You: "Scene 3 dialogue is too formal"
System: Regenerates Scene 3 with conversational dialogue
         ↓
Iteration 2:
You review: "Scene 3 is better, but Ananya needs more Hindi"
System: Adjusts Ananya's dialogue (increases Hindi ratio)
         ↓
Iteration 3:
You review: "Perfect! Approved, proceed to shot breakdown"
System: Moves to Step 4
```

---

## 🎯 Quality Checkpoints

Before approving each step, verify:

### **Story Synopsis Checkpoint** ✓
- [ ] Story is unique, not generic (no clichés)
- [ ] Multi-layered twists (not single twist at end)
- [ ] Story flows naturally from beginning to end
- [ ] Twist recontextualizes everything
- [ ] Language is accessible (simple Bollywood Hindi)
- [ ] WOW factor present (worth making this film)

### **Character Bible Checkpoint** ✓
- [ ] All characters from story covered
- [ ] Principals deeply developed (psychology, arc, voice)
- [ ] Characters feel real and three-dimensional
- [ ] Motivations are clear and believable
- [ ] Each character has distinct voice (can tell who's speaking)
- [ ] Relationships make sense and are mapped
- [ ] Arcs are clear and earned

### **Screenplay Checkpoint** ✓
- [ ] Industry-standard format (INT/EXT headings)
- [ ] Visual storytelling (show don't tell)
- [ ] Genre style applied correctly (thriller = tension)
- [ ] Action lines clear and specific
- [ ] Dialogue is natural and actable
- [ ] Each character sounds DISTINCT (different voices)
- [ ] Language/dialect authentic
- [ ] Memorable, impactful lines present
- [ ] Subtext present (what's unsaid matters)
- [ ] No camera/technical directions (clean)

### **Shot Breakdown Checkpoint** ✓
- [ ] Every scene from screenplay covered
- [ ] Shot specifications complete (12-point detail)
- [ ] Genre visual style applied (thriller = close-ups)
- [ ] Coverage adequate for editing (master + coverage + inserts)
- [ ] Production notes practical (equipment, difficulty)
- [ ] Shooting order optimized (by location/setup)
- [ ] Equipment list complete
- [ ] Production estimates realistic

---

## 🚀 Quick Start Examples

### **Example 1: 5-Minute Thriller**

```
Step 1: "Create a 5-minute thriller about a locked room murder in
        a smart apartment. Technology backfiring theme. Call it band-darwaza."

        Review → Approved ✓

Step 2: "band-darwaza"

        Review → "Make Ananya's backstory show more trauma history"
        System regenerates → Review → Approved ✓

Step 3: "band-darwaza"

        Review → "Scene 5 dialogue too formal, make it natural"
        System regenerates → Review → Approved ✓

Step 4: "band-darwaza"

        Review → "Add 2 more close-ups in interrogation"
        System regenerates → Review → Approved ✓

DONE! Production ready 🎬
```

### **Example 2: 15-Minute Romance with Dialect**

```
Step 1: "Create a 15-minute romantic drama about a struggling
        musician and a deaf painter falling in love. Set in Delhi.
        Call it khamoshi-ka-sangeet. Bittersweet ending."

        Review → Approved ✓

Step 2: "khamoshi-ka-sangeet"

        Review → Approved ✓

Step 3: "khamoshi-ka-sangeet in Hinglish"
        (Urban Delhi youth speak mix of Hindi-English)

        Review → Approved ✓

Step 4: "khamoshi-ka-sangeet"

        Review → Approved ✓

DONE! Production ready 🎬
```

---

## 💡 Pro Tips

### **For Better Story Results**:
1. Be specific about concept and theme
2. Mention reference films if you have them
3. Specify must-have elements upfront
4. State target audience and tone

### **For Better Character Results**:
1. Let the story be approved first (don't rush)
2. Think about which characters need deep development
3. Consider how characters relate to each other
4. Review character voices - they must be distinct

### **For Better Screenplay Results**:
1. Ensure character bible is solid first
2. Specify dialect/language based on character backgrounds
3. Review structure before dialogue (check screenplay-structure.md)
4. Read dialogue aloud to test if it's actable

### **For Better Shot Breakdown Results**:
1. Ensure screenplay is locked (approved)
2. Think about visual style you want
3. Review coverage - is there enough for editing?
4. Check shooting order makes logistical sense

---

## 🎬 What You Get at the End

After completing all 4 steps, your project folder contains:

```
project/band-darwaza/
├── genre-analysis.md        (Reference)
├── story-synopsis.md         (Reference)
├── character-bible.md        (Reference + Actor prep)
├── screenplay.md             ⭐ SHOOTING SCRIPT
└── shot-breakdown.md         ⭐ PRODUCTION PLAN

Total: Production-ready package for filming!
```

**Ready for**:
- Director's prep (shot list, coverage plan)
- Cinematographer's prep (camera, lighting plan)
- Actors' prep (character understanding, dialogue)
- Production team (equipment, scheduling)
- Script supervisor (continuity tracking)

---

## ❓ FAQ

**Q: Can I skip steps?**
A: No. Each step depends on previous steps' outputs. You must go in order.

**Q: Can I go back and change an earlier step?**
A: Yes, but you'll need to regenerate all subsequent steps to maintain consistency.

**Q: How long does each step take?**
A:
- Story Synopsis: 5-15 minutes
- Character Bible: 15-30 minutes (depends on character count)
- Screenplay: 30-60 minutes (depends on length)
- Shot Breakdown: 30-45 minutes (depends on complexity)

**Q: Can I work on multiple projects simultaneously?**
A: Yes! Each project has its own folder. Just specify project name.

**Q: What if I want to change the dialect after screenplay is done?**
A: Re-run Step 3 with new dialect specification. It will regenerate dialogue.

**Q: How many iterations can I do?**
A: Unlimited! Iterate until you're satisfied.

**Q: Can I manually edit the output files?**
A: Yes, but if you regenerate that step, your manual edits will be overwritten.

---

## 🎓 Learning Path

**New to filmmaking?** Follow this learning path:

1. **Start with simple concepts** (5-minute shorts)
2. **Study the outputs** (see how professionals structure things)
3. **Give detailed feedback** (learn what works and what doesn't)
4. **Compare to Bollywood films** (see genre patterns)
5. **Graduate to complex projects** (15+ minutes)

**Key Learning**: Each iteration teaches you about:
- Story structure (what makes stories work)
- Character development (what makes characters real)
- Screenplay craft (how to write for screen)
- Cinematography (how to visualize stories)

---

## 🚦 System Status Indicators

During execution, you'll see:

```
🟡 WORKING - System is generating content
🟢 READY - Output ready for your review
🔴 WAITING - Needs your feedback to proceed
✅ APPROVED - Step complete, ready for next
```

---

**Remember**: This is YOUR creative process. Take your time at each step. The system is here to help you achieve Bollywood professional-level quality, but YOU make the creative decisions.

**Quality over speed. Iteration over perfection. Story first, always.**

---

## 📞 Need Help?

If you're stuck or unsure:

```
"Help with [step name]"
"What should I review in the screenplay?"
"How do I give feedback?"
"Show me example feedback for character bible"
```

The system will guide you!

---

**Ready to create your first film?**

Start with: `"Create a [duration] [genre] about [concept]. Call it [project-name]."`

🎬 **Action!**
