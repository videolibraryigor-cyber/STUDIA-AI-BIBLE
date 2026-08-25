# РУКОВОДСТВО ПО ЗАЩИТЕ ОТ ОШИБОК И ДЕФЕКТОВ ГЕНЕРАЦИИ (ANTI-PITFALLS GUIDE)
## AI FILM STUDIO — ИНЖЕНЕРНЫЕ ПРАВИЛА СОСТАВЛЕНИЯ ПРОМПТОВ

**Статус:** ACTIVE v2.0 (Enhanced Edition)  
**Источник:** Адаптировано из `awesome-gpt-image-2` и адаптировано под кинематографический и исторический реализм студии.  
**Применение:** Обязательно к учету агентами `PROMPT_BRAIN_AI`, `CREATIVE_ASSISTANT_AI`, `PRODUCTION_DESIGNER_AI` и `DIRECTOR_AI`.

---

## 1. Сценарные и актерские правила (Character & Performance Protocols)

### 1.1. Закон декомпозиции черт лица (Анатомия против субъективной красоты)
* **Ловушка:** Использование фраз «очень красивая девушка», «мудрый старец», «привлекательное лицо». Модель не знает ваших субъективных стандартов и подставит шаблонный пластиковый глянец.
* **Инженерное правило:** Всегда раскладывать лицо на конкретные анатомические маркеры:
  * *Вместо:* `very beautiful ancient woman`
  * *Писать:* `eyes with peach-blossom curvature, high defined nose bridge, natural feathery eyebrows, soft eyelid fold, authentic Mediterranean skin texture with visible micro-pores, natural lip shape with soft tone`.

### 1.2. Закон тактильной материальности одежды (Объем через ткань)
* **Ловушка:** Описание одежды общими словами («traditional robe», «simple dress»). Персонаж становится плоским.
* **Инженерное правило:** Фиксация точного состава, переплетения нитей и плотности ткани:
  * *Формулировка:* `unbleached coarse woven linen tunic with visible warp and weft fibers, heavy organic lamb wool mantle with natural drape and rough fiber texture, aged vegetable-tanned leather belt with hammered iron buckle`.

### 1.3. Закон согласованности персонажа (Character Consistency Prefix)
* **Ловушка:** В серии шотов или в сетке ракурсов модель меняет форму бороды, тон кожи или покрой туники.
* **Инженерное правило:** Перед любым списком действий или сеткой кадров **обязательно** ставить префиксную блокировку:
  * *Формулировка:* `The exact same character, 100% consistent facial identity, identical hair and beard, identical outfit, and identical body proportions across all frames and panels.`

### 1.4. Закон якорей идентичности при создании моделей и референсов
* **Инженерное правило:** Сначала фиксируются неизменяемые черты (лицо, разрез глаз, прическа, одежда), и только потом определяются масштаб головы, стилизация или материал, чтобы исключить «превращение в другого человека».

### 1.5. Закон динамического глагола в сцене (Active Verb Rule)
* **Ловушка:** Пассивные «манекенные» описания («человек сидит в комнате»).
* **Инженерное правило:** Использовать глагол физического действия с сопротивлением:
  * *Формулировка:* «Персонаж замирает в движении, пальцы осторожно разглаживают край сухого пергамента, взгляд сфокусирован на строке текста».

---

## 2. Структурные правила сеток и раскадровок (Grid & Breakdown Protocols)

### 2.1. Закон строгой разметки таблиц действий (Action Grid Protocol)
* **Ловушка:** Запрос «нарисуй шаги движения персонажа» приводит к сжатию всех фаз в невнятную кашу.
* **Инженерное правило:** Всегда четко задавать матрицу, нумерацию и структуру каждой ячейки:
  * *Формулировка:* `4x4 grid layout with 16 equal-sized panels, separated by thin border lines, numbered 1 to 16 in top-left corners. Each cell features: bold number badge, centered full-body character action pose, directional motion arrows, and bottom 2-line concise text description.`

### 2.2. Закон процентной фиксации масштаба (Hero Scale Rule)
* **Ловушка:** Модель перегружает фон и отдаляет персонажа.
* **Инженерное правило:** Для средних и крупных планов жестко фиксировать:
  * *Формулировка:* `Subject occupies 40%-55% of the frame area, positioned in sharp optical focus`.

### 2.3. Запрет мудбордизации (`Single Frame Only`)
* **Инженерное правило:** Обязательное включение директивы для готовых кинокадров:
  * *Формулировка:* `Single finished cinematic frame only. No moodboard, no split-screen, no collage, no presentation grid, no sample borders.`

---

## 3. Оптические и исторические правила (Optics & Theological Shield)

### 3.1. Замена эпитетов на физические параметры оптики
* *Вместо «красивый свет»:* `Low-angle raking sunlight at 3200K entering through narrow stone aperture at 45 degrees, creating tactile relief across limestone pores`.
* *Вместо «размытый фон»:* `Cooke Anamorphic 50mm T2.0 with gentle oval bokeh, shallow depth of field, subtle highlight halation`.

### 3.2. Защита от псевдошрифтов и анахронизмов
* *Формулировка в Negative Prompt:* `no modern alphabet, no printed fonts, no latin letters, no illegible alien squiggles, no bound codex book, no plastic surfaces, no modern clothing.`
