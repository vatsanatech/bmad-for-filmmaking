# Quick Shoot Skill

**Command**: `/quick-shoot`
**Workflow**: `quick-shoot.yaml`
**Description**: Plan and execute production for simple projects

---

## Skill Instructions

When user invokes `/quick-shoot`:

1. **Load agents**: 1st AD (lead), Cinematographer, Script Supervisor, Producer, Director's Assistant
2. **Load workflow**: `.bmad-film/workflows/production/quick-shoot.yaml`
3. **Verify prerequisites**: Check that `/quick-film-spec` was completed
4. **Execute workflow**:
   - Create shot list (Director's Assistant + Cinematographer)
   - Build production plan (1st AD)
   - Generate call sheet
   - Guide shoot day execution
   - Track continuity (Script Supervisor)
   - Create production report

5. **Outputs**:
   - Shot list with priorities
   - Production plan
   - Call sheet
   - Continuity notes
   - Production report

6. **Update context** and recommend `/quick-edit`

---

## Workflow Execution

```markdown
# Quick Shoot - Production Planning & Execution

## Step 1: Production Planning (30 min)

**Who's involved**: 1st AD, Producer, Cinematographer

Let's plan your shoot:

### Key Information Needed:
1. **Shoot date and time**: [When are you shooting?]
2. **Location**: [Where are you shooting?]
3. **Crew**: [Who's on your team?]
4. **Equipment**: [What camera/lighting do you have?]

[Continue with production planning steps from workflow...]

## Step 2: Shot List Creation (30 min)

**Who's involved**: Director's Assistant, Cinematographer

[Create detailed shot list based on creative vision...]

## Step 3: Shoot Day Execution

[Guide through production with on-set management...]

## ✓ Production Complete!

Your footage is captured. Next: `/quick-edit`
```
