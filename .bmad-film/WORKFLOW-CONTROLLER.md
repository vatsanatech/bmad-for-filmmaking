# BMAD-FILM WORKFLOW CONTROLLER

# ═══════════════════════════════════════════════════════════════════
# 🔴 THIS FILE IS THE SINGLE AUTHORITY FOR WORKFLOW ENFORCEMENT
# ═══════════════════════════════════════════════════════════════════
#
# ALL workflows MUST follow these rules — no exceptions.
# ALWAYS announce each step. NEVER skip steps. NEVER rush to output.
#
# ═══════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════
# 🔴 GLOBAL LANGUAGE LAW — APPLIES TO EVERY AGENT, EVERY OUTPUT
# ═══════════════════════════════════════════════════════════════════
#
# DEFAULT LANGUAGE = SIMPLE BOLLYWOOD HINDI — NO EXCEPTIONS
# This applies to: Story Synopsis, Character Bible, Beat Sheet,
#                  Screenplay, Shot Breakdown, Dialogue, All outputs
#
# ─────────────────────────────────────────────────────────────────
# STANDARD: 60-70% Hindi + 30-40% naturally spoken English words
# ─────────────────────────────────────────────────────────────────
#
# WHAT THIS MEANS:
#
# Story narration = Hindi mein likhna
# Scene descriptions = Hindi mein likhna
# Character descriptions = Hindi mein likhna
# Action lines = Hindi mein likhna
# Dialogue = Hinglish (character ke hisaab se)
#
# SCENE HEADINGS = English allowed (industry standard: INT./EXT./DAY/NIGHT)
# CHARACTER NAMES = English allowed
# PLACE NAMES = English allowed
# TECHNICAL FILM TERMS = English allowed (close-up, cut to, fade out)
# SECTION HEADERS = English allowed
#
# ─────────────────────────────────────────────────────────────────
# SENTENCE QUALITY — MANDATORY RULES
# ─────────────────────────────────────────────────────────────────
#
# RULE 1 — COMPLETE SENTENCES ONLY (subject + verb mandatory)
#   GALAT ✗: "Pahad. Khamoshi. Teen din."
#   SAHI  ✓: "Pahad par teen din se khamoshi thi."
#
#   GALAT ✗: "Koi backup nahi. Koi team nahi."
#   SAHI  ✓: "Arjun ke paas na koi backup tha, na koi team."
#
# RULE 2 — NATURAL CONNECTORS (sentences must flow, not feel like a list)
#   Use: lekin, par, aur, toh, kyunki, isliye, phir bhi, jab, tab,
#        jaise hi, tabhi, warna, phir, haalaanki, baawajood, jo, jo bhi
#
#   GALAT ✗: "Woh aayi. Usne dekha. Woh ruk gayi."
#   SAHI  ✓: "Woh aayi toh usne dekha, aur ek pal ke liye ruk gayi."
#
# RULE 3 — FORBIDDEN ENGLISH WORDS (use Hindi equivalents)
#   tattered     → phata-puraana, ghisa hua
#   edges        → kinare, kona
#   debris       → malaaba, tootha-phoota
#   proximity    → paas, nazdiki
#   sustains     → jeeti rehti hai, thaami rehti hai
#   subsequently → uske baad, phir
#   encounter    → mulaqat, saamna
#   simultaneously → saath hi saath
#   establishment  → jagah, thikana
#   contemplating  → soch raha tha, samajhne ki koshish kar raha tha
#
# RULE 4 — ALLOWED ENGLISH (naturally spoken in Hindi)
#   notice, building, office, party, time, okay, sorry, problem,
#   system, police, camera, film, music, class, station, workshop,
#   repair, professional, recording, actor, director, script, scene
#
# RULE 5 — NATURAL HINGLISH (not awkward hybrid)
#   GALAT ✗: "He was emotional type ka tha."
#   SAHI  ✓: "Woh bahut emotional kism ka insaan tha."
#
#   GALAT ✗: "Politics ka game khelna tha usse."
#   SAHI  ✓: "Use politics ka game khelna tha."
#
# ─────────────────────────────────────────────────────────────────
# MANDATORY PRE-OUTPUT SELF-CHECK (before writing ANY story output)
# ─────────────────────────────────────────────────────────────────
#
# STOP. Khud se yeh 5 sawaal poochho:
#   [ ] 1. Kya narration Hindi mein hai? (English paragraphs? → Rewrite)
#   [ ] 2. Kya har sentence complete hai? (subject + verb hai?)
#   [ ] 3. Kya sentences connectors se jude hain? (list nahi lag raha?)
#   [ ] 4. Kya forbidden English words hain? (replace karo)
#   [ ] 5. Kya Hinglish natural lag raha hai? (awkward nahi?)
#
# FAIL = RUKNA. REWRITE KARO. PHIR OUTPUT KARO.
# DO NOT output English story narration under any circumstances.
#
# ─────────────────────────────────────────────────────────────────
# ACCESSIBILITY TEST (apply to every paragraph)
# ─────────────────────────────────────────────────────────────────
# "Kya ek Delhi ka autowala ya Himachal ka kisan yeh samajhega?"
#   YES → Theek hai. Output karo.
#   NO  → Too formal ya too English. Rewrite karo.
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

