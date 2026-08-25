# MASTER_STYLE_ASSEMBLY_PROCESS

**Version:** v1.0  
**Status:** OPERATIONAL  
**Purpose:** Systematic process for assembling existing Master Style rules into final Image Prompt  
**Scope:** Prompt Engineer workflow, Stage 4 (Prompt Package creation)  
**Reference:** PRODUCTION_PIPELINE.md, PROMPT_BUILD_ORDER.md, VALIDATION_RULES.md

---

## 1. PURPOSE

### Why This Process Exists

Every Image Prompt must include visual rules from three Master Style layers (v2.0, v2.1, v2.2) plus rules from 10 PROMPT_BLOCKS. Without systematic assembly:

- Rules get missed (human error)
- Time is wasted synthesizing manually
- Inconsistency between shots
- Difficult to audit reasoning
- Rule 3.4 validation fails (VALIDATION_RULES.md)

**This process:**
- Makes rule assembly systematic, not intuitive
- Provides step-by-step guidance
- Ensures completeness (all three layers)
- Creates audit trail (what rules applied, why)
- Reduces errors and time per shot
- Enables consistent output

### Assembly Output

Completed Master Style section of Image Prompt:

```
## Image prompt (Промпт изображения)

### 1. Master style (Главный стиль)

[ASSEMBLED FROM THIS PROCESS]

Ultra photorealistic, museum-quality archaeological reconstruction, Biblical historical realism...
[rules from v2.0]

ARRI Alexa 65 cinematic response, Cooke Full Frame Anamorphic lens character...
[rules from v2.1]

Cinematic human realism: world feels lived not designed, people are inhabitants...
[rules from v2.2]

[Additional rules from PROMPT_BLOCKS applying to shot]

### 2-8. Scene, Characters, Environment, Lighting, Camera, Action, Emotion
[Continue with other Image Prompt sections]
```

---

## 2. INPUT LAYERS

### Layer 1: MASTER_STYLE_v2.md — Core Visual Philosophy

**Contains:** 30 foundational rules organized by category:
- Core Philosophy (6 rules)
- Visual Style (9 rules)
- Cinematic Look (10 rules)
- Color Science (8 rules)
- Lighting (6 rules)
- Materials (5 rules)
- Camera Language (5 rules)
- Character Rendering (4 rules)
- Continuity (3 rules)
- Atmosphere (3 rules)
- Final Rule (1 rule)

**Authority:** Highest. Overrides all other style documents.

**Applied:** Every prompt must include 3-5 specific v2.0 rules appropriate to shot type.

---

### Layer 2: MASTER_STYLE_ENHANCEMENT_v2.1.md — Quality Enhancement

**Contains:** 10 detailed enhancement layers with 63 specific rules:
1. Optical Character (8 rules: camera model, lens behavior, optical effects)
2. Material Microdetail (11 rules: surface texture, aging, imperfections)
3. Historical Realism Enhancement (8 rules: period accuracy, signs of use)
4. Atmospheric Depth (8 rules: dust, light, haze, perspective)
5. Skin Realism Enhancement (7 rules: texture, wrinkles, asymmetry, age)
6. Light Quality Enhancement (5 rules: rolloff, shadows, bounce, contrast)
7. Color Science (7 rules: ARRI palette, saturation, tone curve)
8. Film Grain and Image Texture (4 rules: grain, texture, structure)
9. Human Scale & Camera Observation (6 rules: observation style, gesture, emotion)
10. Final Director Quality Check (5 rules: verification questions)

**Authority:** Medium. Implements v2.0 philosophy with technical specificity.

**Applied:** Every prompt must include 8-12 specific v2.1 rules appropriate to shot type, focusing on layers relevant to shot (e.g., close-up = layers 5+9; wide shot = layers 3+7).

---

### Layer 3: MASTER_STYLE_ENHANCEMENT_v2.2.md — Cinematic Human Realism

**Contains:** 1 section with 16 specific rules:
- World feels lived, not designed
- People are inhabitants of history (not models)
- Every face carries a story
- Natural skin texture and imperfections
- Scenes feel captured by real historical film crew
- No posed characters, no theatrical acting
- No artificial beauty
- Prioritize human emotion and environmental storytelling
- Visual references (The Passion of the Christ, The Chosen, etc.)
- Performance priorities

**Authority:** Medium. Ensures human authenticity across all shots.

**Applied:** Every prompt must include 4-6 specific v2.2 rules, ensuring psychological realism and natural human behavior.

---

### Layer 4: PROMPT_BLOCKS — Locked Constraints (10 Files)

**Files in priority order:**

1. **MASTER_LOCKS.md** — Override rules
   - Priority resolution: MASTER_LOCKS > other locks
   - Continuity never violated
   - Character identity never changed
   - Environment never changed (unless screenplay requires)

2. **CHARACTER_LOCKS.md** — Character identity (absolute)
   - Face, age, hair, beard, eyes, skin tone, body proportions
   - Costume, accessories, expression style
   - Performance constraints (reserved, quiet dignity)
   - Applied to every shot with character present

