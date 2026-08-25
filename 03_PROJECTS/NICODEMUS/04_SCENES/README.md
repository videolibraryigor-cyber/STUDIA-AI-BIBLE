# SCENE CREATION GUIDE (Руководство по созданию сцены)

**Reference:** [STUDIO_CONSTITUTION.md](../../01_GOVERNANCE/STUDIO_CONSTITUTION.md) Part 5  
**Version:** 1.0  
**Last Updated:** 2026-07-24

---

## Overview

This directory contains **scene packages** — the building blocks of the film. Each scene package includes:
- Dramatic intent and continuity plan
- Shot list with descriptions
- Individual shot prompt packages
- Rendered key frames and video
- QC checklist results and approval log

This guide explains how to create a scene from start to finish.

---

## Directory Structure (Per Scene)

```
04_SCENES/
├── README.md                                (this file)
├── SCENE_001/
│   ├── SCENE_PACKAGE_001_v1.0.md           (scene definition)
│   ├── SHOT_001_ESTABLISHING_LIBRARY_v1.0.md
│   ├── SHOT_002_NICODEMUS_CLOSE_v1.0.md
│   ├── SHOT_003_SCROLL_v1.0.md
│   ├── SHOT_PROMPT_001_v1.0.md
│   ├── SHOT_PROMPT_002_v1.0.md
│   ├── SHOT_PROMPT_003_v1.0.md
│   ├── SHOT_001_KEY_FRAME_v1.0.png
│   ├── SHOT_002_KEY_FRAME_v1.0.png
│   ├── SHOT_003_KEY_FRAME_v1.0.png
│   ├── SHOT_001_v1.0.mp4
│   ├── SHOT_002_v1.0.mp4
│   ├── SHOT_003_v1.0.mp4
│   └── ARCHIVE/v0.x/                       (if revisions exist)
├── SCENE_002/
│   └── [same structure]
└── SCENE_003/
    └── [same structure]
```

---

## Prerequisites: Before Creating Any Scene

✅ **Gate 0 Passed:** PROJECT_BIBLE.md approved and locked  
✅ **Creative Authority:** Director committed to project and story arc  
✅ **Asset Library Ready:** CHARACTER_BIBLE.md, ENVIRONMENT_BIBLE.md, PROP definitions ready  
✅ **Team Assembled:** DoP, Production Designer, Character Supervisor, Prompt Engineer available

---

## Step-by-Step Scene Creation Workflow

### STEP 1: Decide Scene Sequence (Director)

**Who:** Director + Story Lead  
**When:** Before any files created  
**What to Decide:**
- Which scene number? (001, 002, 003, etc.)
- What dramatic beat? (Curiosity, Astonishment, Conflict, etc. — from PROJECT_BIBLE.md)
- Approximate duration? (15 seconds, 30 seconds, etc.)
- Estimated shot count? (3-5 shots, typical)
- Location? (Library, exterior, etc.)
- Main character activity? (Reading, contemplating, traveling, etc.)

**Document:** Planning notes (internal; not yet formal file)

### STEP 2: Create Scene Directory

**Who:** Project Coordinator or Director  
**Command:**
```bash
mkdir -p 03_PROJECTS/NICODEMUS/04_SCENES/SCENE_###
```

Replace `###` with scene number (001, 002, etc.)

### STEP 3: Create Scene Package (Director)

**Who:** Director  
**Template:** Copy `04_TEMPLATES/SCENE_PACKAGE_TEMPLATE.md`  
**Output File:** `SCENE_###/SCENE_PACKAGE_###_v1.0.md`

**Sections to Fill:**

**Metadata (YAML Frontmatter):**
```yaml
---
title: "Scene Package: [Brief Title]"
entity: SCENE_###
version: v1.0
status: DRAFT
created: [YYYY-MM-DD]
last_updated: [YYYY-MM-DD]
author: "[Director Name]"
approver: "[Director Name - Self Review]"
approval_date: ""
bible_references:
  - PROJECT_BIBLE.md
  - CHARACTER_BIBLE.md
  - ENVIRONMENT_BIBLE.md
asset_ids:
  - CHAR_NICODEMUS
  - LOC_NICODEMUS_LIBRARY
decision_required: []
notes: ""
---
```