## WORKFLOW 1: STORY SYNOPSIS — v11.0 (Format-First · Structure-First · Summary Approval)
**Trigger**: Any story/film/screenplay request — Movie OR Web Series OR Micro Drama OR Short Film
**Agent**: master-story-director.md → genre-specialist
**Reference**: `.bmad-film/workflows/development/story-synopsis.yaml` (v11.0)
**UNIFIED**: This is THE ONLY story workflow. web-series.yaml and micro-drama.yaml have been DELETED.
**Format is selected at STEP 1 — FIRST question. Structure at STEP 2.**

```
┌─────────────────────────────────────────────────────────────────┐
│          STEP SEQUENCE v11.0 (NEVER SKIP, NEVER REORDER)       │
├─────────────────────────────────────────────────────────────────┤
│ STEP 1 of 13 — Format Selection ← FIRST QUESTION              │
│   4 choices: Movie / Web Series / Micro Drama / Don't Know     │
│   Movie → ask duration (default: 120 min)                      │
│   Web Series → ask episode count + duration per ep             │
│     (defaults: 8 episodes × 30-45 min)                         │
│   Micro Drama → ask episode count + duration per ep            │
│     (defaults: 15 episodes × 5-7 min)                          │
│   Don't Know → auto-assign at STEP 13 from story DNA           │
│   Apply defaults silently if writer skips specifics            │
│                                                                 │
│ STEP 2 of 13 — Story Structure                                 │
│   A) 📏 LINEAR (chronological, sequential)                     │
│   B) 🌀 NON-LINEAR (time jumps, multiple perspectives)         │
│   C) 📋 FRAMEWORK from list:                                   │
│      1) Three-Act  2) Hero's Journey  3) Save the Cat          │
│      4) Bollywood Interval  5) Dan Harmon Circle               │
│      6) Kishōtenketsu  7) Sequence Approach                    │
│   D) 🤖 AUTO-ASSIGN (AI selects based on story DNA)            │
│   Default if skipped: AUTO-ASSIGN                              │
│                                                                 │
│ STEP 3 of 13 — Most Important Factor  [5 options]             │
│   Ask with 5 creative choices + "write your own":             │
│   A) 🌍 DUNIYA (World/Setting)                                 │
│   B) 👤 INSAAN (Character)                                     │
│   C) 🤝 RISHTA (Relationship)                                  │
│   D) ⚡ GHATNA (Plot/Events)                                   │
│   E) 💬 BAAT (Theme/Message)                                   │
│                                                                 │
│ STEP 4 of 13 — Factor-Specific Deep Dive                       │
│   • 3-4 questions based on STEP 3 answer                       │
│   • Each question has creative choices + "write your own"       │
│   • If World → W1-W4 (location, rules, unique detail, time)    │
│   • If Character → C1-C4 (wound, want/need, alone habit, contradiction)│
│   • If Relationship → R1-R4 (history, unsaid, crack, forced closeness)│
│   • If Plot → P1-P4 (turning point, audience knowledge, secret, intense)│
│   • If Theme → T1-T4 (personal origin, corrective truth, opposition, takeaway)│
│                                                                 │
│ STEP 5 of 13 — Genre + Feel                                    │
│   Ask with 8 evocative choices + "write your own":             │
│   A) 🔍 RAHASYA (Thriller/Suspense) — Ghosh/Raghavan           │
│   B) 💘 MOHABBAT (Romance) — Imtiaz Ali/Yash Chopra            │
│   C) 🔥 JUNG (Action/Adventure) — Shetty/Anand/Kashyap         │
│   D) 😂 MAZAK (Comedy) — Mukherjee/Hirani/Priyadarshan         │
│   E) 😢 ZINDAGI (Drama) — Roy/Gulzar/Sircar                    │
│   F) 👻 DARNA (Horror) — Barwe/Kaushik/Varma                   │
│   G) 🎵 SANGEET (Musical) — Farah/Bhansali/Johar               │
│   H) ⚖️ SAMAJ (Social Cinema) — Benegal/Masurkar/Anubhav       │
│   + Tone scale (dark ↔ light) + Genre mixing                    │
│                                                                 │
│ STEP 6 of 13 — Theme + Core Truth                              │
│   Ask with 8 theme choices + "write your own"                  │
│   + Theme opposition (open Q) + Audience takeaway (4 choices)  │
│                                                                 │
│ STEP 7 of 13 — Character Detailing                             │
│   7A: Primary character type (5 creative choices)              │
│   7B: Character's biggest fear (5 choices)                     │
│   7C: Secondary characters (open Q)                            │
│   7D: Want vs Need gap (open Q — must diverge)                 │
│                                                                 │
│ STEP 8 of 13 — Core Emotion                                    │
│   8A: Audience final emotion (6 choices — film-anchored)       │
│   8B: Protagonist's final state (open Q)                       │
│   8C: Overall emotional spine (open Q)                         │
│                                                                 │
│ STEP 9 of 13 — Core Conflict                                   │
│   9A: Internal conflict (5 choices)                            │
│   9B: External conflict (5 choices)                            │
│   9C: Antagonist perspective (open Q — great villains are right)│
│                                                                 │
│ STEP 10 of 13 — Milestones + Highpoints                       │
│   10A: First major turn (4 choices)                            │
│   10B: Darkest moment (4 choices)                              │
│   10C: Climax type (4 choices)                                 │
│   10D: Story's unique element (open Q — anti-generic)          │
│                                                                 │
│ STEP 11 of 13 — Opening + Ending + Language                    │
│   11A: Opening scene type (5 choices)                          │
│   11B: Ending type (6 choices)                                 │
│   11C: Anti-cliché guard (open Q — what NOT to include)        │
│   11D: Language Selection (6 options)                          │
│                                                                 │
│ STEP 12 of 13 — Story Summary Approval ← WRITER CHECKPOINT    │
│   AI generates ONE ~200-word story summary from ALL seeds      │
│   (covers STEPs 1-11: format, structure, world, protagonist,   │
│    opening, tension, turn, emotional landing, language)        │
│   Writer chooses:                                              │
│   ✅ A) APPROVE → go to STEP 13                               │
│   🔄 B) NAYA VARIANT → completely new summary (same seeds)    │
│   ✏️ C) FEEDBACK → refine specific element in current summary  │
│   NO LIMIT on iterations — loop until writer approves          │
│   ← GATE: STEP 13 only after writer explicitly approves ───── │
│                                                                 │
│ STEP 13 of 13 — Genre Routing + Full Story Creation            │
│   13A: Genre agent selected + announced                        │
│   13B: Genre-specific craft questions (5-8 only)              │
│   13C: Write from approved_summary blueprint (no passes)       │
│     • Use approved_summary from STEP 12 as blueprint          │
│     • Apply opening/ending/anti-cliché from STEP 11           │
│     • Apply language from STEP 11D                            │
│     • Apply structure from STEP 2                             │
│   13D: Write Continuous Narrative in story-synopsis.md + save: │
│     Flowing prose in chosen language — NO scene-wise breakdown │
│     (Scene breakdown belongs in beat-sheet, not synopsis)      │
│     ALL FORMATS → project/{name}/ (root)                      │
│   13E: Episode Files [Web Series / Micro Drama ONLY]:          │
│     Web Series → episodes/episode-NN/ FOLDERS                 │
│       Each folder: story-synopsis.md (+ later: beat-sheet,    │
│       screenplay, shot-breakdown, shot-breakdown-ai)           │
│     Micro Drama → episodes/episode-NN.md FLAT FILES           │
│       Each file: Story + Beat-Sheet + Screenplay + Shot Notes  │
│       (all-in-one — no subfolder — eps are 5-7 min)           │
│     Cliffhanger/Hook mandatory on each (except final ep)      │
└─────────────────────────────────────────────────────────────────┘
```

