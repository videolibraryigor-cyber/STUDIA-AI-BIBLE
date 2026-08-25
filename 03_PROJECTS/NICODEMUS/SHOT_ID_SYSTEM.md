# SHOT ID SYSTEM (Система идентификации кадров)

**Reference:** [STUDIO_CONSTITUTION.md](01_GOVERNANCE/STUDIO_CONSTITUTION.md) Part 3.3  
**Version:** 1.0  
**Last Updated:** 2026-07-24  
**Status:** LOCKED

---

## Overview

The **Shot ID System** is the unique identifier for every single shot in the NICODEMUS film. It ensures:
- Unambiguous reference to any shot across all documents
- Consistent naming across prompts, renders, and QC logs
- Machine-readable format for automation and tracking
- Logical ordering from beginning to end of film

This document defines the **format, rules, and allocation process** for all shot IDs.

---

## Shot ID Format

```
SHOT_[SCENE_#]_[POSITION_IN_SCENE]_[DRAMATIC_FUNCTION]_v[MAJOR].[MINOR]
```

### Components

#### 1. SHOT Prefix (Fixed)
- Always `SHOT`
- Indicates entity type

#### 2. Scene Number [SCENE_#]
- Format: `001`, `002`, `003`, etc. (3 digits, zero-padded)
- Corresponds to scene order in film (not editing order)
- Example: `SHOT_001_*` = first scene

#### 3. Position in Scene [POSITION_IN_SCENE]
- Format: `A`, `B`, `C`, `D`, `E`, etc. (alphabetic order within scene)
- Indicates order of shot within that scene
- Example: `SHOT_001_A_*` = first shot of scene 001
- Example: `SHOT_001_B_*` = second shot of scene 001

#### 4. Dramatic Function [DRAMATIC_FUNCTION]
- Format: `[UPPERCASE_SNAKE_CASE]` (no spaces, ASCII only)
- Describes what this shot does dramatically
- Examples:
  - `ESTABLISHING` = wide shot showing location
  - `CLOSE_HANDS` = close-up of character hands
  - `SEARCH` = action shot of searching
  - `DISCOVERY` = reaction to finding something
  - `READING` = character engaged with object
  - `REFLECTION` = emotional beat, contemplation

#### 5. Version [v[MAJOR].[MINOR]] (Added after approval)
- Format: `v1.0`, `v1.1`, `v2.0`, etc.
- `v1.0` = first approval
- `v1.1` = safety fix (non-creative)
- `v2.0` = creative rethink
- Until first G3 approval: version omitted from shot ID (implicitly v0.x in draft)

---

## Shot ID Format Examples

### Before First Approval (Draft)
```
SHOT_001_A_ESTABLISHING_LIBRARY
SHOT_001_B_CLOSE_HANDS_SHELF
SHOT_001_C_DISCOVERY_SCROLL
```

### After G3 Approval (Locked Key Frame)
```
SHOT_001_A_ESTABLISHING_LIBRARY_v1.0
SHOT_001_B_CLOSE_HANDS_SHELF_v1.0
SHOT_001_C_DISCOVERY_SCROLL_v1.0
```

### After Safety Fix (v1.1)
```
SHOT_001_A_ESTABLISHING_LIBRARY_v1.1
```

### After Creative Rethink (v2.0)
```
SHOT_001_A_ESTABLISHING_LIBRARY_v2.0
```

---

## Dramatic Function Keywords (Vocabulary)

Use these standard dramatic function keywords:

### Establishing Shots
- `ESTABLISHING` — wide, location reveal
- `ESTABLISHING_INTERIOR` — interior space reveal
- `ESTABLISHING_EXTERIOR` — exterior space reveal
- `ESTABLISHING_EVENING` — time of day reveal
- `ESTABLISHING_CROWD` — crowd/group context (if applicable)

### Close-Up / Detail Shots
- `CLOSE_HANDS` — hands in detail (writing, holding, gesturing)
- `CLOSE_FACE` — facial expression (emotional beat)
- `CLOSE_EYES` — eyes only (profound emotional moment)
- `CLOSE_OBJECT` — object detail (scroll, lamp, vessel)
- `CLOSE_SCROLL` — specific attention on scroll/document
- `CLOSE_COSTUME` — costume or texture detail

### Action Shots
- `SEARCH` — character searching or investigating
- `READING` — character reading or examining
- `REACHING` — character reaching or grasping
- `WRITING` — character writing or inscribing
- `WALKING` — character moving through space
- `ENTERING` — character entering frame/location
- `EXITING` — character leaving frame/location
- `DESCENDING` — character going downward (stairs, underground)
- `ASCENDING` — character going upward

