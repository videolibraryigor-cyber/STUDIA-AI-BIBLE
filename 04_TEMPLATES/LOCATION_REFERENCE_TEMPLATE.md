# LOCATION & ENVIRONMENT REFERENCE TEMPLATE (Мастер-шаблон референса локации)
## AI FILM STUDIO — 02_ASSET_LIBRARY STANDARDS

**Статус:** MASTER TEMPLATE v1.0  
**Назначение:** Стандартизированный протокол генерации эталонных архитектурных и пространственных референсов (интерьеры, дворы, городские улицы).

---

## 1. Структура эталонного референса локации (3-Angle Environment Kit)

Каждая локация должна быть зафиксирована в 3 пространственных ракурсах:

```text
┌─────────────────────────────────────────────────────────────┐
│ 1. WIDE ESTABLISHING VIEW (Общий план пространства)         │
│    Геометрия стен, балки потолка, проемы окон, пропорции    │
├──────────────────────────────┬──────────────────────────────┤
│ 2. ACTION ZONE VIEW          │ 3. MATERIAL MACRO & TEXTURE  │
│    (Главная рабочая зона)    │    (Макро кладки и дерева)   │
└──────────────────────────────┴──────────────────────────────┘
```

---

## 2. Промпт-формула для генерации Location Reference

```text
Architectural concept reference sheet of {LOCATION_NAME}, {LOCATION_TYPE}, {HISTORICAL_PERIOD}:
Panel 1: Wide establishing view from eye-level perspective showing full room dimensions, limestone ashlar walls, cedar ceiling beams, stone tile floor, window apertures.
Panel 2: Medium shot of primary interaction zone ({DESK_SHELVES_DOOR}), showing spatial relationship between furniture and light sources.
Panel 3: Macro material close-up showing hand-chiseled limestone porosity, authentic mortar seams, aged wood grain, natural dust layer.
Lighting: Neutral diffused daytime lighting revealing true architectural colors (warm limestone, aged cedar brown, terracotta).
Shot on ARRI Alexa 65, 35mm wide anamorphic lens, 2.39:1 aspect ratio, hyper-realistic archaeological accuracy.
No modern construction, no medieval arches, no fantasy elements, no CGI gloss.
```

---

## 3. Критерии правильности локаций:
1. **Перспектива на уровне глаз (Eye-level Perspective):** Исключение искажений вертикальных линий стен.
2. **Археологическая подлинность:** Характер кладки строго соответствует эпохе (иродианский фасет, толщина стен 60–90 см).
3. **Физическая мотивированность источников света:** Четкое понимание, откуда в интерьер попадает естественный и искусственный свет.