**HARD GATES (v11.0):**
- STEP 1 (Format) is ALWAYS the first question — NEVER skip or defer format
- STEP 11 (Opening+Ending+Language) MUST be completed before Story Summary at STEP 12
- STEP 12 MUST show ONE story summary — writer must explicitly APPROVE before STEP 13
- STEP 13 (Story Creation) CANNOT start before STEP 12 is approved
- STEP 13 story MUST follow approved_summary from STEP 12 — no deviations
- NO processing passes at STEP 13 — just write from blueprint
- STEP 13E (Episode Files) MUST run after story-synopsis.md is saved — IF format = Web Series OR Micro Drama
- Web Series: episode FOLDERS (`episodes/episode-NN/`) — full treatment per episode
- Micro Drama: episode FLAT FILES (`episodes/episode-NN.md`) — combined all-in-one (story + beats + screenplay + shots)
- character-bible and character-relations are ROOT-LEVEL ONLY — never per-episode
- ALL common docs (character-bible, beat-sheet, screenplay, etc.) go at project root — same as movie
- web-series.yaml and micro-drama.yaml have been DELETED — they no longer exist
- User says "just write it" → Still complete current step, then next
- NEVER offer "quick version" or "rough outline" — full workflow only
- EVERY question MUST include creative choices — bare open questions alone are not enough
- EVERY question MUST end with "Ya apne words mein:" option

---

## WORKFLOW 2: CHARACTER BIBLE
**Trigger**: User requests character bible (or next step after synopsis approved)
**Agent**: character-developer.md
**Reference**: `.bmad-film/workflows/development/character-bible.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 6 — Read Project Files                                │
│   READ FIRST (mandatory — before asking anything):             │
│   • project/{name}/genre-analysis.md                           │
│   • project/{name}/story-synopsis.md                           │
│   Extract: all characters, their roles, tone, genre            │
│                                                                 │
│ STEP 1 of 6 — CHARACTER FRAMEWORK SELECTION ← NEW             │
│   Show all 12 frameworks + Diagnostic option to writer         │
│   Writer picks: single framework OR combination                 │
│   Framework shapes ALL subsequent questions + output format     │
│   Reference: character-developer.md → STEP 1 section           │
│                                                                 │
│   12 Frameworks:                                                │
│   1. Egri's 3 Dimensions    7. Truby's 22 Blocks               │
│   2. McKee's True Character  8. Maslow's Hierarchy             │
│   3. Save the Cat Ghost      9. Stanislavski Method            │
│   4. Hauge's Inner Journey  10. Vogler's Character Web         │
│   5. Enneagram              11. Trauma-Informed Design         │
│   6. Jungian Archetypes     12. Bollywood Archetype            │
│   D. Diagnostic (5 questions → recommendation)                 │
│                                                                 │
│   DEFAULT (if skipped): Egri #1 + Ghost Method #3              │
│                                                                 │
│ STEP 2 of 6 — Dialect Setup (1 question only)                   │
│   Single dialect (Hindi default) or multi-dialect?             │
│   If multi-dialect: specify languages — AI handles rest        │
│                                                                 │
│ STEP 3 of 6 — Character Questions (streamlined)                 │
│   Base: Q1-Q15 (removed optional/redundant from 18 → 15)      │
│   + Framework extras: 4-6 additional questions (per selection) │
│   • Q1-Q7: Protagonist deep dive (removed actor ref Q8)        │
│   • Q9-Q13: Supporting characters (per character)              │
│   • Q14-Q15: Character dynamics (removed romantic Q15, Q17, Q18)│
│   • Q16+: Framework-specific questions                         │
│                                                                 │
│ STEP 4 of 6 — Synthesis + User Confirmation                     │
│   • Summarize all answers                                       │
│   • Confirm framework interpretation                            │
│   • Confirm before writing profiles                             │
│                                                                 │
│ STEP 5 of 6 — Profile Creation (Framework-Adapted)             │
│   • Write full profiles using CHOSEN FRAMEWORK's structure      │
│   • Principal: Full depth per framework sections                │
│   • Supporting: Depth per Q13 + framework essentials           │
│   • Output format varies by framework (see character-developer) │
│                                                                 │
│ STEP 6 of 6 — QA + Finalize                                    │
│   • Verify profiles match chosen framework + writer's answers   │
│   • Verify Hindi language compliance                            │
│   • Save: project/{name}/character-bible.md                    │
└─────────────────────────────────────────────────────────────────┘
```