3. **ENVIRONMENT_LOCKS.md** — Location constraints (absolute)
   - Props, materials, architectural elements
   - No modern objects, no contemporary design
   - Applied to every location shot

4. **LIGHTING_BIBLE.md** — Lighting rules
   - Only physically motivated sources
   - Specific light direction/color per location/time
   - Applied to all shots with lighting choices

5. **COLOR_LOCKS.md** — Color palette
   - Specific warm earth tones
   - No neon, no synthetic saturation
   - Applied to color grading phase

6. **CAMERA_LOCKS.md** — Camera language
   - Natural framing, eye level observation
   - No impossible shots, no floating camera
   - Applied to every shot's framing

7. **CONTINUITY_LOCKS.md** — Between-shot consistency
   - Lighting consistency within sequence
   - Character state continuity
   - Applied when assembling sequences

8. **EMOTION_LOCKS.md** — Emotional constraints
   - Restrained acting style
   - Subtlety over spectacle
   - Applied to character performance shots

9. **CINEMATOGRAPHY_LOCKS.md** — Cinematic language
   - Quiet observation style
   - No unmotivated movement
   - Applied to camera motion decisions

10. **NEGATIVE_LOCKS.md** (MASTER_NEGATIVE_PROMPT.md)
    - Prohibited terms (modern, medieval, fantasy, Hollywood, CGI, etc.)
    - Applied to Negative Prompt section

---

### Layer 5: Shot Package — Technical Specifications

**Input from SHOT_PACKAGE_###.md sections:**
- Section 3: Continuity (input/output states)
- Section 4: Camera (size, lens, height, distance, movement)
- Section 5: Lighting (time, sources, direction, contrast, color temperature)
- Section 6: Character Performance (expression, eyes, hands, body language, pace)
- Section 7: Environment (active props, background, atmosphere, dust, weather)
- Section 8: Image Generation (Master style notes, continuity handoff)

**Role:** Shot-specific technical decisions made by Director/DoP/Designer.

**Integration:** Assembly process respects these decisions and embeds them in Image Prompt layers.

---

## 3. PRIORITY ORDER (Conflict Resolution)

### Authority Hierarchy When Rules Conflict

If two rules contradict, apply in this order:

```
1. STORY / BIBLICAL ACCURACY (highest)
   └─ What story requires; what historical accuracy demands
      Example: If story requires candlelight only, no other light sources

2. CHARACTER IDENTITY (CHARACTER_LOCKS)
   └─ Character must remain absolutely identical across film
      Example: Nicodemus's face never changes; age never changes

3. ENVIRONMENT AUTHENTICITY (ENVIRONMENT_LOCKS)
   └─ Location/props must remain period-authentic
      Example: No modern furniture, no anachronistic objects

4. MASTER_STYLE_v2.md (Core Philosophy)
   └─ Photorealism, no spectacle, no synthetic look
      Example: Museum-quality reconstruction takes priority over visual beauty

5. CAMERA LANGUAGE (CAMERA_LOCKS, v2.0)
   └─ Observational, natural framing, human eye level
      Example: Natural camera takes priority over dramatic angles

6. ATMOSPHERE & MOOD (MASTER_STYLE_v2.1 + v2.2)
   └─ Ancient feeling, lived-in world, human realism
      Example: Material microdetail reinforces emotional truth

7. TECHNICAL OPTIMIZATION (lowest)
   └─ Generation efficiency, rendering speed
      Example: Can be overridden by any higher authority
```

**MASTER_LOCKS Rule:** "If two lock files conflict, MASTER_LOCKS has priority."  
Applies to conflicts WITHIN locks (CHARACTER_LOCKS vs. ENVIRONMENT_LOCKS). Story/Biblical accuracy still takes precedence over MASTER_LOCKS.

---

## 4. ASSEMBLY FORMULA

### Step-by-Step Assembly Process

**Input:** SHOT_PACKAGE_###_v1.0.md + Scene Package + Character Bible + Environment Bible

