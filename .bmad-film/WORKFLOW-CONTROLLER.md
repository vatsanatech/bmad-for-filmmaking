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
│   • character-bible.md + beat-sheet.md                         │
│   • Detect dialect setup from character-bible                   │
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

### 6. Language Default — GLOBAL LANGUAGE LAW (See top of this file)
- DEFAULT = Simple Bollywood Hindi (60-70% Hindi + 30-40% natural English)
- Complete sentences only — subject + verb mandatory in every sentence
- Natural connectors required — sentences must flow, not feel like a list
- Forbidden formal English — use Hindi equivalents (see top of this file)
- Pre-output self-check is MANDATORY before writing any story content
- Regional dialect only when user explicitly specifies
- English ONLY allowed for: scene headings, character names, place names, technical film terms

---

## QUICK TRIGGER REFERENCE

| User Says | Workflow | First Step |
|-----------|----------|------------|
| "story banao", "ek kahani", "write a story", "film concept" | Story Synopsis | STEP 0 — Format Selection |
| "character bible", "characters develop karo" | Character Bible | STEP 0 — Read Files |
| "beat sheet banao", "beats dikhao" | Beat Sheet | STEP 0 — Read Files |
| "screenplay likho", "script banao" | Screenplay | STEP 0 — Read Files |
| "shot breakdown", "shots plan karo" | Shot Breakdown | STEP 0 — Read Files → Both traditional + AI breakdown |

---

*Reference this file whenever a workflow is triggered to ensure correct step sequence.*
*If in doubt about which step you're on — announce the step to the user to confirm.*