**HARD GATES (Character Bible):**
- STEP 1 (Framework Selection) CANNOT be skipped — minimum ask must happen
- If user skips: Apply DEFAULT (Egri #1 + Ghost #3) and tell user
- STEP 3 (Questions) only after framework confirmed
- STEP 5 (Profile Creation) only after STEP 4 synthesis confirmed
- CHARACTER RELATIONS MAP must be run after Character Bible before Screenplay

---

## WORKFLOW 2.5: CHARACTER RELATIONS MAP
**Trigger**: After Character Bible approved — BEFORE Beat Sheet or Screenplay
**Agent**: character-relations-mapper.md
**Reference**: `.bmad-film/agents/character-relations-mapper.md`

```
┌─────────────────────────────────────────────────────────────────┐
│              STEP SEQUENCE (NEVER SKIP)                         │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 5 — Read ALL Project Files                            │
│   READ (mandatory — before asking anything):                    │
│   • project/{name}/genre-analysis.md                           │
│   • project/{name}/story-synopsis.md                           │
│   • project/{name}/character-bible.md                          │
│   Extract: ALL characters, their roles, all relationships       │
│                                                                 │
│ STEP 1 of 5 — Relationship Pair Identification                  │
│   • Identify ALL meaningful relationship pairs                  │
│   • Categorize: Core / Major / Supporting / Background          │
│   • Show list to user and confirm                               │
│                                                                 │
│ STEP 2 of 5 — Relationship Deep Questions (per pair)            │
│   Core + Major pairs: 8 questions each                          │
│   Q1: History (what happened before the story)                  │
│   Q2: Relationship DNA (what they actually ARE to each other)   │
│   Q3: Power Dynamic (who holds it, does it shift, when)         │
│   Q4: Want vs Need (conscious vs unconscious per character)     │
│   Q5: The Unsaid (what's never spoken, lives in every scene)    │
│   Q6: Subtext Signature (recurring gesture/word/silence)        │
│   Q7: Transformation Arc (beginning → trigger → end)           │
│   Q8: The Defining Scene (one scene that defines this forever)  │
│   Supporting pairs: Q1 + Q3 + Q5 + Q7 only (4 questions)      │
│                                                                 │
│ STEP 3 of 5 — Synthesis + User Confirmation                     │
│   • Summarize each relationship's core dynamic                  │
│   • Identify power web, emotional web, subtext web              │
│   • Confirm before writing                                      │
│                                                                 │
│ STEP 4 of 5 — Character Relations Map Creation                  │
│   • Write full relations map (all pairs)                        │
│   • Include: Power Map table + Subtext Web table                │
│   • Format-specific notes (movie/series/micro)                  │
│   • Language: Bollywood Hindi                                   │
│   • Save: project/{name}/character-relations.md                │
│                                                                 │
│ STEP 5 of 5 — QA + Finalize                                    │
│   • Verify all pairs mapped with all dimensions                 │
│   • Verify Hindi language compliance                            │
│   • Confirm: "Screenplay ab shuru ho sakta hai"                 │
└─────────────────────────────────────────────────────────────────┘
```

**WHY THIS STEP EXISTS:**
Every scene between two characters is powered by their invisible history,
their power dynamic, and what's never been said. Character Relations Map
makes this invisible architecture visible for the dialogue writer, director,
and shot breakdown specialist. Without it, scenes have surface action but
no subtext. With it, every scene carries the weight of the entire relationship.

**HARD GATES (Character Relations):**
- CANNOT start without approved character-bible.md
- Screenplay CANNOT start without approved character-relations.md
- Beat Sheet SHOULD read character-relations.md before creating emotional beats

---

## WORKFLOW 3: BEAT SHEET
**Trigger**: User requests beat sheet
**Agent**: beat-sheet-specialist.md
**Reference**: `.bmad-film/workflows/development/beat-sheet.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 5 — Read Project Files                                │
│   READ (mandatory — before asking anything):                    │
│   • project/{name}/genre-analysis.md                           │
│   • project/{name}/story-synopsis.md                           │
│   • project/{name}/character-bible.md                          │
│   Extract: protagonist arc, genre, tone, format                 │
│                                                                 │
│ STEP 1 of 5 — BEAT FRAMEWORK SELECTION ← NEW                   │
│   Show all 12 frameworks + Diagnostic option to writer          │
│   Writer picks: single framework OR combination                 │
│   Framework shapes ALL subsequent beats + output format         │
│   Reference: beat-sheet-specialist.md → STEP 1 section         │
│                                                                 │
│   12 Frameworks:                                                │
│   1. Save the Cat 15 Beats   7. Sequence Approach (8)          │
│   2. Hero's Journey 12 Stages 8. Fichtean Curve                │
│   3. Three-Act Beat Map       9. Story Grid Obligatory          │
│   4. Dan Harmon Story Circle  10. Emotional Beat Mapping        │
│   5. Bollywood Interval       11. Kishōtenketsu (4 Parts)       │
│   6. Seven-Point Structure    12. Parallel Beat Tracking        │
│   D. Diagnostic (5 questions → recommendation)                  │
│                                                                 │
│   DEFAULT (if skipped): Save the Cat #1 + Emotional Mapping #10 │
│                                                                 │
│ STEP 2 of 5 — Beat Questions (5 Questions)                      │
│   Structure type + Opening hook read from story-synopsis.md    │
│   Transitions handled by AI — no writer input needed           │
│   Base Q1-Q5 (framework shapes focus)                          │
│   + Framework-specific extras (3-4 additional Qs per framework) │
│   • Q1: Pacing rhythm                                           │
│   • Q2-Q3: Emotional highs + lows                              │
│   • Q4: Climax emotion                                          │
│   • Q5: Beat granularity (macro/moderate/micro)                │
│                                                                 │
│ STEP 3 of 5 — Beat Architecture                                 │
│   • Map writer's answers to selected framework's beat structure  │
│   • Bollywood: song beats + interval moment included            │
│   • Confirm emotional arc before writing                        │
│                                                                 │
│ STEP 4 of 5 — Beat Sheet Creation (Framework-Adapted)          │
│   • Write beat map using CHOSEN FRAMEWORK's structure           │
│   • Output format varies by framework (see beat-sheet-specialist)│
│   • Language: Bollywood Hindi                                   │
│                                                                 │
│ STEP 5 of 5 — QA + Finalize                                    │
│   • Verify framework beats all present                          │
│   • Verify emotional arc clear (start → end transformation)     │
│   • Verify Hindi language compliance                            │
│   • Save: project/{name}/beat-sheet.md                         │
└─────────────────────────────────────────────────────────────────┘
```

**HARD GATES (Beat Sheet):**
- STEP 1 (Framework Selection) CANNOT be skipped — minimum ask must happen
- If user skips: Apply DEFAULT (Save the Cat #1 + Emotional Mapping #10) and tell user
- STEP 4 (Beat Creation) only after STEP 3 architecture confirmed

---

## WORKFLOW 4: SCREENPLAY
**Trigger**: User requests screenplay (after character-bible approved)
**Agent**: screenplay-structure-writer.md → dialogue-writer.md
**Reference**: `.bmad-film/workflows/development/screenplay.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 6 — Read ALL Project Files                            │
│   READ (mandatory):                                             │
│   • genre-analysis.md + story-synopsis.md                      │
│   • character-bible.md + character-relations.md (CRITICAL)     │
│   • beat-sheet.md                                               │
│   • Detect dialect setup from character-bible                   │
│   • Load relationship subtext web from character-relations.md  │
│                                                                 │
│ STEP 1 of 6 — SCREENPLAY APPROACH FRAMEWORK ← NEW              │
│   Screenplay Structure Writer presents 12 approach frameworks   │
│   Writer picks: writing approach for scene construction         │
│   Reference: screenplay-structure-writer.md → STEP 1 section   │
│                                                                 │
│   12 Approaches:                                                │
│   1. Hollywood Spec       7. Short Film Economy                 │
│   2. Bollywood Interval   8. Non-Linear Format                  │
│   3. Visual-Forward       9. Ensemble Format                    │
│   4. Dialogue-Forward    10. Voice-Over/Narration               │
│   5. Emotional-Arc       11. Documentary Hybrid                 │
│   6. Genre Template      12. Micro-Drama Format                 │
│   D. Diagnostic                                                 │
│   DEFAULT: Hollywood Spec #1 + Emotional-Arc #5                 │
│                                                                 │
│ STEP 2 of 6 — DIALOGUE STYLE FRAMEWORK ← NEW                   │
│   Dialogue Writer presents 12 style frameworks                  │
│   Writer picks: dialogue voice + texture                        │
│   Reference: dialogue-writer.md → STEP 1 section               │
│                                                                 │
│   12 Styles:                                                    │
│   1. Gulzar Poetic           7. Shoojit Sircar Silent           │
│   2. Hrishikesh Conversational 8. Genre-Coded                   │
│   3. Anurag Kashyap Raw      9. Subtext-Forward                 │
│   4. Rajkumar Hirani Wit    10. Dialect-Specific                │
│   5. Bimal Roy Minimalist   11. Bollywood Commercial            │
│   6. Imtiaz Ali Philosophical 12. Character-Voice Design        │
│   D. Diagnostic                                                 │
│   DEFAULT: Hrishikesh Conversational #2 + Subtext-Forward #9   │
│                                                                 │
│ STEP 3 of 6 — Screenplay + Dialogue Questions (9 total)        │
│   Opening/closing read from story-synopsis.md STEP 11A/11B     │
│   Pacing + emotional beats read from beat-sheet.md             │
│   Language ratio + dialect read from story-synopsis + char-bible│
│   • Q1-Q6: Structure (visual balance, scene length, subtext,    │
│             transitions, must-have scenes, montages)            │
│   • Q7-Q9: Dialogue (formality, memorable lines, density)      │
│   + Framework-specific extras from both selected approaches     │
│                                                                 │
│ STEP 4 of 6 — Structure Draft (Screenplay Structure Writer)     │
│   • Scene headings, action lines, placeholder dialogue          │
│   • Framework approach applied to scene construction            │
│   • Save: screenplay-structure.md                               │
│                                                                 │
│ STEP 5 of 6 — Dialogue Pass (Dialogue Writer)                   │
│   • Replace placeholder dialogue with final impactful lines     │
│   • Selected dialogue style framework applied throughout        │
│   • Genre-appropriate voices (Bollywood masters style)          │
│                                                                 │
│ STEP 6 of 6 — Final Screenplay                                  │
│   • Save: project/{name}/screenplay.md                         │
│   • Credits: "Screenplay by X, Dialogues by Y"                 │
└─────────────────────────────────────────────────────────────────┘
```

**HARD GATES (Screenplay):**
- STEP 1 (Screenplay Framework) CANNOT be skipped — minimum ask must happen
- STEP 2 (Dialogue Framework) CANNOT be skipped — separate from STEP 1
- STEP 4 only after STEP 3 questions complete
- STEP 5 only after STEP 4 structure draft approved
- Both framework defaults apply if skipped — tell user which defaults used

---

## WORKFLOW 5: SHOT BREAKDOWN
**Trigger**: User requests shot breakdown (after screenplay approved)
**Agents**: shot-breakdown-specialist.md + ai-shot-breakdown-specialist.md
**Reference**: `.bmad-film/workflows/pre-production/shot-breakdown.yaml`
**Output**: TWO documents — traditional + AI generation breakdown

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 5 — Read ALL Project Files                            │
│   READ (mandatory):                                             │
│   • genre-analysis.md + story-synopsis.md                      │
│   • character-bible.md + beat-sheet.md + screenplay.md         │
│                                                                 │
│ STEP 1 of 5 — VISUAL GRAMMAR FRAMEWORK                         │
│   Shot Breakdown Specialist presents 12 visual frameworks       │
│   Writer/Director picks: cinematography approach                │
│   Framework shapes ALL shot choices + visual language           │
│   Reference: shot-breakdown-specialist.md → STEP 1 section     │
│                                                                 │
│   12 Visual Frameworks:                                         │
│   1. Classical Coverage     7. Color/Light Driven               │
│   2. Auteur Visual Grammar  8. Montage-Based                    │
│   3. Bollywood Visual Lang  9. Mise-en-Scène                    │
│   4. Handheld/Naturalistic 10. Single-Take Sequence             │
│   5. Static/Contemplative  11. Symbolic/Poetic Visual           │
│   6. Genre-Coded Visual    12. Economical Coverage              │
│   D. Diagnostic                                                 │
│   DEFAULT: Classical Coverage #1 + Genre-Coded Visual #6       │
│                                                                 │
│ STEP 2 of 5 — ALL Questions                                     │
│   Transitions read from screenplay.md — no re-asking           │
│   PART A — Traditional Questions (Q1-Q12, trimmed from 15):    │
│   • Q1-Q4: Visual style (tone, movement, size, lighting)        │
│   • Q5-Q8: Coverage (ref films, signature shots, coverage, CUs) │
│   • Q9-Q12: Production reality (equipment, crew, locations, time)│
│   + Framework-specific extras per selected visual approach      │
│                                                                 │
│   PART B — AI Platform Questions (Q16-Q20):                    │
│   • Q16: AI video platform (Veo3/Nano Banana/Runway/Pika)      │
│   • Q17: AI image tool (Midjourney/Flux/DALL-E/Firefly)        │
│   • Q18: Shot duration (2-4s / 4-8s / 8-15s / scene-dependent)│
│   • Q19: Character consistency (ref image/descriptive/LoRA)    │
│   • Q20: Visual style override (default ultra-realistic/custom) │
│   DEFAULT: Veo3 + scene-dependent + descriptive + keep default  │
│                                                                 │
│ STEP 3 of 5 — Traditional Shot Breakdown                        │
│   • Shot-by-shot shooting script (industry format)              │
│   • Selected visual grammar + Q1-Q15 answers applied           │
│   • Save: project/{name}/shot-breakdown.md                     │
│   • Equipment requirements + production notes + shooting order  │
│                                                                 │
│ STEP 4 of 5 — AI Shot Breakdown                                 │
│   Agent: ai-shot-breakdown-specialist.md                        │
│   • 18-field entry per shot — ALL fields mandatory              │
│   • Hyper-detailed environment + character + action             │
│   • Platform-specific paste-ready AI INSTRUCTIONS per shot     │
│   • Dialogue in Devanagari (for lip-sync accuracy)             │
│   • Character anchors for consistency across shots              │
│   • Explicit REALISM CONSTRAINTS per shot                      │
│   • Save: project/{name}/shot-breakdown-ai.md                  │
│                                                                 │
│ STEP 5 of 5 — QA Both Files + Final Confirm                    │
│   • Traditional breakdown completeness check                    │
│   • AI breakdown 18-field completeness check                    │
│   • Character consistency check (anchors identical)            │
│   • Both files confirmed + announced to user                   │
└─────────────────────────────────────────────────────────────────┘
```

**DELIVERABLES (Shot Breakdown Workflow)**:
```
project/{name}/shot-breakdown.md     ← Traditional (for directors, DPs, set)
project/{name}/shot-breakdown-ai.md  ← AI generation (Veo3, Nano Banana, Runway, Pika)
```

**18-FIELD AI SHOT STRUCTURE** (every entry in shot-breakdown-ai.md):
```
SHOT NO. | SHOT TYPE/SCALE | LOCATION | TIME & DAY |
ENVIRONMENT & SET DETAIL | CHARACTERS IN FRAME |
CHARACTER ACTION | FACIAL EXPRESSION & BODY LANGUAGE |
DIALOGUE (Devanagari) | CORE VOICE TONE |
CAMERA MOVEMENT | CAMERA SPECS | LIGHTING |
COLOR & TONE RULE | AUDIO/SFX | MOOD & SUBTEXT |
REALISM CONSTRAINTS | AI INSTRUCTIONS (platform-optimized)
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

### 4. Seed Phase Before Creation Phase — 40/60 MODEL
- 40% from writer: 12 deep seeds (Main Q + Depth Probe each) — STEP 1
- AI Architecture Proposal from seeds — STEP 1b (60% creative contribution)
- Writer calibrates proposal — STEP 1c (completes writer's 40%)
- Story creation ONLY after STEP 1 + 1b + 1c complete — then STEP 9A/9B/9C
- Character Bible ONLY after synopsis approved
- Screenplay ONLY after character-bible approved
- Shot Breakdown ONLY after screenplay approved
- Depth Probe is MANDATORY — surface answers = incomplete seeds = generic risk

### 5. Story Synopsis = Continuous Narrative ONLY
Story Synopsis produces ONE format: flowing prose narrative.
Scene-by-Scene Breakdown belongs in the Beat Sheet — NOT the synopsis.
No exceptions.

### 6. Language Default — GLOBAL LANGUAGE LAW (See top of this file)
- DEFAULT = Simple Bollywood Hindi (60-70% Hindi + 30-40% natural English)
- Complete sentences only — subject + verb mandatory in every sentence
- Natural connectors required — sentences must flow, not feel like a list
- Forbidden formal English — use Hindi equivalents (see top of this file)
- Pre-output self-check is MANDATORY before writing any story content
- Regional dialect only when user explicitly specifies
- English ONLY allowed for: scene headings, character names, place names, technical film terms

### 7. Creative Elevation Mandate — APPLIES TO ALL OUTPUT STEPS
**AI is a creative collaborator, not a transcriptionist.**

Every output creation step (story, character, beats, screenplay, shots) must follow:

- **WHERE WRITER WAS SPECIFIC**: Honor it exactly. Then build outward — add the specific image, the unexpected word, the sensory detail that makes it cinematic.
- **WHERE WRITER WAS VAGUE**: AI makes the most cinematically interesting, specific, original choice — never the generic default.
- **WHERE WRITER SKIPPED**: AI decides — always the choice only THIS story could have.

**SPECIFICITY TEST** (mandatory before saving any output):
"Could any element of this output belong to a different film with the same genre?"
If YES → make it more specific until only THIS story fits.

**DEPENDENCY CHAIN** (each step builds on all previous):
Story Synopsis → feeds → Character Bible → feeds → Beat Sheet → feeds → Screenplay → feeds → Shot Breakdown
Every step must explicitly read and build on all previous outputs.
Consistency across all outputs is non-negotiable.

**QUALITY FLOOR**: Every output should match the craft standard of the genre masters each agent is trained on. That is the minimum, not the target.

---

---

## REVISION PROTOCOL — WHAT HAPPENS WHEN WRITER SAYS NO

*Rejection is not failure — it's information. Every "nahi" is a direction.*

### WHEN WRITER REJECTS THE STORY (after STEP 9C):

**TRIAGE — ask immediately:**
"Kya aapko story ka:
  a) Direction pasand nahi (galat rasta gaya)
  b) Protagonist pasand nahi (character feel nahi hua)
  c) Ending pasand nahi (resolution sahi nahi lagi)
  d) Tone pasand nahi (feel match nahi ki)
  e) Sab kuch wrong hai (seeds se shuru karte hain)"

