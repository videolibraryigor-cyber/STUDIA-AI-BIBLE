# PROP & ARTIFACT REFERENCE TEMPLATE (Мастер-шаблон референса реквизита)
## AI FILM STUDIO — 02_ASSET_LIBRARY STANDARDS

**Статус:** MASTER TEMPLATE v1.0  
**Назначение:** Стандартизированный протокол генерации эталонных референсов предметного мира (свитки, светильники, посуда, печати, мебель).

---

## 1. Структура эталонного референса предмета (Prop Sheet)

Каждый ключевой реквизит создается в виде ортографического планшета из 3 элементов:

```text
┌──────────────────────────────┬──────────────────────────────┐
│       HERO 3/4 VIEW          │     TOP / SIDE PROFILE       │
│   (Главный изометрический)   │    (Проекция сбоку/сверху)   │
├──────────────────────────────┴──────────────────────────────┤
│               TACTILE MACRO & MATERIAL BREAKDOWN            │
│          (Макро-текстура поверхности, стыки, износ)         │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Промпт-формула для генерации Prop Reference

```text
Prop design reference sheet of {PROP_NAME}, {ERA_AND_CULTURE}:
Main view: 3/4 hero perspective showing full item geometry, volume, and authentic proportions.
Side view: clean orthographic profile showing thickness, silhouette, and joinery.
Macro insert: extreme close-up showing material texture, tactile surface imperfections, tool marks, natural aging, wear patterns.
Made of authentic historical materials: {MATERIALS_SPEC: e.g., aged animal parchment, hand-turned olive wood, porous clay, oxidized bronze}.
Clean neutral studio lighting, soft neutral light gray background (#e8e8e8), razor-sharp optical detail, 8k resolution product render.
No modern elements, no plastic sheen, no varnish, no fantasy glowing runes, no artificial perfection.
```

---

## 3. Критерии правильности предметов:
1. **Историческая материальность:** Следы ручной работы (нетесаные волокна дерева, следы гончарного круга на глине, неровности краев папируса).
2. **Следы эксплуатации (Weathering):** Потемнения в местах хвата руками, мелкие сколы, патина на бронзе, копоть у фитиля.
3. **Масштабная привязка:** Указание относительного размера (относительно ладони или стола).