### Reaction / Emotional Shots
- `DISCOVERY` — moment of finding or realizing
- `ASTONISHMENT` — shock, surprise, awe
- `CONTEMPLATION` — thinking, reflecting, processing
- `REALIZATION` — understanding dawning
- `CONCERN` — worry, doubt, internal conflict
- `RESOLUTION` — acceptance, peace, conclusion
- `REFLECTION` — looking back, memory moment

### Transition Shots
- `TRANSITION_LIGHT_CHANGE` — shift from one light to another (no movement)
- `TRANSITION_TIME_SKIP` — subtle passage of time
- `TRANSITION_WINDOW` — framing through window to next scene
- `TRANSITION_BLUR` — intentional blur for transition

### Multi-Purpose or Composite Shots
- `MONTAGE_SEQUENCE` — multiple moments compressed (if used)
- `SPLIT_FOCUS` — two subjects in one frame
- `LAYERED_ACTION` — multiple actions simultaneously

---

## Rules for Shot ID Assignment

### Rule 1: Sequential Scene Numbers
- First scene = `001`
- Second scene = `002`
- Count sequentially throughout film
- Do NOT restart numbering per act or location

### Rule 2: Alphabetic Position Order
- First shot in scene = `A`
- Second shot in scene = `B`
- Third shot in scene = `C`
- Maximum 26 shots per scene (Z limit)
- If scene exceeds 26 shots: reconsider scene structure (too complex)

### Rule 3: Dramatic Function Must Be Specific
- NOT generic (`SHOT_001_A_SHOT`)
- NOT vague (`SHOT_001_A_SCENE`)
- MUST describe dramatic intent (`SHOT_001_A_DISCOVERING_SCROLL`)

### Rule 4: NO Special Characters in Function
- ASCII alphanumerics + underscore ONLY
- NOT: `SHOT_001_A_Hands-Close-Up` ❌
- NOT: `SHOT_001_A_CLOSE_HANDS!` ❌
- YES: `SHOT_001_A_CLOSE_HANDS` ✅

### Rule 5: Version Added Only After Approval
- Draft phase: No version suffix
  - `SHOT_001_A_ESTABLISHING_LIBRARY` (in Scene Package and prompts)
- After G3 approval: Version required in filenames
  - `SHOT_001_A_ESTABLISHING_LIBRARY_v1.0.md` (prompt file)
  - `SHOT_001_A_ESTABLISHING_LIBRARY_v1.0.png` (key frame)
  - `SHOT_001_A_ESTABLISHING_LIBRARY_v1.0.mp4` (video)

### Rule 6: Consistent Across All Documents
- Scene Package must use ID without version: `SHOT_001_A_*`
- Prompt file uses ID with version (after approval): `SHOT_001_A_*_v1.0.md`
- QC logs reference ID with version: `SHOT_001_A_*_v1.0`
- Approval log records ID with version: `SHOT_001_A_*_v1.0 | APPROVED`

---

## Shot ID Allocation Process

### Phase 0 (Planning - Current)
1. Director decides total scene count
2. Director estimates shots per scene
3. Allocate SHOT IDs sequentially: `SHOT_001_A`, `SHOT_001_B`, etc.
4. Record in MASTER_SHOT_LIST.md (not yet created; Drama Brief only)

### Phase 1 (Production Planning - Current)
1. Create MASTER_SHOT_LIST with all SHOT_IDs assigned
2. Create MASTER_TIMELINE aligning shots with music
3. Verify no ID conflicts or gaps

### Phase 2 (Scene Package Creation)
1. Scene Package references shots by ID without version: `SHOT_001_A_*`
2. Director describes each shot using assigned ID
3. Specialists fill shot templates using this ID

### Phase 3 (After G3 Approval)
1. Add version suffix to all files: `_v1.0`
2. Rename files: `SHOT_001_A_*` → `SHOT_001_A_*_v1.0.md`
3. Update INDEX.md asset tracking to include version

---

## Machine-Readable Format

For automation/tools, SHOT ID can be parsed:

```python
# Example parser
import re

shot_id_pattern = r'SHOT_(\d{3})_([A-Z])_([A-Z_]+)(?:_v(\d+\.\d+))?'
# Groups: (scene_number, position, dramatic_function, version)

example = "SHOT_001_A_ESTABLISHING_LIBRARY_v1.0"
match = re.match(shot_id_pattern, example)

if match:
    scene_num = match.group(1)      # "001"
    position = match.group(2)        # "A"
    function = match.group(3)        # "ESTABLISHING_LIBRARY"
    version = match.group(4)         # "1.0"
```