**BASED ON ANSWER:**

TYPE A (Direction): Return to STEP 9B (Diverge Before Converge) → show remaining 2 directions → do NOT rerun all 12 seeds

TYPE B (Protagonist): Re-run S5 (Want/Need) + S6 (Core Relationship) + Depth Probes → re-run STEP 1b with updated seeds → proceed to 9A/9B/9C

TYPE C (Ending): Re-run S9 (Last Image) + S3 (Last Feeling) → redesign conclusion only → rewrite ending (keep Act 1/2 architecture)

TYPE D (Tone): Re-run S10 (Feel Reference) + S11 (What NOT to have) → re-run genre questions with new tone → rewrite full story (architecture stays)

TYPE E (Full): Return to STEP 1 → ask writer: "Kya pehle seeds mein se kuch sach tha?" → keep correct seeds, rerun rest → full path: 1 → 1b → 1c → 7 → 8 → 9A/9B/9C

---

### WHEN WRITER REJECTS CHARACTER (after Character Bible STEP 5):

TYPE A (Psychology wrong): Re-run Q1-Q8 with specific correction
TYPE B (Voice wrong): Re-run STEP 2 (Dialect Setup) → rewrite dialogue samples only
TYPE C (Arc wrong): Re-run Q14-Q18 (dynamics/arc Qs) → rewrite character's journey section
TYPE D (Relationships wrong): Return to Character Relations Map — re-run affected pair questions

