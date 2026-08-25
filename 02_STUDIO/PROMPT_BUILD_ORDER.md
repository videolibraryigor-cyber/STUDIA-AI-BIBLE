PROMPT_BUILD_ORDER.md

## CANONICAL MASTER STYLE (Обязательная цепочка)

Все три слоя Master Style ОБЯЗАТЕЛЬНЫ при сборке финального Image Prompt.
Отсутствие любого слоя = невалидный промпт.

**Layer 1: MASTER_STYLE_v2.md**
- Base visual philosophy (базовая философия)
- Core rules: photorealism, museum authenticity, no spectacle

**Layer 2: MASTER_STYLE_ENHANCEMENT_v2.1.md**
- 10 quality enhancement layers (10 детальных слоёв усиления)
- Optical character, material microdetail, historical realism, atmospheric depth,
  skin realism, light quality, color science, film grain, human scale, director QC

**Layer 3: MASTER_STYLE_ENHANCEMENT_v2.2.md**
- CINEMATIC HUMAN REALISM (17-й раздел визуальной философии)
- Lived world feeling, human authenticity, no theatrical acting

---

## PROMPT BUILD ORDER (Порядок сборки промпта)

1. **MASTER_STYLE** (MANDATORY: v2.0 + v2.1 + v2.2)
2. MASTER_LOCKS
3. CHARACTER_LOCKS
4. ENVIRONMENT_LOCKS
5. LIGHTING_LOCKS
6. COLOR_LOCKS
7. CAMERA_LOCKS
8. CONTINUITY_LOCKS
9. EMOTION_LOCKS
10. CINEMATOGRAPHY_LOCKS
11. SHOT_DESCRIPTION
12. NEGATIVE_PROMPT
