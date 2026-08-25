# AI FILM STUDIO (ИИ-КИНОСТУДИЯ)

Автономная мультиагентная производственная среда для создания кинематографических фильмов с помощью ИИ (AI-assisted cinematic film production).

Флагманский завершенный проект — `NICODEMUS`. Студия готова к производству новых картин (`DAVID_AND_SAUL` и последующих).

## Быстрый старт и документация

1. **Главная инструкция по эксплуатации:** [`STUDIO_OPERATING_MANUAL.md`](file:///Users/ihorsedy/Documents/AI_FILM_STUDIO%202/STUDIO_OPERATING_MANUAL.md) — пошаговый регламент создания фильмов.
2. **Конституция и правила:** [`01_GOVERNANCE/STUDIO_CONSTITUTION.md`](file:///Users/ihorsedy/Documents/AI_FILM_STUDIO%202/01_GOVERNANCE/STUDIO_CONSTITUTION.md), [`01_GOVERNANCE/AGENTS.md`](file:///Users/ihorsedy/Documents/AI_FILM_STUDIO%202/01_GOVERNANCE/AGENTS.md).
3. **Производственный конвейер:** [`02_STUDIO/WORKFLOWS/PRODUCTION_PIPELINE.md`](file:///Users/ihorsedy/Documents/AI_FILM_STUDIO%202/02_STUDIO/WORKFLOWS/PRODUCTION_PIPELINE.md).
4. **Спецификация моделей генерации:** [`01_GOVERNANCE/MODEL_STACK_SPEC.md`](file:///Users/ihorsedy/Documents/AI_FILM_STUDIO%202/01_GOVERNANCE/MODEL_STACK_SPEC.md).

## Консольный оркестратор (`studio_agent.py`)

* `python3 05_AUTOMATION/studio_agent.py --status` — статус студии и список проектов;
* `python3 05_AUTOMATION/studio_agent.py --new-project <NAME> --title "<TITLE>"` — создать новый фильм;
* `python3 05_AUTOMATION/studio_agent.py --compile-prompt <PATH_TO_SHOT>` — скомпилировать промпт кадра;
* `python3 05_AUTOMATION/studio_agent.py --qc-image <IMAGE> --shot-id <ID>` — визуальный аудит кадра;
* `python3 05_AUTOMATION/studio_agent.py --audit` — системный аудит целостности студии.

## Карта системы

- `00_SOURCE_ARCHIVE/` — исходные защищенные архивы проектов (точка отката).
- `01_GOVERNANCE/` — конституция студии, гейты контроля качества и матрица нейросетей.
- `02_STUDIO/` — роли виртуальной группы (Director, DoP, Production Designer, Sound Designer, QC) и пайплайны.
- `03_PROJECTS/` — кинопроекты студии (`NICODEMUS`, `DAVID_AND_SAUL`, ...).
- `04_TEMPLATES/` — мастер-шаблоны сцен, шотов, промптов и генераций.
- `05_AUTOMATION/` — скрипты компиляции промптов, визуального аудита и мастер-оркестратор агентов.
- `06_REPORTS/` — протоколы системного аудита и архитектурные отчеты.
- `07_ARCHIVE/` — архивные версии и промежуточные материалы.
- `08_MASTER_STYLE/` — 3-уровневый кинематографический мастер-стиль (v2.0, v2.1, v2.2).
- `09_PROMPT_BLOCKS/` — 11 залоченных модульных блоков фиксации (Locks).

## Статусы документов

`DRAFT` → `IN_REVIEW` → `APPROVED` → `LOCKED`.

`LOCKED` — только для чтения. Любое изменение начинается как новая версия `v1.1`, а не перезапись.
