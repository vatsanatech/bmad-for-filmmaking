# DIALECT & MULTI-LANGUAGE ADAPTATION GUIDE
## BMAD-FILM Framework

**Version**: 1.0.0
**Created**: 2026-02-18
**Purpose**: Guide for creating multi-dialect Indian content from single story

═══════════════════════════════════════════════════════

## 🌏 OVERVIEW

BMAD-FILM supports creating content in **multiple Indian languages/dialects** from a single story foundation.

**Use Cases**:
- Pan-India releases (Hindi + Tamil + Telugu + others)
- Regional OTT content (same story, local language)
- Cost-efficient multi-language production
- Cultural localization for different markets

**Example**: Create "The Last Celebration" in:
- Hindi (for North India, general audience)
- Tamil (for Tamil Nadu market)
- Telugu (for Andhra Pradesh/Telangana)
- Bengali (for West Bengal market)

═══════════════════════════════════════════════════════

## 📊 LOCALIZATION LEVELS

### **LEVEL 1: DIALOGUE ONLY** (Easiest, Fastest)

**What Changes**: Only dialogue translated to regional language
**What Stays Same**: Character names, locations, culture, costumes, everything else

**Best For**:
- Urban/modern stories (no strong regional identity)
- Quick multi-language releases
- Budget productions

**Example**:
```
Hindi: "Aap kaise hain?"
Tamil: "Neengal eppadi irukeenga?"
Telugu: "Meeru ela unnaru?"
```
**Character Name**: Arjun (same in all versions)
**Setting**: Generic city (same)

---

### **LEVEL 2: DIALOGUE + NAMES** (Moderate)

**What Changes**: Dialogue + character names culturally adapted
**What Stays Same**: Locations, culture, costumes

**Best For**:
- Stories where names matter for cultural authenticity
- Regional audience preference
- Moderate budget

**Example**:
```
Hindi:  Arjun says "Kya ho raha hai?"
Tamil:  Arun says "Enna nadakkuthu?"
Telugu: Aravind says "Emi jarigindi?"
```

**Character Names**:
- Hindi: Arjun, Priya
- Tamil: Arun, Priya
- Telugu: Aravind, Priya
- Bengali: Arnab, Priya

---

### **LEVEL 3: DIALOGUE + CULTURE** (Deep)

**What Changes**: Dialogue + names + cultural references (festivals, food, customs)
**What Stays Same**: Location geography, costumes mostly

**Best For**:
- Stories with strong cultural elements
- Regional festival-based stories
- Authentic regional content

**Example**:
```
Hindi:  "Diwali ki raat ko..."
Tamil:  "Pongal ki raat ko..."
Telugu: "Sankranti ki raat ko..."
Bengali: "Durga Puja ki raat ko..."
```

**Cultural References**:
- Hindi: Diwali, samosas, rangoli
- Tamil: Pongal, idli-dosa, kolam
- Telugu: Sankranti, biryani, muggu
- Bengali: Durga Puja, rasgulla, alpana

---

### **LEVEL 4: FULL CULTURAL ADAPTATION** (Complete, Most Authentic)

**What Changes**: Everything - dialogue, names, culture, locations, attire
**What Stays Same**: Core story beats, character arcs

**Best For**:
- Regional cinema targeting specific state
- High-budget multi-language production
- Stories deeply rooted in culture

**Example**:
```
Hindi Version:
- Setting: Delhi wedding in Punjabi family home
- Character: Arjun (DJ from Karol Bagh)
- Attire: Kurta-pajama, turban
- Culture: Bhangra music, tandoori food

Tamil Version:
- Setting: Chennai wedding in Mylapore temple hall
- Character: Arun (DJ from T Nagar)
- Attire: Veshti-shirt, angavastram
- Culture: Carnatic fusion music, filter coffee, kolam

Bengali Version:
- Setting: Kolkata wedding in Ballygunge community hall
- Character: Arnab (DJ from Park Street)
- Attire: Kurta-dhoti, gamcha
- Culture: Rabindra Sangeet fusion, mishti, alpana
```

═══════════════════════════════════════════════════════

## 🎬 WORKFLOW INTEGRATION

### **Step-by-Step Process**:

