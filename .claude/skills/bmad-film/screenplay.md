# Screenplay Development Skill

**Command**: `/screenplay [project-name] [optional: in Dialect]`
**Step**: 4 of 5 in BMAD-FILM pipeline
**Workflow**: `.bmad-film/workflows/development/screenplay.yaml`

---

## Skill Instructions

When the user invokes `/screenplay [project-name]` (optionally with dialect like "in Haryanvi"), execute:

### 1. Setup

- Read workflow: `.bmad-film/workflows/development/screenplay.yaml`
- Read agents:
  - `.bmad-film/agents/screenplay-structure-writer.md`
  - `.bmad-film/agents/dialogue-writer.md`
  - `.bmad-film/agents/master-story-director.md`
- Read existing files from `project/{project-name}/`:
  - `story-synopsis.md` (REQUIRED)
  - `genre-analysis.md` (REQUIRED)
  - `character-bible.md` (REQUIRED)
  - `beat-sheet.md` (REQUIRED — don't skip this)
- If any required file is missing, tell user which step to complete first.

Read genre specialist from `.bmad-film/agents/genre-specialists/` based on genre-analysis.md.

**Detect dialect**: If user wrote "in Haryanvi" / "in Punjabi" / etc., note it. Default = Simple Bollywood Hindi.

### 2. Phase 0 — Dialect Auto-Detection

Check if multi-dialect character-bible exists (e.g., character-bible-punjabi.md). If yes, offer to create dialect-specific screenplays automatically.

### 3. Phase 1 — Screenplay Questions (ask 8-10 questions total, split between two agents)

**Agent 1: Screenplay Structure Writer asks (5 questions):**
1. "Kaun sa scene sabse visually powerful hona chahiye? (Hero scene)"
2. "Screenplay ki pacing kaisi rakhen? Fast cuts ya long takes?"
3. "Koi specific scene hai jo aapke dimag mein already picturize hua hai?"
4. "Opening shot kaisa hoga — wide establishing ya tight close-up?"
5. "Indoor heavy hai ya outdoor? Night scenes hain?"

**Agent 2: Dialogue Writer (Samvad Lekhak) asks (3-5 questions):**
6. "Hindi-English ratio kya rakhen? (60-40 default, ya pure Hindi, ya 80-20?)"
7. "Koi regional dialect chahiye? (Haryanvi / Punjabi / Awadhi / Bombay cutting?)"
8. "Ek iconic line ya moment hai jo aapko chahiye — woh describe karo"
9. "Characters ke beech banter kaisa hoga? Sharp wit / emotional / poetic?"

### 4. Phase 2 — Two-Agent Bollywood Model

**AGENT 1: Screenplay Structure Writer**

Write the complete structural screenplay with:
- Proper scene headings: `INT. LOCATION - DAY/NIGHT`
- Action lines (visual, present tense, show don't tell)
- Character blocking and physical beats
- `[DIALOGUE PLACEHOLDER: emotion/intent here]` for dialogue spots
- Camera and visual notes in brackets: `[CLOSE ON: hands shaking]`
- Transitions
- Genre-specific visual language from the genre agent

**AGENT 2: Dialogue Writer (Samvad Lekhak)**

Go through every dialogue placeholder and replace with FINAL impactful dialogue:
- Match character voice from character-bible
- Apply correct language ratio and dialect
- Write subtext — what's NOT said is as important
- Include memorable, quotable lines (Bollywood standard)
- Avoid clichés — if a line has been said before, rewrite it

Credits line: `Screenplay: [Structure Writer] | Dialogues: [Samvad Lekhak]`

### 5. Phase 3 — Quality Check with Master Story Director

Master Story Director reviews:
- Does every scene serve the story?
- Are all beats from beat-sheet.md covered?
- Is pacing correct for the format?
- Does dialogue feel authentic, not written?

### 6. Save Output

- `project/{project-name}/screenplay-structure.md` (structural pass — internal)
- `project/{project-name}/screenplay.md` (FINAL — structure + dialogue combined)
- Multi-dialect: `project/{project-name}/screenplay-punjabi.md`, etc.

### 7. Confirm & Next Step

```
✅ Screenplay saved to: project/{project-name}/screenplay.md

Next step: /shot-breakdown {project-name}
```

---

## Language/Dialect Options

```
/screenplay project-name                    → Default Bollywood Hindi (60% Hindi, 40% English)
/screenplay project-name in pure Hindi      → 90%+ Hindi, minimal English
/screenplay project-name in Haryanvi        → Haryanvi dialect dialogue
/screenplay project-name in Punjabi         → Punjabi dialect dialogue
/screenplay project-name in Gujarati        → Gujarati dialect dialogue
/screenplay project-name in Bombay Hindi    → Street Mumbai Hindi
```

---

## Error Handling

- Beat-sheet missing: "Beat sheet nahi hai — `/beat-sheet {project-name}` chalao pehle. Bina beats ke screenplay hollow hoga."
- Generic dialogue detected: Rewrite immediately — "Yeh line toh hazaron films mein hai. Kuch naya likho."
- Scene count wrong for runtime: Flag pacing issue and suggest cuts/additions
