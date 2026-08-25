DIRECTOR_AI_CONTINUITY_UPGRADE_PROPOSAL_v1.0.md


# DIRECTOR AI CONTINUITY UPGRADE PROPOSAL v1.0

Status:
DRAFT

Purpose:
Improve Director AI prompt generation by adding cinematic continuity control between shots.

## Problem Statement

Current AI generation workflow creates visually strong individual shots, but sometimes loses continuity between sequential shots.

Observed problems:

1. Props disappear between shots.
Example:
Shot 001:
Jesus prepares rope in the Temple.

Shot 002:
Jesus continues the action, but the rope is missing.

2. Character continuity breaks:
- clothing changes;
- hairstyle changes;
- age changes;
- facial features change.

3. Lighting continuity breaks:
- warm candlelight becomes cold daylight;
- different color temperature between adjacent shots;
- inconsistent shadows.

4. Video generation may introduce unwanted changes:
- camera moves too much;
- environment changes;
- new objects appear;
- scene composition changes.

## Required Solution

Create a Continuity Engine inside Director AI.

The system must maintain continuity between:

- previous shot;
- current shot;
- next shot.

## Continuity State

Every shot must contain:

### Character State
- identity
- age
- face
- costume
- emotional state
- position

### Prop State
- objects present
- object location
- object condition

### Environment State
- location
- architecture
- weather
- time of day

### Lighting State
- light source
- color temperature
- shadow direction
- contrast

### Camera State
- lens
- camera position
- movement restrictions

## Video Prompt Rules

Video prompts must not only describe movement.

They must contain:

- what can change;
- what cannot change.

Example:

LOCKED SHOT

Do not change:
- character identity
- clothing
- location
- lighting
- props

Allowed:
- small natural movement
- facial expression
- slow camera movement

Forbidden:
- scene transition
- new objects
- costume changes
- environment changes

## Goal

Every generated shot must feel like it belongs to the same film scene.