**Status:** CHAR_NICODEMUS

**Purpose:** 2-3 sentences describing dramatic intent  
- Example: "Nicodemus alone in library, beginning to search through old scrolls. Seeking evidence of divine action. Moves from routine scholarly work to desperate questioning."

**Music Timecode:** (if applicable)  
- Example: "00:15-00:45 (30 seconds, second section of score)"

**Director's Intention (2-3 paragraphs):**
- What changes in Nicodemus? (Internal state, emotion, understanding)
- What does viewer feel? (The emotional beat)
- Why does this scene exist? (Narrative function)

**Scene Continuity:**
- **Input State:** How does scene begin? (Nicodemus's emotional/physical state, environment state)
  - Example: "Nicodemus enters library after sunset. Thoughtful but composed. Library empty, undisturbed."
- **Dramatic Action:** What happens in scene? (Plot event or internal realization)
  - Example: "Discovers old scroll containing testimony about miraculous healing. Begins reading. Emotion shifts from curiosity to astonishment."
- **Output State:** How does scene end? (Nicodemus's state after action; environment state)
  - Example: "Nicodemus stands holding scroll, trembling slightly. Library now feels too small. He must seek more answers."

**Shot List (Table):**
- Include rough descriptions of each shot
- Reference dramatic function of each shot
- Note rough duration estimate

| Shot ID | Dramatic Function | Rough Description | Camera | Duration Est. |
|---------|-------------------|-------------------|--------|---|
| SHOT_001 | Establishing | Nicodemus enters library | Wide shot, stationary | 3-5 sec |
| SHOT_002 | Search begins | Close: hands searching shelf | Medium close, slight pan | 5-7 sec |
| SHOT_003 | Discovery | Nicodemus reads scroll | Close-up, eyes, hand movement | 8-10 sec |

**Approval Section (to be filled after director review):**
```
| Director Approval | PENDING |
| QC Approval       | PENDING |
| Date              |         |
```

**Status After Completion:** DRAFT

### STEP 4: Director Self-Review

**Who:** Director  
**What to Check:**
- Is dramatic intent clear?
- Do continuity states connect logically?
- Is each shot tied to story beat?
- Do shots flow properly? (Does scene breathe?)
- Are asset requirements clear?

**Action:** If satisfied, mark status = IN_REVIEW and submit for formal approval (G1 gate)

### STEP 5: Gate 1 Approval (Director)

**Who:** Director (approver role)  
**Reference:** [GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) Gate 1 section

**Gate 1 Checklist:**
- [ ] Dramatic function clear (story purpose)
- [ ] Continuity logical (input → action → output)
- [ ] Each shot serves story beat
- [ ] Asset requirements explicit
- [ ] Scene respects creative laws from PROJECT_BIBLE.md
- [ ] Feasible with available resources

**Outcome:** APPROVED or REVISION NEEDED

**If APPROVED:**
- Status = APPROVED
- Approval Log entry: `| 2026-07-24 | SCENE_001_v1.0 | v1.0 | G1 | APPROVED | Director | Scene approved |`
- Proceed to Step 6

**If REVISION NEEDED:**
- Mark specific sections needing revision
- Director revises; resubmits
- Return to Step 4

### STEP 6: Create Shot Template Files (All Specialists)

**Who:** Director, DoP, Production Designer, Character Supervisor  
**Template:** Copy `04_TEMPLATES/SHOT_PROMPT_TEMPLATE.md`  
**Output Files:** For each shot, create `SHOT_###_v1.0.md` in scene directory

For each shot in Scene Package:

1. **Director Fills:**
   - Creative Brief (2-3 sentences describing this shot's dramatic purpose and emotional intent)

2. **DoP Fills:**
   - Camera: framing (wide/medium/close)
   - Lens: focal length
   - Movement: static/pan/dolly/crane + motivation
   - Lighting logic: which light sources, why

3. **Production Designer Fills:**
   - Environment: specific details of library visible in frame
   - Props: which props visible, in what condition
   - Materials: confirm historical authenticity

4. **Character Supervisor Fills:**
   - Identity: confirm matches CHARACTER_BIBLE.md
   - Costume: state of costume (clean/dusty/torn, etc.)
   - Gaze: where is Nicodemus looking, why
   - Emotion: emotional state matching Creative Brief
   - Continuity: relation to previous/next shot

5. **Each Specialist Signs:** Initials and date in their section

**Metadata (YAML Frontmatter):**
```yaml
---
entity: SHOT_###
version: v1.0
status: DRAFT
scene: SCENE_001
created: [YYYY-MM-DD]
author: "Director/DoP/Designer/Supervisor"
approver: "Prompt Engineer"
approval_date: ""
bible_references:
  - CHARACTER_BIBLE.md
  - ENVIRONMENT_BIBLE.md
  - CAMERA_LIGHTING_BIBLE.md
asset_ids:
  - CHAR_NICODEMUS
  - LOC_NICODEMUS_LIBRARY
  - PROP_CEDAR_TABLE
decision_required: []
notes: ""
---
```

**Status After Completion:** DRAFT

### STEP 7: Prompt Engineering (Prompt Engineer)

**Who:** Prompt Engineer  
**Input:** All completed SHOT_###_v1.0.md files from scene  
**Output:** SHOT_PROMPT_###_v1.0.md for each shot

**Process:**
1. Collect all SHOT_###_v1.0.md decisions
2. Synthesize into **Image Prompt** (8 subsections):
   - Master Style (visual approach)
   - Scene (time, place, historical context)
   - Characters (Nicodemus, using asset ID CHAR_NICODEMUS)
   - Environment/Props (library, props, using asset IDs)
   - Lighting (which sources, direction, mood)
   - Camera (framing, lens, composition, movement motivation)
   - Action (what Nicodemus does)
   - Emotion (what viewer feels)

3. Build **Negative Prompt** from:
   - MASTER_NEGATIVE_PROMPT.md (base: modern objects, fantasy, CGI, etc.)
   - Scene-specific additions (e.g., "no modern furniture," "no anachronisms")

4. Write **Video Prompt** (motion only):
   - Beginning state (pose, position)
   - Motion (camera movement, character action, environment change)
   - Ending state (pose, position)
   - Timing/pace
   - **Do NOT repeat Image Prompt sections**

5. Complete **Continuity Handoff:**
   - Previous shot ending state → this shot beginning state
   - This shot ending state → next shot beginning state
   - Hand positions, gaze direction, emotional continuity

6. Create SHOT_PROMPT_###_v1.0.md with all sections

**Metadata (YAML Frontmatter):**
```yaml
---
entity: SHOT_PROMPT
version: v1.0
status: DRAFT
scene: SCENE_001
shot: SHOT_###
created: [YYYY-MM-DD]
author: "Prompt Engineer"
approver: "QC / Validation"
approval_date: ""
asset_ids:
  - CHAR_NICODEMUS
  - LOC_NICODEMUS_LIBRARY
  - PROP_CEDAR_TABLE
bible_references:
  - CHARACTER_BIBLE.md
  - ENVIRONMENT_BIBLE.md
  - MASTER_NEGATIVE_PROMPT.md
decision_required: []
notes: ""
---
```

**Status After Completion:** IN_REVIEW (ready for G2)

### STEP 8: Gate 2 Validation (Prompt Engineer + QC)

**Who:** Prompt Engineer, QC  
**Reference:** [GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) Gate 2 section

**Validation Checklist:**
- [ ] All Image Prompt subsections filled
- [ ] Negative Prompt includes MASTER_NEGATIVE_PROMPT.md base
- [ ] Scene-specific negative risks added
- [ ] All asset IDs (CHAR_, LOC_, PROP_) exist in INDEX.md
- [ ] Continuity Handoff states match Scene Package
- [ ] Video Prompt describes motion only (no Image duplication)
- [ ] YAML metadata complete
- [ ] No prohibited terms found
- [ ] Format valid (markdown syntax)

**Automated Checks (Future):**
- `validate_prompts.zsh` — Check asset IDs against INDEX.md
- `validate_content.py` — Check for prohibited terms
- `validate_metadata.zsh` — Check YAML frontmatter

**Outcome:** PASS or FAIL

**If PASS:**
- Status = APPROVED
- Approval Log entry: `| 2026-07-24 | SHOT_001_PROMPT_v1.0 | v1.0 | G2 | PASS | Prompt Eng. | Validated |`
- Ready for generation

**If FAIL:**
- QC notes specific failures (missing sections, invalid asset IDs, prohibited terms)
- Prompt Engineer revises
- Resubmit for G2

### STEP 9: Key Image Generation (Generator)

**Who:** AI Image Generator (Midjourney, DALL-E, etc.)  
**Input:** SHOT_PROMPT_###_v1.0.md → Image Prompt section only  
**Output:** `SHOT_###_KEY_FRAME_v1.0.png`

**Process:**
1. Copy Image Prompt section from SHOT_PROMPT_###_v1.0.md
2. Submit to image generator with settings:
   - Resolution: High (suitable for detailed QC review)
   - Style: Photorealistic (match PROJECT_BIBLE.md requirements)
   - Seed: Stable (if generator allows; for consistency)
3. Receive generated image
4. Save as `SHOT_###_KEY_FRAME_v1.0.png` in scene directory

### STEP 10: Gate 3 Pre-Generation QC (Character Supervisor + Production Designer)

**Who:** Character Supervisor, Production Designer  
**Input:** SHOT_###_KEY_FRAME_v1.0.png + SHOT_PROMPT_###_v1.0.md + Scene Package  
**Reference:** [GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) Gate 3 section

**18-Point Checklist (See QC_CHECKLIST.md for details):**
- [ ] Story/drama function clear
- [ ] Continuity states match (input/output)
- [ ] Camera framing justified
- [ ] Lens choice visible
- [ ] Camera movement clear
- [ ] Nicodemus identity matches (master ref, age, appearance)
- [ ] Costume state correct
- [ ] Hands visible and correct
- [ ] Gaze/emotion correct
- [ ] Location matches Bible definition
- [ ] Props positioned correctly
- [ ] No modern/fantasy/medieval elements
- [ ] All light sources motivated (world, not studio)
- [ ] No unmotivated studio lighting
- [ ] No rendering artifacts

**Outcome:** PASS / PASS WITH NOTES / FAIL

**If PASS or PASS WITH NOTES:**
- Status = APPROVED
- Approval Log entry: `| 2026-07-24 | SHOT_001_KEY_FRAME_v1.0 | v1.0 | G3 | PASS | QC | Identity locked |`
- Ready for video generation

**If FAIL:**
- QC notes specific failures with line item
- Prompt Engineer revises Image Prompt section
- Regenerate key frame
- Resubmit G3

### STEP 11: Video Generation (Generator)

**Who:** AI Video Generator (Runway, Pika, etc.)  
**Input:** SHOT_PROMPT_###_v1.0.md → Video Prompt section only  
**Output:** `SHOT_###_v1.0.mp4` (5-15 seconds)

**Process:**
1. Copy Video Prompt section
2. Reference approved key frame (SHOT_###_KEY_FRAME_v1.0.png) as starting frame
3. Submit to video generator with settings:
   - Duration: Per Scene Package duration estimate
   - Motion: Per Video Prompt description
   - Style: Photorealistic, consistent with key frame
4. Receive generated video
5. Save as `SHOT_###_v1.0.mp4`

### STEP 12: Gate 4 Post-Generation QC (QC + Editor)

**Who:** QC, Editor  
**Input:** SHOT_###_v1.0.mp4 + Scene Package + previous shot video  
**Reference:** [GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) Gate 4 section

**8-Point Checklist (See QC_CHECKLIST.md for details):**
- [ ] Motion continuity (begin/end states match)
- [ ] NO personality flicker
- [ ] NO costume flicker
- [ ] NO hand/finger flicker
- [ ] NO light flicker
- [ ] NO prop flicker
- [ ] Rhythm allows silence (not over-edited)
- [ ] Sound/color support emotion

**Outcome:** PASS / PASS WITH NOTES / FAIL

**If PASS or PASS WITH NOTES:**
- Status = APPROVED
- Approval Log entry: `| 2026-07-24 | SHOT_001_v1.0 | v1.0 | G4 | PASS | QC | Video approved |`
- Ready for director review

**If FAIL:**
- QC notes specific failure (e.g., "frame 142-156: hand flicker")
- Editor attempts fix in post if possible
- If unfixable: Prompt Engineer revises Video Prompt
- Regenerate video
- Resubmit G4

### STEP 13: Final Editing & Post-Production (Editor, Color, VFX)

**Who:** Editor, Color Supervisor, VFX Supervisor  
**Input:** All approved SHOT_###_v1.0.mp4 files for scene  
**Output:** Scene sequence with sound, color, minimal effects

**Process:**
1. **Edit:** Arrange shots in sequence, verify pacing, add cuts/transitions
2. **Color:** Apply grade (historical authenticity, emotional palette)
3. **Sound:** Design ambience, add music sync, dialogue (if applicable)
4. **VFX:** Add minimal physical effects only (dust, smoke, fire — if justified)

### STEP 14: Gate 5 Director Final Approval (Director)

**Who:** Director  
**Input:** Final edited scene sequence  
**Reference:** [GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) Gate 5 section

**Review Criteria:**
- [ ] Dramatic impact matches Creative Brief
- [ ] Story function served
- [ ] Emotional authenticity
- [ ] Integration with adjacent scenes
- [ ] Technical quality

**Outcome:** APPROVED / APPROVED WITH NOTES / REVISE

**If APPROVED:**
- Status = LOCKED
- Approval Log entry: `| 2026-07-24 | SCENE_001_LOCKED_v1.0 | v1.0 | G5 | APPROVED | Director | Final locked |`
- Scene ready for final compilation

---

## Scene Naming Convention

**Format:** `SCENE_###_[BRIEF_DESCRIPTION]_v[MAJOR].[MINOR]`

**Examples:**
- `SCENE_001_LIBRARY_MEMORY_v1.0`
- `SCENE_002_BETHEL_ENCOUNTER_v1.0`
- `SCENE_003_RETURN_PEACE_v1.1` (safety fix)
- `SCENE_001_LIBRARY_MEMORY_v2.0` (creative rethink)

---

## Related Documents

- [STUDIO_CONSTITUTION.md](../../01_GOVERNANCE/STUDIO_CONSTITUTION.md) — Master governance
- [GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) — Gate definitions and approval rules
- [../../04_TEMPLATES/SCENE_PACKAGE_TEMPLATE.md](../../04_TEMPLATES/SCENE_PACKAGE_TEMPLATE.md) — Scene template
- [../../04_TEMPLATES/SHOT_PROMPT_TEMPLATE.md](../../04_TEMPLATES/SHOT_PROMPT_TEMPLATE.md) — Prompt template
- [../05_QC/QC_CHECKLIST.md](../05_QC/QC_CHECKLIST.md) — QC standards
- [../05_QC/APPROVAL_LOG.md](../05_QC/APPROVAL_LOG.md) — Approval records
- [../../01_GOVERNANCE/VERSIONING_PROTOCOL.md](../../01_GOVERNANCE/VERSIONING_PROTOCOL.md) — Version rules

---

**SCENE CREATION GUIDE Status: LOCKED v1.0**  
**Effective: 2026-07-24**  
**Next Review: After first scene completed**

