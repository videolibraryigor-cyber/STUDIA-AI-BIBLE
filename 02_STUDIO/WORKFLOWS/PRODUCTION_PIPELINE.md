# PRODUCTION PIPELINE (Производственный конвейер)

This document defines every production stage for AI FILM STUDIO projects and assigns responsibility for each stage to the correct AI role. `FILM_BLUEPRINT.md` is the single source of truth for creative, dramatic, and emotional decisions.

## Core Rule

- Director AI holds exclusive authority for cinematic decisions, shot composition, emotional beats, camera language, prompt wording, and directing choices.
- Theological Scholar AI holds scriptural and historical audit authority (Gate G0.5 and G3 artifact review).
- Copilot AI may only execute, document, structure, validate, and follow Director AI instructions.
- Production Designer & DoP establish 3-layer spatial depth, historical scenography, and optical character.
- Creative Assistant ensures subtext, action against resistance, and shot-to-shot transition continuity.
- No derived document may override `FILM_BLUEPRINT.md`.

## Production Stages

```text
1. Idea / Blueprint
   ↓ (Gate G0: Blueprint Lock)
2. Scriptural & Theological Audit (Theological Scholar AI / Gate G0.5)
   ↓
3. Scene Package & Subtext Pass (Creative Assistant AI / Gate G1)
   ↓
4. Staging & Technical Pass (Production Designer / DoP / Character Supervisor)
   ↓
5. Prompt Package Assembly (Prompt Brain AI / assemble_prompt.py)
   ↓ (Gate G2: Prompt Validation)
6. Key Image Generation (Multi-Pass Composition & Identity)
   ↓ (Gate G3: Identity, Depth & Theological Prop QC)
7. Video Generation (Single Motion Vector & Keyframe Interpolation)
   ↓ (Gate G4: Video Physics QC)
8. Edit / Sound / Color (Sound Designer & Colorist)
   ↓ (Gate G5: Final Approved Export)
```

## AI Roles and Boundaries

- **Director AI**
  - Responsibility: all creative authority, dramatic intent, and narrative alignment.
  - Inputs: `FILM_BLUEPRINT.md`, Project Bible, character and environment bibles, scene continuity.
  - Outputs: locked creative documents, scene packages, shot-level creative briefs, approval decisions.
  - Forbidden: Never delegate cinematic or emotional decisions to Copilot or generation AIs.

- **Theological Scholar AI**
  - Responsibility: scriptural accuracy, historical-archaeological validation of 1st-century Near East / biblical settings, checking props (scrolls vs books, lamps vs candles), and halakhic/biblical law compliance.
  - Inputs: `FILM_BLUEPRINT.md`, scene packages, asset libraries, scriptural texts.
  - Outputs: Theological Audit Reports, Gate G0.5 approvals, mandatory scriptural corrections.

- **Creative Assistant AI**
  - Responsibility: micro-dramaturgy, formulating action against resistance, checking eyeline matches, and scene pacing.
  - Inputs: Director creative briefs, scene packages.
  - Outputs: subtext notes, actor micro-action specs, transition continuity checks.

- **Production Designer & DoP AI**
  - Responsibility: 3-layer spatial depth (Foreground / Midground / Background), material micro-textures, archaeological accuracy, optical character (ARRI 65 / Cooke Anamorphic), and physically motivated light physics.
  - Inputs: Scene packages, environment bibles, shot list.
  - Outputs: spatial depth plans, material and lighting specifications for Shot Packages.

- **Character Supervisor AI**
  - Responsibility: character identity lock, costume states, hand and eye continuity, age and facial consistency.
  - Inputs: Character Bibles, asset library master turnarounds.
  - Outputs: character lock validation and continuity reports.

- **Sound Designer AI**
  - Responsibility: acoustic environment simulation (RT60 decay), organic foley design (parchment, cedar, linen, breathing), and mastering to -16 LUFS.
  - Inputs: `SOUND_DESIGN_BIBLE.md`, scene packages, master timeline.
  - Outputs: sound design cue sheets and audio generation prompts.

- **Prompt Engineer AI**
  - Responsibility: assemble technical prompt packages applying Master Style synthesis (v2.0 + v2.1 + v2.2), negative prompt bases, and Single Motion Vector constraints.
  - Inputs: Approved Scene Package, Staging and Technical decisions.
  - Outputs: `SHOT_###_PROMPT_vX.Y.md` files ready for generation engines.

- **QC AI & Vision QC AI**
  - Responsibility: validate compliance against locked materials, 3-layer depth, motion vector rules, and quality gates.
  - Inputs: scene packages, prompts, key images, generated video, QC checklists.
  - Outputs: pass/fail decisions, QC notes, version status updates.

- **Generation AI**
  - Responsibility: execute multi-pass image generation and keyframe-interpolated video generation.
  - Inputs: approved prompt packages, anchor keyframes, motion masks.
  - Outputs: key frames, video clips, rendered media.

- **Post-Production AI**
  - Responsibility: assemble approved renders, apply editorial timing, sound design, and color grading in DaVinci Resolve.
  - Inputs: QC-approved video clips, key frames, director notes.
  - Outputs: final cut, sound mix, color grade.

---

## Handoff Criteria Summary

- **Gate 0 (G0):** Project Bible locked.
- **Gate 0.5 (G0.5):** Scriptural & Theological Audit passed (Theological Scholar AI).
- **Gate 1 (G1):** Scene Package and Subtext approved.
- **Gate 2 (G2):** Prompt Package validated (all 3 Master Style layers + Single Motion Vector).
- **Gate 3 (G3):** Key image identity, 3-layer depth, and theological prop QC passed.
- **Gate 4 (G4):** Video motion and physics QC passed.
- **Gate 5 (G5):** Final export approved by Director.
