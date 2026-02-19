# BMAD-FILM Complete Workflow Guide
## From Concept to Shot-Ready Production

**Version**: 2.0.0 (Genre-Routed, Modular Workflow)
**Last Updated**: February 2026

---

## Overview

The BMAD-FILM framework provides a complete, modular workflow from initial story concept to detailed shot-by-shot breakdown ready for production or AI video generation.

**Key Features**:
- ✅ **Genre-Routed**: Automatically selects appropriate genre specialist based on your story
- ✅ **Modular**: Each step is independent and can be refined separately
- ✅ **Production-Ready**: All outputs ready for traditional filming or AI video generation
- ✅ **Bollywood Masters Training**: Each genre agent trained on specific Bollywood directors
- ✅ **Extreme Detail**: Every specification needed for AI video generation included

---

## The 5-Step Workflow

```
CONCEPT → SYNOPSIS → ARCHITECTURE → CHARACTERS → SCREENPLAY → SHOTS
  (Idea)     (STEP 1)     (STEP 2)       (STEP 3)      (STEP 4)    (STEP 5)
```

### Each step is **separate and distinct** - you must approve before proceeding to next step.

---

## STEP 1: Story Synopsis (Genre-Routed)

**Workflow File**: `.bmad-film/workflows/development/story-synopsis.yaml`
**Version**: 2.0.0
**Duration**: 30-60 minutes

### What It Does

Creates a simple 5-7 paragraph story with twist/revelation, automatically routing to the appropriate genre specialist.

### Agents Involved

1. **Master Story Director** (Lead)
   - Analyzes your concept
   - Identifies primary genre
   - Selects appropriate specialist
   - Routes to specialist agent

2. **Genre-Specific Story Architect** (Selected based on concept)
   - **Thriller**: Suspense Architect (Sujoy Ghosh, Sriram Raghavan, Anurag Kashyap)
   - **Romance**: Romance Architect (Yash Chopra, Sanjay Leela Bhansali, Imtiaz Ali)
   - **Action**: Action Architect (Rohit Shetty, Siddharth Anand, Ali Abbas Zafar)
   - **Comedy**: Comedy Architect (Hrishikesh Mukherjee, Rajkumar Hirani, Priyadarshan)
   - **Drama**: Drama Architect (Bimal Roy, Gulzar, Ashutosh Gowariker)
   - **Horror**: Horror Architect (Ram Gopal Varma, Vikram Bhatt, Vishal Bhardwaj)
   - **Musical**: Musical Architect (Farah Khan, Karan Johar, Aditya Chopra)
   - **Social**: Social Cinema Architect (Shyam Benegal, Govind Nihalani, Anurag Basu)

### Inputs

- Story concept (even vague is fine)
- Target length (5 min, 15 min, 90 min, etc.)
- Genre/tone preference

### Outputs

- `story-synopsis.md` - Simple story in narrative form (5-7 paragraphs + twist)
- `genre-analysis.md` - Genre identification with rationale

### Next Step

**If approved** → Proceed to STEP 2: Story Architecture
**If needs refinement** → Re-run synopsis with adjustments

---

## STEP 2: Story Architecture

**Workflow File**: `.bmad-film/workflows/development/story-architecture.yaml`
**Version**: 1.0.0
**Duration**: 1-2 hours

### What It Does

Develops complete narrative structure, world-building, thematic foundation, and visual language specifications.

### Agents Involved

1. **Master Story Director** (Lead)
2. **Genre-Specific Architect** (from Step 1)
3. **BMAD Film Master** (Quality check)

### Prerequisites

- Approved story synopsis
- Genre identification

### Process

1. Synopsis deep analysis
2. Structural framework design (3/4/5-act structure)
3. World-building foundation (setting as character)
4. Thematic architecture (embedded, not stated)
5. Visual language specifications (camera, color, lighting approach)
6. Integration & documentation

### Outputs

- `story-architecture.md` containing:
  - Logline
  - Act structure with beats and timing
  - Information reveal architecture
  - World-building specifications
  - Thematic foundation
  - Visual language guide
  - Color palette
  - Camera philosophy

### Next Step

**If approved** → Proceed to STEP 3: Character Profiles
**If needs refinement** → Re-run architecture with adjustments

---

## STEP 3: Character Profiles

**Workflow File**: `.bmad-film/workflows/development/character-profiles.yaml`
**Version**: 1.0.0
**Duration**: 1-2 hours

### What It Does

