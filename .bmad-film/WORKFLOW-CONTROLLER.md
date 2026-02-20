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

## WORKFLOW 1: STORY SYNOPSIS
**Trigger**: Any story/film/screenplay request
**Agent**: master-story-director.md → genre-specialist → format-selector
**Reference**: `.bmad-film/workflows/development/story-synopsis.yaml`

```
┌─────────────────────────────────────────────────────────────────┐
│                 STEP SEQUENCE (NEVER SKIP)                      │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 9 — Format Selection                                  │
│   • What are you making?                                         │
│     1. Movie (Feature Film)                                      │
│     2. Web Series (Multi-Episode)                                │
│     3. Micro Drama (Multi-Episode)                               │
│   • After selection: ask format-specific follow-up questions    │
│     Movie → runtime, release, approach                          │
│     Web Series → episode count, duration, episodic/serialized   │
│     Micro Drama → episode count, duration, vertical/horizontal  │
│   • Which story structure? (Three-Act/Hero's Journey/etc.)      │
│   • Structure-specific writer questions (format-selector.md)    │
│                                                                 │
│ STEP 1 of 9 — Core Seed Questions (12 Deep Seeds)               │
│   40/60 MODEL: Writer gives 12 seeds, AI builds 60% from them  │
│   • Concept Mining first (3-5 threads from writer's words)      │
│   • Then 12 seeds in 3 groups (Main Q + Depth Probe each)       │
│   GROUP 1 — WHY + CORE (S1-S4):                                │
│     S1: Personal origin — kab se, woh exact moment kya tha     │
│     S2: First image — visual + light/sound depth probe         │
│     S3: Last feeling — emotional destination + personal connect │
│     S4: Uncomfortable truth — what's missing without it        │
│   GROUP 2 — WHO + RELATIONSHIP (S5-S8):                        │
│     S5: Want vs need — + wound origin moment depth probe        │
│     S6: Core relationship — + first meeting feel + divergence   │
│     S7: The unsaid — + unspeakable sentence depth probe         │
│     S8: The one decision — + where, alone/together, sensory     │
│   GROUP 3 — LANDING + TONE (S9-S12):                           │
│     S9: Last image — + contrast with S2 depth probe            │
│     S10: Feel reference — + specific scene described            │
│     S11: What NOT to have — + feeling to avoid                 │
│     S12: Unexpected element + subtext sentence — + origins     │
│   Depth Probe MANDATORY after every seed — no exceptions       │
│                                                                 │
│ STEP 1b — AI Architecture Proposal (runs after STEP 1)         │
│   • PASS 0: Seed Traceability (every element traced to S1-S12) │
│   • AI generates: Character psychology (from S5 depth probe)   │
│     World details (from S2/S4), Relationship blueprint (S6/S7) │
│     Story spine (S8/S9), Subtext layer (S12), Tone (S10)       │
│   • Each element shown with its seed source                    │
│   • Show full proposal to writer for calibration               │
│                                                                 │
│ STEP 1c — Writer Reaction Protocol (40% calibration)           │
│   • Writer reacts to each element: theek hai / wrong / change  │
│   • AI adjusts based on reactions                              │
│   • Confirmed architecture synthesized from:                   │
│     seeds + AI proposal + writer reactions                     │
│   • Pass confirmed architecture to genre specialist            │
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
│                                                                 │
│   STEP 9A — Anti-Pattern Reveal (MANDATORY BEFORE WRITING):    │
│   • Show user 3 predictable versions being avoided:            │
│     ❌ Version 1: [generic trap 1]                              │
│     ❌ Version 2: [generic trap 2]                              │
│     ❌ Version 3: [generic trap 3]                              │
│   • State: "Ab 4th version likh raha hoon."                    │
│                                                                 │
│   STEP 9B — Diverge Before Converge (MANDATORY BEFORE WRITING):│
│   • Present 3 radically different directions from SAME answers:│
│     🔵 Direction A — [dark/character-driven] — from Q2/Q19    │
│     🟡 Direction B — [plot/twist-driven] — from Q10b-Q10e     │
│     🔴 Direction C — [quiet/subtext-driven] — from Q23/Q23a   │
│   • Writer RECOGNIZES direction (not chooses) → lock it        │
│   • Hybrid allowed: "A ka X element + C ka Y element"          │
│                                                                 │
│   STEP 9C — Write Story (after 9A + 9B complete):             │
│   • Write BOTH formats in story-synopsis.md:                    │
│     1. Continuous Narrative (flowing Hindi prose)               │
│     2. Scene-by-Scene Breakdown (technical production version)  │
│   • Language: Simple Bollywood Hindi (60-70% Hindi)             │
│   • Save: project/{project_name}/story-synopsis.md             │
└─────────────────────────────────────────────────────────────────┘
```

