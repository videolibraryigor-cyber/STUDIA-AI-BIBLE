# ASSET LIBRARY INDEX (Индекс библиотеки ассетов)

**Reference:** [STUDIO_CONSTITUTION.md](../../01_GOVERNANCE/STUDIO_CONSTITUTION.md) Part 3.4  
**Version:** 1.0  
**Last Updated:** 2026-07-24  
**Status:** ACTIVE (Updated as new assets created)

---

## Overview

This index is the **single source of truth for all assets** in the NICODEMUS project. Every asset has a unique ID, current status, file location, and usage tracking.

**Use this index to:**
- Verify asset ID exists before referencing in prompts
- Find which scenes/shots use each asset
- Track asset status (locked, approved, pending)
- Avoid duplicates or conflicting asset definitions

---

## Asset Inventory (Current)

### CATEGORY: CHARACTERS

| Asset ID | Name | Type | Status | Version | Location | Bible Reference | First Used | Notes |
|----------|------|------|--------|---------|----------|-----------------|-----------|-------|
| CHAR_NICODEMUS | Nicodemus | Character (Primary) | LOCKED SOURCE REF | v1.0 | 02_ASSET_LIBRARY/CHARACTERS/NICODEMUS.md | CHARACTER_BIBLE.md | TBD | 60-62 year old Jewish teacher; master/face/turnaround refs in ZIP |

**Future Characters (To Be Created):**
- CHAR_PHARISEE_01 (if secondary characters introduced)
- CHAR_PHARISEE_02 (if secondary characters introduced)

---

### CATEGORY: LOCATIONS

| Asset ID | Name | Type | Status | Version | Location | Bible Reference | First Used | Notes |
|----------|------|------|--------|---------|----------|-----------------|-----------|-------|
| LOC_NICODEMUS_LIBRARY | Nicodemus's Library | Location (Primary) | LOCKED SOURCE REF | v1.0 | 02_ASSET_LIBRARY/LOCATIONS/NICODEMUS_LIBRARY.md | ENVIRONMENT_BIBLE.md | TBD | Jerusalem private library; limestone/cedar/worn stone |

**Future Locations (To Be Created):**
- LOC_JERUSALEM_STREET_EAST_GATE (exterior)
- LOC_BETHEL_LOCATION (travel destination, if applicable)
- LOC_TEMPLE_INTERIOR (if applicable)

---

### CATEGORY: PROPS

| Asset ID | Name | Object | Status | Version | Location | Continuity Lock | First Used | Notes |
|----------|------|--------|--------|---------|----------|-----------------|-----------|-------|
| PROP_MEMORY_SCROLL | Memory Scroll | Scroll/Record | DESIGN PENDING | v1.0 | 02_ASSET_LIBRARY/PROPS/HERO_PROPS.md | Locked after first approved shot | TBD | Design/scale/material fixed in G3 |
| PROP_CANDLE | Candle | Light Source | APPROVED | v1.0 | 02_ASSET_LIBRARY/PROPS/HERO_PROPS.md | Position/height/burn state locked | TBD | Tallow or beeswax; warm emotional marker |
| PROP_CEDAR_TABLE | Cedar Desk | Furniture | APPROVED | v1.0 | 02_ASSET_LIBRARY/PROPS/HERO_PROPS.md | Position/size/texture locked | TBD | Center of library; emotional focal point |
| PROP_WINDOW | High Window | Architectural | APPROVED | v1.0 | 02_ASSET_LIBRARY/PROPS/HERO_PROPS.md | Architecture/light direction locked | TBD | Open; provides natural light; directional |
| PROP_STONE_WEIGHT | Stone Press-Paper | Object | APPROVED | v1.0 | 02_ASSET_LIBRARY/PROPS/HERO_PROPS.md | Position relative to scroll locked | TBD | Keeps scrolls from unrolling |

**Future Props (To Be Created):**
- PROP_BRONZE_LAMP (oil lamp; future scenes)
- PROP_WRITING_QUILL (writing implement)
- PROP_INKWELL (ink container)
- PROP_WOODEN_SHELF (storage)
- PROP_WOODEN_BENCH (seating)

