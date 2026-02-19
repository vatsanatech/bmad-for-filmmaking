# BMAD-FILM FRAMEWORK FOLDER STRUCTURE
**Version**: 3.1.0

Complete organizational structure for the BMAD-FILM framework.

═══════════════════════════════════════════════════════

## 📂 ROOT STRUCTURE

```
bmad-for-filmmaking/
├── .bmad-film/                 # Framework core
├── project/                    # User projects
├── .claude/                    # Claude Code integration
├── README.md                   # Main documentation
└── package.json                # Project metadata
```

═══════════════════════════════════════════════════════

## 🎯 .bmad-film/ (Framework Core)

```
.bmad-film/
├── agents/                     # AI agent definitions
│   ├── master-story-director.md
│   ├── character-developer.md
│   ├── screenplay-structure-writer.md
│   ├── dialogue-writer.md
│   ├── shot-breakdown-specialist.md
│   └── genre-specialists/
│       ├── suspense-architect.md
│       ├── romance-architect.md
│       ├── horror-architect.md
│       ├── comedy-architect.md
│       ├── drama-architect.md
│       ├── action-architect.md
│       ├── musical-architect.md
│       └── social-cinema-architect.md
│
├── workflows/                  # Workflow definitions
│   ├── development/
│   │   ├── story-synopsis.yaml
│   │   ├── character-bible.yaml
│   │   ├── beat-sheet.yaml          ✨ NEW!
│   │   └── screenplay.yaml
│   ├── pre-production/
│   │   └── shot-breakdown.yaml
│   ├── production/
│   │   └── (future production workflows)
│   ├── post-production/
│   │   └── (future post-production workflows)
│   └── distribution/
│       └── (future distribution workflows)
│
├── guides/                     # Documentation & guides
│   ├── CHANGELOG-v3.1.0.md                ✨ Version changelog
│   ├── dialect-adaptation-guide.md        📘 Multi-dialect guide
│   ├── BOLLYWOOD-LANGUAGE-GUIDE.md        📘 Language standards
│   ├── INTERACTIVE-FILMMAKING-FRAMEWORK.md 📘 Framework overview
│   ├── COMPLETE-WORKFLOW-GUIDE.md         📘 All workflows
│   ├── DEVELOPMENT-WORKFLOW-GUIDE.md      📘 Development phase
│   ├── SCREENPLAY-WORKFLOW-GUIDE.md       📘 Screenplay specifics
│   ├── WORKFLOW-EXECUTION-GUIDE.md        📘 How to run workflows
│   ├── QUESTION-FRAMEWORKS.md             📘 Question design
│   ├── STORY-SYNOPSIS-FORMAT-EXAMPLE.md   📘 Format examples
│   ├── LANGUAGE-STANDARDS-APPLIED.md      📘 Language rules
│   └── QUICK-REFERENCE.md                 📘 Quick ref guide
│
├── templates/                  # Document templates
│   ├── shot-breakdown-template.md
│   └── ai-prompt-template.md
│
├── config/                     # Configuration files
│   └── bmad-film-config.yaml
│
├── manifests/                  # System manifests
│   └── (future manifest files)
│
├── tasks/                      # Task templates
│   └── (future task definitions)
│
└── FOLDER-STRUCTURE.md         # This file ✨ NEW!
```

═══════════════════════════════════════════════════════

## 🎬 project/ (User Projects)

### **Single-Dialect Project Structure**:
```
project/film-name/
├── genre-analysis.md          # Step 1: Genre + visual language
├── story-synopsis.md          # Step 2: Story (2 versions)
├── beat-sheet.md              # Step 3: Beat-by-beat breakdown ✨ NEW!
├── character-bible.md         # Step 4: Character profiles
├── screenplay.md              # Step 5: Full screenplay
└── shot-breakdown.md          # Step 6: Shooting script
```