**HARD GATES:**
- Cannot reach STEP 9 without completing STEPS 0-8
- Cannot write story (STEP 9C) without completing 9A (Anti-Pattern Reveal) + 9B (Diverge Before Converge)
- User says "just write it" → Still complete current step, then next
- Never offer "quick version" or "rough outline" — full workflow only
- STEP 9A: 3 avoided versions MUST be shown to user — internal-only is a violation
- STEP 9B: Direction must be confirmed by writer — never assume direction

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
│ STEP 2 of 6 — Dialect Setup                                     │
│   Ask: Single dialect (Bollywood Hindi) or character-specific? │
│   If character-specific: dialect per character                  │
│                                                                 │
│ STEP 3 of 6 — Deep Character Questions                          │
│   Base: Q1-Q18 (always asked)                                   │
│   + Framework extras: 4-6 additional questions (per selection) │
│   • Q1-Q8: Protagonist deep dive                                │
│   • Q9-Q13: Supporting characters (per character)              │
│   • Q14-Q18: Character dynamics                                 │
│   • Q19-Q24: Framework-specific questions                       │
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
│ STEP 2 of 5 — Beat Questions (8 Questions)                      │
│   Base Q1-Q8 (always asked, framework shapes focus)             │
│   + Framework-specific extras (3-4 additional Qs per framework) │
│   • Q1-Q3: Core change + emotional arc (start → end)           │
│   • Q4-Q6: Turning points + lowest point + recovery             │
│   • Q7-Q8: Climax + final image                                 │
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
│ STEP 3 of 6 — Screenplay + Dialogue Questions                   │
│   Framework-shaped questions (both approaches applied)          │
│   • Q1-Q10: Structure Writer (style, pacing, scenes)            │
│   • Q11-Q15: Dialogue Writer (language, voice, lines)           │
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
│   PART A — Traditional Questions (Q1-Q15):                     │
│   • Q1-Q7: Visual style (tone, movement, size, lighting)        │
│   • Q8-Q11: Coverage strategy                                   │
│   • Q12-Q15: Production reality (equipment, crew, time)         │
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

## WORKFLOW 6: WEB SERIES
**Trigger**: User selects "Web Series" or "Multi-Episode Series" format
**Reference**: `.bmad-film/workflows/development/web-series.yaml`
**Architecture**: TWO-LEVEL (Season Level + Episode Level)

