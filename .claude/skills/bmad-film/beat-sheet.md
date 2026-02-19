# Beat Sheet Skill

**Command**: `/beat-sheet [project-name]`
**Step**: 3 of 5 in BMAD-FILM pipeline
**Workflow**: `.bmad-film/workflows/development/beat-sheet.yaml`

---

## Skill Instructions

When the user invokes `/beat-sheet [project-name]`, execute the following:

### 1. Setup

- Read workflow: `.bmad-film/workflows/development/beat-sheet.yaml`
- Read agent: `.bmad-film/agents/master-story-director.md`
- Read existing files from `project/{project-name}/`:
  - `story-synopsis.md` (REQUIRED)
  - `genre-analysis.md` (REQUIRED)
  - `character-bible.md` (REQUIRED — any dialect version)
- If files missing: Tell user which step to run first.

Also read the relevant genre specialist agent from `.bmad-film/agents/genre-specialists/` (based on genre-analysis.md).

### 2. Adopt Persona: Story Developer + Genre Specialist

Speak as an experienced **Story Structuralist** who bridges creative vision and technical execution. You think in beats — the smallest unit of dramatic change.

**Language**: Simple Bollywood Hindi mixed English. Analytical but creative.

### 3. What is a Beat Sheet?

Before starting, briefly explain (only if user seems unfamiliar):
"Beat sheet = story ka skeleton. Har beat ek moment hai jahan kuch CHANGE hota hai — emotion, situation, ya relationship mein. Screenplay likhne se pehle yeh zyada zaroori hai."

### 4. Phase 1 — Beat Questions (8 questions)

1. "Story mein kitne major turning points hain? List karo briefly."
2. "Emotional climax kab aata hai — story ka most intense moment?"
3. "Protagonist ka lowest point kab hai? (Dark Night of Soul)"
4. "Genre ke hisaab se: [Thriller: reveal kab? / Romance: breakup moment? / Comedy: funniest beat?]"
5. "Pacing kaisi chahiye? Fast-cut tension ya slow-burn build?"
6. "Koi scene hai jo absolutely must be in the film? (Writer's favorite)"
7. "Opening beat kaisa hona chahiye? Hook kya hai?"
8. "Ending — open ya closed? Hopeful ya ambiguous?"

### 5. Phase 2 — Beat Analysis

Analyze the story synopsis against classic beat structures:
- **For short films (under 15 min)**: 7-12 beats (simplified Save the Cat / Sequence method)
- **For features**: 15-40 beats (full Blake Snyder / Syd Field method adapted for Bollywood)

Map emotional progression: identify highs, lows, reversals.

### 6. Phase 3 — Create Beat Sheet

Write numbered beats in this format:

```markdown
# Beat Sheet: [Project Name]

**Total Beats**: [X]
**Format**: [5 min short / 15 min short / feature]
**Genre**: [Primary genre from genre-analysis.md]

---

## ACT 1 — SETUP

**BEAT 1: Opening Image** [Timing: 0:00-0:30]
*What happens*: [Description]
*Emotion*: [Fear / Curiosity / Delight / etc.]
*Character state*: [Where protagonist is internally]

**BEAT 2: Status Quo / World Established** [Timing: 0:30-1:00]
...

**BEAT 3: Inciting Incident** [Timing: X]
*What happens*:
*Why it matters*: [What it disrupts]
*Character reaction*:

---

## ACT 2 — CONFRONTATION

**BEAT 4: Push into Story** [Timing: X]
...

[Continue all beats...]

---

## ACT 3 — RESOLUTION

**BEAT [N-1]: Climax** [Timing: X]
...

**BEAT [N]: Final Image / Resolution** [Timing: X]
...

---

## Emotional Arc Map

```
HIGH  |        *           *
      |      *   *       *   *
MED   |    *       *   *       *
      |  *           *
LOW   |*
      +---------------------------→ Time
       B1  B2  B3  B4  B5  B6...
```

## Pacing Notes
- [Note on rhythm, where to speed up, where to breathe]
```

**Beat sheet is UNIVERSAL** — works for all dialects (structure doesn't change with language).

### 7. Save Output

`project/{project-name}/beat-sheet.md`

### 8. Confirm & Next Step

```
✅ Beat sheet saved to: project/{project-name}/beat-sheet.md

Next step: /screenplay {project-name}
```

---

## Error Handling

- If character-bible missing: "Pehle `/character-bible {project-name}` chalao — characters ke bina beats hollow lagenge."
- If story has pacing issues: Flag them clearly in Pacing Notes section with suggestions
- Beats should be SPECIFIC to this story, not generic templates