#### **1. STORY SYNOPSIS** (Universal Foundation)
- Create region-agnostic story
- Use generic settings ("a village", "a city")
- Universal character types
- Minimal cultural specificity

**Output**: `story-synopsis.md` (single file, works for all dialects)

---

#### **2. CHARACTER BIBLE** (Dialect Selection Point)

**Step 0 Questions**:
- Q0a: Single dialect or multi-dialect?
- Q0b: Which dialects? (Select: Hindi, Tamil, Telugu, etc.)
- Q0c: Localization depth? (Dialogue only / Full cultural)
- Q0d: Names strategy? (Universal or adapted)
- Q0e: Locations? (Generic or dialect-specific)

**IF MULTI-DIALECT SELECTED**:
- Creates separate `character-bible-{dialect}.md` files
- Each file has culturally-appropriate character profiles

**Example**:
```
hindi/character-bible.md
tamil/character-bible.md
telugu/character-bible.md
bengali/character-bible.md
```

Each contains:
- Localized character names (if Q0d = adapt)
- Regional speech patterns
- Cultural backgrounds
- Dialect-specific sample dialogue

---

#### **3. SCREENPLAY** (Auto-Dialect Creation)

**Step 0**: Auto-detects character-bible files
**Result**: Creates screenplay per dialect automatically

**Files Created**:
```
hindi/screenplay.md   (Hindi/Hinglish dialogue)
tamil/screenplay.md   (Tamil dialogue)
telugu/screenplay.md  (Telugu dialogue)
bengali/screenplay.md (Bengali dialogue)
```

**Same Structure, Localized Dialogue**:
- Scene headings: Same
- Action lines: Same (or culturally adapted if Level 4)
- Dialogue: Regional language
- Cultural references: Per localization level

---

#### **4. SHOT BREAKDOWN** (Master + Dialect Notes)

**Approach**: Single master shooting script + dialect appendix

**File**: `shot-breakdown.md` (one file)

**Structure**:
- Universal camera/visual plan (shots, angles, movement)
- Dialect-specific production notes:
  - Costume variations per dialect
  - Prop differences (cultural items)
  - Location signage (regional scripts)
  - Cultural elements

**Benefit**: Shoot efficiently - same camera setup, swap costumes/props

═══════════════════════════════════════════════════════

## 🎯 BEST PRACTICES

### **1. Name Adaptation Strategy**

**Universal Names** (Easier, but less authentic):
- Use pan-India names that work everywhere
- Examples: Arjun, Priya, Rohan, Neha
- Benefit: Simpler production, casting

**Culturally Adapted Names** (Authentic, but more work):
- Adapt names to regional preferences
- Examples:
  - North: Arjun, Vikram, Priya
  - Tamil: Arun, Vijay, Priya
  - Telugu: Aravind, Vikram, Priya
  - Bengali: Arnab, Bikram, Priyanka
  - Malayalam: Arun, Vineeth, Priya

**Best Practice**: Use universal for modern urban stories, adapted for regional/traditional stories.

---

### **2. Cultural References**

**Generic** (Dialogue-only level):
```
"Festival ki raat hai" (works for all)
```

**Specific** (Cultural adaptation level):
```
Hindi:    "Diwali ki raat hai"
Tamil:    "Pongal ki raat hai"
Telugu:   "Sankranti ki raat hai"
Bengali:  "Durga Puja ki raat hai"
```

**Best Practice**: Keep festivals generic if not central to plot. Make specific if culturally important.

---

### **3. Location Strategy**

**Region-Agnostic** (Recommended for multi-dialect):
```
- "Ek shahar mein" (in a city)
- "Ek gaon mein" (in a village)
- "Community hall" (generic venue)
```

**Dialect-Specific** (Full cultural adaptation):
```
Hindi:    Delhi, Mumbai, specific Punjabi household
Tamil:    Chennai, Madurai, specific Tamil home
Telugu:   Hyderabad, Vijayawada, specific Telugu home
Bengali:  Kolkata, specific Bengali para
```

**Best Practice**: Region-agnostic for efficiency. Specific if budget allows separate shoots.

---

### **4. Costume & Attire**

**Universal** (Modern/Urban):
- Jeans, t-shirts, western casuals (works everywhere)
- Formal suits (pan-India)