```
┌─────────────────────────────────────────────────────────────────┐
│   LEVEL 1: SEASON — Run Once Before Any Episode Work            │
├─────────────────────────────────────────────────────────────────┤
│ STEP 0 of 12 — Series Concept Intake                            │
│   • Standard story questions (Phase A-E from Story Synopsis)    │
│   • PLUS Series-specific: Episode count, platform, audience     │
│   • PLUS: What question does the WHOLE SEASON answer?           │
│                                                                 │
│ STEP 1 of 12 — Season Format Selection                          │
│   • How many episodes? (4/6/8/10/13/other)                     │
│   • Episode duration? (20-30 min / 40-50 min / 60+ min)        │
│   • Platform? (OTT/YouTube/Television)                          │
│   • Season structure? (Mid-season break? Arc structure?)        │
│                                                                 │
│ STEP 2 of 12 — Season Story Structure Questions (15 Qs)         │
│   Element Treatment for Series:                                 │
│   CHARACTER: How does protagonist transform across the season?  │
│   RELATIONSHIP: Which relationships form the season's web?      │
│   EMOTION: Episode emotional peaks + season-level crescendo     │
│   PLOT: Season arc (big story) + episode arcs (small stories)   │
│   WORLD: What world rules are revealed gradually across eps?    │
│   CONFLICT: Season-spanning external + internal conflict        │
│   THEME: One theme, explored from multiple angles per episode   │
│   SUBTEXT: Season-level unsaid that everything points toward    │
│                                                                 │
│ STEP 3 of 12 — Season Bible Creation                            │
│   Save: project/{name}/season-bible.md                         │
│   Contents:                                                     │
│   • The One Question This Season Answers (thematic)            │
│   • World Rules (stays consistent across all episodes)          │
│   • Season Arc (start state of world → end state)              │
│   • Character Arc Map (every character: start → end, season)   │
│   • Relationship Evolution Map (which relationships shift, ep)  │
│   • Emotional Calendar (what audience feels at end of each ep)  │
│                                                                 │
│ STEP 4 of 12 — Character Bible                                  │
│   Standard Character Bible workflow (Workflow 2)                │
│   PLUS: Series-specific — character arc across all episodes     │
│                                                                 │
│ STEP 5 of 12 — Character Relations Map                          │
│   Standard Relations Map (Workflow 2.5)                         │
│   PLUS: Episode-by-episode relationship evolution table         │
│   Which episode does each relationship shift? What triggers it? │
│                                                                 │
│ STEP 6 of 12 — Episode Map Creation                             │
│   Save: project/{name}/episode-map.md                          │
│   One paragraph per episode — visible all at once:             │
│   • A-Story (episode's own story — completes within episode)   │
│   • B-Story (season arc advancement — may not resolve)          │
│   • Emotional Button (what audience feels at end of episode)    │
│   • Cliffhanger/Hook for next episode                          │
│   • Season Arc Checkpoint (does this episode advance big story?)│
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│   LEVEL 2: EPISODE — Runs Per Episode                           │
├─────────────────────────────────────────────────────────────────┤
│ STEP 7 of 12 — Episode Synopsis (per episode)                   │
│   Structure per episode:                                        │
│   • Cold Open: Hook within 90 seconds                           │
│   • A-Story: Episode's complete story                           │
│   • B-Story: Season arc thread                                  │
│   • Episode Climax                                              │
│   • Cliffhanger or emotional button                             │
│   Save: project/{name}/episode-{XX}/synopsis.md               │
│                                                                 │
│ STEP 8 of 12 — Episode Beat Sheet (per episode)                 │
│   Standard Beat Sheet workflow per episode                      │
│   Save: project/{name}/episode-{XX}/beat-sheet.md             │
│                                                                 │
│ STEP 9 of 12 — Episode Screenplay (per episode)                 │
│   Standard Screenplay workflow per episode                      │
│   Read character-relations.md for current episode's dynamics   │
│   Save: project/{name}/episode-{XX}/screenplay.md             │
│                                                                 │
│ STEP 10 of 12 — Episode Shot Breakdown (per episode)            │
│   Standard Shot Breakdown per episode                           │
│   Save: project/{name}/episode-{XX}/shot-breakdown.md         │
│                                                                 │
│ STEP 11 of 12 — Episode Completion Check                        │
│   • Does this episode advance season arc?                       │
│   • Is emotional calendar entry fulfilled?                      │
│   • Is A-Story complete? Is B-Story thread advanced?            │
│   • Is cliffhanger strong enough to pull to next episode?       │
│                                                                 │
│ STEP 12 of 12 — Season Consistency Review (after all episodes)  │
│   • Character arcs match season-bible.md plan                   │
│   • Relationship evolution matches character-relations.md       │
│   • Season question answered by final episode                   │
└─────────────────────────────────────────────────────────────────┘
```

**Project Structure (Web Series):**
```
project/{name}/
├── season-bible.md          ← HARD GATE (all episode work requires this)
├── genre-analysis.md
├── story-synopsis.md        (season-level)
├── character-bible.md
├── character-relations.md   (with episode-by-episode evolution)
├── episode-map.md
├── episode-01/
│   ├── synopsis.md
│   ├── beat-sheet.md
│   ├── screenplay.md
│   └── shot-breakdown.md
├── episode-02/
│   └── ...
```

