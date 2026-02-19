# BMAD-FILM Distribution Checklist

**What to Push to Repo (For Framework Maintainer)**

---

## ✅ Files to TRACK (Push to Repo)

### **Core Framework**
```
✓ .bmad-film/
  ✓ agents/                    (All 13 agent definitions)
  ✓ workflows/                 (All workflow YAML files)
  ✓ *.md files                 (All guides and docs)
```

### **Documentation**
```
✓ README.md
✓ QUICK-START.md
✓ QUICK-REFERENCE.md
✓ SYSTEM-SUMMARY.md
✓ UPDATES.md
✓ DISTRIBUTION-CHECKLIST.md (this file)
✓ project/README.md          (Directory explanation)
```

### **Configuration**
```
✓ .gitignore                  (Excludes user projects)
```

---

## ❌ Files to IGNORE (Don't Push)

### **User Projects**
```
✗ project/*/                  (All user film projects)
✗ project/band-darwaza/
✗ project/awaaz-ka-chehra/
✗ project/sharma-ji-ka-beta/
✗ project/last-selfie/
```

### **System Files**
```
✗ .DS_Store
✗ *.log
✗ *-old.md
✗ *-backup.md
```

---

## 📋 Pre-Push Checklist

Before pushing updates:

### **1. Test Locally**
```bash
# Clean test (simulate new user)
cd /tmp
git clone [your-repo]
cd bmad-for-filmmaking

# Test full workflow
"Create a 1-minute test film. Call it test-project."
"test-project"  # Character bible
"test-project"  # Screenplay
"test-project"  # Shot breakdown

# Verify outputs
ls -la project/test-project/
```

### **2. Verify .gitignore**
```bash
# Check what will be pushed
git status

# Should NOT see:
# - project/*/  (user projects)
# - .DS_Store
# - *.log

# Should see:
# - .bmad-film/
# - *.md docs
```

### **3. Update Documentation**
```bash
# Update version in UPDATES.md
# Add changes to changelog
# Update SYSTEM-SUMMARY.md if major changes
# Update README.md if needed
```

### **4. Commit and Push**
```bash
git add .
git commit -m "Update agents: [describe changes]"
git push origin main
```

---

## 🔄 Update Types to Push

### **Agent Updates**
```
When: Agent persona refinements, new agents
Files: .bmad-film/agents/*.md
Test: Run workflow with updated agent
```

### **Workflow Updates**
```
When: Workflow improvements, new steps
Files: .bmad-film/workflows/**/*.yaml
Test: Execute full workflow
```

### **Documentation Updates**
```
When: Guides improved, new features documented
Files: *.md (all documentation)
Test: Read through for accuracy
```

---

## 🎯 What Users Get

When users `git pull`:

### **✓ They Get**
- Updated agents (improved personas)
- Enhanced workflows (better processes)
- New documentation (clearer guides)
- Bug fixes
- New features

### **✗ They Don't Lose**
- Their project files (untouched)
- Their local setup (preserved)
- Their creative work (safe)

---

## 📦 Directory Structure (What's Tracked)

```
bmad-for-filmmaking/              ← REPO ROOT
│
├── .bmad-film/                   ✓ TRACKED (Framework)
│   ├── agents/                   ✓ All agents
│   ├── workflows/                ✓ All workflows
│   ├── QUICK-REFERENCE.md        ✓ Cheat sheet
│   └── ...                       ✓ Other docs
│
├── project/                      ✗ IGNORED (Except README)
│   ├── README.md                 ✓ TRACKED (Explains directory)
│   └── */                        ✗ IGNORED (User projects)
│
├── README.md                     ✓ TRACKED
├── QUICK-START.md                ✓ TRACKED
├── SYSTEM-SUMMARY.md             ✓ TRACKED
├── UPDATES.md                    ✓ TRACKED
├── DISTRIBUTION-CHECKLIST.md     ✓ TRACKED
└── .gitignore                    ✓ TRACKED
```

---

## 🚀 Quick Push Workflow

```bash
# 1. Make changes to agents/workflows
vim .bmad-film/agents/dialogue-writer.md

# 2. Test locally
"Create test film"

# 3. Check what's changed
git status
git diff

# 4. Stage framework changes only
git add .bmad-film/
git add *.md

# 5. Commit with clear message
git commit -m "Improve dialogue-writer agent: [specific change]"

# 6. Push
git push origin main

# 7. Announce (optional)
# Post update notification to users
```

---

## 📝 Commit Message Guidelines

### **Good Commit Messages**
```
✓ "Add Haryanvi dialect support to dialogue-writer"
✓ "Fix character-bible workflow: improve arc tracking"
✓ "Update thriller-specialist: enhance twist generation"
✓ "Docs: Add troubleshooting section to QUICK-START"
```

### **Bad Commit Messages**
```
✗ "Update stuff"
✗ "Fix"
✗ "Changes"
✗ "WIP"
```

---

## 🎓 For Framework Maintainer

### **Regular Maintenance**
- Weekly: Review agent performance
- Bi-weekly: Update documentation
- Monthly: Major feature additions
- As needed: Bug fixes

### **Version Numbering**
```
Major.Minor.Patch

1.0.0 → Initial release
1.1.0 → New agent/workflow
1.0.1 → Bug fix
2.0.0 → Breaking change
```

### **Changelog Format**
```markdown
## v1.1.0 (2025-02-20)

### Added
- New agent: Period-drama specialist
- Workflow: Festival strategy

### Improved
- Dialogue-writer: Better Hindi-English balance
- Shot-breakdown: More detailed coverage notes

### Fixed
- Character-bible: Arc tracking bug
- Screenplay: Scene numbering issue
```

---

## 🔒 What's Protected

The `.gitignore` ensures:

```
Protected from tracking:
✗ project/*/              User's creative work
✗ .DS_Store               System files
✗ *.log                   Debug logs
✗ *-old.md                Backup files

Safe to update:
✓ .bmad-film/             Framework core
✓ Documentation           All guides
✓ Configuration           .gitignore, etc.
```

---

## 🎬 Distribution Flow

```
MAINTAINER                    USERS
    │                          │
    │ 1. Update agents         │
    │ 2. Test locally          │
    │ 3. git push              │
    │                          │
    │ ──────── UPDATE ────────→│
    │                          │
    │                          │ 4. git pull
    │                          │ 5. Keep working
    │                          │    (projects safe)
    │                          │
    │                          ✓ Updated framework
    │                          ✓ Kept their work
```

---

## ✅ Final Check Before Push

- [ ] Tested all workflows locally
- [ ] No user project files in commit
- [ ] Documentation updated
- [ ] Version number updated (if major change)
- [ ] Commit message is clear
- [ ] .gitignore is correct

```bash
git status   # Should show only framework files
git push     # Deploy updates
```

---

**Framework files = Shared**
**User projects = Private**
**Updates = Seamless**

🎬 Push updates confidently!