Creates psychologically complex, production-ready character profiles with extreme visual detail for AI generation.

### Agents Involved

1. **Character Designer** (Lead)
2. **Genre-Specific Architect** (for genre consistency)
3. **Dialogue Agent** (for voice establishment)
4. **BMAD Film Master** (Quality check)

### Prerequisites

- Approved story architecture
- World-building established

### Process

1. Character roster definition (who's in the story)
2. Protagonist(s) deep design (psychological + physical)
3. Antagonist(s) design (equal complexity)
4. Supporting characters design
5. Relationship dynamics mapping
6. Consistency tracking framework
7. Genre alignment review
8. Integration & documentation

### Outputs

- `character-profiles/` folder containing:
  - `protagonist-[name].md` - Complete profile with AI-ready descriptions
  - `antagonist-[name].md` - Full antagonist profile
  - `supporting-[name].md` - Supporting character profiles
  - `relationship-dynamics.md` - Character relationship map
  - `consistency-tracking.md` - Visual and behavioral tracking system

### Character Profile Contains

**Psychological Core**:
- Want vs Need
- Moral ambiguity
- Character arc
- Core fears and desires

**Physical Appearance** (AI-Generation Ready):
- Demographics (age, gender, ethnicity, build)
- Face & features (extreme detail)
- Physical markers (height, posture, movement)
- Costume/wardrobe (scene-specific)
- AI prompt formula for consistency
- Bollywood actor references

**Voice & Behavior**:
- Speech patterns
- Regional dialect
- Behavioral mannerisms

### Next Step

**If approved** → Proceed to STEP 4: Screenplay Development
**If needs refinement** → Re-run character profiles with adjustments

---

## STEP 4: Screenplay Development

**Workflow File**: `.bmad-film/workflows/development/screenplay-development.yaml`
**Version**: 1.0.0
**Duration**: 2-4 hours

### What It Does

Creates complete formatted screenplay with visual storytelling, authentic dialogue with subtext, and proper formatting.

### Agents Involved

1. **Screenplay Developer** (Lead)
2. **Dialogue Agent** (Dialogue creation)
3. **Genre-Specific Architect** (Visual storytelling verification)
4. **Character Designer** (Voice verification)
5. **BMAD Film Master** (Quality check)

### Prerequisites

- Approved story architecture
- Complete character profiles

### Process

1. Scene list construction (all scenes identified)
2. Scene-by-scene structure (goal, obstacle, outcome, turn)
3. Dialogue development (with subtext)
4. Action lines & scene descriptions
5. Screenplay assembly (formatted)
6. Visual storytelling verification
7. Character voice verification
8. Pacing & rhythm review
9. Final integration & polish

### Outputs

- `complete-screenplay.md` containing:
  - All scenes in proper screenplay format
  - Hindi dialogue (or target language) with translations
  - Action lines and scene descriptions
  - Character names, locations, timing
  - Proper formatting throughout

### Screenplay Format

```markdown
## SCENE [X]: [SCENE NAME]
**Location**: INT/EXT. SPECIFIC LOCATION - TIME
**Duration**: [XX seconds]

Scene description.

CHARACTER NAME
(action/emotion if needed)
Hindi dialogue line.
*[English translation]*

Action line describing what happens.

[Continue...]
```

### Quality Standards

- ✓ Every scene has clear purpose
- ✓ Visual storytelling dominates over exposition
- ✓ All characters have distinct voices
- ✓ Dialogue has subtext (not on-the-nose)
- ✓ Regional/language authenticity maintained
- ✓ Pacing creates engaging rhythm
- ✓ Screenplay is shootable

### Next Step

**If approved** → Proceed to STEP 5: Shot Breakdown
**If needs refinement** → Re-run screenplay or specific scenes

---

## STEP 5: Shot Breakdown

**Workflow File**: `.bmad-film/workflows/pre-production/shot-breakdown.yaml`
**Version**: 1.0.0
**Duration**: 2-4 hours

### What It Does

Breaks screenplay into detailed shot-by-shot breakdown with complete technical specifications and AI-generation-ready prompts.

### Agents Involved

1. **Director's Assistant** (Lead)
2. **Cinematographer** (Camera and lighting specs)
3. **Production Designer** (Visual consistency)
4. **Master Story Director** (Genre visual language)

### Prerequisites

- Complete formatted screenplay
- Character profiles (for visual consistency)
- Story architecture (for visual language)

### Process

1. Screenplay analysis (identify visual storytelling needs)
2. Genre-specific visual language application
3. Cinematography specification (camera, lighting, movement)
4. Shot-by-shot breakdown (complete technical specs)
5. AI video prompt generation (ready for Runway/Pika/Sora)
6. Production documentation (shot list, equipment, timing)

### Outputs

- `shot-breakdown/` folder containing:
  - `scene-[X]-shots.md` - Shot-by-shot breakdown per scene
  - `ai-prompts/` - AI video generation prompts
  - `master-shot-list.md` - Complete shot list for entire project
  - `equipment-list.md` - Camera and lighting requirements
  - `coverage-checklist.md` - Coverage verification

### Each Shot Contains

**Technical Specifications**:
- Shot number and type (WS/MS/CU/ECU/POV/etc.)
- Camera specs (lens, angle, height, movement)
- Duration (exact seconds)
- Framing and composition
- Lighting description (source, direction, color temp)

**Production Details**:
- Actor blocking and movement
- Performance notes (micro-expressions)
- Sound elements (dialogue, effects, music)
- Emotional objective
- Continuity notes

**AI Generation Prompt** (ready to copy-paste):
```
VISUAL: [Detailed visual description with all elements]
CAMERA: [Specifications]
LIGHTING: [Specifications]
PERFORMANCE: [Actor details]
MOOD: [Emotional tone]
STYLE: [Bollywood/cinematic references]
DURATION: [Seconds]

NEGATIVE PROMPT: [What to avoid]
```

### Quality Standards

- ✓ Every shot has complete technical specifications
- ✓ AI prompts detailed enough for direct generation
- ✓ Coverage adequate for editing
- ✓ Visual consistency across all shots
- ✓ Genre visual language applied consistently
- ✓ Production documentation ready for set

### Final Output

**Complete Production Package**:
- ~30-50 shots for 5-minute film
- ~80-120 shots for 15-minute film
- ~500-1000+ shots for feature film
- All ready for either traditional filming OR AI video generation

---

## Complete Workflow Summary

| Step | Workflow | Duration | Output | Next |
|------|----------|----------|--------|------|
| **1** | Story Synopsis | 30-60 min | `story-synopsis.md`<br>`genre-analysis.md` | → Step 2 |
| **2** | Story Architecture | 1-2 hours | `story-architecture.md` | → Step 3 |
| **3** | Character Profiles | 1-2 hours | `character-profiles/*.md`<br>`relationship-dynamics.md`<br>`consistency-tracking.md` | → Step 4 |
| **4** | Screenplay Development | 2-4 hours | `complete-screenplay.md` | → Step 5 |
| **5** | Shot Breakdown | 2-4 hours | `shot-breakdown/*.md`<br>`ai-prompts/*.md`<br>`master-shot-list.md` | ✅ DONE |

**Total Time**: 6-12 hours for complete concept-to-shots development

---

## File Organization

```
project/
├── development/
│   ├── story-synopsis.md              # STEP 1
│   ├── genre-analysis.md              # STEP 1
│   ├── story-architecture.md          # STEP 2
│   ├── character-profiles/            # STEP 3
│   │   ├── protagonist-[name].md
│   │   ├── antagonist-[name].md
│   │   ├── supporting-[name].md
│   │   ├── relationship-dynamics.md
│   │   └── consistency-tracking.md
│   └── complete-screenplay.md         # STEP 4
│
└── pre-production/
    └── shot-breakdown/                # STEP 5
        ├── scene-1-shots.md
        ├── scene-2-shots.md
        ├── [...all scenes...]
        ├── ai-prompts/
        │   ├── scene-1-prompts.md
        │   └── [...all scenes...]
        ├── master-shot-list.md
        ├── equipment-list.md
        └── coverage-checklist.md
```

---

## Key Principles

### 1. Modular Workflow
Each step is independent. You can:
- Refine individual steps without affecting others
- Stop at any point (e.g., just get screenplay, skip shots)
- Re-run specific steps if changes needed

### 2. Genre Intelligence
Genre-specific agents ensure:
- Appropriate storytelling techniques
- Correct visual language
- Authentic genre conventions
- Trained on Bollywood masters who excelled in that genre

### 3. Production-Ready Output
All outputs serve dual purpose:
- Traditional filming (human crew with cameras)
- AI video generation (feeding prompts to AI tools)
- Extreme detail supports EITHER approach

### 4. Approval Gates
Must approve each step before proceeding:
- Prevents wasted work on wrong foundation
- Allows refinement at each stage
- Ensures filmmaker maintains creative control

### 5. Bollywood Production Level
All outputs achieve:
- Cinema-grade story quality
- Professional character depth
- Authentic dialogue with subtext
- Bollywood visual standards
- Hindi-dominant language (where appropriate)

---

## Usage Examples

### Example 1: 5-Minute Short Film

**Input**: "Murder mystery set in Delhi, psychological thriller, twist ending"

**Workflow**:
1. **Synopsis** (30 min) → "Sabak" story created by Suspense Architect
2. **Architecture** (1 hour) → 4-act structure, Delhi as character, visual language
3. **Characters** (1 hour) → Meera, Inspector, Shweta, Rajat profiles with AI-ready detail
4. **Screenplay** (2 hours) → 7 scenes, Hindi dialogue, 5:00 runtime
5. **Shots** (2 hours) → ~40-60 shots with complete AI prompts

**Total**: 6-7 hours, complete production package

### Example 2: 90-Minute Feature Film

**Input**: "Romance between musician and dancer, set in Mumbai, Bollywood musical"

**Workflow**:
1. **Synopsis** (1 hour) → Created by Musical Architect (Farah Khan/Karan Johar training)
2. **Architecture** (2 hours) → Song placement strategy, 5-act structure with music integration
3. **Characters** (2 hours) → Protagonist couple, supporting characters, relationship dynamics
4. **Screenplay** (4 hours) → 50-60 scenes, bilingual dialogue, song sequences
5. **Shots** (4 hours) → 800-1000 shots with choreography notes

**Total**: 12-15 hours, feature film production package

---

## Quality Standards

### Story Level
- ✓ Theme embedded in action, not stated
- ✓ Moral ambiguity creates genuine tension
- ✓ Twist recontextualizes entire narrative
- ✓ Bollywood masters' principles applied

### Character Level
- ✓ Characters feel like real humans, not constructs
- ✓ Psychological depth with moral ambiguity
- ✓ Physical descriptions AI-generation ready
- ✓ Each character has distinct voice

### Screenplay Level
- ✓ Visual storytelling dominates over exposition
- ✓ Every scene passes "Are you sure?" test (Raghavan)
- ✓ Dialogue has subtext, not on-the-nose
- ✓ Regional/language authenticity maintained

### Shot Level
- ✓ Every shot has complete technical specifications
- ✓ AI prompts ready for direct use in video generation
- ✓ Coverage adequate for editing
- ✓ Visual consistency across all shots
- ✓ Genre visual language applied throughout

---

## What Makes This "The World's Most Intelligent Framework"

1. **Genre Intelligence**: Automatically routes to appropriate specialist trained on Bollywood masters
2. **Modular Flexibility**: Each step independent, can refine without affecting others
3. **Dual-Purpose Output**: Works for both traditional filming and AI video generation
4. **Production-Grade Quality**: Cinema-level story, character, screenplay, and shots
5. **Extreme Detail**: Every specification needed for AI generation included
6. **Approval Gates**: Filmmaker maintains creative control at every step
7. **Complete Package**: From vague concept to shot-ready production in 6-12 hours

---

## Next Steps After Shot Breakdown

Once shot breakdown is complete, you have multiple options:

### Traditional Production
- **Budget Breakdown**: Cost all shots, equipment, crew
- **Schedule Build**: Create shooting schedule
- **Location Scout**: Find and secure locations
- **Casting**: Cast actors based on character profiles
- **Production**: Shoot using shot list and coverage checklist

### AI Video Generation
- **Generate Videos**: Use AI prompts in Runway, Pika, Sora, etc.
- **Edit Assembly**: Edit generated shots into complete film
- **Sound Design**: Add dialogue, effects, music
- **Color Grade**: Final color correction
- **Delivery**: Export final video

### Hybrid Approach
- **AI Generate**: Wide shots, establishing shots, atmospheric shots
- **Traditional Film**: Close-ups, dialogue scenes, performance-heavy shots
- **Combine**: Edit together for final film

---

## Support & Documentation

- **Workflow Files**: `.bmad-film/workflows/`
- **Agent Definitions**: `.bmad-film/agents/`
- **Templates**: `.bmad-film/templates/`
- **This Guide**: `.bmad-film/workflows/COMPLETE-WORKFLOW-GUIDE.md`

---

**BMAD-FILM Framework v2.0.0**
*The World's Most Intelligent Filmmaking Framework*
From Concept to Shots in 5 Clear Steps
