# BMAD-FILM FRAMEWORK CHANGELOG
## Version 3.1.0 - Restructured Multi-Dialect + Beat Sheet Workflow

**Date**: 2026-02-18
**Changes**: Major structural improvements + new beat sheet workflow

═══════════════════════════════════════════════════════

## 🎯 MAJOR CHANGES

### 1. **NEW WORKFLOW: Beat Sheet** (Step 3)

Added professional beat sheet workflow between Character Bible and Screenplay.

**Why Beat Sheet?**
- Industry-standard tool (Save the Cat, Blake Snyder, Syd Field)
- Maps story beats before writing full screenplay
- Identifies pacing issues early
- Ensures emotional progression is clear
- Bridges gap between story synopsis and screenplay

**File**: `.bmad-film/workflows/development/beat-sheet.yaml`
**Version**: 1.0.0-multi-dialect
**Output**: `project/{project_name}/beat-sheet.md` (universal)

**Features**:
- 8 interactive questions about structure, pacing, emotional beats
- Beat-by-beat breakdown with emotional mapping
- Supports macro/moderate/micro granularity
- Universal for all dialects (story structure doesn't change)

---

### 2. **FOLDER STRUCTURE FOR MULTI-DIALECT** (Option 1 Implemented)

**OLD STRUCTURE** (Flat files - messy):
```
project/aakhri-dhun/
├── character-bible-hindi.md
├── character-bible-tamil.md
├── screenplay-hindi.md
├── screenplay-tamil.md
```

**NEW STRUCTURE** (Organized folders - clean):
```
project/aakhri-dhun/
├── genre-analysis.md          ✅ Universal (root)
├── story-synopsis.md           ✅ Universal (root)
├── beat-sheet.md               ✅ Universal (root) NEW!
├── shot-breakdown.md           ✅ Universal (root)
│
├── 📂 hindi/                   🇮🇳 Hindi version
│   ├── character-bible.md
│   └── screenplay.md
│
├── 📂 tamil/                   🇮🇳 Tamil version
│   ├── character-bible.md
│   └── screenplay.md
│
└── 📂 telugu/                  🇮🇳 Telugu version
    ├── character-bible.md
    └── screenplay.md
```

**Benefits**:
- ✅ Clean separation of dialects
- ✅ Universal files easy to find (at root)
- ✅ Each dialect team can work independently
- ✅ Easy to add/remove dialects
- ✅ Industry-standard approach (like /en/, /fr/ in software)

---

## 📝 UPDATED WORKFLOWS

### **character-bible.yaml** (v3.0.0-multi-dialect)
**Changes**:
- Updated Step 12 (Finalize) to create dialect folders
- Old: `character-bible-hindi.md`, `character-bible-tamil.md`
- New: `hindi/character-bible.md`, `tamil/character-bible.md`

### **screenplay.yaml** (v6.0.0-multi-dialect)
**Changes**:
- Added beat-sheet.md to context requirements (MUST READ)
- Updated Step 0 to detect dialect folders (not flat files)
- Updated Step 5 to read beat-sheet for emotional progression/pacing
- Updated finalization to save in dialect folders
- Old: `screenplay-hindi.md`, `screenplay-tamil.md`
- New: `hindi/screenplay.md`, `tamil/screenplay.md`
- Added beat sheet as Step 3 in workflow sequence notes

### **shot-breakdown.yaml** (v4.0.0-multi-dialect)
**Changes**:
- Added beat-sheet.md to context requirements (MUST READ)
- Updated Step 4 to read beat-sheet for emotional mapping
- Updated consistency checks to include beat-sheet pacing
- Updated dialect detection to look for folders
- Added beat sheet as Step 3 in workflow sequence notes

### **dialect-adaptation-guide.md**
**Changes**:
- Updated all file path examples to use folder structure
- Added beat-sheet.md to workflow examples
- Updated Example 1 and Example 2 sections

---

## 🔄 UPDATED WORKFLOW SEQUENCE

**COMPLETE DEVELOPMENT WORKFLOW** (Now 5 steps instead of 4):

```
1. Story Synopsis        → story-synopsis.md (universal)
2. Character Bible       → character-bible.md OR {dialect}/character-bible.md
3. Beat Sheet           → beat-sheet.md (universal) ✨ NEW!
4. Screenplay           → screenplay.md OR {dialect}/screenplay.md
5. Shot Breakdown       → shot-breakdown.md (universal with dialect notes)
```

**Beat Sheet Integration**:
- Story Synopsis → Character Bible → **Beat Sheet** → Screenplay → Shot Breakdown
- Beat sheet reads: story-synopsis.md, character-bible.md
- Screenplay reads: story-synopsis.md, character-bible.md, **beat-sheet.md**
- Shot breakdown reads: genre-analysis.md, **beat-sheet.md**, character-bible.md, screenplay.md

---

## 🎬 WHAT THIS MEANS FOR USERS

### **For Single-Dialect Projects** (e.g., Hindi only):
```
project/your-film/
├── genre-analysis.md
├── story-synopsis.md
├── beat-sheet.md           ⬅️ NEW!
├── character-bible.md
├── screenplay.md
└── shot-breakdown.md
```
**Impact**: One new step (beat sheet) improves screenplay quality.

---

### **For Multi-Dialect Projects** (e.g., Hindi + Tamil + Telugu):
```
project/your-film/
├── genre-analysis.md         ✅ Universal (root)
├── story-synopsis.md         ✅ Universal (root)
├── beat-sheet.md             ✅ Universal (root) - NEW!
├── shot-breakdown.md         ✅ Universal (root)
│
├── hindi/
│   ├── character-bible.md
│   └── screenplay.md
│
├── tamil/
│   ├── character-bible.md
│   └── screenplay.md
│
└── telugu/
    ├── character-bible.md
    └── screenplay.md
```
**Impact**: Cleaner organization + beat sheet improves all dialect versions.

---

## ⚙️ TECHNICAL CHANGES

### **File Naming Convention**:

**Single Dialect**:
- `character-bible.md` (root)
- `screenplay.md` (root)

**Multi-Dialect**:
- `{dialect}/character-bible.md` (folder)
- `{dialect}/screenplay.md` (folder)

### **Context Requirements Updated**:

All workflows now read:
```yaml
context_requirements:
  read:
    - "project/{project_name}/genre-analysis.md"
    - "project/{project_name}/story-synopsis.md"
    - "project/{project_name}/beat-sheet.md"          # NEW!
    - "project/{project_name}/character-bible.md (or dialect-specific versions)"
    - "project/{project_name}/screenplay.md (or dialect-specific versions)"
```

---

## 📊 MIGRATION GUIDE

### **Existing Single-Dialect Projects**:
✅ **No action required** - Continue using root-level files.

### **Existing Multi-Dialect Projects** (if any exist):
If you have old flat structure:
```
character-bible-hindi.md
character-bible-tamil.md
screenplay-hindi.md
screenplay-tamil.md
```

Migrate to folder structure:
```bash
# Create dialect folders
mkdir -p project/your-film/hindi
mkdir -p project/your-film/tamil

# Move files
mv character-bible-hindi.md hindi/character-bible.md
mv character-bible-tamil.md tamil/character-bible.md
mv screenplay-hindi.md hindi/screenplay.md
mv screenplay-tamil.md tamil/screenplay.md
```

---

## 🎓 NEW BEAT SHEET QUESTIONS (8 Questions)

**Structure Approach** (Q1-Q3):
- Q1: Story structure type (three-act/five-act/non-linear/circular/single timeline)
- Q2: Opening hook strategy (in medias res/slow burn/mystery/character intro/world building)
- Q3: Pacing rhythm (fast-paced/measured/slow burn/uneven/relentless)

**Emotional Beats** (Q4-Q6):
- Q4: Emotional highs (where audience should feel excited - list 2-3 moments)
- Q5: Emotional lows (where audience should feel tense - list 2-3 moments)
- Q6: Climax emotional peak (triumph/tragedy/bittersweet/shock/catharsis/ambiguous)

**Beat Detail Level** (Q7-Q8):
- Q7: Beat granularity (macro 10-15 beats/moderate 20-30/micro 40+/minimal 5-8)
- Q8: Scene transition notes (yes/no/selective)

---

## ✅ TESTING CHECKLIST

**For Implementers**:
- [ ] Beat sheet workflow creates beat-sheet.md correctly
- [ ] Multi-dialect character bible creates folder structure
- [ ] Multi-dialect screenplay detects folders correctly
- [ ] Shot breakdown reads beat-sheet for emotional mapping
- [ ] Single-dialect projects still work (root-level files)
- [ ] Multi-dialect projects use new folder structure
- [ ] All context requirements resolve correctly
- [ ] Dialect-adaptation-guide examples updated

---

## 🚀 BENEFITS SUMMARY

**Beat Sheet Workflow**:
- ✅ Professional industry-standard tool added
- ✅ Catches pacing issues before screenplay writing
- ✅ Maps emotional progression clearly
- ✅ Universal for all dialects (efficiency)

**Folder Structure**:
- ✅ Cleaner project organization
- ✅ Easier dialect management
- ✅ Scalable (add/remove dialects easily)
- ✅ Industry-standard approach
- ✅ Better for version control

**Integration**:
- ✅ All workflows updated consistently
- ✅ Dependency chain preserved
- ✅ Documentation updated
- ✅ Backward compatible (single-dialect unchanged)

---

## 📞 QUESTIONS?

For questions about these changes:
- Check workflow yamls: `beat-sheet.yaml`, `character-bible.yaml`, `screenplay.yaml`, `shot-breakdown.yaml`
- Review this changelog
- Check dialect-adaptation-guide.md for updated examples
- Contact BMAD-FILM framework maintainers

═══════════════════════════════════════════════════════

**Version**: 3.1.0
**Previous Version**: 3.0.0-multi-dialect
**Breaking Changes**: Folder structure for multi-dialect (migration required for existing multi-dialect projects)
**Backward Compatible**: Yes (single-dialect projects unaffected)

🎬 **Happy Filmmaking with Beat Sheets and Organized Multi-Dialect Structure!** 🌏