---

### CATEGORY: COSTUMES

| Asset ID | Name | Character | Status | Version | Location | Variants | First Used | Notes |
|----------|------|-----------|--------|---------|----------|----------|-----------|-------|
| COSTUME_NICODEMUS_BASE | Base Costume | Nicodemus | LOCKED SOURCE REF | v1.0 | 02_ASSET_LIBRARY/CHARACTERS/NICODEMUS.md | Clean, dusty, torn, soaked | TBD | Cream linen tunic, dark wool cloak, simple sandals |

**Potential Variants:**
- COSTUME_NICODEMUS_DUSTY_TRAVEL (dusty from journey)
- COSTUME_NICODEMUS_SOAKED_RAIN (wet from weather)
- COSTUME_NICODEMUS_TORN_STRUGGLE (damaged from event)

---

## Asset Status Definitions

| Status | Meaning | Can Use In Production? | When Changes Allowed | Notes |
|--------|---------|----------------------|----------------------|-------|
| LOCKED SOURCE REF | Original from archive; immutable | YES (reference only) | Never without director | Visual reference; master authority |
| APPROVED | Passed gates; ready for production | YES | v1.1 safety fix only | Can be versioned (v2.0 for rethinks) |
| APPROVED SOURCE REF | From archive; passed integration | YES (reference only) | Only versioned as v1.1 or v2.0 | Imported from ZIP; normalized |
| DESIGN PENDING | Awaiting first approved shot | NO | Until first shot G3 | Cannot use in prompts yet |
| IN_REVIEW | Being evaluated | NO (tentative) | Subject to feedback | Wait for approval |
| DRAFT | Initial exploration | NO | Freely; not official | Internal use; may be discarded |
| ARCHIVED | Superseded by newer version | NO | Reference only | Old version kept for history |

---

## Asset Usage Matrix (Scene × Asset)

**Current Status:** No scenes created yet (04_SCENES empty)

**Template for Tracking:**

```
SCENE_001:
  - Uses: CHAR_NICODEMUS
  - Uses: LOC_NICODEMUS_LIBRARY
  - Uses: PROP_CEDAR_TABLE
  - Uses: PROP_CANDLE
  - Uses: PROP_MEMORY_SCROLL (version after G3)
  
SCENE_002:
  - Uses: CHAR_NICODEMUS
  - Uses: LOC_NICODEMUS_LIBRARY
  - Uses: PROP_WINDOW
  - Uses: PROP_STONE_WEIGHT
```

**Will be updated as scenes created**

---

## Asset Deprecation & Versioning

### When Asset Status Changes

**v1.0 → v1.1 (Safety Fix):**
- Non-creative correction only
- Example: "Fixed typo in costume description; physical appearance unchanged"
- Old v1.0 archived but not deleted

**v1.0 → v2.0 (Creative Rethink):**
- Substantial revision required (director or creative lead decision)
- Example: "Nicodemus costume changed; now wears formal teaching robes instead of simple tunic"
- Full creative discussion and documentation required
- Old v1.0 archived for history

### Archive Organization

Old versions stored in `07_ARCHIVE/ASSETS/` or within their category:

```
02_ASSET_LIBRARY/
  CHARACTERS/
    NICODEMUS.md (current v1.0)
    ARCHIVE/v0.x/ (if pre-release versions exist)
```

---

## How to Add New Assets

### Process for New Character

1. Create file: `02_ASSET_LIBRARY/CHARACTERS/[CHARACTER_NAME].md`
2. Assign ID: `CHAR_[CHARACTER_NAME_CAPS]`
3. Status: Start as DRAFT
4. Submit with Scene Package that introduces character
5. Upon first approved shot (G3): Status becomes APPROVED
6. Update this INDEX with entry

### Process for New Location