---

### WHEN WRITER REJECTS SCREENPLAY:

TYPE A (Structure wrong): Re-run STEP 1 (Screenplay Approach Framework) — different approach may be needed
TYPE B (Dialogue wrong): Return to STEP 5 (Dialogue Pass) — re-run or try alternate dialogue style
TYPE C (Pacing wrong): Apply Pacing Architecture audit → targeted scene rewrites
TYPE D (Key scene missing): Identify from beat-sheet.md → write and insert → run subtext tracking on new scene

---

### UNIVERSAL REVISION RULES:
→ Never delete seed answers — revised answers ADD to original seeds
→ Rejected output = NEGATIVE SEED: "Story ne yeh direction liya — woh wrong tha"
→ Negative seeds are as valuable as positive seeds — eliminate wrong paths
→ Maximum 3 full revisions per workflow stage — if 3rd revision also rejected → full diagnostic: "Kya zaroori information missing hai?"
→ Revision does NOT restart step count — returns to specific step, completes it, continues forward

---

## CROSS-WORKFLOW DRIFT PREVENTION

*Files ek doosre ke saath sync mein rehne chahiye. Drift = inconsistent story.*

### WHAT IS DRIFT:
When a character, relationship, or story element changes in a later workflow (screenplay) without earlier workflow files (character-bible, story-synopsis) being updated.
Result: character-bible says one thing, screenplay does another.

