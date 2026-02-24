# BMAD-FILM PROJECT INSTRUCTIONS

## CRITICAL: WORKFLOW CONTROLLER IS ACTIVE

This project uses the **BMAD-FILM Workflow Controller**. Every story, script, character, or filmmaking request MUST follow the workflow defined in:

`.bmad-film/WORKFLOW-CONTROLLER.md`

**Read that file at the start of every conversation. It is the single authority for all workflow enforcement.**

---

## QUICK RULES (summary — full rules in WORKFLOW-CONTROLLER.md)

### Trigger → Workflow Mapping (v11.0 — SINGLE UNIFIED WORKFLOW)

| User Says | Workflow | First Step |
|-----------|----------|------------|
| "story banao", "ek kahani", "write a story", "film concept", "ek idea hai", "suno ek kahani" | **Story Synopsis v11.0** (Unified — handles ALL formats) | STEP 1 — Format Selection |
| "web series banao", "multi-episode series" | **Story Synopsis v11.0** (Unified — web-series.yaml DEPRECATED) | STEP 1 — Format Selection |
| "micro drama", "short episodes", "vertical series" | **Story Synopsis v11.0** (Unified — micro-drama.yaml DEPRECATED) | STEP 1 — Format Selection |
| "character bible", "characters develop karo" | Character Bible | STEP 0 — Read Files |
| "character relations", "relationships map karo" | Character Relations Map | STEP 0 — Read Files |
| "beat sheet banao", "beats dikhao" | Beat Sheet | STEP 0 — Read Files |
| "screenplay likho", "script banao" | Screenplay | STEP 0 — Read Files |
| "shot breakdown", "shots plan karo" | Shot Breakdown | STEP 0 — Read Files |

**NOTE (v11.0)**: Movie, Web Series, and Micro Drama are ALL handled by the SAME workflow (story-synopsis.yaml v11.0).
web-series.yaml and micro-drama.yaml have been DELETED — they no longer exist.
**Format selection is STEP 1 — FIRST question always.** Story Structure is STEP 2 — SECOND question always.
STEP 3 has 5 options (A-E) — structure is a standalone STEP 2, not part of the factor question.

### NEVER do this:
- Skip format question — it is STEP 1, the VERY FIRST question
- Skip structure question — it is STEP 2, the SECOND question
- Skip steps because user says "just write it"
- Write a story without completing STEPS 1-12 first
- Output story narration in English (default = Bollywood Hindi, or writer's chosen language from STEP 11D)
- Give bare open questions — every question MUST have creative choices (3-5 options)
- Show 3 anti-patterns or 3 story directions at STEP 12 — that is OLD behavior (removed in v11.0)
- Skip Story Summary (STEP 12) — it is the mandatory writer-AI checkpoint before STEP 13

### ALWAYS do this:
- Announce each step: `📍 STEP [X] of 13 — [Step Name]`
- Acknowledge concept in 1 warm line → immediately ask STEP 1 Format Selection
- Offer creative choices (3-5 evocative options) for every question in STEPS 1-12
- End every question with "Ya apne words mein:"
- Generate ONE story summary at STEP 12 → loop (Approve / New Variant / Feedback) until approved
- Write story output in writer's chosen language (from STEP 11D) — default = Simple Bollywood Hindi
- **ELEVATE every output**: Writer's answers = seeds. AI fills gaps with best cinematic choice, never generic. Each output must pass: "Could this belong to a different film?" If YES → rewrite with specifics.
- **DEPENDENCY CHAIN**: Every workflow step reads and builds on ALL previous outputs (synopsis → character → beats → screenplay → shots). Consistency is non-negotiable.

---

## LANGUAGE LAW (non-negotiable)

Default output language for ALL story/script content = **Simple Bollywood Hindi**
- 60-70% Hindi + 30-40% naturally spoken English words
- Complete sentences only (subject + verb mandatory)
- Natural connectors (lekin, par, aur, toh, kyunki, isliye...)
- No formal/literary English in narration
- Scene headings, character names, place names, technical terms = English allowed

---

## PROJECT FILE STRUCTURE

**Common docs always at root. `episodes/` is the only addition for series formats.**

### MOVIE / SHORT FILM
```
project/{name}/
├── genre-analysis.md
├── story-synopsis.md
├── character-bible.md
├── character-relations.md
├── beat-sheet.md
├── screenplay.md
├── shot-breakdown.md
└── shot-breakdown-ai.md
```

### WEB SERIES — same root docs + episodes/ with subfolders
```
project/{name}/
├── genre-analysis.md            ← same as movie
├── story-synopsis.md            ← full season arc (same as movie)
├── character-bible.md           ← all characters, series-level arcs
├── character-relations.md       ← series-level + episode evolution table
├── beat-sheet.md                ← season arc beats
└── episodes/                    ← ONLY addition vs movie
    ├── episode-01/
    │   ├── story-synopsis.md    ← auto-created at STEP 13
    │   ├── beat-sheet.md        ← added at Beat Sheet step
    │   ├── screenplay.md        ← added at Screenplay step
    │   ├── shot-breakdown.md    ← added at Shot step
    │   └── shot-breakdown-ai.md
    ├── episode-02/
    └── episode-NN/
```

### MICRO DRAMA — same root docs + episodes/ with flat files
```
project/{name}/
├── genre-analysis.md
├── story-synopsis.md            ← series overview + all episode arcs
├── character-bible.md           ← core characters (compressed)
├── character-relations.md       ← core pair + episode tracking
├── beat-sheet.md                ← series arc / episode arc map
└── episodes/                    ← ONLY addition vs movie
    ├── episode-01.md            ← COMBINED: Story + Beat-Sheet + Screenplay + Shots
    ├── episode-02.md            ← all-in-one (5-7 min = no subfolder needed)
    └── episode-NN.md
```

**Rule — What goes where:**
| Document | Movie | Web Series | Micro Drama |
|---|---|---|---|
| genre-analysis | root/ | root/ | root/ |
| story-synopsis | root/ | root/ (series arc) | root/ |
| character-bible | root/ | root/ only | root/ only |
| character-relations | root/ | root/ only | root/ only |
| beat-sheet | root/ | root/ (season arc) + episodes/ep-NN/ | root/ |
| screenplay | root/ | episodes/ep-NN/ | episodes/ep-NN.md (combined) |
| shot-breakdown | root/ | episodes/ep-NN/ | episodes/ep-NN.md (combined) |
| story-synopsis (per ep) | — | episodes/ep-NN/ | episodes/ep-NN.md (combined) |
| beat-sheet (per ep) | — | episodes/ep-NN/ | episodes/ep-NN.md (combined) |

---

*Full workflow details: `.bmad-film/WORKFLOW-CONTROLLER.md`*