**HARD GATES (Web Series):**
- Season Bible MUST be created before any episode work
- Character Bible + Character Relations MUST be complete before Episode Map
- Episode Map must be approved before individual episode development
- Episodes developed IN ORDER (01 → 02 → 03) — never skip ahead

---

## WORKFLOW 7: MICRO DRAMA
**Trigger**: User selects "Micro Drama" format (3-7 min episodes, multiple episodes)
**Reference**: `.bmad-film/workflows/development/micro-drama.yaml`
**Architecture**: Compressed — Series Bible + Episode Arc Map + Per-Episode

```
┌─────────────────────────────────────────────────────────────────┐
│           MICRO DRAMA — STEP SEQUENCE (NEVER SKIP)              │
├─────────────────────────────────────────────────────────────────┤
│ CORE RULES FOR MICRO DRAMA:                                     │
│   • Every episode = ONE emotional beat (not a full story)       │
│   • Episode 1 = World + Character + Hook in 60 seconds          │
│   • Episodes 2-N = Each starts with micro-recap anchor          │
│   • Every episode ends with micro-cliffhanger (even small)      │
│   • Dialogue is PRIMARY story carrier — every line must work    │
│   • No scene can "breathe" — every second is story              │
│   • Each episode must be partially self-contained               │
│                                                                 │
│ STEP 0 of 8 — Micro Drama Concept Intake                        │
│   • What is the ONE relationship this series is about?          │
│   • How many episodes? (10/20/30/50/100)                        │
│   • Episode duration? (2-3 min / 3-5 min / 5-7 min)            │
│   • Platform? (YouTube Shorts/Instagram/OTT/Television)        │
│   • Vertical or horizontal format?                              │
│                                                                 │
│ STEP 1 of 8 — Series Story Questions (Compressed — 12 Qs)       │
│   Element Treatment for Micro Drama:                            │
│   CHARACTER: One trait revealed per episode (not full arc)      │
│   RELATIONSHIP: ONE core relationship — this IS the series      │
│   EMOTION: Single emotion per episode, punchy, immediate        │
│   PLOT: One scene = one beat = one episode                      │
│   WORLD: Instantly recognizable — NO setup needed               │
│   CONFLICT: Compressed — one line establishes, rest is impact   │
│   THEME: Never stated, only felt — emerges from all eps combined│
│   SUBTEXT: IS the episode — unsaid = what episode is about      │
│                                                                 │
│ STEP 2 of 8 — Micro Series Bible Creation                       │
│   Save: project/{name}/micro-series-bible.md                   │
│   Contents:                                                     │
│   • World (instantly recognizable — 3 sentences max)           │
│   • Character Essence (one paragraph each — no backstory)       │
│   • Core Relationship (the ONE relationship — fully mapped)     │
│   • Emotional Arc Map (what emotion each episode delivers)      │
│   • The Unsaid (what series never says but always points to)    │
│                                                                 │
│ STEP 3 of 8 — Character Relations Map (Compressed)              │
│   Only CORE pair — full 8 questions                             │
│   Track: Which episode is each "unsaid" moment closest to       │
│   being said? That's where the episode cliffhanger comes from.  │
│   Save: project/{name}/character-relations.md                  │
│                                                                 │
│ STEP 4 of 8 — Episode Arc Map Creation                          │
│   Save: project/{name}/episode-arc-map.md                      │
│   Format: ONE LINE per episode — all visible at once:           │
│   EP 01: [What happens] | [Emotion delivered] | [Hook]          │
│   EP 02: [What happens] | [Emotion] | [Hook]                    │
│   ...all episodes mapped before any episode is written...       │
│                                                                 │
│   Arc Structure (example: 20 episodes):                         │
│   EP 1-5 (Arc 1): World + Character + First conflict ignited   │
│   EP 6-14 (Arc 2): Escalation + Relationship micro-shifts      │
│   EP 15-20 (Arc 3): Climax build + One irreversible moment     │
│                                                                 │
│ STEP 5 of 8 — Episode Script Creation (Compressed Format)       │
│   Each episode = combined synopsis + screenplay in ONE file     │
│   Compressed screenplay format (different from feature film):   │
│   • Scene description: 2 lines MAXIMUM                          │
│   • Dialogue: PRIMARY story carrier — every line does work      │
│   • Action lines: ONLY what camera MUST see                     │
│   • NO standard INT./EXT. blocks — too space-wasteful           │
│   • Micro-recap line at TOP of each episode (Ep 2 onwards)     │
│   Save: project/{name}/episode-{XX}.md (combined file)        │
│                                                                 │
│ STEP 6 of 8 — Episode QA (per episode)                          │
│   • Does episode deliver its ONE designated emotion?            │
│   • Is micro-cliffhanger strong enough?                         │
│   • Is the "unsaid" present but not stated?                     │
│   • Can new viewer partially understand this episode?           │
│   • Is every second of dialogue carrying story?                 │
│                                                                 │
│ STEP 7 of 8 — Series Consistency Review (after all episodes)    │
│   • Does the core relationship's unsaid remain unsaid until     │
│     the designated final episode?                               │
│   • Is the emotional arc map honored?                           │
│   • Does binge-watching create a complete emotional experience? │
│                                                                 │
│ STEP 8 of 8 — AI Shot Breakdown (Optional — per episode)        │
│   • Micro Drama often AI-generated (Veo3/Runway/Pika)           │
│   • Shot breakdown for each episode if needed                   │
│   • Platform-specific format (vertical/horizontal specs)        │
└─────────────────────────────────────────────────────────────────┘
```

