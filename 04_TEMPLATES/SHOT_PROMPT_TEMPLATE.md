# SHOT_### — PROMPT PACKAGE (Пакет промптов)

**Scene / Shot:** `SCENE_### / SHOT_###`  
**Status:** `PLANNED` / `VALIDATED`  
**Timecode / Duration:** `MM:SS–MM:SS (X.X sec)`  
**Reference assets:** `02_ASSET_LIBRARY/INDEX.md` (Asset IDs)  

---

## 1. Creative Brief & Subtext (Режиссёрская задача и подтекст)

2–3 предложения:
- Зачем существует кадр в истории.
- Внутренний конфликт / действие с сопротивлением (Action against resistance).
- Что эмоционально уносит зритель (Emotional takeaway).

---

## 2. Image Prompt (Промпт изображения)

### 1. Master Style (Главный стиль — обязательны все 3 слоя)
* **Layer 1 (v2.0):** Ultra photorealistic, museum-quality archaeological reconstruction, Biblical historical realism, natural imperfections, real materials, physically motivated lighting only, character consistency, no visual drift.
* **Layer 2 (v2.1):** ARRI Alexa 65 cinematic response, Cooke Full Frame Anamorphic lens character, optical depth, visible material microdetails (limestone pores, hand-cut stone, aged wood grain, coarse linen fibers), real skin pores and wrinkles, physically motivated light sources (3200K window / 2200K candle), ARRI color science, subtle cinematic film grain.
* **Layer 3 (v2.2):** Cinematic human realism: world feels lived not designed, inhabitants of history (not models), natural facial asymmetry, real historical film crew observation, no posed characters, no theatrical acting, prioritize human emotion.

### 2. Spatial Staging & 3-Layer Depth (Сценография и 3 плана глубины)
* **Foreground:** Размытый край кедрового стола / глиняная масляная лампа / угол свитка (optical framing & depth).
* **Midground:** Персонаж в резком фокусе, активный реквизит, точка взаимодействия.
* **Background:** Известняковая кладка (ashlar blocks), стеллажи свитков, луч заката из окна, взвесь пыли.

### 3. Scene (Сцена: место, время, исторический контекст)
### 4. Characters (Персонаж: locked identity, возраст, костюм, взгляд)
### 5. Lighting (Физический свет: угол падения, температура 3200K/2200K, глубокие мягкие тени)
### 6. Camera (Камера: крупность, оптика 35mm/50mm/85mm Anamorphic, ракурс на уровне глаз)
### 7. Action with Subtext (Действие с внутренним сопротивлением, положение рук)
### 8. Emotion & Micro-Expression (Эмоция, взгляд, дыхание, микромимика)

---

## 3. Negative Prompt (Негативный промпт)

Обязательная база: `MASTER_NEGATIVE_PROMPT.md`
+ Специфические запреты кадра:
`digital sharpening, oversaturated colors, modern objects, fantasy lighting, plastic skin, cgi look, theatrical grimacing, studio softbox, extra limbs, modern textiles, glass windows.`

---

## 4. Video Prompt & Motion Protocol (Промпт видео)

### Single Motion Vector (Один доминирующий вектор движения)
Выбрать строго **ОДИН** тип движения для предотвращения деформации лица:
* **Камера:** Медленный наезд (slow push-in / gentle dolly in 0.5m) при статичном персонаже.
* **Персонаж:** Микро-движение взгляда / медленный поворот головы / замирание руки при статичной камере.
* **Окружение:** Колебание пламени свечи и медленное движение пылинок в луче света.

### Keyframe Interpolation Guidance (First Frame → Last Frame)
* **Start Frame:** `SHOT_###_KEY_FRAME_START.png` (Исходное положение).
* **End Frame:** `SHOT_###_KEY_FRAME_END.png` (Целевое положение).
* **Motion Prompt:** Описание промежуточного перехода без перерисовки архитектуры и черт лица.
* **Negative Motion:** `no morphing, no face warping, no jitter, no camera shake, no deformation, preserve exact facial structure.`

---

## 5. Continuity Handoff (Передача непрерывности)

`Previous Shot Output State` → `This Shot Execution` → `Next Shot Input State`.
Фиксация: положение рук, направление взгляда (Eyeline match), состояние свечи/свитка, освещенность.