**Regional** (Traditional/Cultural):
```
Hindi/North:  Kurta-pajama, salwar-kameez, lehenga
Tamil:        Veshti-shirt, half-saree, pattu pavadai
Telugu:       Pancha-jubba, langa-voni, pattu langa
Bengali:      Dhoti-punjabi, saree (tant/silk), kurta-dhoti
```

**Best Practice**: Modern urban = universal costumes. Traditional/village = regional costumes.

---

### **5. Dialogue Language Mix**

**Hindi**:
- 60-70% Hindi + 30-40% English (Hinglish)
- Code-switching natural for urban characters

**Regional Languages**:
- Tamil: Pure Tamil OR Tamil-English mix (Tanglish)
- Telugu: Pure Telugu OR Telugu-English mix
- Bengali: Pure Bengali OR Bengali-English mix

**Best Practice**: Match language purity to character education/background.

---

### **6. Production Efficiency**

**EFFICIENT MULTI-DIALECT SHOOTING**:

1. **Same Camera Setups**:
   - Frame shots ONCE (universal blocking)
   - Use same shot list for all dialects

2. **Batch by Location**:
   - Shoot ALL Hindi scenes at location
   - Swap costumes/props → Shoot ALL Tamil scenes
   - Swap again → Shoot ALL Telugu scenes

3. **Re-shoot Only Cultural Elements**:
   - Close-ups of regional signage
   - Cultural prop inserts (kolam, alpana, rangoli)
   - Festival-specific decorations

4. **Actor Dubbing Option**:
   - Shoot in one language (Hindi)
   - Dub to other languages in post
   - OR cast regional actors per dialect

**Time Savings**: Shoot 3 dialect versions in ~1.5x time of single version (not 3x)

═══════════════════════════════════════════════════════

## 📋 DECISION TREE

```
START: Do you want multi-dialect content?
├─ NO → Single Dialect (Hindi default)
│  └─ Simple workflow, single files
│
└─ YES → Multi-Dialect
   │
   ├─ Urban/Modern Story?
   │  └─ YES → LEVEL 1 or 2 (Dialogue only / Dialogue+Names)
   │     ├─ Localization: Minimal
   │     ├─ Costumes: Universal modern
   │     └─ Locations: Generic city
   │
   └─ Traditional/Regional Story?
      └─ YES → LEVEL 3 or 4 (Culture / Full Adaptation)
         ├─ Localization: Deep
         ├─ Costumes: Regional traditional
         └─ Locations: Dialect-specific cities
```

═══════════════════════════════════════════════════════

## 🎥 EXAMPLES

### **EXAMPLE 1: Urban Thriller (Dialogue Only)**

**Story**: Corporate espionage in a tech company
**Setting**: Generic metro city
**Localization**: Level 1 (Dialogue Only)

**Files**:
- `story-synopsis.md` (universal)
- `beat-sheet.md` (universal)
- `character-bible.md` (single - names: Arjun, Priya)
- `hindi/screenplay.md` (Hindi dialogue)
- `tamil/screenplay.md` (Tamil dialogue - same Arjun, Priya names)
- `telugu/screenplay.md` (Telugu dialogue)
- `shot-breakdown.md` (universal - no regional notes needed)

**Production**: Shoot ONCE, dub to multiple languages in post.

---

### **EXAMPLE 2: Festival Romance (Full Cultural Adaptation)**

**Story**: Love story during regional festival
**Setting**: Specific regional cities
**Localization**: Level 4 (Full Cultural)

**Files**:
- `story-synopsis.md` (generic "festival" theme)
- `beat-sheet.md` (universal story beats)
- `hindi/character-bible.md` (Arjun, Delhi, Diwali references)
- `tamil/character-bible.md` (Arun, Chennai, Pongal references)
- `bengali/character-bible.md` (Arnab, Kolkata, Durga Puja references)
- `hindi/screenplay.md` (Diwali celebration, Delhi locations)
- `tamil/screenplay.md` (Pongal celebration, Chennai locations)
- `bengali/screenplay.md` (Durga Puja, Kolkata locations)
- `shot-breakdown.md` (master + detailed dialect notes for costumes, decorations)

