# BMAD-FILM Quick Reference Card

**Fast Commands & Workflow Cheat Sheet**

---

## 🎯 The 4-Step Workflow

```
STEP 1: Story Synopsis → STEP 2: Character Bible → STEP 3: Screenplay → STEP 4: Shot Breakdown
```

Each step reads previous outputs automatically. Review and approve before moving to next.

---

## 📝 Commands

### **STEP 1: Story Synopsis**
```
"Create a [duration] [genre] about [concept]. Call it [project-name]."
```
**Examples**:
```
"Create a 5-minute thriller about locked room murder. Call it band-darwaza."
"Create a 15-minute romance about strangers on a train. Call it train-se-pyaar."
```

**Creates**: `project/{project-name}/genre-analysis.md` + `story-synopsis.md`

---

### **STEP 2: Character Bible**
```
"[project-name]"
```
**Example**:
```
"band-darwaza"
```

**Creates**: `project/{project-name}/character-bible.md`

---

### **STEP 3: Screenplay**

**Default (Simple Bollywood Hindi)**:
```
"[project-name]"
```

**With Dialect**:
```
"[project-name] in [dialect]"
```

**Examples**:
```
"band-darwaza"
"band-darwaza in Haryanvi"
"band-darwaza in Hinglish"
"band-darwaza in Pure Hindi"
"band-darwaza in Punjabi-influenced"
```

**Creates**: `project/{project-name}/screenplay.md` ⭐ (FINAL)

---

### **STEP 4: Shot Breakdown**
```
"[project-name]"
```

**Example**:
```
"band-darwaza"
```

**Creates**: `project/{project-name}/shot-breakdown.md`

---

## 💬 Feedback Commands

### **Approve & Continue**:
```
"Approved, proceed to next step"
"Looks good, continue"
```

### **Request Changes**:
```
"Change [element] to [change]"
"Make [character] more [trait]"
"The dialogue in Scene X is too [issue], make it [desired]"
"Add [element]"
```

### **Regenerate**:
```
"Regenerate [step name]"
"Rewrite with [changes]"
```

---

## 📁 Output Structure

All files go to: `project/{project-name}/`

```
project/
└── {project-name}/
    ├── genre-analysis.md       (Step 1)
    ├── story-synopsis.md        (Step 1)
    ├── character-bible.md       (Step 2)
    ├── screenplay.md            (Step 3) ⭐
    └── shot-breakdown.md        (Step 4)
```

---

## ✅ Quick Checklist

**Story Synopsis**:
- [ ] Unique, not generic
- [ ] Multi-layered twists
- [ ] WOW factor present

**Character Bible**:
- [ ] All characters covered
- [ ] Distinct voices
- [ ] Clear arcs

**Screenplay**:
- [ ] Industry format
- [ ] Natural dialogue
- [ ] Character voices distinct
- [ ] Memorable lines

**Shot Breakdown**:
- [ ] All scenes covered
- [ ] Adequate coverage
- [ ] Production-ready

---

## 🎬 Full Example

```
Step 1: "Create a 5-minute thriller about locked room murder. Call it band-darwaza."
        Review → "Approved"

Step 2: "band-darwaza"
        Review → "Approved"

Step 3: "band-darwaza"
        Review → "Approved"

Step 4: "band-darwaza"
        Review → "Approved"

✓ Production Ready!
```

---

## 🆘 Help

```
"Help with [step]"
"Show example feedback for [step]"
```

---

**Need Details?** See: `.bmad-film/workflows/WORKFLOW-EXECUTION-GUIDE.md`