**Output:** Completed Master Style section (### 1. Master style) for SHOT_PROMPT_###_v1.0.md

---

### STEP 1: Read Shot Context

**What:** Understand the shot before applying rules

```
[ ] 1.1 Read Shot Package section 8 (Image Generation) → Master Style notes
[ ] 1.2 Identify shot type: WIDE / MEDIUM / CLOSE-UP / EXTREME_CLOSE / MEDIUM_CLOSE
[ ] 1.3 Identify shot function: Establishing / Character focus / Emotional beat / Continuity
[ ] 1.4 Identify location from Shot Package section 7 (Environment)
[ ] 1.5 Identify time of day from Section 5 (Lighting State)
[ ] 1.6 Note character state from Section 6 (Character Performance)
```

---

### STEP 2: Assemble Layer 1 — MASTER_STYLE_v2.md

**What:** Core visual philosophy foundation

**How:** Read v2.0 rules, select 3-5 rules applicable to this shot

**Start with these always-applicable rules:**
- "Ultra photorealistic, museum-quality archaeological reconstruction"
- "Biblical historical realism"
- "Everything must feel physically photographed instead of AI generated"
- "Beauty is always secondary to truth"

**Add shot-type specific rules:**

```
For WIDE / ESTABLISHING shots:
[ ] "Natural framing, natural perspective"
[ ] "No impossible drone shots, no virtual camera feeling"
[ ] "Large format depth"

For CLOSE-UP / CHARACTER shots:
[ ] "Characters must remain absolutely identical across entire film"
[ ] "Natural human proportions"
[ ] "Emotion through composition instead of effects"

For LIGHTING scenes:
[ ] "Lighting must always be physically motivated"
[ ] "Every light source must exist inside the scene"
[ ] "Never fake dramatic lighting, never use studio lighting"

For ENVIRONMENT shots:
[ ] "Every material must contain microscopic imperfections"
[ ] "Everything carries age, everything carries use"
[ ] "Nothing is factory perfect"
```

**Result:** 1 paragraph with 3-5 v2.0 rules + their specific articulation

**Example:**
```
Ultra photorealistic, museum-quality archaeological reconstruction, Biblical historical realism 
with natural imperfections and real materials. Every frame must feel physically photographed; 
nothing should look digital or synthetic. Physically motivated lighting only (window and candle). 
Character identity absolutely locked across entire film.
```

---

### STEP 3: Assemble Layer 2 — MASTER_STYLE_ENHANCEMENT_v2.1.md

**What:** Technical quality enhancements (10 layers, 63 rules)

**How:** Review the 10 enhancement layers, select 8-12 rules applicable to this shot's technical requirements

**Enhancement Layer Selection by Shot Type:**

```
WIDE / ESTABLISHING shot → Select from:
[ ] Layer 1: Optical Character (ARRI 65, Cooke lens)
[ ] Layer 3: Historical Realism (architecture, period accuracy)
[ ] Layer 4: Atmospheric Depth (dust, volumetric light, distance haze)
[ ] Layer 7: Color Science (natural earth palette)
[ ] Layer 10: Director QC (Does it look photographed?)

CLOSE-UP / CHARACTER shot → Select from:
[ ] Layer 2: Material Microdetail (for hands, costume, textures)
[ ] Layer 5: Skin Realism (pores, wrinkles, asymmetry, age)
[ ] Layer 6: Light Quality (highlight rolloff, shadow transitions)
[ ] Layer 9: Human Scale (quiet observation, small gestures)
[ ] Layer 10: Director QC

LIGHTING-CRITICAL shot → Select from:
[ ] Layer 4: Atmospheric Depth (dust, light quality, perspective)
[ ] Layer 6: Light Quality (shadows, bounce, contrast)
[ ] Layer 7: Color Science (ARRI palette, warm/cool balance)
[ ] Layer 8: Film Grain (natural photographic texture)

ENVIRONMENT / LOCATION shot → Select from:
[ ] Layer 2: Material Microdetail (limestone, wood, leather, aging)
[ ] Layer 3: Historical Realism (uneven surfaces, human presence)
[ ] Layer 4: Atmospheric Depth (subtle haze, distance)
[ ] Layer 7: Color Science (weathered cedar, dust browns, stone gray)
```

**Result:** 2-3 paragraphs with 8-12 specific v2.1 rules + their technical articulation

**Example (Close-up):**
```
ARRI Alexa 65 cinematic response with Cooke Full Frame Anamorphic lens character; natural anamorphic 
depth and subtle lens breathing. Real skin pores, natural wrinkles, small facial asymmetry, subtle age 
details visible (60-year-old scholar). Realistic beard texture, authentic Mediterranean skin tones. 
Soft highlight rolloff and natural shadow transitions; realistic bounce light from candlelight fill. 
ARRI-style color science with warm amber tones. Subtle cinematic film grain, natural photographic texture, 
organic image structure. Quiet observation style; camera observes life unfolding.
```

---

### STEP 4: Assemble Layer 3 — MASTER_STYLE_ENHANCEMENT_v2.2.md

**What:** Cinematic human realism (16 rules)

**How:** Select 4-6 rules ensuring psychological authenticity

**Always include for character-present shots:**
- "World feels lived, not designed"
- "People are inhabitants of history (not models)"
- "No posed characters, no theatrical acting, no artificial beauty"

**Add psychological depth:**
```
[ ] "Every face carries a story" (then articulate Nicodemus's age/wisdom)
[ ] "Scenes feel captured by real historical film crew" (quiet observation)
[ ] "Small imperfections and natural asymmetry" (not perfect beauty)
[ ] "Prioritize human emotion and environmental storytelling" (why this moment matters)
```

**For environment-only shots:**
```
[ ] "World must feel lived" → How environment shows human habitation?
[ ] "Environmental storytelling" → What does space reveal about its inhabitants?
```

**Result:** 1 paragraph with 4-6 v2.2 rules + psychological articulation

**Example:**
```
Cinematic human realism: world feels lived, not designed. Nicodemus is an inhabitant of history, 
not a model in costume. His face carries the story of a 60-year-old scholar; small imperfections 
and natural asymmetry convey authenticity. Scenes feel captured by a real historical film crew 
observing life unfolding. No posed characters, no theatrical acting, no artificial beauty. 
Prioritize human emotion and environmental storytelling.
```

---

### STEP 5: Apply PROMPT_BLOCKS in Priority Order

**What:** Add locked constraints from 10 PROMPT_BLOCKS files

**When:** After assembling all three Master Style layers, check and add applicable locks

**Order of application:**

```
[ ] 5.1 Read MASTER_LOCKS.md
     └─ Understand override hierarchy; check for conflicts between other locks
     
[ ] 5.2 Apply CHARACTER_LOCKS.md (if character present)
     └─ Character identity constraints (absolute lock)
     └─ Add to Master Style: specific reference to CHAR_NICODEMUS locked appearance
     
[ ] 5.3 Apply ENVIRONMENT_LOCKS.md (if location shot)
     └─ Location/prop constraints (absolute lock)
     └─ Add to Master Style: specific reference to LOC_NICODEMUS_LIBRARY locked details
     
[ ] 5.4 Apply LIGHTING_BIBLE.md
     └─ Lighting source and direction rules
     └─ Already included in Master Style v2.0 (physically motivated only)
     
[ ] 5.5 Apply COLOR_LOCKS.md
     └─ Color palette rules
     └─ Already included in Master Style v2.0 (natural earth palette)
     
[ ] 5.6 Apply CAMERA_LOCKS.md
     └─ Natural framing, observational stance
     └─ Already included in Master Style v2.0 (camera language)
     
[ ] 5.7 Apply CONTINUITY_LOCKS.md
     └─ Between-shot consistency rules
     └─ Reference in Continuity Handoff section, not Master Style
     
[ ] 5.8 Apply EMOTION_LOCKS.md
     └─ Restrained acting, subtlety
     └─ Already included in Master Style v2.0 + v2.2
     
[ ] 5.9 Apply CINEMATOGRAPHY_LOCKS.md
     └─ Quiet observation, no unmotivated movement
     └─ Already included in Master Style v2.0 (camera language)
     
[ ] 5.10 Note NEGATIVE_LOCKS.md
     └─ Applied to Negative Prompt section (Step 8), not Master Style
```

**Result:** Confirm all applicable locks are referenced in Master Style section

---

### STEP 6: Synthesize into Master Style Section

**What:** Combine all three layers + locks into single coherent section

**Format:**

```
### 1. Master style (Главный стиль)

**Reference:** MASTER_STYLE_v2.md + MASTER_STYLE_ENHANCEMENT_v2.1.md + MASTER_STYLE_ENHANCEMENT_v2.2.md

[Paragraph 1: Layer 1 rules + foundation]
Ultra photorealistic, museum-quality archaeological reconstruction...

[Paragraph 2: Layer 2 rules + technical specifications]
ARRI Alexa 65 cinematic response, Cooke Full Frame Anamorphic lens...

[Paragraph 3: Layer 3 rules + human authenticity]
Cinematic human realism: world feels lived, not designed...

[Paragraph 4: Character/Location locks if applicable]
Character reference: CHAR_NICODEMUS locked appearance (age 60-62, olive Mediterranean, grey beard...)
Location reference: LOC_NICODEMUS_LIBRARY locked environment (limestone, cedar, natural light)...

[Total: 3-5 coherent paragraphs, 150-300 words]
```

---

### STEP 7: Validate Master Style Section Against VALIDATION_RULES Rule 3.4

**What:** Check that all three layers are present

**Checklist (Rule 3.4):**

```
[ ] 3-5 specific rules from MASTER_STYLE_v2.md included?
    └─ Check for: photorealistic, historical realism, no synthetic, no spectacle
    
[ ] 8-12 specific rules from MASTER_STYLE_ENHANCEMENT_v2.1.md included?
    └─ Check for: camera model, lens behavior, material detail, skin texture, light quality, color science, film grain
    
[ ] 4-6 specific rules from MASTER_STYLE_ENHANCEMENT_v2.2.md included?
    └─ Check for: lived world, inhabitants not models, no theatrical acting, psychological depth, emotional realism
```

**If validation fails:**
- Return to Step 2 and add missing rules
- Do not proceed until all three layers present

**If validation passes:**
- Continue to STEP 8

---

### STEP 8: Continue with Image Prompt Sections 2-8

**What:** After Master Style is complete, assemble remaining Image Prompt sections

**Sections:**
```
### 2. Scene (Сцена: место, время, история)
└─ Use Shot Package section 7 (Environment)

### 3. Characters (Персонажи и asset IDs)
└─ Use Shot Package section 6 (Character Performance) + CHARACTER_LOCKS

### 4. Environment / Props (Среда / реквизит)
└─ Use Shot Package section 7 (Environment) + ENVIRONMENT_LOCKS

### 5. Lighting (Свет)
└─ Use Shot Package section 5 (Lighting) + LIGHTING_BIBLE

### 6. Camera (Камера: крупность, объектив, композиция)
└─ Use Shot Package section 4 (Camera) + CAMERA_LOCKS

### 7. Action (Действие)
└─ Use Shot Package section 6 (Character Performance)

### 8. Emotion (Эмоция)
└─ Use Shot Package section 2 (Narrative Purpose / Emotional Goal)
```

---

### STEP 9: Assemble Negative Prompt

**What:** Prohibited terms (NEGATIVE_LOCKS.md = MASTER_NEGATIVE_PROMPT.md)

**Structure:**
```
## Negative Prompt

Master base (from MASTER_NEGATIVE_PROMPT.md):
[Include full base list]

Scene-specific additions:
[Add shot-specific anachronisms to avoid]
```

**Reference:** VALIDATION_RULES.md Rule 2.1 + Rule 2.2

---

### STEP 10: Assemble Video Prompt (If Applicable)

**What:** Motion, timing, physics (separate from Image Prompt)

**Reference:** Shot Package section 9 (Video Generation)

**Rule:** Do not duplicate Image Prompt descriptions; only motion-specific instructions

---

### STEP 11: Complete Continuity Handoff

**What:** Input state → this shot → output state

**Reference:** Shot Package section 3 (Continuity)

**Structure:**
```
## Continuity handoff

Previous state: [what was true in previous shot]
This shot: [what changes in this shot]
Next state: [what will be true in next shot]

Hands: [position continuity]
Gaze: [eye direction continuity]
Props: [object state continuity]
Light: [lighting consistency]
Direction: [screen direction]
Emotion: [emotional arc]
```

---

### STEP 12: Validate Complete SHOT_PROMPT Against VALIDATION_RULES

**What:** Final QC before submission to Gate 2

**Checklist (see Section 6 below)**

**If all checks pass:** Submit for Gate 2 validation

**If any check fails:** Revise sections 2-12 and revalidate

---

## 5. SHOT TYPE ADAPTATION

### How to Apply Assembly Formula to Different Shot Types

**Same assembly process for all shots, but EMPHASIS varies by type:**

---

### 5.1 WIDE / ESTABLISHING SHOT

**Purpose:** Reveal location, context, time, mood

**Master Style emphasis:**
- Layer 1: Visual style + cinematic look + camera language
- Layer 2: Optical character (ARRI 65, lens), atmospheric depth, color science, historical realism
- Layer 3: World feels lived (not decorated)
- Locks: ENVIRONMENT_LOCKS (location details), LIGHTING_BIBLE, COLOR_LOCKS

**Master Style focus (3-5 rules from each layer):**

```
Layer 1 examples:
- "Large format depth, organic film grain, natural lens softness"
- "Every material contains microscopic imperfections"
- "No decorative polish; everything carries age and use"

Layer 2 examples:
- "ARRI Alexa 65 cinematic response, Cooke anamorphic lens character"
- "Visible material microdetails: limestone pores, hand-cut stone, aged wood grain, cedar beams"
- "Subtle atmospheric depth: thin airborne dust, soft volumetric sunlight, gentle atmospheric perspective"
- "Natural earth palette: warm limestone, olive greens, weathered cedar, dust browns, stone gray"

Layer 3 examples:
- "World feels lived, not designed; people inhabit this space"
- "Environmental storytelling: what does the space reveal about its inhabitants?"
```

---

### 5.2 CLOSE-UP / CHARACTER SHOT

**Purpose:** Reveal inner state, emotion, identity detail

**Master Style emphasis:**
- Layer 1: Character rendering + emotion through composition
- Layer 2: Skin realism, light quality, human scale, material microdetail
- Layer 3: Small imperfections, natural asymmetry, every face carries a story
- Locks: CHARACTER_LOCKS (identity locked), EMOTION_LOCKS, LIGHTING_BIBLE

**Master Style focus (3-5 rules from each layer):**

```
Layer 1 examples:
- "Characters remain absolutely identical across entire film"
- "Emotion through composition instead of effects"
- "Natural human proportions, no stylization"

Layer 2 examples:
- "Real skin pores, natural wrinkles, small facial asymmetry, subtle age details (60-year-old scholar)"
- "Realistic beard texture, authentic Mediterranean skin tones"
- "Soft highlight rolloff, natural shadow transitions, realistic bounce light"
- "Subtle cinematic film grain, natural photographic texture"

Layer 3 examples:
- "Every face carries a story; Nicodemus's age and wisdom visible"
- "Small imperfections convey authenticity, not perfection"
- "No posed character; capture natural human behavior"
```

---

### 5.3 CHARACTER SHOT (Medium shot with emotional focus)

**Purpose:** Balance character and environment; emotional moment with spatial context

**Master Style emphasis:**
- Layer 1: Character rendering + natural framing + emotion
- Layer 2: All 10 enhancement layers apply (optical, skin, light, human scale)
- Layer 3: World feels lived; character inhabits space
- Locks: CHARACTER_LOCKS, ENVIRONMENT_LOCKS, EMOTION_LOCKS

**Master Style focus (3-5 rules from each layer):**

```
Layer 1 examples:
- "Character identity absolutely locked; environment consistent with locked location"
- "Natural framing observes character in context; camera does not show off"
- "Emotion through subtle channels: eyes, breath, careful gestures"

Layer 2 examples:
- "ARRI Alexa 65 with Cooke anamorphic lens; natural depth balances character and space"
- "Material details: skin texture, costume fabric aging, environmental weathering all visible"
- "Light quality: physically motivated (only window and candle), soft rolloff, natural shadows"
- "Quiet observation: small gestures, meaningful pauses, no theatrical posturing"

Layer 3 examples:
- "World feels lived; character inhabits this space naturally"
- "No posed acting; character behaves like a real inhabitant of history"
```

---

### 5.4 ENVIRONMENT SHOT (Location detail, no character)

**Purpose:** Establish or reinforce space authenticity

**Master Style emphasis:**
- Layer 1: Materials + continuity + atmosphere
- Layer 2: Material microdetail, historical realism, atmospheric depth, color science
- Layer 3: Environmental storytelling (what does space reveal?)
- Locks: ENVIRONMENT_LOCKS, LIGHTING_BIBLE, COLOR_LOCKS

**Master Style focus (3-5 rules from each layer):**

```
Layer 1 examples:
- "Every material contains microscopic imperfections; everything carries age and use"
- "No visual drift within sequence; lighting remains consistent"
- "Ancient atmosphere: dust moves naturally, silence is visible"

Layer 2 examples:
- "Visible limestone pores, hand-cut stone irregularities, natural erosion marks"
- "Aged wood grain, cedar texture, olive wood imperfections"
- "Subtle atmospheric depth: dust in warm light, volumetric sunlight, natural distance haze"
- "Period-accurate materials and construction methods visible"

Layer 3 examples:
- "Environmental storytelling: space reveals its inhabitants (orderly scholar's library)"
- "World feels lived in: signs of human presence, realistic scale, small imperfections"
```

---

### 5.5 DIALOGUE SCENE SHOT

**Purpose:** Character interaction, emotional beats through conversation

**Master Style emphasis:**
- Layer 1: Character rendering + natural framing + continuity
- Layer 2: Skin realism, light quality, human scale, film grain
- Layer 3: Natural behavior, no theatrical acting, small gestures, meaningful pauses
- Locks: CHARACTER_LOCKS, EMOTION_LOCKS, CONTINUITY_LOCKS, LIGHTING_BIBLE

**Master Style focus (3-5 rules from each layer):**

```
Layer 1 examples:
- "Characters remain absolutely identical; emotional drift tracking character arc"
- "Natural framing over-the-shoulder or profile; camera observes conversation"
- "Continuity locked: same lighting, same character state, no jarring cuts"

Layer 2 examples:
- "Real skin pores, natural expressions, subtle micro-expressions visible"
- "Natural shadow transitions as characters move; realistic bounce light between faces"
- "Quiet observation style: camera captures authentic reactions, not reactions for camera"
- "Subtle film grain maintains organic, photographed feeling"

Layer 3 examples:
- "No posed acting; character responds naturally to dialogue"
- "Small gestures convey emotion: a hand movement, a gaze shift, a breath pause"
- "Emotional truth through subtlety, not theatrical expression"
```

---

## 6. FINAL QC CHECKLIST

### Pre-Generation Validation (Before Submitting to Gate 2)

**Use this checklist to validate SHOT_PROMPT_###_v1.0.md before submitting for QC approval**

---

### 6.1 Master Style v2.0 Completeness

```
[ ] Core Philosophy included?
    └─ Photorealistic? Museum-quality reconstruction? Biblical realism?
    
[ ] Visual Style included?
    └─ No synthetic look, no spectacle, emotion through composition?
    
[ ] Cinematic Look included?
    └─ ARRI 65, Cooke anamorphic, organic film grain, natural softness?
    
[ ] Color Science included?
    └─ Natural earth palette, no neon, no synthetic saturation?
    
[ ] Lighting included?
    └─ Physically motivated only, fire/moon/sun behave like real, no fake dramatic lighting?
    
[ ] Materials included?
    └─ Microscopic imperfections, age and use visible, nothing factory perfect?
    
[ ] Camera Language included?
    └─ Natural framing, human eye level, no impossible shots?
    
[ ] Character Rendering included (if character present)?
    └─ Absolutely identical across film?
    
[ ] Continuity included?
    └─ No visual drift, identical lighting/weather/props within sequence?
    
[ ] Total v2.0 rules: 3-5 included? ✓
```

---

### 6.2 Master Style v2.1 Completeness

```
[ ] Optical Character included?
    └─ ARRI Alexa 65, Cooke lens character, optical imperfections?
    
[ ] Material Microdetail included?
    └─ Limestone pores, hand-cut stone, aged wood grain, woven fibers, wear marks?
    
[ ] Historical Realism included?
    └─ Period authenticity, signs of human presence, archaeological accuracy?
    
[ ] Atmospheric Depth included?
    └─ Dust, volumetric light, distance haze, natural perspective?
    
[ ] Skin Realism included (if close-up)?
    └─ Real pores, wrinkles, asymmetry, age details, Mediterranean tones?
    
[ ] Light Quality included?
    └─ Soft rolloff, shadow transitions, bounce light, warm/cool contrast?
    
[ ] Color Science included?
    └─ ARRI-style palette, warm highlights, balanced white balance?
    
[ ] Film Grain included?
    └─ Subtle cinematic grain, natural photographic texture?
    
[ ] Human Scale included?
    └─ Quiet observation, natural movement, small gestures, meaningful pauses?
    
[ ] Director QC included?
    └─ Does it look photographed? Feel historically possible? Lighting exist in world? Materials real?
    
[ ] Total v2.1 rules: 8-12 included? ✓
```

---

### 6.3 Master Style v2.2 Completeness

```
[ ] Lived World included?
    └─ World feels lived, not designed?
    
[ ] Inhabitants included?
    └─ People are inhabitants of history (not models)?
    
[ ] Story in Face included (if character)?
    └─ Every face carries a story (age, wisdom, emotion)?
    
[ ] Small Imperfections included?
    └─ Natural asymmetry, not artificial beauty?
    
[ ] Captured by Real Crew included?
    └─ Scenes feel like historical cinematography?
    
[ ] No Theatrical included?
    └─ No posed characters, no theatrical acting, no artificial beauty?
    
[ ] Human Emotion included?
    └─ Prioritize emotion and environmental storytelling?
    
[ ] Total v2.2 rules: 4-6 included? ✓
```

---

### 6.4 CHARACTER_LOCKS Applied

```
[ ] Character name and reference included?
    └─ Example: "CHAR_NICODEMUS locked appearance (age 60-62, olive Mediterranean, grey beard...)"
    
[ ] Face identity locked?
    └─ Age, eyes, nose, beard, expression style?
    
[ ] Costume locked?
    └─ "Cream/off-white linen tunic, dark wool cloak, simple belt, leather sandals"?
    
[ ] Body locked?
    └─ Height, build, posture, proportions?
    
[ ] Performance locked?
    └─ "Reserved, quiet dignity, never smiling broadly, always calm"?
    
[ ] No drift in identity?
    └─ Prompt does not suggest changing any locked aspects?
```

---

### 6.5 ENVIRONMENT_LOCKS Applied

```
[ ] Location name and reference included?
    └─ Example: "LOC_NICODEMUS_LIBRARY locked environment"?
    
[ ] Materials specified?
    └─ Limestone walls, cedar beams, wooden shelves?
    
[ ] Props locked?
    └─ "Cedar desk, memory scrolls, candle, stone weight, oil lamp"?
    
[ ] No anachronisms?
    └─ No modern furniture, no contemporary objects, no wrong period elements?
    
[ ] Architectural authenticity?
    └─ Hand-cut stone, aged materials, worn surfaces, lived-in appearance?
```

---

### 6.6 LIGHTING_BIBLE Applied

```
[ ] Only physically motivated sources listed?
    └─ "Window sunlight at sunset, desk candle" (example for library)?
    
[ ] Light direction specified?
    └─ "Side/back light from high window, fill from candle"?
    
[ ] No studio lighting, no glamour lighting?
    └─ Prompt does not suggest beauty lighting or dramatic rigs?
    
[ ] Color temperature accurate?
    └─ "Warm amber from candlelight, golden edge from sunset"?
    
[ ] Consistency within sequence?
    └─ Lighting state referenced from previous shot continuity?
```

---

### 6.7 CAMERA_LOCKS Applied

```
[ ] Natural framing?
    └─ "Observational", "eye level", "non-judgmental"?
    
[ ] Shot size specified?
    └─ WIDE / MEDIUM / CLOSE-UP justified for shot purpose?
    
[ ] Lens specified?
    └─ Normal / wide / telephoto appropriate to story?
    
[ ] No impossible shots?
    └─ "Static or slow dolly" (not unmotivated floating camera)?
    
[ ] Camera height human?
    └─ "Eye level" or justified exception?
```

---

### 6.8 NEGATIVE_LOCKS Applied

```
[ ] Base negative prompt included?
    └─ Full MASTER_NEGATIVE_PROMPT.md terms listed?
    
[ ] Scene-specific additions included?
    └─ Shot-specific anachronisms and risks added?
    
[ ] No prohibited terms in Image Prompt?
    └─ Check Image Prompt sections 2-8 do not mention "modern", "fantasy", "CGI", etc.?
```

---

### 6.9 Validation Rules Compliance

```
[ ] Rule 3.4: All Master Style layers included? ✓
[ ] Rule 3.1: All Image Prompt sections completed? ✓
[ ] Rule 2.1: Negative base + scene-specific? ✓
[ ] Rule 1.1-1.3: Asset IDs valid format? ✓
[ ] No prohibited terms in Image Prompt? ✓
[ ] YAML metadata correct? ✓
```

---

### 6.10 Final Sign-Off

```
SHOT_PROMPT_###_v1.0.md Status:

[ ] All sections completed (no "TBD" or "PENDING")
[ ] All three Master Style layers present
[ ] All applicable locks applied
[ ] All validation rules pass
[ ] Ready for Gate 2 submission

Prompt Engineer signature: ____________________
Date: ____________________
```

---

## ESCALATION & NOTES

### When to Ask for Clarification

**STOP assembly and escalate if:**

1. **Shot Package contradicts locked materials**
   - Example: Character state conflicts with CHARACTER_LOCKS
   - Escalate to: Director AI

2. **Master Style rules contradict each other**
   - Example: v2.0 says "quiet" but shot calls for "dramatic"
   - Escalate to: Director AI (resolve via authority hierarchy)

3. **Technical specification impossible**
   - Example: Extreme close-up demands ARRI 65 + Cooke anamorphic (incompatible)
   - Escalate to: Director AI (propose alternative)

4. **Ambiguity in Shot Package sections**
   - Example: Lighting state unclear or missing
   - Escalate to: Director AI / DoP (request shot package revision)

5. **Conflict between Shot Package and Character/Environment Bibles**
   - Example: Environment Bible says location has windows, Shot Package says indoor lighting only
   - Escalate to: Director AI (resolve continuity)

### Assembly Time Estimate

- STEP 1-2 (read + Layer 1): 5-10 minutes
- STEP 3 (Layer 2): 10-15 minutes
- STEP 4 (Layer 3): 5 minutes
- STEP 5 (PROMPT_BLOCKS): 5-10 minutes
- STEP 6-7 (synthesis + validation): 5-10 minutes
- STEP 8-12 (other sections): 15-25 minutes
- **Total per shot: 45-75 minutes** (depending on complexity)

### Recording Reasoning

Consider recording why each major rule was applied:

```
ASSEMBLY NOTES (for audit trail):

SHOT_001_A is WIDE/ESTABLISHING shot
├─ Applied v2.0: Cinematic Look (ARRI, Cooke, film grain) — needed for establishing scale/period
├─ Applied v2.1: Atmospheric Depth + Historical Realism + Color Science — needed to show lived environment
├─ Applied v2.2: World feels lived — library must feel like inhabited space
├─ Applied CHARACTER_LOCKS: Nicodemus entering space, identity locked
├─ Applied ENVIRONMENT_LOCKS: Library architecture, cedar/limestone/natural light only
└─ Time spent: 58 minutes
```

---

## REFERENCE DOCUMENTS

- [PROMPT_BUILD_ORDER.md](../PROMPT_BUILD_ORDER.md) — 12-step sequence
- [MASTER_STYLE_v2.md](../08_MASTER_STYLE/MASTER_STYLE_v2.md) — Layer 1 core philosophy
- [MASTER_STYLE_ENHANCEMENT_v2.1.md](../08_MASTER_STYLE/MASTER_STYLE_ENHANCEMENT_v2.1.md) — Layer 2 enhancements
- [MASTER_STYLE_ENHANCEMENT_v2.2.md](../08_MASTER_STYLE/MASTER_STYLE_ENHANCEMENT_v2.2.md) — Layer 3 human realism
- [09_PROMPT_BLOCKS/MASTER_LOCKS.md](../09_PROMPT_BLOCKS/MASTER_LOCKS.md) — Lock override rules
- [09_PROMPT_BLOCKS/CHARACTER_LOCKS.md](../09_PROMPT_BLOCKS/CHARACTER_LOCKS.md) — Character constraints
- [09_PROMPT_BLOCKS/ENVIRONMENT_LOCKS.md](../09_PROMPT_BLOCKS/ENVIRONMENT_LOCKS.md) — Location constraints
- [SHOT_PROMPT_TEMPLATE.md](../../04_TEMPLATES/SHOT_PROMPT_TEMPLATE.md) — Output format
- [VALIDATION_RULES.md](../../03_PROJECTS/NICODEMUS/03_PROMPT_LIBRARY/VALIDATION_RULES.md) — QC rules
- [PRODUCTION_PIPELINE.md](./PRODUCTION_PIPELINE.md) — Stage 4 context

---

**Process Version:** v1.0  
**Effective Date:** 2026-08-09  
**Status:** OPERATIONAL