**Project Structure (Micro Drama):**
```
project/{name}/
├── micro-series-bible.md    ← HARD GATE (everything requires this)
├── character-relations.md   (core relationship — compressed)
├── episode-arc-map.md       (all episodes visible at once)
├── episode-01.md            (combined synopsis + screenplay)
├── episode-02.md
├── ...
└── episode-{XX}.md
```

**HARD GATES (Micro Drama):**
- Micro Series Bible MUST be created before Episode Arc Map
- Episode Arc Map MUST be complete and approved before any individual episode
- Episodes developed IN ORDER — never jump ahead
- Each episode must serve the emotional arc map before proceeding to next

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

### 5. Both Story Formats Mandatory
Story Synopsis ALWAYS produces:
1. Continuous Narrative (flowing Hindi prose)
2. Scene-by-Scene Breakdown (technical version)
Both in same file. No exceptions.

### 6. Language Default — GLOBAL LANGUAGE LAW (See top of this file)
- DEFAULT = Simple Bollywood Hindi (60-70% Hindi + 30-40% natural English)
- Complete sentences only — subject + verb mandatory in every sentence
- Natural connectors required — sentences must flow, not feel like a list
- Forbidden formal English — use Hindi equivalents (see top of this file)
- Pre-output self-check is MANDATORY before writing any story content
- Regional dialect only when user explicitly specifies
- English ONLY allowed for: scene headings, character names, place names, technical film terms

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

## QUICK TRIGGER REFERENCE

| User Says | Workflow | First Step |
|-----------|----------|------------|
| "story banao", "ek kahani", "write a story", "film concept" | Story Synopsis | STEP 0 — Format Selection |
| "character bible", "characters develop karo" | Character Bible | STEP 0 — Read Files |
| "character relations", "relationships map karo", "rishta map" | Character Relations Map | STEP 0 — Read Files |
| "beat sheet banao", "beats dikhao" | Beat Sheet | STEP 0 — Read Files |
| "screenplay likho", "script banao" | Screenplay | STEP 0 — Read Files (including character-relations.md) |
| "shot breakdown", "shots plan karo" | Shot Breakdown | STEP 0 — Read Files → Both traditional + AI breakdown |
| "web series banao", "multi-episode series" | Web Series | STEP 0 — Series Concept Intake |
| "micro drama", "short episodes", "vertical series" | Micro Drama | STEP 0 — Micro Drama Concept Intake |

---

*Reference this file whenever a workflow is triggered to ensure correct step sequence.*
*If in doubt about which step you're on — announce the step to the user to confirm.*