1. Create file: `02_ASSET_LIBRARY/LOCATIONS/[LOCATION_NAME].md`
2. Assign ID: `LOC_[LOCATION_NAME_CAPS]`
3. Status: Start as DRAFT
4. Reference to ENVIRONMENT_BIBLE if detailed definition needed
5. Upon first approved shot (G3): Status becomes APPROVED
6. Update this INDEX with entry

### Process for New Prop

1. Create entry in `02_ASSET_LIBRARY/PROPS/HERO_PROPS.md`
2. Assign ID: `PROP_[OBJECT_NAME_CAPS]`
3. Status: DESIGN PENDING until first shot
4. Define continuity tracking rules in HERO_PROPS.md
5. Upon first approved shot (G3): Status becomes APPROVED
6. Update this INDEX with entry

### Process for New Costume Variant

1. Create entry in costume section (if file doesn't exist)
2. Assign ID: `COSTUME_[CHARACTER]_[VARIANT_CAPS]`
3. Status: DESIGN PENDING
4. Describe variant condition (clean, dusty, soaked, etc.)
5. Upon first use (G3): Status becomes APPROVED
6. Update this INDEX with entry

---

## Validation Against This Index

**Before Creating Prompt:**
- [ ] Verify all asset IDs referenced in prompt exist in this INDEX
- [ ] Verify all asset IDs have APPROVED or LOCKED status (not DRAFT or PENDING)
- [ ] If asset is DESIGN PENDING: confirm first shot already passed G3 before using in subsequent shots

**Automated Check (Future):**
- Script `05_AUTOMATION/validate_prompts.zsh` will compare prompt asset IDs against this INDEX
- Reports missing or invalid IDs
- Prevents invalid prompts from reaching G2 gate

---

## Cross-Reference Cleanup & Duplication Check

**Single Source of Truth for Each Asset:**

1. **CHAR_NICODEMUS** defined in:
   - `/02_ASSET_LIBRARY/CHARACTERS/NICODEMUS.md` (primary reference card)
   - `/01_PRODUCTION_BOOK/CHARACTER_BIBLE.md` (locked detailed definition)
   - This INDEX (entry with status and usage)
   - **NO duplication; each file has distinct purpose**

2. **LOC_NICODEMUS_LIBRARY** defined in:
   - `/02_ASSET_LIBRARY/LOCATIONS/NICODEMUS_LIBRARY.md` (primary reference card)
   - `/01_PRODUCTION_BOOK/ENVIRONMENT_BIBLE.md` (locked detailed definition)
   - This INDEX (entry with status and usage)
   - **NO duplication; each file has distinct purpose**

3. **Props (PROP_*)** defined in:
   - `/02_ASSET_LIBRARY/PROPS/HERO_PROPS.md` (primary tracking table)
   - This INDEX (asset status and usage)
   - **NO duplication; complementary purposes**

---

## Related Documents

- [STUDIO_CONSTITUTION.md](../../01_GOVERNANCE/STUDIO_CONSTITUTION.md) — Master governance
- [02_ASSET_LIBRARY/CHARACTERS/NICODEMUS.md](CHARACTERS/NICODEMUS.md) — Character reference card
- [02_ASSET_LIBRARY/LOCATIONS/NICODEMUS_LIBRARY.md](LOCATIONS/NICODEMUS_LIBRARY.md) — Location reference card
- [02_ASSET_LIBRARY/PROPS/HERO_PROPS.md](PROPS/HERO_PROPS.md) — Props continuity tracking
- [../01_PRODUCTION_BOOK/CHARACTER_BIBLE.md](../01_PRODUCTION_BOOK/CHARACTER_BIBLE.md) — Character locked definition
- [../01_PRODUCTION_BOOK/ENVIRONMENT_BIBLE.md](../01_PRODUCTION_BOOK/ENVIRONMENT_BIBLE.md) — Environment locked definition
- [../../05_AUTOMATION/validate_prompts.zsh](../../05_AUTOMATION/validate_prompts.zsh) (future) — Asset ID validation script

---

**ASSET INDEX Status: ACTIVE v1.0**  
**Last Updated: 2026-07-24**  
**Next Update: When first scene assets confirmed**  
**Review Frequency: After each scene completed**

