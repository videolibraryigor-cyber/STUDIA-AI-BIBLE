# MOTION LOCKS (Фиксация движения в видеогенерации)
## AI FILM STUDIO — VIDEO GENERATION RULES

---

# MASTER MOTION RULE (Главное правило движения)

Only ONE primary motion vector per 3–5 second generation clip.

Never mix complex camera movement with large character body movement and heavy environmental physics in a single AI generation.

---

# MOTION VECTORS (Векторы движения)

### 1. CAMERA VECTOR (Вектор камеры)
* Allowed: Imperceptible slow push-in, gentle dolly in (max 0.5m), subtle lateral drift.
* Character state: Static or subtle breathing only.
* Environment: Subtle flame/dust motion.

### 2. CHARACTER VECTOR (Вектор персонажа)
* Allowed: Eyeline shift, subtle head turn, slow hand hesitation, finger adjustment on prop, visible slow inhale/exhale.
* Camera state: Locked-off / completely static tripod.

### 3. ENVIRONMENT VECTOR (Вектор среды)
* Allowed: Candle flame flicker, drifting dust motes in sunbeam, subtle fabric drape vibration.
* Camera & Character: Static.

---

# KEYFRAME CONTROL (First Frame → Last Frame)

For character and action transitions, use dual keyframe interpolation:
* `Start Keyframe`: Exact established state.
* `End Keyframe`: Target state.
* Video engine generates only intermediate physical movement.

---

# PROHIBITED IN VIDEO GENERATION (Строго запрещено)

* ❌ Face warping / facial structure mutation (сохранять 100% геометрию лица).
* ❌ Character morphing / costume changes during clip.
* ❌ Fast or sudden camera panning / whip pans.
* ❌ Unnatural sliding / floaty feet motion.
* ❌ Digital glitching, limb multiplication, physics breaks.
* ❌ Sudden lighting, exposure, or color temperature shifts.
