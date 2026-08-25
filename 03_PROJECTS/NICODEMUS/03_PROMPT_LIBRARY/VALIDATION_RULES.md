# VALIDATION RULES (Правила валидации)

**Reference:** [STUDIO_CONSTITUTION.md](../../01_GOVERNANCE/STUDIO_CONSTITUTION.md) Part 3.6  
**Location:** 03_PROMPT_LIBRARY/  
**Version:** 1.0  
**Last Updated:** 2026-07-24

---

## Overview

This document defines validation rules for all prompts. **Every prompt must pass these rules before G2 gate approval.** Validation prevents invalid prompts from consuming generation time and ensures consistency across all shots.

---

## Rule Set 1: Asset ID Validation

### Rule 1.1: All Asset IDs Must Exist in INDEX

**Standard:** Every reference to CHAR_*, LOC_*, PROP_*, or COSTUME_* must exist in [02_ASSET_LIBRARY/INDEX.md](../02_ASSET_LIBRARY/INDEX.md)

**Check Process:**
1. Extract all asset IDs from prompt
2. Cross-reference against INDEX.md
3. Verify each ID has entry in correct category

**Valid IDs (Current):**
- CHAR_NICODEMUS
- LOC_NICODEMUS_LIBRARY
- PROP_MEMORY_SCROLL
- PROP_CANDLE
- PROP_CEDAR_TABLE
- PROP_WINDOW
- PROP_STONE_WEIGHT
- COSTUME_NICODEMUS_BASE

