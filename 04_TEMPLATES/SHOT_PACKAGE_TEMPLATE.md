# SHOT PACKAGE TEMPLATE

This document is the MASTER TEMPLATE for a single cinematic shot in AI FILM STUDIO. It is the production passport for one shot and the authoritative reference for all shot-level deliverables.

This template is NOT a prompt template and NOT a scene template.
It is a shot-level package that records:
- creative intent from the Director,
- continuity locks,
- spatial staging (3-layer depth) and production design,
- technical camera and lighting requirements,
- character subtext and performance constraints,
- video motion vector and keyframing protocols,
- generation handoff data,
- QC criteria,
- deliverables and version history.

## Core Integration

Use this template with the following locked reference documents:
- `FILM_BLUEPRINT.md` — single source of narrative, tone, story structure, and visual philosophy
- `03_PROJECTS/NICODEMUS/01_PRODUCTION_BOOK/PROJECT_BIBLE.md` — dramatic route and creative laws
- `03_PROJECTS/NICODEMUS/01_PRODUCTION_BOOK/CHARACTER_BIBLE.md` — locked character identity and performance constraints
- `03_PROJECTS/NICODEMUS/01_PRODUCTION_BOOK/ENVIRONMENT_BIBLE.md` — locked environment definition and historical authenticity
- `03_PROJECTS/NICODEMUS/MASTER_SHOT_LIST.md` — authoritative shot inventory and asset mapping
- `03_PROJECTS/NICODEMUS/MASTER_TIMELINE.md` — timing and music synchronization
- `03_PROJECTS/NICODEMUS/SHOT_ID_SYSTEM.md` — shot identification, naming, and versioning rules
- `03_PROJECTS/NICODEMUS/03_PROMPT_LIBRARY/VALIDATION_RULES.md` — prompt validation requirements
- `01_GOVERNANCE/GOVERNANCE_GATES.md` — gate definitions and approvals
- `01_GOVERNANCE/VERSIONING_PROTOCOL.md` — version lifecycle and revision rules
- `02_STUDIO/WORKFLOWS/PRODUCTION_PIPELINE.md` — production role boundaries and handoff criteria

Do not duplicate information that already exists in these source documents. Instead, reference them explicitly and record only shot-specific implementation details.

---

## 1. Metadata

---

**Shot ID:** `SHOT_###_[DRAMATIC_FUNCTION]`

**Scene ID:** `SCENE_###`

**Version:** `v1.0` / `v1.1` / `v2.0`

**Status:** `DRAFT` / `IN_REVIEW` / `APPROVED`

**Gate:** `G1` / `G2` / `G3` / `G4` / `G5`

**Owner:** Director AI / Production Designer / DoP / Prompt Engineer AI / QC AI / Generation AI / Post-Production AI

**Dependencies:**
- `SCENE_PACKAGE_###_vX.Y.md` (scene package reference)
- `MASTER_SHOT_LIST.md` (shot allocation)
- `MASTER_TIMELINE.md` (timing reference)
- `SHOT_###_PROMPT_vX.Y.md` (after G2)
- previous shot package or preceding continuity package
- relevant asset IDs from `02_ASSET_LIBRARY/INDEX.md`

**References:**
- `FILM_BLUEPRINT.md`
- `PROJECT_BIBLE.md`
- `CHARACTER_BIBLE.md`
- `ENVIRONMENT_BIBLE.md`
- `SHOT_ID_SYSTEM.md`
- `VALIDATION_RULES.md`
- `GOVERNANCE_GATES.md`
- `VERSIONING_PROTOCOL.md`
- `PRODUCTION_PIPELINE.md`

---

## 2. Story & Subtext

### Narrative Purpose
Describe the one reason this shot exists in the film. Connect it directly to the Blueprint story structure and to the shot's dramatic function in the scene.

### Dramatic Beat
Record the exact emotional/dynamic beat from the Blueprint or Project Bible.
- Example: `Curiosity → Wonder`, `Inner Conflict`, `Search for answers`, `Return to Present`, `Peace`.

### Emotional Goal
Specify what the audience should feel and why. Use film-production terminology such as:
- `tension`, `revelation`, `restraint`, `uncertainty`, `repose`, `resolve`, `contemplation`, `anticipation`.

### Director's Intention & Subtext
Capture the Director's approved creative note in 2–3 precise sentences. Detail the **subtext** (what remains unspoken) and ensure the shot avoids static, unmotivated posing.

---

## 3. Continuity

### Input State
Document the shot's beginning state in terms of:
- Nicodemus's emotional/physical state
- environment state
- props state
- lighting and time of day
- continuity relationship to previous shot or scene

