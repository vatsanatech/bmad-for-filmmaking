# BMAD-FILM Framework Updates

**How to Get Latest Agents and Workflows**

---

## 🚀 Getting Updates (Super Simple)

### **Step 1: Pull Latest Framework**
```bash
cd bmad-for-filmmaking
git pull
```

That's it! ✓

---

## 🔄 What Gets Updated

When you pull:

### **✓ Framework Files (Updated)**
- `.bmad-film/agents/` - Agent improvements
- `.bmad-film/workflows/` - Workflow enhancements
- Documentation - Guides and references
- Bug fixes and new features

### **✗ Your Projects (Untouched)**
- `project/your-project-name/` - Your work stays safe
- All your film outputs preserved
- No conflicts, no overwrites

---

## 🎯 Update Workflow

```
Your Work              Framework Updates
    ↓                        ↓
project/               .bmad-film/
├── my-film/           ├── agents/        ← Updated
│   ├── screenplay.md  │   └── improved!
│   └── ...            └── workflows/     ← Updated
    ↑                      └── enhanced!
    └─ NEVER TOUCHED
```

---

## 📊 Version Info

Current Version: 1.1.0

### **What's New in v1.1.0** (2025-02-17)
✓ **NEW**: Shooting script format for shot breakdown (industry-standard)
✓ Genre-specific visual languages (thriller/romance/horror/comedy/action)
✓ Professional format matching Bollywood production standards
✓ Updated shot-breakdown-specialist agent with cinematography training

### **What's New in v1.0.0** (2025-02-17)
✓ 13 genre-trained agents
✓ Two-agent screenplay model (Bollywood authentic)
✓ Clean project structure (all files in one folder)
✓ Complete documentation with feedback loops
✓ Shot breakdown specialist (technical format)
✓ Dialect control (Hindi, Haryanvi, Hinglish, etc.)

---

## 🆘 If Something Breaks After Update

### **Quick Fix**
```bash
# Check what changed
git status

# If agents aren't working
git log --oneline -5

# Restore previous version if needed
git checkout HEAD~1 .bmad-film/agents/specific-agent.md
```

### **Safe Reset** (if needed)
```bash
# This restores framework but keeps YOUR projects
git reset --hard origin/main
```

**Your projects are safe** - they're not tracked by git.

---

## 🔔 Update Notifications

Check for updates when:
- New genre agents announced
- Workflow improvements released
- Bug fixes published
- New features added

### **Check Version**
```bash
# See current version
cat UPDATES.md | grep "Current Version"

# See what's new
git log --oneline -10
```

---

## 📦 Update Types

### **Minor Updates** (Weekly/Bi-weekly)
- Agent persona refinements
- Workflow tweaks
- Documentation improvements
- Bug fixes

**Action**: `git pull` and continue working

### **Major Updates** (Monthly/Quarterly)
- New agents (genre specialists, new roles)
- New workflows (production, post-production)
- Breaking changes (rare)
- New features

**Action**: `git pull` and read CHANGELOG

---

## 🎓 Update Best Practices

### **Before Pulling Updates**
```bash
# Check if you have uncommitted work on framework files
git status

# If you modified framework files (advanced users only)
git stash
git pull
git stash pop
```

### **After Pulling Updates**
```bash
# Quick test - create a test project
"Create a 1-minute test film. Call it framework-test."

# If works → Updates successful ✓
# If breaks → Report issue
```

---

## 🔧 Troubleshooting Updates

### **Problem: Pull fails with conflicts**
```bash
# Your projects are safe - these are framework conflicts
# Choose one:

# Option A: Keep your framework changes (advanced)
git stash
git pull
git stash pop

# Option B: Use latest framework (recommended)
git reset --hard origin/main
git pull
```

### **Problem: Agents not working after update**
```bash
# Check agent files weren't corrupted
ls -la .bmad-film/agents/
ls -la .bmad-film/workflows/

# Re-pull if needed
git pull --force
```

### **Problem: New workflow not appearing**
```bash
# Check workflows directory
ls -la .bmad-film/workflows/development/
ls -la .bmad-film/workflows/pre-production/

# Verify file permissions
chmod -R u+rw .bmad-film/
```

---

## 🎯 What You NEVER Need to Update Manually

✗ Project files - Created by workflows
✗ Agent definitions - Managed by framework
✗ Workflow YAML - Managed by framework
✗ Documentation - Updated with pull

---

## 💡 Pro Tips

1. **Pull regularly** - Get improvements and bug fixes
2. **Read changelogs** - Know what changed
3. **Test after major updates** - Run a quick test project
4. **Your projects are safe** - They're never touched by updates
5. **Report issues** - Help improve the framework

---

## 🚦 Update Safety

**SAFE**: Your creative work (projects) ✓
**SAFE**: Your workflow outputs ✓
**SAFE**: Your local setup ✓

**UPDATED**: Agents, workflows, documentation
**IMPROVED**: Quality, features, performance

---

## 📞 Getting Help

**Before updating**:
```
"How do I update the framework?"
```

**After updating**:
```
"Something broke after update - [describe issue]"
```

**Checking version**:
```
"What version am I running?"
```

---

## 🎬 Update and Continue

```bash
git pull    # Get latest
[Review changes]
Continue creating films! 🎬
```

**Framework updates ≠ Project disruption**

Your work is safe. Pull anytime. Keep creating.

---

**Current Version**: 1.0.0
**Last Updated**: 2025-02-17
**Next Update**: TBD (follow repo for announcements)
