# BMAD-FILM Quick Reference
**Breakthrough Method of Agile AI-Driven Filmmaking**

---

## 5-STEP PIPELINE

| Step | Command | Output | Reads |
|------|---------|--------|-------|
| 1 | `/story-synopsis [name]` | `story-synopsis.md` + `genre-analysis.md` | Your concept |
| 2 | `/character-bible [name]` | `character-bible.md` | Step 1 |
| 3 | `/beat-sheet [name]` | `beat-sheet.md` | Steps 1+2 |
| 4 | `/screenplay [name]` | `screenplay.md` | Steps 1+2+3 |
| 5 | `/shot-breakdown [name]` | `shot-breakdown.md` | Step 4 |

---

## CALLING AGENTS DIRECTLY

```
*master-story-director       → Orchestrator / routing
*suspense-architect          → Thriller specialist
*romance-architect           → Romance specialist
*horror-architect            → Horror specialist
*comedy-architect            → Comedy specialist
*action-architect            → Action specialist
*drama-architect             → Drama specialist
*social-cinema-architect     → Social cinema specialist
*musical-architect           → Musical specialist
*character-developer         → Character depth
*screenplay-structure-writer → Structure pass only
*dialogue-writer             → Dialogue / dialect only
*shot-breakdown-specialist   → Cinematography only
```

---

## DIALECT CONTROL

```
/screenplay [name]                   → Default Bollywood Hindi (60/40)
/screenplay [name] in pure Hindi     → 90%+ Hindi
/screenplay [name] in Haryanvi       → Haryanvi
/screenplay [name] in Punjabi        → Punjabi
/screenplay [name] in Gujarati       → Gujarati
/screenplay [name] in Bombay Hindi   → Street Mumbai Hindi
```

---

## UTILITY COMMANDS

```
/bmad-film-help    → Full command reference
/project-status    → See project progress
/quick-film-spec   → Micro projects (ads, social media)
```

---

## PROJECT STRUCTURE

```
project/{name}/
├── genre-analysis.md       ← Step 1
├── story-synopsis.md       ← Step 1
├── character-bible.md      ← Step 2
├── beat-sheet.md           ← Step 3
├── screenplay.md           ← Step 4 (FINAL)
└── shot-breakdown.md       ← Step 5
```

---

## 8 GENRE SPECIALISTS (trained on Bollywood masters)

```
Thriller  → Sujoy Ghosh, Sriram Raghavan, Anurag Kashyap
Romance   → Yash Chopra, Sanjay Leela Bhansali, Imtiaz Ali
Horror    → Ram Gopal Varma, Vikram Bhatt
Comedy    → Rajkumar Hirani, Hrishikesh Mukherjee
Action    → Rohit Shetty, Siddharth Anand
Drama     → Zoya Akhtar, Shoojit Sircar
Social    → Shyam Benegal, Neeraj Ghaywan
Musical   → Farah Khan, Karan Johar, Aditya Chopra
```

---

## HOW TO USE

1. Start with a concept: `"5 minute thriller about a woman who confesses a murder she didn't commit. Project: ikraar"`
2. Run steps in order: each step reads the previous step's output
3. Skip a step only if you already have that content
4. Each step is interactive — agents ask questions, you shape the story

---

## EXAMPLE FULL RUN

```
/story-synopsis andha-kuan
/character-bible andha-kuan
/beat-sheet andha-kuan
/screenplay andha-kuan
/shot-breakdown andha-kuan
```

Done. `project/andha-kuan/` has everything needed to shoot.

---

*BMAD-FILM v2.0 | Beat Sheet added to pipeline | Multi-dialect support available*