### Output State
Document the shot's ending state in the same terms. Ensure the output state feeds into the next shot without creating new dramatic events.

### Character State
Record the approved character condition from `CHARACTER_BIBLE.md`:
- costume state
- gaze direction & Eyeline Match
- breathing / micro-expression anchor
- emotional register

### Prop State
Describe key prop condition and placement at shot start and finish, including scroll position, table objects, lamp/candle state, and any hand-object relationships.

### Environment State
Describe the locked environment for this shot:
- location: `LOC_NICODEMUS_LIBRARY` or other approved set
- room condition and spatial orientation
- background continuity elements that must remain stable

### Lighting State
Describe exact light sources and their state at the start and end of the shot:
- natural light direction and quality
- candle / oil lamp placement and intensity
- any transition or change in light during the shot

---

## 4. Spatial Staging & Camera (Production Designer & DoP Pass)

### 3-Layer Spatial Depth Plan (Эшелонирование планов)
1. **Foreground (Передний план / Кулисы):**
   - Out-of-focus edge of cedar table / unlit terracotta oil lamp / hanging linen weave / limestone doorframe corner.
   - Purpose: Creates authentic optical depth, frame within a frame, and cinematic immersion.
2. **Midground (Средний план / Центр внимания):**
   - Nicodemus in sharp optical focus, active prop interaction (scroll / candle / desk).
   - Purpose: Narrative focus and emotional delivery.
3. **Background (Задний план / Окружение):**
   - Deep limestone masonry (ashlar blocks), scroll shelves, window light shaft, atmospheric dust.
   - Purpose: Archaeological context, spatial scale, and atmospheric perspective.

### Shot Size
Choose one standard size and justify it in relation to story intent:
- `EXTREME_WIDE`, `WIDE`, `MEDIUM`, `MEDIUM_CLOSE`, `CLOSE_UP`, `EXTREME_CLOSE`

### Lens & Optical Character
- Optics: `ARRI Alexa 65 Large Format`, `Cooke Full Frame Anamorphic` (2.39:1 aspect ratio)
- Focal length: `35mm Anamorphic` (wide/environment), `50mm Anamorphic` (medium), `85mm Anamorphic T1.9` (close-up)
- Depth of Field: `deep focus`, `shallow focus with organic anamorphic bokeh falloff`, `selective focus`

### Camera Height & Angle
- Relative height: `eye level` (default for dignity/observation), `waist level`, `table level`, `low angle`, `high angle`

### Distance & Stance
- Physical relationship: `intimate`, `observational`, `detached`, `immersive`

### Composition Strategy
- Visual balance: `rule of thirds`, `leading lines (desk/shelves)`, `negative space (isolation/thought)`
- Framing: full body, torso, head-and-shoulders, detail/macro

### Focus Strategy & Eyeline Match
- Focus point: primary subject plane, optical falloff
- Eyeline angle: direction of gaze aligned with light source, prop, or off-screen subject

### Blocking
- Actor & prop blocking in 3D space: coordinates relative to desk, window, and primary light source.

---

## 5. Lighting & Scenography

### Time of Day & Narrative Atmosphere
Exact narrative time: `sunset`, `night`, `late evening`, `dawn`, `blue hour`.

### Motivated Light Sources & Temperature
- Primary source: `window sunset (3200–3800K)` / `moonlight (5600K)`
- Secondary source: `beeswax candle / oil lamp flame (2000–2400K)`
- Bounce & Fill: `warm limestone bounce (natural fill)`, strictly no artificial studio lighting.

### Light Direction & Modeling
- `Raking side light` (revealing stone pores and facial micro-texture), `soft highlight rolloff`, `natural deep shadows`.

### Contrast Ratio
- `High contrast` / `soft-medium contrast` / `gentle shadow gradients`.

---

## 6. Character Performance & Micro-Action

### Action Against Resistance (Действие с сопротивлением)
Describe the physical action motivated by internal conflict (e.g., hesitant touch, arrested breath, slow deliberate unrolling of parchment).

### Facial Micro-Expressions & Eyes
Gaze quality (focused, searching, softening), brow tension, jaw set, subtle eye moisture.

### Hands & Tactile Interaction
Hand state (resting, trembling, protective, searching), exact finger placement on scroll/props.

### Body Language & Posture
Spine posture (dignified, burdened, leaning forward in discovery), shoulder alignment.

### Performance Pace & Rhythm
Tempo: `measured`, `hesitant`, `deliberate`, `urgent`, `soft`, `arrested pause`.

---

## 7. Environment & Material Authenticity