### DRIFT TRIGGERS (watch for):
→ Writer says "make this character more [quality]" during screenplay session
→ A scene contradicts established world rules (from story-synopsis)
→ A relationship changes significantly from character-relations.md
→ Ending changes from what story-synopsis.md describes

### DRIFT DETECTION:

**AT SCREENPLAY STEP 0 (before starting):**
→ Read character-bible.md → list every character's core want, wound, voice
→ Compare to story-synopsis.md character descriptions
→ Discrepancy found → flag to writer: "Character X mein inconsistency hai — kaunsa sahi maana jaye?"
→ Resolve before screenplay begins

**AFTER SCREENPLAY STEP 4 (Structure Draft):**
→ For each major character: do their actions match character-bible psychology?
→ For each relationship: does scene dynamic match character-relations.md power map?
→ Scene where character acts out of character (without arc reason) = drift → flag and fix

**AFTER SCREENPLAY STEP 5 (Dialogue Pass):**
→ Mini Blind Voice Test: does each character's dialogue sound like their character-bible voice?
→ Mismatch → revise before final

### DRIFT RESOLUTION:
**OPTION A — Update earlier file:** Character genuinely evolved → update character-bible.md
**OPTION B — Fix later file:** Change was a mistake → rewrite scene to match character-bible
**OPTION C — Document evolution:** Add "CHARACTER EVOLUTION NOTE" in character-bible.md