**Invalid Examples (Will Fail):**
- CHAR_PHARISEE (not in INDEX yet; don't use until created)
- LOC_STREET (not defined; use exterior location once created)
- PROP_LAMP (not in INDEX; use PROP_BRONZE_LAMP after creation)

**Action on Failure:** Prompt Engineer corrects asset ID or creates missing asset definition

---

### Rule 1.2: Asset Status Must Be APPROVED or LOCKED

**Standard:** Cannot reference assets with status DRAFT, DESIGN PENDING, or IN_REVIEW

**Check Process:**
1. Find asset in INDEX.md
2. Verify Status column = APPROVED, APPROVED SOURCE REF, or LOCKED SOURCE REF
3. Confirm Version ≥ v1.0 (not -beta or v0.x)

**Examples:**
- ✅ CHAR_NICODEMUS (Status: LOCKED SOURCE REF)
- ✅ LOC_NICODEMUS_LIBRARY (Status: LOCKED SOURCE REF)
- ❌ PROP_MEMORY_SCROLL (Status: DESIGN PENDING until first shot G3)
- ❌ CHAR_PHARISEE (Status: DRAFT; not yet in production)

**Action on Failure:** Wait for asset to reach APPROVED status before using in prompt

---

### Rule 1.3: Reference Format Must Be Correct

**Standard:** Asset IDs must be in exact format: `[TYPE]_[NAME_IN_CAPS]`

**Valid Formats:**
- `CHAR_NICODEMUS` ✅
- `LOC_NICODEMUS_LIBRARY` ✅
- `PROP_CEDAR_TABLE` ✅
- `COSTUME_NICODEMUS_BASE` ✅

**Invalid Formats (Will Fail):**
- `char_nicodemus` (lowercase) ❌
- `CHAR_Nicodemus` (mixed case) ❌
- `CharNicodemus` (no underscore) ❌
- `nicodemus` (no type prefix) ❌
- `Nicodemus` (no ID format) ❌

**Action on Failure:** Correct ID format to match INDEX.md exactly

---

## Rule Set 2: Prohibited Terms

### Rule 2.1: Base Negative Prompt Always Included

**Standard:** Every prompt must include [MASTER_NEGATIVE_PROMPT.md](NEGATIVE/MASTER_NEGATIVE_PROMPT.md) as baseline

**Base Prohibited Terms:**
```
modern objects, modern architecture, modern clothing,
medieval Europe, fantasy, Hollywood glamour,
plastic skin, CGI look, illustration, anime, cartoon,
inconsistent Nicodemus identity, different age, different hair,
different beard, blue eyes, fashion styling, armor,
jewelry excess, unexplained studio light, lens flare,
magical glow, halos, dramatic VFX, random camera spin,
empty decorative spectacle, incorrect props, duplicate limbs,
distorted hands, low resolution, blur
```

**Check Process:**
1. Find "Negative Prompt" section of SHOT_PROMPT_###.md
2. Verify starts with `Master base (from MASTER_NEGATIVE_PROMPT.md):`
3. Verify includes all base terms (complete list verbatim or summarized with ellipsis)

**Valid Structure:**
```
## Negative Prompt

Master base (from MASTER_NEGATIVE_PROMPT.md):
modern objects, modern architecture, modern clothing,
medieval Europe, fantasy, Hollywood glamour,
plastic skin, CGI look, illustration, anime, cartoon,
...
[complete list or indicates summary]

Scene-specific additions:
[any shot-specific risks]
```

**Action on Failure:** Add MASTER_NEGATIVE_PROMPT.md base to Negative Prompt section

---

### Rule 2.2: Scene-Specific Negative Risks Added

**Standard:** Beyond base, add any risks specific to this shot

**Common Scene-Specific Risks to Consider:**
- Location anachronisms: "modern furniture," "electric lights," "windows with frames"
- Character anachronisms: "blue eyes," "blonde hair," "modern jewelry"
- Costume violations: "formal suit," "modern fashion," "high heels"
- Prop anachronisms: "plastic bottles," "modern books," "electric lamp"
- Environmental violations: "marble floor," "glass walls," "neon lights"
- Action issues: "Nicodemus smiling," "Nicodemus angry," "Nicodemus young"

**Example (Library Scene):**
```
Scene-specific additions:
no modern furniture, no glass windows, no electric lights,
no modern-style bookcase, no contemporary pottery,
Nicodemus not smiling, Nicodemus not young
```

**Check Process:**
1. Review Creative Brief (what is this shot about?)
2. Identify anachronisms specific to scene action
3. Add 3-5 scene-specific prohibitions to Negative Prompt

**Action on Failure:** Prompt Engineer adds scene-specific risks

---

### Rule 2.3: No Prohibited Terms Appear in Image Prompt

**Standard:** Image Prompt sections must never include prohibited terms (only Negative Prompt contains them)

**Examples of Prohibited Terms Appearing in Image Prompt:**
- ❌ "Modern leather chair" (contains "modern")
- ❌ "Anime-style Nicodemus" (contains "anime")
- ❌ "Blue-eyed scholar" (contains "blue eyes")
- ❌ "Magical glow from scroll" (contains "magical glow")
- ❌ "Hollywood lighting" (contains "Hollywood")
- ❌ "CGI particle effects" (contains "CGI")

**Why This Matters:** Negative prompts are hints to avoid; they may be weighted wrong or misinterpreted. Better to avoid even mentioning prohibited concepts in Image Prompt.

**Check Process:**
1. Read Image Prompt sections (all 8 subsections)
2. Cross-check against Master Negative list
3. Flag any prohibited terms found in Image Prompt

**Correct Approach:**
- ❌ WRONG: "Magical glow from ancient scroll" (mentions magic)
- ✅ RIGHT: "Warm light illuminating scroll from oil lamp" (describe world source instead)

**Action on Failure:** Rewrite Image Prompt section to remove prohibited term reference; use affirmative description instead

---

## Rule Set 3: Completeness Check

### Rule 3.1: All Required Sections Filled

**Standard:** SHOT_PROMPT_###.md must have all sections completed (no placeholders or TBD)

**Required Sections:**

**Metadata (YAML Frontmatter):**
- [ ] title
- [ ] entity
- [ ] version
- [ ] status
- [ ] created
- [ ] last_updated
- [ ] author
- [ ] approver
- [ ] approval_date (can be empty if IN_REVIEW)
- [ ] bible_references (at minimum CHARACTER_BIBLE, ENVIRONMENT_BIBLE)
- [ ] asset_ids (all referenced assets)

**Content Sections:**
- [ ] Creative Brief (2-3 sentences, not placeholder)
- [ ] Image Prompt — all 8 subsections:
  - [ ] Master Style
  - [ ] Scene (time, place, context)
  - [ ] Characters (with asset IDs)
  - [ ] Environment / Props (with asset IDs)
  - [ ] Lighting (sources only)
  - [ ] Camera (framing, lens, movement, motivation)
  - [ ] Action (what Nicodemus does)
  - [ ] Emotion (what viewer feels)
- [ ] Negative Prompt (base + scene-specific)
- [ ] Video Prompt (motion only; not repeating Image)
- [ ] Continuity Handoff (states, not vague)

**Check Process:**
1. Open SHOT_PROMPT_###.md
2. Verify each section has content (not "TODO" or "[fill in]")
3. Verify sections are specific and detailed (not generic placeholders)

**Action on Failure:** Prompt Engineer completes all empty or placeholder sections

---

### Rule 3.2: Bible References Complete

**Standard:** Metadata must reference all relevant Bibles

**Minimum Required References:**
- CHARACTER_BIBLE.md (if Nicodemus appears)
- ENVIRONMENT_BIBLE.md (if library or location appears)
- MASTER_NEGATIVE_PROMPT.md (always)

**Additional References (As Applicable):**
- PROJECT_BIBLE.md (story/drama context)
- CAMERA_LIGHTING_BIBLE.md (lighting logic)
- CONTINUITY_BIBLE.md (continuity rules)

**Check Process:**
1. Look at asset_ids in YAML
2. For each asset, verify corresponding Bible referenced

**Action on Failure:** Add missing Bible references to metadata

---

### Rule 3.3: Asset IDs in Metadata Match Text

**Standard:** asset_ids listed in YAML metadata must match all assets mentioned in prompt text

**Check Process:**
1. List all asset IDs in YAML metadata
2. Search prompt text for all instances of CHAR_, LOC_, PROP_, COSTUME_
3. Verify every ID in text appears in metadata
4. Verify no extra IDs in metadata without corresponding text

**Examples:**
- ✅ Metadata lists `- CHAR_NICODEMUS` and text says "CHAR_NICODEMUS reading scroll" → Match
- ❌ Metadata lists `- CHAR_NICODEMUS` but prompt never mentions character asset ID → Remove from metadata
- ❌ Metadata missing `- LOC_NICODEMUS_LIBRARY` but prompt describes the library → Add to metadata

**Action on Failure:** Update asset_ids to match prompt content exactly

---

### Rule 3.4: All Master Style Layers Included (MANDATORY)

**Standard:** Image Prompt MUST include rules from ALL THREE Master Style layers. Absence of any layer = INVALID prompt.

**Required Content From MASTER_STYLE_v2.md (Layer 1):**
- Ultra photorealistic / museum-quality archaeological reconstruction
- Biblical historical realism
- Natural imperfections, real materials, natural weathering
- Physically motivated lighting ONLY
- Character consistency across entire film (face, age, hair, beard, eyes, skin, height, proportions, wardrobe, color palette)
- No visual drift permitted; identical lighting, color, weather, dust level, lens, terrain, vegetation, time of day across sequence
- Ancient atmosphere; dust moves naturally, wind behaves realistically, silence is visible
- FINAL RULE: Audience must never think the image is digital, synthetic, game-like, or AI-generated

**Required Content From MASTER_STYLE_ENHANCEMENT_v2.1.md (Layer 2):**
- Optical Character: ARRI Alexa 65 cinematic response, Cooke Full Frame Anamorphic lens, natural anamorphic depth, subtle lens breathing, natural optical imperfections, soft highlight halation, gentle edge falloff, filmic separation, real lens behavior
- Material Microdetail: visible limestone pores, hand-cut stone irregularities, erosion marks, aged wood grain, cedar texture, olive wood imperfections, woven linen fibers, wool structure, natural leather wear, parchment wrinkles, dust in corners
- Historical Realism Enhancement: uneven surfaces, small architectural irregularities, signs of human presence, archaeological authenticity, period-accurate materials and construction
- Atmospheric Depth: thin airborne dust, soft volumetric sunlight, gentle atmospheric perspective, natural distance haze, warm/cool tones believable
- Skin Realism Enhancement: real skin pores, natural wrinkles, small facial asymmetry, subtle age details, realistic beard texture, authentic Mediterranean skin tones
- Light Quality Enhancement: soft highlight rolloff, natural shadow transitions, realistic bounce light, subtle warm/cool contrast, physically accurate exposure
- Color Science: ARRI-style color science, natural highlight rolloff, warm realistic highlights, balanced white balance, restrained saturation, organic film colors
- Film Grain: subtle cinematic film grain, natural photographic texture, organic image structure
- Human Scale and Camera Observation: quiet observation, human emotion, natural movement, authentic reactions, small gestures, meaningful pauses
- Final Director Quality Check: Does it look photographed? Does it feel historically possible? Does lighting exist in the scene? Do materials feel real? Do people feel like real humans?

**Required Content From MASTER_STYLE_ENHANCEMENT_v2.2.md (Layer 3):**
- CINEMATIC HUMAN REALISM: World must feel lived, not designed; people are inhabitants of history, not models; every face carries a story
- Natural human qualities: small imperfections, different ages, different emotions
- Film crew perspective: scenes feel captured by real historical film crew, camera observes life unfolding
- No theatrical elements: no posed characters, no theatrical acting, no artificial beauty
- Film references: The Passion of the Christ, The Chosen, Mary Magdalene, historical documentary cinematography
- Priorities: human emotion, natural behavior, physical reality, environmental storytelling

**Check Process:**
1. Open SHOT_PROMPT_###.md
2. Navigate to "## Image prompt" → "### 1. Master style" section
3. Verify section explicitly references all three Master Style files
4. Verify section contains at least 3-5 specific rules from EACH layer (v2.0, v2.1, v2.2)
5. Verify rules are not generic (e.g., "photorealistic" alone is insufficient; must include specific rules like lens type, material details, atmospheric qualities)

**Invalid Examples (Will Fail):**
- ❌ "Photorealistic historical style" (too vague; lacks specific layer content)
- ❌ Only includes v2.0 rules (missing v2.1 and v2.2)
- ❌ Only mentions "natural lighting" without optical character, material microdetail, skin realism, color science details from v2.1
- ❌ Lacks any mention of human authenticity, lived world, or emotional realism from v2.2

**Valid Example (Will Pass):**
```
Master style reference: MASTER_STYLE_v2.md + MASTER_STYLE_ENHANCEMENT_v2.1.md + MASTER_STYLE_ENHANCEMENT_v2.2.md

Ultra photorealistic museum-quality archaeological reconstruction with natural imperfections, real materials, 
character locked identity. ARRI Alexa 65 cinematic response, Cooke anamorphic lens character, visible material 
microdetails (limestone pores, hand-cut stone, aged wood grain, woven fibers), subtle atmospheric depth with 
volumetric dust light, real skin pores and wrinkles, physically motivated lighting only (sun/moon/candle/oil lamp), 
ARRI-style color science with organic film grain. Cinematic human realism: world feels lived, people inhabit 
history as real humans, no posed characters, no theatrical acting, prioritize human emotion and environmental 
storytelling. Visual style must feel photographed by historical film crew, never digital or AI-generated.
```

**Action on Failure:** Revise Master Style section to explicitly include content from all three layers (v2.0, v2.1, v2.2); add specific rules from each layer; ensure section is detailed and comprehensive, not vague

---

## Rule Set 4: Format Validation

### Rule 4.1: YAML Frontmatter Syntax Valid

**Standard:** YAML must be properly formatted (hyphens, colons, quotes, arrays correct)

**Valid Format:**
```yaml
---
title: "Shot Prompt: Establishing Library"
version: v1.0
status: DRAFT
asset_ids:
  - CHAR_NICODEMUS
  - LOC_NICODEMUS_LIBRARY
---
```

**Invalid Formats (Will Fail):**
```yaml
---
title: Shot Prompt: Establishing Library (missing quotes)
version v1.0 (missing colon)
---
```

**Tool:** YAML validator (check via linter or online validator)

**Action on Failure:** Correct YAML syntax

---

### Rule 4.2: Markdown Syntax Valid

**Standard:** Markdown must render correctly (headings, lists, emphasis, code blocks)

**Common Errors:**
- Missing `#` on heading level (e.g., `##` instead of `#`)
- Unmatched bold/italic markers (e.g., `**text` without closing `**`)
- Broken lists (incorrect indentation or markers)
- Missing code block fences (e.g., ` ```markdown` without closing)

**Tool:** Markdown linter (check in editor or via automated tool)

**Action on Failure:** Fix Markdown syntax

---

### Rule 4.3: Version Format Correct

**Standard:** version in YAML must be `vX.Y` format (no spaces, lowercase v)

**Valid:** `v1.0`, `v1.1`, `v2.0`, `v3.0`  
**Invalid:** `V1.0` (uppercase), `v1` (missing minor), `1.0` (no v prefix), `v 1.0` (space)

**Action on Failure:** Correct version format to `vX.Y`

---

### Rule 4.4: Status Enum Valid

**Standard:** status in YAML must be one of: DRAFT, IN_REVIEW, APPROVED, LOCKED

**Valid:** `DRAFT`, `IN_REVIEW`, `APPROVED`, `LOCKED`  
**Invalid:** `Draft`, `IN_PROGRESS`, `APPROVED `, (with space), `pending`

**Action on Failure:** Correct status to valid enum value

---

## Rule Set 5: Continuity Check

### Rule 5.1: Continuity Handoff States Match Scene Package

**Standard:** Continuity Handoff section must align with Scene Package input/output states

**Check Process:**
1. Open Scene Package: `SCENE_###_v1.0.md`
2. Find Continuity section (input state → action → output state)
3. Open shot prompt for first shot: "Previous state" should describe scene input
4. Open shot prompts for middle shots: "Previous/next states" should chain logically
5. Open shot prompt for last shot: "Next state" should describe scene output

**Example (Scene with 3 shots):**
```
SCENE_PACKAGE: Nicodemus enters library (input) → searches shelf (action) → finds scroll (output)

SHOT_001 (establishing):
  Previous state: [scene start; Nicodemus entering]
  This shot: Establish library, show entrance
  Next state: Nicodemus moving toward shelf

SHOT_002 (search):
  Previous state: Nicodemus at shelf
  This shot: Hands searching scrolls
  Next state: Scroll found; Nicodemus frozen in recognition

SHOT_003 (discovery):
  Previous state: Scroll found; Nicodemus trembling
  This shot: Close-up face as reads
  Next state: Emotional realization; scene ends
```

**Check Process:**
1. Verify state descriptions chain logically (→ → →)
2. Verify each shot's "next state" matches next shot's "previous state"
3. Verify first shot aligns with Scene Package input
4. Verify last shot aligns with Scene Package output

**Action on Failure:** Revise Continuity Handoff states to chain logically; ensure alignment with Scene Package

---

### Rule 5.2: Emotional Continuity Makes Sense

**Standard:** Emotional arc across shots should follow Character Bible performance arc

**Check Process:**
1. List emotional state of each shot (from Creative Brief)
2. Verify emotional progression aligns with film's dramatic route (PROJECT_BIBLE.md)
3. Verify no unexplained emotional jumps (e.g., sad → happy → sad without motivation)

**Example (Good Emotional Arc):**
```
SHOT_001: Curiosity (Nicodemus searching)
SHOT_002: Astonishment (discovery moment)
SHOT_003: Contemplation (absorbing what found)
→ Progression is logical within scene
```

**Example (Bad Emotional Arc):**
```
SHOT_001: Curiosity
SHOT_002: Anger (no setup for anger)
SHOT_003: Peace (unexplained mood swing)
→ Jumps not justified; needs revision
```

**Action on Failure:** Revise emotional descriptions; ensure progression is motivated

---

## Rule Set 6: AI Generation Readiness

### Rule 6.1: Prompt Specificity Level Appropriate

**Standard:** Image Prompt must be specific enough for generator to understand but not overly technical

**Too Vague (Fails):**
- "A man in a room"
- "Scholar studying"
- "Ancient library"

**Too Technical (Acceptable but less useful):**
- "65mm lens, f/2.8 aperture, 1/125 shutter, ISO 400"
- "Dutch angle composition, rule of thirds violation"

**Right Level (Best):**
- "Close-up of weathered hands holding ancient scroll, lit by warm candlelight from left, olive-toned skin, elderly scholar's fingers, aged parchment visible"
- "Wide shot of limestone-walled library, oil lamp on wooden desk center-frame, high narrow window upper left providing cool daylight, shadows cast downward"

**Check Process:**
1. Read Image Prompt
2. Ask: "Could I visualize this scene from this description?"
3. If too vague: too many unknowns
4. If too specific: generator may fail to match constraints exactly

**Action on Failure:** Rewrite Image Prompt to appropriate specificity level

---

### Rule 6.2: No Conflicting Instructions in Image & Negative

**Standard:** Image and Negative prompts should never contradict each other

**Examples of Conflicts:**
- ❌ Image says "blue eyes" / Negative says "no blue eyes"
- ❌ Image says "modern furniture" / Negative says "no modern"
- ❌ Image says "theatrical pose" / Negative says "no theatrical"

**Check Process:**
1. Identify key visual elements in Image Prompt
2. Check if any explicitly prohibited in Negative Prompt
3. If conflict found: resolve by removing from Image or reconsidering Negative

**Action on Failure:** Remove conflict by clarifying intention; choose Image or Negative direction

---

## Validation Workflow (Automated & Manual)

### Automated Checks (Future Automation)

```bash
# Validate asset IDs
validate_prompts.zsh SHOT_PROMPT_###_v1.0.md

# Validate prohibited terms
validate_content.py SHOT_PROMPT_###_v1.0.md

# Validate metadata
validate_metadata.zsh SHOT_PROMPT_###_v1.0.md
```

### Manual Review Checklist

**Before Submitting SHOT_PROMPT_### for G2 Gate:**

- [ ] All asset IDs exist in INDEX.md
- [ ] All asset statuses APPROVED or LOCKED
- [ ] Asset ID format correct (CHAR_*, LOC_*, PROP_*)
- [ ] MASTER_NEGATIVE_PROMPT.md base included
- [ ] Scene-specific negative terms added
- [ ] No prohibited terms in Image Prompt text
- [ ] All required sections completed (no placeholders)
- [ ] Bible references complete in metadata
- [ ] Asset IDs in metadata match prompt text
- [ ] YAML syntax valid
- [ ] Markdown renders correctly
- [ ] Version format correct (vX.Y)
- [ ] Status is DRAFT or IN_REVIEW (not APPROVED without approval)
- [ ] Continuity Handoff states match Scene Package
- [ ] Emotional continuity makes sense
- [ ] Image Prompt specificity appropriate
- [ ] No conflicting Image/Negative instructions

**Action if Any Fail:** Revise prompt and recheck before submission

---

## Related Documents

- [MASTER_NEGATIVE_PROMPT.md](NEGATIVE/MASTER_NEGATIVE_PROMPT.md) — Base negative prompt
- [../../02_ASSET_LIBRARY/INDEX.md](../../02_ASSET_LIBRARY/INDEX.md) — Asset catalog
- [../../01_GOVERNANCE/GOVERNANCE_GATES.md](../../01_GOVERNANCE/GOVERNANCE_GATES.md) — Gate 2 validation rules
- [../../01_PRODUCTION_BOOK/CHARACTER_BIBLE.md](../../01_PRODUCTION_BOOK/CHARACTER_BIBLE.md) — Character constraints
- [../../01_PRODUCTION_BOOK/ENVIRONMENT_BIBLE.md](../../01_PRODUCTION_BOOK/ENVIRONMENT_BIBLE.md) — Environment constraints
- [../../04_TEMPLATES/SHOT_PROMPT_TEMPLATE.md](../../04_TEMPLATES/SHOT_PROMPT_TEMPLATE.md) — Template

---

**VALIDATION RULES Status: LOCKED v1.0**  
**Effective: 2026-07-24**  
**Automated Tool Status: TODO (implement validate_prompts.zsh, validate_content.py)**

