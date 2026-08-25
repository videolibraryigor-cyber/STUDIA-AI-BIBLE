# CHARACTER REFERENCE SHEET TEMPLATE (Мастер-шаблон референса персонажа)
## AI FILM STUDIO — 02_ASSET_LIBRARY STANDARDS

**Статус:** MASTER TEMPLATE v1.0  
**Назначение:** Стандартизированный протокол генерации эталонных референсов персонажей (Model Sheet / Turnaround Sheet / Expression Sheet).

---

## 1. Структура эталонного референса персонажа (Turnaround Sheet)

Эталонный референс персонажа состоит из 4 обязательных ракурсов в едином масштабе на одном листе:

```text
┌──────────────┬──────────────┬──────────────┬──────────────┐
│  FRONT VIEW  │   3/4 LEFT   │ PROFILE LEFT │  BACK VIEW   │
│  (Прямо)     │ (3/4 Слева)  │  (Профиль)   │  (Со спины)  │
└──────────────┴──────────────┴──────────────┴──────────────┘
```

### Критерии правильности Turnaround:
1. **Нейтральный студийный фон:** Однородный нейтрально-серый (`#d8d8d8`) или чистый белый фон. *Запрещены сложные интерьеры, пейзажи и случайные тени.*
2. **Рассеянный нейтральный свет:** Мягкий бестеневой свет (Soft daylight / Flat neutral lighting). Исключить жесткие контрастные тени, скрывающие черты лица или одежду.
3. **Единый масштаб и выравнивание:** Линия глаз, подбородка, плеч, пояса и стоп строго выровнена по горизонтали на всех 4 ракурсах.
4. **Фиксация позы:** Базовая T-pose или расслабленная A-pose (руки опущены вдоль тела, ладони полураскрыты).

---

## 2. Промпт-формула для генерации Turnaround Sheet

```text
Character design model sheet, 4-view turnaround of {CHARACTER_NAME}: front view, three-quarter view, profile side view, back view. 
Consistent character identity across all views: {AGE} years old, {ETHNICITY} facial features, {EYE_COLOR} eyes, {HAIR_BEARD_SPEC}.
Wearing authentic historical costume: {COSTUME_LAYERS_AND_COLORS}, natural materials ({LINEN_WOOL_LEATHER}).
All 4 views aligned horizontally with exact same proportions, height, and clothing details.
Neutral studio lighting, soft diffused light, pure light gray background (#e0e0e0), full body standing pose, ultra-high resolution, sharp optical focus.
No background elements, no scenery, no dramatic lighting, no modern clothing, no identity drift.
```

---

## 3. Матрица мимики и эмоций (Expression Sheet)

Сетка 2×3 (6 ключевых эмоциональных состояний персонажа для крупных планов):
1. **Contemplative / Neutral (Покой / Размышление):** базовое расслабленное состояние, спокойный взгляд.
2. **Curiosity / Wonder (Интерес / Удивление):** легкий подъем бровей, расширение зрачков, дыхание задержано.
3. **Inner Conflict / Doubt (Сомнение / Конфликт):** легкое сведение бровей, напряжение челюсти.
4. **Fear / Uncertainty (Опасение / Тревога):** настороженный взгляд, плотно сжатые губы.
5. **Grief / Empathy (Скорбь / Сострадание):** увлажненные глаза, мягкий наклон головы.
6. **Faith / Peace (Вера / Преображение):** открытый взгляд, мягкое расслабление лица, внутренний свет.

---

## 4. Чек-лист приемки референса персонажа (Character Asset QC)

- [ ] Лицо четко различимо на всех ракурсах (поры кожи, структура бороды, форма носа).
- [ ] Одежда детализирована (швы, фактура ткани, отсутствие синтетического блеска).
- [ ] Руки и пальцы анатомически безупречны (5 пальцев на каждой кисти, натуральные ногти).
- [ ] Отсутствуют артефакты диффузии, смазывания и пластиковая кожа.
