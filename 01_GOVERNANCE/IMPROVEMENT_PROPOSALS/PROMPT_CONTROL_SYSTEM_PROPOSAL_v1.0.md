PROMPT_CONTROL_SYSTEM_PROPOSAL_v1.0.md

# PROMPT CONTROL SYSTEM PROPOSAL v1.0

Status:
DRAFT

Purpose:
Create a controlled prompt generation system that preserves director intent during image and video generation.

---

# Problem Statement

Current AI generation can produce visually attractive results but may lose:

- character identity;
- scene continuity;
- lighting consistency;
- camera intention;
- historical accuracy;
- narrative purpose.

A prompt must not only describe what should appear.

A prompt must control what must NOT change.

---

# Prompt Generation Philosophy

The AI is not creating independent images.

The AI is creating shots belonging to one film.

Every generated shot must inherit:

- story context;
- previous shot state;
- character state;
- environment state;
- lighting state;
- camera language.

---

# Required Prompt Structure

Every shot output must contain:

## 1. STORY PURPOSE

Why this shot exists in the film.

---

## 2. CONTINUITY STATE

Previous shot information:

Character:
- identity
- appearance
- costume

Props:
- objects
- position
- condition

Environment:
- location
- time
- weather

Lighting:
- source
- color temperature
- contrast

---

## 3. IMAGE PROMPT

Must include:

- subject;
- action;
- environment;
- composition;
- lens;
- lighting;
- visual style.

---

## 4. NEGATIVE PROMPT

Must protect:

Character:
- no face change
- no age change
- no costume change

Environment:
- no architecture change
- no modern elements

Lighting:
- no color temperature shift
- no random lighting

Camera:
- no unwanted angles
- no scene change

---

## 5. VIDEO PROMPT

Video generation must be treated as animation of an existing shot.

Rules:

Use reference image as locked source.

Allowed:
- subtle movement;
- natural breathing;
- small gestures;
- controlled camera movement.

Forbidden:
- changing character;
- changing clothes;
- changing location;
- adding objects;
- changing lighting;
- changing time of day;
- cinematic transitions.

---

# Camera Control Rules

The prompt must specify:

- shot type;
- lens;
- camera position;
- camera movement;
- speed;
- duration.

Avoid vague instructions:

"cinematic movement"

Replace with:

"slow 10 cm push-in over 4 seconds, camera remains on same axis."

---

# Lighting Continuity Rules

Every scene must have:

LIGHTING LOCK:

- main light source;
- color temperature;
- shadow direction;
- contrast;
- atmosphere.

Adjacent shots must inherit the same lighting conditions.

---

# Goal

Create prompts that generate controlled cinematic shots instead of independent images.

The AI should behave like a cinematographer following a director's instructions.