### **Multi-Dialect Project Structure**:
```
project/film-name/
├── genre-analysis.md          # Universal (Step 1)
├── story-synopsis.md          # Universal (Step 2)
├── beat-sheet.md              # Universal (Step 3) ✨ NEW!
├── shot-breakdown.md          # Universal (Step 6)
│
├── hindi/                     # Hindi version
│   ├── character-bible.md    # Step 4
│   └── screenplay.md         # Step 5
│
├── tamil/                     # Tamil version
│   ├── character-bible.md
│   └── screenplay.md
│
├── telugu/                    # Telugu version
│   ├── character-bible.md
│   └── screenplay.md
│
└── bengali/                   # Bengali version
    ├── character-bible.md
    └── screenplay.md
```

═══════════════════════════════════════════════════════

## 🔧 .claude/ (Claude Code Integration)

```
.claude/
└── skills/
    └── bmad-film/
        └── (future Claude Code skill files)
```

═══════════════════════════════════════════════════════

## 📋 FILE NAMING CONVENTIONS

### **Universal Files** (Root of project):
- `genre-analysis.md`
- `story-synopsis.md`
- `beat-sheet.md`
- `shot-breakdown.md`

### **Single-Dialect Files** (Root of project):
- `character-bible.md`
- `screenplay.md`

### **Multi-Dialect Files** (Inside dialect folders):
- `{dialect}/character-bible.md`
- `{dialect}/screenplay.md`

**Supported Dialects**:
- hindi, tamil, telugu, bengali, marathi, punjabi, gujarati, kannada, malayalam, haryanvi, bhojpuri, odia, assamese, rajasthani

═══════════════════════════════════════════════════════

## 🎯 ORGANIZATIONAL PRINCIPLES

### **1. Separation of Concerns**:
- **Framework Core** → `.bmad-film/`
- **User Projects** → `project/`
- **Documentation** → `.bmad-film/guides/`

### **2. Universal vs Dialect-Specific**:
- **Universal** (Story structure doesn't change): genre-analysis, story-synopsis, beat-sheet, shot-breakdown
- **Dialect-Specific** (Language/culture changes): character-bible, screenplay

### **3. Folder Structure for Multi-Dialect**:
- **Clean**: Each dialect in its own folder
- **Scalable**: Easy to add/remove dialects
- **Industry Standard**: Similar to `/en/`, `/fr/` in software

### **4. Documentation Organization**:
- **All guides** in `.bmad-film/guides/`
- **No loose docs** in root or workflow folders
- **Versioned changelogs** for tracking updates

═══════════════════════════════════════════════════════

## ✅ STRUCTURE VERIFICATION CHECKLIST

**Framework Structure**:
- [ ] All agent definitions in `.bmad-film/agents/`
- [ ] All workflow YAML files in `.bmad-film/workflows/{phase}/`
- [ ] All documentation in `.bmad-film/guides/`
- [ ] All templates in `.bmad-film/templates/`
- [ ] No loose markdown files in `.bmad-film/` root
- [ ] No loose markdown files in `.bmad-film/workflows/`

**Project Structure**:
- [ ] All projects in `project/` folder
- [ ] Single-dialect: 6 files at project root
- [ ] Multi-dialect: 4 universal files + dialect folders
- [ ] Each dialect folder contains 2 files (character-bible + screenplay)

**Clean State**:
- [ ] No test/example projects in `project/`
- [ ] All guides organized in `guides/`
- [ ] All documentation up to date with v3.1.0

═══════════════════════════════════════════════════════

## 🚀 WHAT'S NEW IN v3.1.0

1. **Beat Sheet Workflow** → `.bmad-film/workflows/development/beat-sheet.yaml`
2. **Folder Structure for Multi-Dialect** → Dialect folders instead of flat files
3. **Organized Guides** → All documentation in `.bmad-film/guides/`
4. **This Structure Doc** → `.bmad-film/FOLDER-STRUCTURE.md`
5. **Project README** → `project/README.md` template

═══════════════════════════════════════════════════════

**Last Updated**: 2026-02-18
**Framework Version**: 3.1.0
**Maintained By**: BMAD-FILM Team

🎬 **Keep structure clean for efficient filmmaking!** 📁
