# BMAD-FILM WORKFLOW CONTROLLER

# ═══════════════════════════════════════════════════════════════════
# 🔴 THIS FILE IS THE SINGLE AUTHORITY FOR WORKFLOW ENFORCEMENT
# ═══════════════════════════════════════════════════════════════════
#
# ALL workflows MUST follow these rules — no exceptions.
# ALWAYS announce each step. NEVER skip steps. NEVER rush to output.
#
# ═══════════════════════════════════════════════════════════════════

---

## MANDATORY STEP ANNOUNCEMENT FORMAT

Before executing ANY step, announce to user:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 STEP [X] of [TOTAL] — [Step Name]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

After completing a step:
```
✅ STEP [X] complete. Moving to STEP [X+1].
```

**This announcement is the enforcement mechanism. It cannot be skipped.**

---

## WORKFLOW 1: STORY SYNOPSIS
**Trigger**: Any story/film/screenplay request
**Agent**: master-story-director.md → genre-specialist → format-selector
**Reference**: `.bmad-film/workflows/development/story-synopsis.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 9 — Format Selection                                  │
│   • What are you making? (feature/short/web series/etc.)        │
│   • Which story structure? (Three-Act/Hero's Journey/etc.)      │
│   • Structure-specific writer questions (format-selector.md)    │
│                                                                 │
│ STEP 1 of 9 — Concept Mining                                    │
│   • Extract 3-5 specific threads from writer's OWN words        │
│   • Probe each thread before starting structured questions      │
│   • "70% story must come from writer's words" — extract first   │
│                                                                 │
│ STEP 2 of 9 — Phase A: Writer's Soul (Q1-Q5)                   │
│   Q1: Why this story? What pulls you back?                      │
│   Q2: First image you see — describe it                         │
│   Q3: What should audience feel at the end?                     │
│   Q4: What's uncomfortable but necessary to say?                │
│   Q5: Who is this story for?                                    │
│                                                                 │
│ STEP 3 of 9 — Phase B: Protagonist Interior (Q6-Q10)           │
│   Q6: Character's first image — what worn, how moves            │
│   Q7: What they WANT (surface) vs what they NEED (deep)         │
│   Q8: Their hidden shame — a secret they never tell             │
│   Q9: How do they change by end?                                │
│   Q10: A wrong thing they did that felt completely right        │
│                                                                 │
│ STEP 4 of 9 — Phase C: World & Atmosphere (Q11-Q14)            │
│   [Skip for <5 min films — ask only Q11 and Q12]               │
│   Q11: Main location — smell, sound, light, feeling            │
│   Q12: What time of day/season? Why does it fit?               │
│   Q13: The place protagonist never wants to go but must         │
│   Q14: What's breaking or building in the background?           │
│                                                                 │
│ STEP 5 of 9 — Phase D: Conflict & Structure (Q15-Q19)          │
│   Q15: The one decision that changes everything                 │
│   Q16: The lowest point — when all seems lost                   │
│   Q17: One person they can be completely honest with            │
│   Q18: Any twist or reveal? (Not required — share if exists)   │
│   Q19: Last image of the film                                   │
│                                                                 │
│ STEP 6 of 9 — Phase E: Soul & Tone (Q20-Q23)                   │
│   Q20: Any humor or warmth? Or pure dark?                       │
│   Q21: One film whose FEEL matches (not story, just feel)       │
│   Q22: What you absolutely DON'T want (clichés, tropes)        │
│   Q23: Something unexpected for this genre                      │
│                                                                 │
│ STEP 7 of 9 — Genre Analysis + Agent Routing                    │
│   • Summarize all answers                                       │
│   • Identify primary + secondary genre                          │
│   • Select genre specialist                                     │
│   • Save genre-analysis.md                                      │
│                                                                 │
│ STEP 8 of 9 — Genre-Specific Questions (10-15 Qs)              │
│   • Thriller: Antagonist, twist timing, suspense type           │
│   • Romance: Obstacle, chemistry moment, separation             │
│   • Action: Set-piece, combat style, climax                     │
│   • [Etc. per selected genre specialist]                        │
│                                                                 │
│ STEP 9 of 9 — Story Creation ← ONLY NOW, NOT BEFORE            │
│   • Write BOTH formats in story-synopsis.md:                    │
│     1. Continuous Narrative (flowing Hindi prose)               │
│     2. Scene-by-Scene Breakdown (technical production version)  │
│   • Language: Simple Bollywood Hindi (60-70% Hindi)             │
│   • Save: project/{project_name}/story-synopsis.md             │
└─────────────────────────────────────────────────────────────────┘
```

**HARD GATES:**
- Cannot reach STEP 9 without completing STEPS 0-8
- User says "just write it" → Still complete current step, then next
- Never offer "quick version" or "rough outline" — full workflow only

---

## WORKFLOW 2: CHARACTER BIBLE
**Trigger**: User requests character bible (or next step after synopsis approved)
**Agent**: character-developer.md
**Reference**: `.bmad-film/workflows/development/character-bible.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 5 — Read Project Files + Dialect Setup               │
│   READ FIRST (mandatory):                                       │
│   • project/{name}/genre-analysis.md                           │
│   • project/{name}/story-synopsis.md                           │
│   Then: Ask dialect strategy (single/multi)                     │
│                                                                 │
│ STEP 1 of 5 — Character Roster                                  │
│   • Extract all characters FROM the story synopsis             │
│   • Do not invent new characters                                │
│                                                                 │
│ STEP 2 of 5 — 18 Character Questions                           │
│   • Q1-Q8: Protagonist deep dive                                │
│   • Q9-Q13: Supporting characters (per character)              │
│   • Q14-Q18: Character dynamics                                 │
│                                                                 │
│ STEP 3 of 5 — Synthesis + User Confirmation                     │
│   • Summarize all answers                                       │
│   • Confirm before writing profiles                             │
│                                                                 │
│ STEP 4 of 5 — Profile Creation                                  │
│   • Write full profiles for all characters                      │
│   • Principal: 8 aspects full depth                             │
│   • Supporting: depth per Q13 answers                          │
│                                                                 │
│ STEP 5 of 5 — QA + Finalize                                    │
│   • Verify all profiles use writer's specific answers           │
│   • Save: project/{name}/character-bible.md                    │
└─────────────────────────────────────────────────────────────────┘
```