**Production**:
- Separate shoots OR same shoot with costume/decor swaps
- Regional actors per version
- Cultural consultants per dialect

═══════════════════════════════════════════════════════

## ⚠️ COMMON MISTAKES

### **❌ MISTAKE 1: Direct Translation**
```
❌ Hindi: "Mujhe ghar jana hai"
❌ Tamil: "Enakku veetuku poga vendum" (literal word-by-word)
```
**Problem**: Loses natural speech, sounds translated.

**✅ CORRECT**: Write naturally in target language
```
✓ Tamil: "Naan veetuku ponum" (natural Tamil phrasing)
```

---

### **❌ MISTAKE 2: Ignoring Regional Speech Patterns**
```
❌ Tamil character using "aap/tum" structure
```
**Problem**: Tamil has different pronoun usage (neengal/nee, not aap/tum).

**✅ CORRECT**: Use regional speech patterns
```
✓ Tamil: "Neengal eppadi irukeenga?" (natural pronoun usage)
```

---

### **❌ MISTAKE 3: Cultural Insensitivity**
```
❌ Using North Indian festival in Tamil version without changing
```
**Problem**: Feels inauthentic to regional audience.

**✅ CORRECT**: Adapt culturally
```
✓ Hindi: Diwali references
✓ Tamil: Pongal references
✓ Bengali: Durga Puja references
```

---

### **❌ MISTAKE 4: Over-Localization**
```
❌ Changing core story beats per dialect
```
**Problem**: No longer the "same story", becomes different films.

**✅ CORRECT**: Same story, local flavor
```
✓ Story beats identical
✓ Only dialogue/culture/names adapted
✓ Character arcs unchanged
```

═══════════════════════════════════════════════════════

## 🎓 RESOURCES

### **Language Consultants Recommended**:
- Hire native speakers for authentic dialogue
- Cultural consultants for regional references
- Dialect coaches for actors

### **Regional Cinema References**:
- **Tamil**: Mani Ratnam, Vetrimaaran films
- **Telugu**: S.S. Rajamouli, Trivikram films
- **Bengali**: Satyajit Ray, Rituparno Ghosh films
- **Malayalam**: Anjali Menon, Lijo Jose Pellissery films

### **Script Formats**:
- Use Unicode for regional scripts (not ASCII transliteration)
- Tamil: Tamil Unicode fonts
- Telugu: Telugu Unicode fonts
- Bengali: Bengali Unicode fonts

═══════════════════════════════════════════════════════

## ✅ SUCCESS CHECKLIST

**Before Starting Multi-Dialect Production**:

- [ ] Story works in region-agnostic format (no hard regional locks)
- [ ] Budget allows for localization depth chosen
- [ ] Regional actors available OR dubbing plan ready
- [ ] Cultural consultants identified per dialect
- [ ] Production team understands multi-dialect workflow
- [ ] Post-production plan for multiple versions
- [ ] Distribution strategy per regional market
- [ ] Legal clearances for all languages/regions

**During Production**:

- [ ] Character-bible created per dialect (if multi-dialect)
- [ ] Screenplay dialogue natural in each language (not translated)
- [ ] Cultural references appropriate per region
- [ ] Costumes match regional aesthetic (if full cultural adaptation)
- [ ] Props culturally accurate
- [ ] Location signage in regional scripts

**Post-Production**:

- [ ] Dubbing quality natural (if dubbing approach)
- [ ] Subtitles accurate for cross-regional viewing
- [ ] Cultural elements preserved in editing
- [ ] Music/sound design appropriate per version
- [ ] Final deliverables per dialect ready

═══════════════════════════════════════════════════════

## 📞 SUPPORT

For questions about multi-dialect workflow:
- Check workflow yamls: `character-bible.yaml`, `screenplay.yaml`, `shot-breakdown.yaml`
- Review this guide
- Contact BMAD-FILM framework maintainers

═══════════════════════════════════════════════════════

**Created with**: BMAD-FILM Interactive Multi-Dialect Framework
**Purpose**: Enabling authentic Indian regional content from single story foundation
**Vision**: One story, many voices, cultural authenticity preserved

🎬 **Make content that speaks every Indian language!** 🌏