---

## Reserved Patterns (NOT Used for Regular Shots)

The following patterns are reserved for special use:

| Pattern | Purpose | Example |
|---------|---------|---------|
| `SHOT_000_*` | Prologue or title sequence (if applicable) | `SHOT_000_A_TITLE_CARD` |
| `SHOT_999_*` | Epilogue or end credits (if applicable) | `SHOT_999_A_FINAL_TEXT` |
| `SHOT_*_AA_*` | Reshoots of scene (rare) | `SHOT_001_AA_ESTABLISHING_LIBRARY_v2.0` |
| `MASTER_SHOT_*` | Archival/reference shots (not in final film) | `MASTER_SHOT_REFERENCE_001` |

---

## Examples of Well-Formed Shot IDs

### Acceptable
- ✅ `SHOT_001_A_ESTABLISHING_LIBRARY`
- ✅ `SHOT_001_B_CLOSE_HANDS_SHELF`
- ✅ `SHOT_001_C_DISCOVERY_SCROLL_v1.0`
- ✅ `SHOT_002_A_BETHEL_ROAD_MORNING`
- ✅ `SHOT_002_B_WALKING_ASTONISHMENT`
- ✅ `SHOT_003_A_TEMPLE_STEPS`
- ✅ `SHOT_003_B_CLOSE_FACE_REALIZATION_v1.1`

### Unacceptable (Will Fail Validation)
- ❌ `SHOT_1_A_ESTABLISHING` (scene not 3 digits)
- ❌ `SHOT_001_1_ESTABLISHING` (position not letter)
- ❌ `SHOT_001_A_establishing` (function lowercase)
- ❌ `SHOT_001_A_Close-Up` (hyphen; use underscore)
- ❌ `SHOT_001_A_NICODEMUS_THINKING_v1` (version missing minor)
- ❌ `SHOT_001_A_v1.0` (no dramatic function)
- ❌ `SHOT-001-A-ESTABLISHING` (use underscore, not hyphen)

---

## Conflict Resolution

### What If Scene Exceeds 26 Shots?
**Action:** This indicates scene is too complex.
- Split into two scenes
- Use `SHOT_001_A...Z` and `SHOT_002_A...Z`
- Adjust MASTER_TIMELINE to reflect new scene structure
- Maximum = 26 shots per scene (Z limit)

### What If Two Shots Assigned Same ID?
**Action:** Not allowed. Validation will catch this.
- Audit MASTER_SHOT_LIST for duplicates
- Reassign conflicting shot to next available position
- Update all references in Scene Packages and prompts

### What If Shot Renumbered After Approval?
**Action:** Create new version, never rename existing ID
- Old shot: `SHOT_001_A_ESTABLISHING_v1.0` (archived)
- New shot: `SHOT_001_A_ESTABLISHING_v2.0` (replaces in timeline)
- Both versions kept for history; only v2.0 used in final export

---

## Related Documents

- [MASTER_SHOT_LIST.md](MASTER_SHOT_LIST.md) — Complete inventory of all shots (uses this system)
- [MASTER_TIMELINE.md](MASTER_TIMELINE.md) — Shots sequenced with music timings (uses this system)
- [STUDIO_CONSTITUTION.md](01_GOVERNANCE/STUDIO_CONSTITUTION.md) — Master governance
- [ASSET_LIBRARY/INDEX.md](03_PROJECTS/NICODEMUS/02_ASSET_LIBRARY/INDEX.md) — Asset tracking (linked to shots)
- [04_SCENES/README.md](03_PROJECTS/NICODEMUS/04_SCENES/README.md) — Scene creation guide (applies this system)

---

## Validation Tools (Future Implementation)

```bash
# Validate all SHOT IDs in MASTER_SHOT_LIST
validate_shot_ids.zsh MASTER_SHOT_LIST.md

# Check for conflicts and gaps
check_shot_id_sequences.py MASTER_SHOT_LIST.md MASTER_TIMELINE.md

# Rename files after approval (from v0.x to v1.0)
apply_version_to_shots.zsh 04_SCENES/SCENE_001/
```

---

**SHOT ID SYSTEM Status: LOCKED v1.0**  
**Effective: 2026-07-24**  
**Validation: Automated checks to be implemented**