---

## WORKFLOW 3: BEAT SHEET
**Trigger**: User requests beat sheet
**Agent**: beat-sheet-specialist (or master-story-director)
**Reference**: `.bmad-film/workflows/development/beat-sheet.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│ STEP 0 — Read synopsis + character-bible                        │
│ STEP 1 — 8 Beat Questions                                       │
│ STEP 2 — Beat Architecture                                      │
│ STEP 3 — Beat Sheet Creation                                    │
│ STEP 4 — QA + Finalize                                          │
│   Save: project/{name}/beat-sheet.md                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## WORKFLOW 4: SCREENPLAY
**Trigger**: User requests screenplay (after character-bible approved)
**Agent**: screenplay-structure-writer.md → dialogue-writer.md
**Reference**: `.bmad-film/workflows/development/screenplay.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 4 — Read ALL Project Files                            │
│   READ (mandatory):                                             │
│   • genre-analysis.md + story-synopsis.md                      │
│   • character-bible.md + beat-sheet.md                         │
│   • Detect dialect setup                                        │
│                                                                 │
│ STEP 1 of 4 — Screenplay Questions (15 questions)               │
│   • Q1-Q10: Structure Writer asks (style, pacing, scenes)       │
│   • Q11-Q15: Dialogue Writer asks (language, voice, lines)      │
│                                                                 │
│ STEP 2 of 4 — Structure Draft (Screenplay Structure Writer)     │
│   • Scene headings, action lines, placeholder dialogue          │
│   • Save: screenplay-structure.md                               │
│                                                                 │
│ STEP 3 of 4 — Dialogue Pass (Dialogue Writer)                   │
│   • Replace all placeholder dialogue with final impactful lines │
│   • Genre-appropriate dialogue (Bollywood masters style)        │
│                                                                 │
│ STEP 4 of 4 — Final Screenplay                                  │
│   • Save: project/{name}/screenplay.md                         │
│   • Credits: "Screenplay by X, Dialogues by Y"                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## WORKFLOW 5: SHOT BREAKDOWN
**Trigger**: User requests shot breakdown (after screenplay approved)
**Agent**: shot-breakdown-specialist.md
**Reference**: `.bmad-film/workflows/pre-production/shot-breakdown.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 3 — Read ALL Project Files                            │
│   READ (mandatory):                                             │
│   • genre-analysis.md + story-synopsis.md                      │
│   • character-bible.md + beat-sheet.md + screenplay.md         │
│                                                                 │
│ STEP 1 of 3 — Visual Questions (15 questions)                   │
│   • Q1-Q7: Visual style questions                               │
│   • Q8-Q11: Coverage strategy                                   │
│   • Q12-Q15: Production reality                                 │
│                                                                 │
│ STEP 2 of 3 — Shot Draft                                        │
│   • Shot-by-shot breakdown per scene                            │
│   • Story order + shooting order                                │
│                                                                 │
│ STEP 3 of 3 — Final Shot Breakdown                              │
│   • Save: project/{name}/shot-breakdown.md                     │
│   • Equipment requirements + production notes                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## UNIVERSAL RULES (Apply to ALL Workflows)

### 1. Step Announcement is NON-NEGOTIABLE
Every step must be announced with `📍 STEP X of Y — [Name]` before executing.
This is what keeps the workflow on track.

### 2. File Reading is MANDATORY at Workflow Start
Every workflow MUST read all relevant project files before asking questions.
This ensures continuity across steps.

### 3. User Can't Skip Steps
Even if user says "skip to the story" or "just write it":
→ Still announce current step → Complete it → Move to next
Never jump ahead.

### 4. Question Phase Before Creation Phase
Story creation ONLY happens after ALL question phases complete.
Character Bible ONLY after synopsis approved.
Screenplay ONLY after character-bible approved.
Shot Breakdown ONLY after screenplay approved.

### 5. Both Story Formats Mandatory
Story Synopsis ALWAYS produces:
1. Continuous Narrative (flowing Hindi prose)
2. Scene-by-Scene Breakdown (technical version)
Both in same file. No exceptions.

### 6. Language Default
Simple Bollywood Hindi (60-70% Hindi + 30-40% natural English)
Unless user specifies regional dialect.

---

## QUICK TRIGGER REFERENCE

| User Says | Workflow | First Step |
|-----------|----------|------------|
| "story banao", "ek kahani", "write a story", "film concept" | Story Synopsis | STEP 0 — Format Selection |
| "character bible", "characters develop karo" | Character Bible | STEP 0 — Read Files |
| "beat sheet banao", "beats dikhao" | Beat Sheet | STEP 0 — Read Files |
| "screenplay likho", "script banao" | Screenplay | STEP 0 — Read Files |
| "shot breakdown", "shots plan karo" | Shot Breakdown | STEP 0 — Read Files |

---

*Reference this file whenever a workflow is triggered to ensure correct step sequence.*
*If in doubt about which step you're on — announce the step to the user to confirm.*
