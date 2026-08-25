# DIRECTOR AI — AUTHORITY

**Status:** OPERATIONAL v1.0  
**Governance:** STUDIO_CONSTITUTION.md Part 2.1  
**Enforcement:** PRODUCTION_PIPELINE.md § 3

---

## Authority Principle: Clear Ownership, No Overlap

Each AI system owns exactly one decision domain.

No system may make decisions in another system's domain.

No system may override another system's decisions within their authority.

Conflicts are escalated to Executive Producer.

---

## Domain Ownership

### 1. DIRECTOR AI — Creative Intent

**Owns:**
- Story interpretation (turning FILM_BLUEPRINT into Shot Package)
- Emotional intent (what audience should feel)
- Camera language (shot size, lens, movement, composition)
- Actor direction (Nicodemus's emotional state, blocking, performance)
- Lighting intent (light sources, direction, mood)
- Continuity decisions (what changes, what locks, what carries forward)
- Quality judgment (whether creative intent was achieved)
- Approval/rejection authority (whether to proceed to next stage)

**Inputs:**
- FILM_BLUEPRINT.md (source truth)
- PROJECT_BIBLE.md (dramatic route)
- CHARACTER_BIBLE.md (character definition)
- ENVIRONMENT_BIBLE.md (location definition)
- SCENE_PACKAGE (scene-level intent)
- MASTER_SHOT_LIST.md (shot inventory)
- MASTER_TIMELINE.md (timing/music)

**Outputs:**
- Shot Package (complete creative specification)
- Director Notes (guidance to other systems)
- Approval Decision (proceed or revise)

**Authority Boundary:**
- Cannot generate prompts
- Cannot validate technical generation quality
- Cannot edit locked assets
- Cannot override Executive Producer decisions
- Cannot change FILM_BLUEPRINT or locked Bibles

---

### 2. PROMPT BRAIN — Translation Only

**Owns:**
- Translating Shot Package into generation prompt language
- Optimizing prompt syntax for AI models
- Testing prompt variations to achieve Director intent
- Technical prompt structure and validation

**Cannot Own:**
- Creative decisions (all creative comes from Director AI)
- Emotional intent (comes from Shot Package)
- Character or environment definition (comes from Bibles)
- Camera language (comes from Shot Package)
- Lighting specifications (comes from Shot Package)

**Inputs:**
- Shot Package (from Director AI)
- VALIDATION_RULES.md (prompt constraints)
- MASTER_NEGATIVE_PROMPT.md (prohibited terms)

**Outputs:**
- Generation Prompt (technical document for AI model)
- Prompt Approval (meets validation rules)

**Authority Boundary:**
- Cannot change Shot Package intent
- Cannot invent creative decisions
- Cannot modify camera, lighting, or performance specifications
- Cannot approve final image/video (QC owns that)

**Escalation Path:**
- If Shot Package is unclear: ask Director AI for clarification
- If prompt cannot achieve Shot Package: report to Director AI for revision decision
- If conflict with VALIDATION_RULES: escalate to Executive Producer

---

### 3. GENERATION AI — Execution Only

**Owns:**
- Image generation from approved prompt
- Video generation from approved prompt
- Technical quality of generation
- Model selection and parameter tuning
- Rendering and delivery format

**Cannot Own:**
- Creative decisions (all creative comes from Director AI)
- Prompt creation (Prompt Brain owns that)
- Quality judgment of creative intent (QC owns that)
- Approval authority (Director AI and QC own that)

**Inputs:**
- Generation Prompt (from Prompt Brain)
- Technical specifications (timing, resolution, format)

**Outputs:**
- Key Frame Image
- Video Output
- Raw generation logs

**Authority Boundary:**
- Cannot modify prompt during generation
- Cannot make creative substitutions
- Cannot override Shot Package specifications
- Cannot approve final deliverables

---

### 4. QC BRAIN — Validation Only

**Owns:**
- Pre-generation checklist (does Shot Package meet locked standards?)
- Post-generation checklist (does generated output match Shot Package intent?)
- Technical quality assessment (resolution, artifacts, errors)
- Continuity validation (character, costume, props, environment, light)
- Pass/Fail determination

**Cannot Own:**
- Creative decisions (Director AI owns those)
- Whether intent is good or bad (Director AI owns that)
- Whether to accept or reject creative changes (Director AI owns that)

**Inputs:**
- Shot Package (from Director AI)
- Generated Key Frame (from Generation AI)
- Generated Video (from Generation AI)
- Previous Shot Packages (for continuity check)

**Outputs:**
- Pre-generation Validation Result (Pass/Fail)
- Post-generation Validation Result (Pass/Fail)
- QC Checklist (marked items)
- QC Report (findings and issues)

**Authority Boundary:**
- Cannot change Shot Package
- Cannot approve generated content (Director AI owns final approval)
- Cannot make creative revisions
- Cannot override Director AI judgment

**Escalation Path:**
- If generation fails validation: return to Director AI with specific issues
- If ambiguity in Shot Package: ask Director AI for clarification
- If repeated failure: escalate to Executive Producer

---

### 5. CONTINUITY BRAIN — Tracking & Reporting Only

**Owns:**
- Character state tracking (costume, age, appearance across shots)
- Prop state tracking (position, condition, presence across shots)
- Environment state tracking (light, time, weather, location state)
- Continuity chain documentation
- Continuity violation reporting

**Cannot Own:**
- Continuity decisions (Director AI owns those in Shot Package)
- Continuity changes (Director AI approves those)
- Whether violations should be accepted or fixed (Director AI decides)

**Inputs:**
- Shot Packages (to lock continuity state)
- Previous approved shots (to verify continuity chains)
- CONTINUITY_BIBLE.md (rules for what must/cannot change)

**Outputs:**
- Continuity Chain (record of locked state)
- Continuity Violation Report (if continuity rules are broken)
- Continuity Lock Documentation (what changed and why)

**Authority Boundary:**
- Cannot mandate continuity changes
- Cannot override Director AI continuity decisions
- Cannot rewrite Scene Packages
- Cannot modify previous Shot Packages

---

### 6. EXECUTIVE PRODUCER — Highest Authority

**Owns:**
- Approval of FILM_BLUEPRINT (immutable once approved)
- Resolution of conflicts between departments
- Project scope and resource allocation
- Final film approval and delivery
- Authority to override any system (rarely used)

**Typical Role:**
- Approves FILM_BLUEPRINT once at project start
- Reviews Director AI decisions only if escalated
- Resolves authority conflicts
- Approves final film for delivery

**Inputs:**
- FILM_BLUEPRINT (for initial approval)
- Escalated conflicts (from any system)
- Final film (for delivery approval)

**Outputs:**
- Blueprint Approval
- Conflict Resolution Decision
- Delivery Approval

---

## Decision Hierarchy

When a decision must be made:

```
1. Is this within Director AI authority?
   YES → Director AI decides
   NO → Does it require FILM_BLUEPRINT interpretation?
        YES → Is this interpretation clear in locked Bibles?
              YES → Director AI decides (via Bibles)
              NO → Escalate to Executive Producer
        NO → Assign to appropriate system based on domain
```

---

## Conflict Resolution

If two systems disagree:

**Step 1:** Identify which system has authority for this decision domain
- If Director AI has authority: Director AI decides, others comply
- If Prompt Brain has authority: Prompt Brain decides, others comply
- If QC Brain has authority: QC Brain decides within validation scope
- If unclear: escalate to Executive Producer

**Step 2:** If authority is unclear, check hierarchy
- Creative decisions → Director AI
- Translation decisions → Prompt Brain
- Generation decisions → Generation AI
- Quality decisions → QC Brain
- Scope decisions → Executive Producer

**Step 3:** If still unclear, escalate to Executive Producer
- Document the conflict
- Present both positions
- Accept Executive Producer decision as final

---

## Authority Enforcement

**Director AI Violations:**
- Director AI generates prompts → VIOLATION (Prompt Brain owns that)
- Director AI approves technical quality → VIOLATION (QC owns that)
- Director AI edits locked assets → VIOLATION (breaks authority)
- Director AI overrides Executive Producer → VIOLATION

**Prompt Brain Violations:**
- Prompt Brain changes Shot Package intent → VIOLATION
- Prompt Brain makes creative decisions → VIOLATION
- Prompt Brain approves final image → VIOLATION (Director AI and QC own that)
- Prompt Brain modifies VALIDATION_RULES without approval → VIOLATION

**QC Brain Violations:**
- QC Brain makes creative changes → VIOLATION
- QC Brain overrides Director AI judgment → VIOLATION
- QC Brain makes approval decisions → VIOLATION (Director AI owns that)
- QC Brain modifies continuity without Director → VIOLATION

**Generation AI Violations:**
- Generation AI modifies prompt → VIOLATION
- Generation AI makes creative choices → VIOLATION
- Generation AI approves deliverables → VIOLATION
- Generation AI changes Shot Package → VIOLATION

---

## Authority Cannot Be Transferred

Once a decision domain is assigned, it cannot be transferred:

- Director AI cannot give creative authority to Prompt Brain
- Prompt Brain cannot claim creative decisions
- QC Brain cannot make creative changes
- No system can exceed its domain

If a system asks for authority outside its domain, escalate to Executive Producer.

---

## Communication Channels

**Director AI → Prompt Brain:**
- Shot Package (one-way, no feedback on creative)
- "Create prompt for this Shot Package"
- Prompt Brain reports: "Prompt created and validated"

**Prompt Brain → Generation AI:**
- Generation Prompt (one-way, no modification)
- "Generate image/video from this prompt"
- Generation AI reports: "Generation complete"

**Generation AI → QC Brain:**
- Key Frame + Video (for validation)
- QC Brain reports: "Pass" or "Fail with issues"

**QC Brain → Director AI:**
- Validation results (if Fail: specific issues only)
- Director AI decides: approve, request revision, or reject

**Any System → Executive Producer:**
- Conflict escalation only
- Authority questions only
- Not for routine reporting

---

## Authority Summary Table

| Decision | Director AI | Prompt Brain | QC Brain | Generation AI | Executive Producer |
|----------|:--:|:--:|:--:|:--:|:--:|
| Creative intent | ✓ OWNS | — | — | — | Approves only |
| Camera language | ✓ OWNS | — | — | — | — |
| Actor direction | ✓ OWNS | — | — | — | — |
| Light specification | ✓ OWNS | — | — | — | — |
| Prompt creation | — | ✓ OWNS | — | — | — |
| Technical optimization | — | ✓ OWNS | — | — | — |
| Image generation | — | — | — | ✓ OWNS | — |
| Video generation | — | — | — | ✓ OWNS | — |
| Creative validation | — | — | ✓ REPORTS | — | Director approves |
| Technical validation | — | — | ✓ OWNS | — | — |
| Continuity check | — | — | ✓ OWNS | — | — |
| Approval/rejection | ✓ OWNS | — | — | — | — |
| Quality judgment | ✓ OWNS | — | — | — | — |
| Blueprint approval | — | — | — | — | ✓ OWNS |
| Conflict resolution | — | — | — | — | ✓ OWNS |

This is the law of the studio.
