# 📋 Automation Rules & Folder Organization

**Last Updated:** 2026-04-30  
**Purpose:** Central reference for how Claude should organize and handle content creation

---

## Rule 1: New Slide Deck Creation 🎯
**Status:** Active

When you request a new slide deck, Claude will automatically save it here:
```
📁 Library/slides/[slide-deck-name]/
   ├── learning/     (main slide content goes here)
   └── assets/       (images, files, resources)
```

**Example paths:**
- `Library/slides/product-thinking-101/learning/`
- `Library/slides/ux-research-methods-intro/learning/`

**What triggers this:** Any request like:
- "Create a slide deck for..."
- "Make slides about..."
- "Design a presentation for..."

**File naming convention:** Use lowercase-hyphens (no spaces)
- ✅ `product-thinking-intro.pptx`
- ❌ `Product Thinking Intro.pptx`

---

## Rule 2: Design Consistency 🎨
**Status:** Active

When creating slide decks, Claude will reference the **Templates folder** to ensure visual consistency:
```
📁 Templates/
   ├── design-system/
   ├── color-palette.md
   ├── typography-guide.md
   └── slide-templates/
```

**What this means:**
- Check Templates for existing design standards before creating new slides
- Reuse color schemes, typography, and layouts from Templates
- If templates don't exist for a specific deck, create them in Templates first
- Maintain consistent branding across all slides

**Design checklist before finalizing slides:**
- [ ] Colors match approved palette from Templates
- [ ] Typography follows established font standards
- [ ] Layout structure aligns with slide-templates
- [ ] Assets stored in corresponding `assets/` folder

---

## Rule 3: Updating These Rules ✏️
**How to modify this file:**

1. **Location:** `/Users/winnie.nguyen/Library/CloudStorage/GoogleDrive-nguyenphuctuongvan@gmail.com/My Drive/03_Mentoring/AUTOMATION_RULES.md`

2. **To request changes:** Just tell Claude:
   - "Update Rule 1 to..."
   - "Add a new automation rule for..."
   - "Change the slide folder location to..."

3. **I will update this file directly** and save the changes so you can reference it anytime

---

## Additional Settings (Add more rules here)

### Rule 4: [Your custom rule name]
**Status:** [Active/Draft]

*Add your own automation preferences here*

---

## Quick Reference Table

| Trigger | Action | Output Folder |
|---------|--------|---------------|
| "Create slide deck" | Generate pptx + organize | `Library/slides/[name]/learning/` |
| Check before finalizing | Reference Templates folder | `Templates/` |
| Need to adjust rules | Edit this file | `AUTOMATION_RULES.md` |

---

**📍 How to find this file:**
- In your Mentoring folder: `03_Mentoring/AUTOMATION_RULES.md`
- Or search: "AUTOMATION_RULES.md"
- It's always in the root of your 03_Mentoring folder

**💡 Pro tip:** This file is your source of truth. Claude will check it before creating slides, so keeping it updated ensures consistent behavior!
