# Quick Film Spec Skill

**Command**: `/quick-film-spec`
**Workflow**: `quick-film-spec.yaml`
**Description**: Rapidly define a simple film project (30-sec commercial, social media content)

---

## Skill Instructions

When the user invokes `/quick-film-spec`, execute the Quick Film Specification workflow:

### 1. Load Required Agents
- Activate: `bmad-film-master`, `story-developer`, `producer`, `directors-assistant`
- Load workflow: `.bmad-film/workflows/development/quick-film-spec.yaml`

### 2. Initialize Context
- If `film-project-context.md` doesn't exist, create from template
- Set project scale: "micro"
- Set phase: "development"

### 3. Execute Workflow Steps

#### Step 1: Gather Project Information
**Agent**: Story Developer

Ask the user these key questions:

```markdown
# Quick Film Spec - Let's define your project

I'll help you quickly define your film project. This should take about 30-60 minutes.

## Core Questions

### 1. Project Type
What are you creating?
- [ ] 30-second commercial
- [ ] 15-second social media ad
- [ ] 60-second promo
- [ ] Music video snippet
- [ ] Other: _______

### 2. Concept
**What's the core idea or brief?**
[User describes concept]

### 3. Key Message
**What's the ONE thing the audience should feel or understand?**
[User response]

### 4. Target Length
**How long should the final piece be?**
- [ ] 15 seconds
- [ ] 30 seconds
- [ ] 60 seconds
- [ ] Other: _______

### 5. Visual Style
**Any visual references or style preferences?**
(Films, ads, mood boards, or descriptive words like "energetic", "cinematic", "documentary-style")
[User response]

### 6. Requirements
**What MUST be included?**
(Product shots, logo, specific messaging, brand guidelines, etc.)
[User response]

### 7. Constraints
**What are your constraints?**
- **Budget**: $_______ (or "very limited", "moderate", "flexible")
- **Timeline**: Need it by _______ (date)
- **Resources**: What do you have access to? (camera, crew, locations, etc.)
[User response]
```

#### Step 2: Develop Creative Vision
**Agents**: Story Developer + Director's Assistant

Based on responses, create:

```markdown
## Creative Vision: [Project Title]

### Logline
[One-sentence summary of the concept]

### Genre & Tone
**Genre**: [Commercial / Promo / Social Media]
**Tone**: [e.g., "Energetic and uplifting" / "Intimate and authentic" / "Bold and dynamic"]

### Story Beats (for 30-second structure)
1. **Hook** (0-5 sec): [How it opens/grabs attention]
2. **Message** (5-23 sec): [Core content/story]
3. **Resolution** (23-30 sec): [Payoff/call-to-action]

### Visual Approach
**Style**: [Naturalistic / Stylized / Documentary / Cinematic]
**Camera**: [Handheld / Locked-off / Mix]
**Color**: [Warm / Cool / Vibrant / Muted]

**References**:
- [Reference 1]: [What we're taking from it]
- [Reference 2]: [What we're taking from it]

### Key Requirements
- [Requirement 1: e.g., "Must feature product prominently"]
- [Requirement 2: e.g., "Logo must appear in final 3 seconds"]
```

#### Step 3: Feasibility Assessment
**Agent**: Producer

Provide quick feasibility check:

```markdown
## Feasibility Assessment

### Budget Estimate
**Estimated Total**: $[amount]
**Breakdown**:
- Crew: $[amount] ([X] people for [Y] days)
- Equipment: $[amount] (rental or owned)
- Location: $[amount]
- Post-production: $[amount]
- Contingency: $[amount]

**Assessment**: ✓ Feasible within stated budget / ⚠️ Tight—will need optimization / ✗ Over budget—needs adjustment

### Timeline Estimate
**Total Time**: [X] weeks
- **Prep**: [X] days
- **Shoot**: [X] days
- **Post**: [X] days

**Assessment**: ✓ Achievable / ⚠️ Tight / ✗ Need more time

### Resource Requirements
**Crew**: [Minimal—3-5 people / Standard—5-10 people]
**Equipment**: [List key equipment needs]
**Locations**: [Number of locations, type]

### Risk Factors
- [Risk 1 + mitigation]
- [Risk 2 + mitigation]

### Recommendation
✓ **GO** - Project is feasible as defined
⚠️ **GO WITH ADJUSTMENTS** - [List adjustments needed]
✗ **NO-GO** - [Explain why and what would need to change]
```

#### Step 4: Generate Quick Brief
**Agent**: BMAD-FILM Master

Create one-page project brief:

```markdown
# Project Brief: [Title]

**Date**: [Date]
**Project Type**: [Type]
**Target Length**: [Length]
**Scale**: Micro Project

---

## Overview
[2-3 sentence project description]

## Creative Vision
**Logline**: [One sentence]
**Tone**: [Description]
**Visual Style**: [Description]

**Story Structure**:
1. Hook: [Brief]
2. Message: [Brief]
3. Resolution: [Brief]

## Production Details
**Budget**: $[amount]
**Timeline**: [X weeks] (Delivery by [date])
**Shoot Days**: [X days]

**Key Resources**:
- Crew: [List]
- Equipment: [List]
- Locations: [List]

## Requirements & Constraints
**Must Include**:
- [Requirement 1]
- [Requirement 2]

**Constraints**:
- [Constraint 1]
- [Constraint 2]

## Next Steps
1. ✓ Project brief complete
2. → Next: `/quick-shoot` (prepare for production)
3. → Timeline: [When to start production]

---

**Status**: Ready for production planning
```

### 4. Update Context
- Write complete project details to `film-project-context.md`
- Save project brief to `project/development/quick-brief.md`
- Set phase status: "Development complete, ready for production"

### 5. Provide Next Steps

```markdown
## ✓ Quick Film Spec Complete!

Your project is defined and ready to move forward.

### What We've Created
- ✓ Creative vision and logline
- ✓ Story structure (Hook → Message → Resolution)
- ✓ Visual style defined
- ✓ Feasibility confirmed
- ✓ Budget and timeline estimated

### Files Created
- `project/film-project-context.md` - Master project context (single source of truth)
- `project/development/quick-brief.md` - One-page project brief

### Next Steps
When you're ready to prepare for production, run:
**`/quick-shoot`**

This will create your shot list, production plan, and prepare for shoot day.

### Questions?
- Run `/bmad-film-help` for more information
- Run `/project-status` to see current project state
```

---

## Error Handling

**If concept is unclear:**
- Story Developer asks clarifying questions
- Helps user focus the core message

**If budget is insufficient:**
- Producer identifies specific areas to optimize
- Suggests scaled-down approach
- Provides "must-have vs. nice-to-have" analysis

**If timeline is too tight:**
- Producer assesses what's realistic
- Suggests either timeline extension or scope reduction

---

## Success Criteria

Skill is successful when:
- ✓ Clear logline and concept defined
- ✓ Visual style and tone articulated
- ✓ Feasibility confirmed (or path to feasibility identified)
- ✓ User understands budget, timeline, and next steps
- ✓ `film-project-context.md` initialized with complete project details
- ✓ User feels confident moving to production
