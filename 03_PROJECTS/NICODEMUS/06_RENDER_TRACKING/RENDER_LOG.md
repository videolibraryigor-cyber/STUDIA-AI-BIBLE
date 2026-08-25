# RENDER LOG & TRACKING REGISTRY
## PROJECT: NICODEMUS — 06_RENDER_TRACKING

**Status:** ACTIVE v1.0  
**Authority:** GENERATION AI / QC SUPERVISOR  
**Reference:** `01_GOVERNANCE/MODEL_STACK_SPEC.md`  

---

## Active Render Table

| Shot ID | Engine / Model | Seed / Settings | Keyframe Pass | Video Pass | QC Status | Render Output File | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `SHOT_001_A_ESTABLISHING` | FLUX.1 dev / Kling 1.5 | Seed: `849201948`, CFG: `3.5`, Motion: `3` | PASS (3-Layer Depth) | PASS (Slow push-in) | `APPROVED (G4)` | `SHOT_001_A_v1.0.mp4` | Establishing library shot, sunset light |
| `SHOT_001_B_CLOSE_FACE` | FLUX.1 dev + IP-Adapter | Seed: `109283741`, CFG: `3.2`, Motion: `2` | PLANNED | PLANNED | `IN_REVIEW` | — | Focus on eyes and micro-expression |
| `SHOT_002_A_SCROLL_SHELF` | FLUX.1 dev / Kling 1.5 | Seed: `550291823`, CFG: `3.5`, Motion: `3` | PLANNED | PLANNED | `DRAFT` | — | Shelf detail, hand hesitation |

---

## Log Template for New Generations

```markdown
### SHOT_###_[NAME]
- **Date / Time:** YYYY-MM-DD HH:MM
- **Generator Engine:** [e.g., FLUX.1 dev / Kling 1.5 Pro]
- **Seed:** [e.g., 49201948]
- **Parameters:** CFG: [X.X], Steps: [XX], Sampler: [DPM++ 2M], Motion Scale: [X]
- **Input Keyframe:** `03_PROJECTS/NICODEMUS/04_SCENES/SCENE_###/SHOT_###_KEY_FRAME_START.png`
- **Output Video:** `03_PROJECTS/NICODEMUS/07_FINAL_EXPORTS/SHOT_###_v1.0.mp4`
- **QC Result:** [PASS / FAIL] (Notes on anatomy, face stability, lighting drift)
```