### SOURCE OF TRUTH HIERARCHY:
- story-synopsis.md = SOURCE OF TRUTH for story
- character-bible.md = SOURCE OF TRUTH for characters
- character-relations.md = SOURCE OF TRUTH for relationships
When in conflict → ask writer which version is correct → update ALL files to match

---

## QUICK TRIGGER REFERENCE (v9.0 — SINGLE STORY WORKFLOW)

| User Says | Workflow | First Step |
|-----------|----------|------------|
| "story banao", "ek kahani", "write a story", "film concept", "ek idea hai", "suno ek kahani" | **Story Synopsis v9.0** (Unified) | STEP 0 — Concept Mining |
| "web series banao", "multi-episode series" | **Story Synopsis v9.0** (Unified — format at STEP 12) | STEP 0 — Concept Mining |
| "micro drama", "short episodes", "vertical series" | **Story Synopsis v9.0** (Unified — format at STEP 12) | STEP 0 — Concept Mining |
| "short film banao", "5 min story" | **Story Synopsis v9.0** (Unified — format at STEP 12) | STEP 0 — Concept Mining |
| "character bible", "characters develop karo" | Character Bible | STEP 0 — Read Files |
| "character relations", "relationships map karo", "rishta map" | Character Relations Map | STEP 0 — Read Files |
| "beat sheet banao", "beats dikhao" | Beat Sheet | STEP 0 — Read Files |
| "screenplay likho", "script banao" | Screenplay | STEP 0 — Read Files (including character-relations.md) |
| "shot breakdown", "shots plan karo" | Shot Breakdown | STEP 0 — Read Files → Both traditional + AI breakdown |

**NOTE (v9.0)**: Movie, Web Series, and Micro Drama ALL use the SAME Story Synopsis v9.0 workflow.
Format selection happens at **STEP 12** — after the brief synopsis is approved by the writer.
NEVER route "web series banao" or "micro drama" to separate workflows. Those are DEPRECATED.

---

*Reference this file whenever a workflow is triggered to ensure correct step sequence.*
*If in doubt about which step you're on — announce the step to the user to confirm.*