### Active Props & Artifacts
- `PROP_MEMORY_SCROLL`, `PROP_CEDAR_TABLE`, `PROP_CANDLE`, `PROP_STONE_WEIGHT`, `PROP_WINDOW`.

### Material Micro-Textures (Production Designer Pass)
- Porous limestone grain, aged cedar wood fibers, coarse woven linen tunic, aged parchment edges, beeswax melting texture.

### Atmospheric Quality
- Air density, subtle airborne dust motes in light beams, absence of modern/synthetic air effects.

---

## 8. Image Generation (Keyframe Pass)

### MASTER STYLE Reference
Unified synthesis of `MASTER_STYLE_v2.0` (Core Philosophy) + `v2.1` (Optical & Microdetail) + `v2.2` (Human Realism).

### Image Prompt
Final generator-ready narrative prompt assembled from Story, Staging, Character, Camera, Lighting, and Master Style.

### Negative Prompt
Comprehensive negative protection lock (`MASTER_NEGATIVE_PROMPT.md` + shot-specific prohibitions).

---

## 9. Video Generation & Motion Protocol

### Single Motion Vector Rule (Принцип одного вектора движения)
*CRITICAL:* To prevent AI video model morphing and facial distortion, specify **ONLY ONE primary motion vector** per 3–5 second clip:
- [ ] **Vector Option A — Camera Motion:** Slow observational push-in / gentle dolly (subject and environment remain in micro-motion).
- [ ] **Vector Option B — Subject Motion:** Character turns head / shifts gaze / moves hand (camera remains locked-off).
- [ ] **Vector Option C — Environmental Motion:** Drifting dust in light beam / flickering candle flame / moving fabric (camera and character static).

### Keyframe Interpolation Protocol (First Frame → Last Frame)
- **First Frame (Start State):** `SHOT_###_FRAME_START.png` (Exact approved keyframe).
- **Last Frame (End State):** `SHOT_###_FRAME_END.png` (Target state after motion completes).
- **Interpolation Goal:** Smooth linear/natural transition without structural redesign.

### Motion Brush & Masking Guidance
- **Locked Zones (No motion):** Facial bone structure, background architecture, table geometry.
- **Active Motion Zones:** Eye pupil shift, gentle breathing (chest displacement ≤ 2%), candle flame, dust motes.

### Secondary Motion & Physics
- Physically motivated fabric drape, flame behavior, dust air currents.

### Timing & Music Cue
- Exact duration (seconds), timeline timecode, audio rhythm synchronization.

---

## 10. Quality Control

### Pre-generation Checklist (G2 Gate)
- [ ] Director-approved shot purpose matches `FILM_BLUEPRINT.md`
- [ ] 3-layer spatial depth (Foreground / Midground / Background) defined
- [ ] Action formulated with subtext and resistance (no static posing)
- [ ] Single Motion Vector selected for video generation
- [ ] Optical and lighting parameters physically motivated
- [ ] Master Style includes all three layers (v2.0 + v2.1 + v2.2)
- [ ] Negative Prompt includes `MASTER_NEGATIVE_PROMPT.md`

### Post-generation Checklist (G3/G4 Gate)
- [ ] Key image matches 3-layer staging and character identity
- [ ] Video motion preserves facial structure without morphing or warping
- [ ] No digital sharpening artifacts, plastic skin, or anachronisms
- [ ] Continuity and lighting direction preserved across adjacent shots

### Validation Results & Sign-off
- Pre-gen QC: `PASS` / `FAIL` | Key Image QC: `PASS` / `FAIL` | Video QC: `PASS` / `FAIL`
- Approver: Director AI / QC AI / Date: `YYYY-MM-DD`

---

## 11. Deliverables

- **Key Frame (Start):** `SHOT_###_KEY_FRAME_vX.Y.png`
- **Key Frame (End):** `SHOT_###_KEY_FRAME_END_vX.Y.png` (if using 2-frame protocol)
- **Video:** `SHOT_###_vX.Y.mp4`
- **Upscale:** `SHOT_###_UPSCALED_vX.Y.png`
- **Source & Final Prompt:** Reference ID in Prompt Library
- **QC Report:** Link to QC log entry

---

## 12. Revision History

| Version | Date | Author | Summary | Notes |
|---------|------|--------|---------|-------|
| v1.0 | YYYY-MM-DD | [Name] | Production-ready shot package | Full gate cycle |
| v1.1 | YYYY-MM-DD | [Name] | Non-creative fix (metadata) | Quick pass |
| v2.0 | YYYY-MM-DD | [Name] | Creative / staging rethink | Full re-approval |
