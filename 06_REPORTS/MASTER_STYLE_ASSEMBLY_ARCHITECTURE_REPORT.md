# MASTER_STYLE_ASSEMBLY_ARCHITECTURE_REPORT

**Report Date:** 2026-08-09  
**Scope:** Current state of Prompt Assembly Architecture  
**Focus:** Master Style assembly mechanism and automation  
**Status:** AUDIT ONLY — NO MODIFICATIONS

---

## EXECUTIVE SUMMARY

**Finding:** The project has a **documented prompt build order** but **NO automated mechanism** to implement it.

**Current State:**
- ✅ PROMPT_BUILD_ORDER.md lists 12-step sequence
- ✅ PROMPT_BLOCKS folder contains 10 locked rule files
- ✅ Templates exist (SHOT_PROMPT_TEMPLATE.md)
- ✅ Validation rules exist (VALIDATION_RULES.md Rule 3.4)
- ❌ **NO automation script**
- ❌ **NO Master Style assembly tool**
- ❌ **NO automated synthesis process**

**Result:** Prompt Engineer must manually:
1. Read three Master Style files
2. Read 10 PROMPT_BLOCKS files
3. Read Shot Package
4. Synthesize all into one Image Prompt
5. Validate manually against VALIDATION_RULES

**Risk:** Human error, inconsistency, missing components

---

## PART 1: CURRENT PROMPT ASSEMBLY ARCHITECTURE

### 1.1 Documented Workflow

**Location:** `PRODUCTION_PIPELINE.md` Stage 4

```
Stage 4: Prompt Package Creation
- Responsible AI: Prompt Engineer AI
- Input: approved Scene Package and technical decisions
- Output: SHOT_###_PROMPT_v1.0.md with all 8 Image Prompt sections
- Gate: G2 (Pre-generation validation)
```

**What It Says:**
- Prompt Engineer assembles prompt from Scene Package
- Must preserve Director intent
- Must validate against VALIDATION_RULES.md
- Output ready for Generation AI

**What It Does NOT Say:**
- HOW to assemble
- WHERE Master Style comes from
- WHEN to apply PROMPT_BLOCKS
- HOW to synthesize all three Master Style layers
- WHAT order to follow
- HOW to automate this

---

### 1.2 Prompt Build Order (No Implementation Details)

**Location:** `PROMPT_BUILD_ORDER.md`

**Current Content:**
```
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
```

**Problem:** This is a **list, not a process**. It tells WHAT order but not:
- HOW to apply each step
- WHEN to check for conflicts
- HOW to merge/synthesize components
- WHICH file contains each component
- HOW to handle dependencies

---

### 1.3 PROMPT_BLOCKS: Rules Without Automation

**Location:** `/02_STUDIO/ 09_PROMPT_BLOCKS/`

**Contents:**
| File | Purpose | Usage |
|------|---------|-------|
| MASTER_LOCKS.md | Override rules for conflict resolution | Manual reference |
| CHARACTER_LOCKS.md | Character identity constraints | Manual reference |
| ENVIRONMENT_LOCKS.md | Location/prop constraints | Manual reference |
| LIGHTING_BIBLE.md | Lighting rules | Manual reference |
| COLOR_LOCKS.md | Color palette constraints | Manual reference |
| CAMERA_LOCKS.md | Camera language rules | Manual reference |
| CONTINUITY_LOCKS.md | Continuity constraints | Manual reference |
| EMOTION_LOCKS.md | Emotional rules | Manual reference |
| CINEMATOGRAPHY_LOCKS.md | Cinematic language rules | Manual reference |
| NEGATIVE_LOCKS.md | Prohibited elements | Manual reference |

**Status:** All files exist and are locked. None are automated. Prompt Engineer must manually read and apply.

---

### 1.4 Master Style Assembly: Currently Manual

**Current Process:**

```
┌─────────────────────────────────────────────────┐
│ PROMPT ENGINEER MUST MANUALLY:                  │
├─────────────────────────────────────────────────┤
│ 1. Open MASTER_STYLE_v2.md                      │
│ 2. Read 30 core rules                           │
│ 3. Decide which apply to this shot              │
│ 4. Open MASTER_STYLE_ENHANCEMENT_v2.1.md        │
│ 5. Read 10 enhancement layers (63 rules)        │
│ 6. Decide which apply to this shot              │
│ 7. Open MASTER_STYLE_ENHANCEMENT_v2.2.md        │
│ 8. Read human realism section (16 rules)        │
│ 9. Decide which apply to this shot              │
│ 10. Synthesize all three into one section       │
│ 11. Write "Master style" subsection of Image... │
│ 12. VALIDATE against VALIDATION_RULES.md        │
│ 13. If Rule 3.4 fails, go back to step 1        │
└─────────────────────────────────────────────────┘

Potential failure points: 13 manual steps = 13 places to make mistakes
```

**Estimated Time:** 30-60 minutes per shot  
**Error Risk:** High (especially under time pressure)

---

### 1.5 Template Guidance: Post-Change Plan

**Location:** `SHOT_PROMPT_TEMPLATE.md`

**What It Provides:**
- Section-by-section structure (Image Prompt, Negative Prompt, Video Prompt)
- Subsection names (Scene, Characters, Environment, Lighting, Camera, Action, Emotion)
- Example of Master Style section with all three layers (AFTER Change Plan update)
- Continuity handoff format

**What It Does NOT Provide:**
- Step-by-step assembly instructions
- Decision tree for choosing which rules apply
- Conflict resolution logic
- Synthesis algorithm
- Example of completed Image Prompt assembly

---

### 1.6 Validation: After Assembly, Not During

**Location:** `VALIDATION_RULES.md`

**Rule 3.4: All Master Style Layers Included (NEW)**

```
Standard: Image Prompt MUST include rules from ALL THREE Master Style layers

Check Process:
1. Open SHOT_PROMPT_###.md
2. Navigate to "## Image prompt" → "### 1. Master style"
3. Verify explicit references to all three files
4. Verify 3-5 specific rules from EACH layer
5. If missing, REJECT

Action on Failure: Revise Master Style section to include all three layers
```

**When It Happens:** Gate 2 (G2) — AFTER Prompt Engineer submits  
**Problem:** Validation happens **after synthesis**, not during. If Rule 3.4 fails, Prompt Engineer must restart.

---

## PART 2: WHAT'S MISSING

### 2.1 No Automated Master Style Assembly

**Gap:** No process that automatically:
- Pulls rules from v2.0, v2.1, v2.2
- Filters rules for shot context
- Synthesizes into single Master Style section
- Validates completeness

**Current Workaround:** Prompt Engineer must manually synthesize (error-prone)

---

### 2.2 No Master Style Assembly Guide

**Gap:** No document that explains:
- HOW to assemble Master Style
- WHY each layer is needed
- WHEN to apply rules
- WHICH rules apply to different shot types
- HOW to handle conflicts between layers

**Current Workaround:** Prompt Engineer must infer from SHOT_PROMPT_TEMPLATE example (incomplete)

---

### 2.3 No Automation for PROMPT_BLOCKS Application

**Gap:** No mechanism that:
- Reads all 10 PROMPT_BLOCKS in priority order
- Checks for conflicts
- Enforces MASTER_LOCKS override rule
- Applies rules to Image Prompt systematically

**Current Workaround:** Prompt Engineer reads each file manually (tedious)

---

### 2.4 No Synthesis Decision Logic

**Gap:** No guidance for:
- Which Master Style rules apply to establishing shots vs. close-ups
- Which rules apply to day scenes vs. night scenes
- How to prioritize when space is limited
- How to blend rules without contradiction

**Current Workaround:** Prompt Engineer must make decisions without framework

---

### 2.5 No Integrated Automation Tool

**Gap:** No script/tool that:
- Takes Shot Package as input
- Applies PROMPT_BUILD_ORDER automatically
- Synthesizes Master Style from all three files
- Generates Image Prompt sections
- Performs validation

**Current Workaround:** Manual process with external validation (Gate 2)

---

## PART 3: ARCHITECTURAL REQUIREMENTS FOR SOLUTION

### 3.1 Scope of Assembly Problem

**Problem Statement:**
Currently, Prompt Engineer must synthesize 109 Master Style rules (30 from v2.0 + 63 from v2.1 + 16 from v2.2) into one coherent Master Style section of Image Prompt, while also applying 10 PROMPT_BLOCKS constraints, all without systematic guidance.

**Needed:** A framework that makes this process:
- Systematic (not intuitive)
- Documented (not inferred)
- Verifiable (not subjective)
- Repeatable (same input = same output)
- Efficient (not 30-60 minutes per shot)

---

### 3.2 Solution Options

#### **Option A: Documentation + Manual Process (Light)**
- Create MASTER_STYLE_ASSEMBLY_GUIDE.md
- Document decision tree for choosing rules
- Provide examples by shot type
- Require manual validation
- **Pros:** Low complexity, no code
- **Cons:** Still relies on Prompt Engineer diligence

#### **Option B: Python Automation Tool (Medium)**
- Create `assemble_master_style.py`
- Input: Shot Package, Scene Package, PROMPT_BLOCKS
- Output: Synthesized Master Style section
- Validate against Rule 3.4
- **Pros:** Fast, consistent, auditable
- **Cons:** Requires Python environment

#### **Option C: Zsh Script Automation (Medium)**
- Create `assemble_master_style.zsh`
- Read files, extract rules, synthesize
- Run as pre-processing step before Prompt Engineer
- **Pros:** Uses existing automation framework (audit_workspace.zsh exists)
- **Cons:** Less sophisticated than Python

#### **Option D: Formal Process Document (Hybrid)**
- Create MASTER_STYLE_ASSEMBLY_PROCESS.md
- Step-by-step checklist for assembly
- Links to all source files
- Integration points with VALIDATION_RULES.md
- **Pros:** Clear, documented, implementable
- **Cons:** Still manual but with systematic guidance

#### **Option E: Combination (Comprehensive)**
- Create MASTER_STYLE_ASSEMBLY_GUIDE.md (documentation)
- Create template for assembly results
- Create validation checklist
- Suggest automation tool (defer to later phase)
- **Pros:** Immediate solution + future automation path
- **Cons:** Most complex to implement

---

### 3.3 Recommended Integration Points

Any assembly mechanism should:

1. **Reference PROMPT_BUILD_ORDER.md**
   - Use 12-step sequence as framework
   - Check that Master Style is completed before moving to MASTER_LOCKS

2. **Apply PROMPT_BLOCKS in Priority Order**
   - Start with MASTER_LOCKS (highest priority)
   - Check for conflicts between layers
   - Enforce override rules

3. **Use SHOT_PROMPT_TEMPLATE.md as Output Format**
   - Populate Master Style subsection (### 1. Master style)
   - Ensure consistency with other subsections

4. **Validate Against VALIDATION_RULES.md**
   - Rule 3.4 (all three Master Style layers)
   - Rule 3.1 (completeness)
   - Rule 2.1 (negative prompt base)

5. **Record Source References**
   - Which Master Style rules were applied?
   - Which PROMPT_BLOCKS rules were applied?
   - What was the decision process?

---

## PART 4: PROPOSED ARCHITECTURAL SOLUTION

### 4.1 Recommended Approach: Comprehensive Process Document

**Based on:**
- Least disruption to current workflow
- Maximum immediate impact
- Clear path to automation later

**Solution:** Create `MASTER_STYLE_ASSEMBLY_PROCESS.md`

**Location:** `/02_STUDIO/WORKFLOWS/`

**Contents Should Include:**

```
1. OVERVIEW
   - Why this process exists
   - What it accomplishes
   - Expected output

2. INPUTS CHECKLIST
   - Is Shot Package approved? (Gate 1)
   - Are PROMPT_BLOCKS accessible?
   - Is PROMPT_BUILD_ORDER available?
   - Are Master Style files v2.0, v2.1, v2.2 present?

3. ASSEMBLY PROCESS (12 Steps)
   Step 1: Read Shot Package section 8 (Image Generation)
   Step 2: Identify shot context (establishing? close-up? wide?)
   Step 3: Assemble Master Style Layer 1 (v2.0)
           - Read 30 rules
           - Choose 5-8 applicable rules
           - Document reasoning
   Step 4: Assemble Master Style Layer 2 (v2.1)
           - Review 10 enhancement layers
           - Choose 8-12 applicable rules
           - Check for conflicts with Layer 1
   Step 5: Assemble Master Style Layer 3 (v2.2)
           - Read human realism section
           - Choose 4-6 applicable rules
           - Integrate with Layer 1 & 2
   Step 6: Apply PROMPT_BLOCKS in priority order
           - Start with MASTER_LOCKS
           - Apply CHARACTER_LOCKS
           - Apply others in priority order
           - Resolve conflicts using MASTER_LOCKS rule
   Step 7: Synthesize into single Master Style section
   Step 8: Check against VALIDATION_RULES Rule 3.4
   Step 9: If validation fails, return to Step 3
   Step 10: Write Master Style subsection (### 1. Master style)
   Step 11: Continue with Image Prompt sections 2-8
   Step 12: Validate full Image Prompt against VALIDATION_RULES

4. DECISION TREE
   - Shot Type → Which Master Style rules apply?
   - Scene Lighting → Which rules change?
   - Character Close-up → Extra skin realism rules?
   - etc.

5. CONFLICT RESOLUTION
   - What if two rules contradict?
   - Use MASTER_LOCKS override
   - Document conflict and resolution

6. EXAMPLES
   - SHOT_001_A (establishing) — Worked example
   - SHOT_002_B (close-up) — Worked example
   - SHOT_003_C (complex lighting) — Worked example

7. VALIDATION CHECKLIST
   - All three Master Style layers present? ✓
   - 3-5 rules from v2.0? ✓
   - 8-12 rules from v2.1? ✓
   - 4-6 rules from v2.2? ✓
   - PROMPT_BLOCKS applied? ✓
   - No contradictions? ✓

8. OUTPUT FORMAT
   - Where to save assembled Master Style
   - What to name it
   - How to record in SHOT_PROMPT_###.md

9. ESCALATION
   - When to ask for clarification
   - When to escalate to Director AI
   - When to request Shot Package revision
```

---

### 4.2 Alternative: Comprehensive with Automation Path

**If more automation is desired later:**

**Immediate (Phase 1):**
1. Create MASTER_STYLE_ASSEMBLY_PROCESS.md (documentation)
2. Create working examples
3. Train Prompt Engineer on process

**Future (Phase 2 — if needed):**
1. Create `assemble_master_style.py` script
2. Takes Shot Package as input
3. Returns synthesized Master Style
4. Can be called by Prompt Engineer: `python assemble_master_style.py SHOT_001_A_v1.0.md`

**Future (Phase 3 — if needed):**
1. Integrate script into PRODUCTION_PIPELINE
2. Automate at Stage 4 (Prompt Package creation)
3. Script runs before Prompt Engineer starts
4. Provides pre-filled Master Style section

---

### 4.3 File Organization for Solution

**Recommended Structure:**

```
02_STUDIO/WORKFLOWS/
├── PRODUCTION_PIPELINE.md (unchanged)
├── MASTER_STYLE_ASSEMBLY_PROCESS.md (NEW)
│   ├── Overview & purpose
│   ├── 12-step assembly process
│   ├── Decision tree
│   ├── Conflict resolution rules
│   ├── 3 worked examples
│   ├── Validation checklist
│   └── Escalation procedures
└── (future) assemble_master_style.py

02_STUDIO/ 09_PROMPT_BLOCKS/
├── README.md (with link to Assembly Process)
├── MASTER_LOCKS.md (unchanged)
├── CHARACTER_LOCKS.md (unchanged)
└── ... (other locks unchanged)

04_TEMPLATES/
├── SHOT_PROMPT_TEMPLATE.md (unchanged, but now references Assembly Process)
└── (future) MASTER_STYLE_ASSEMBLY_EXAMPLE.md

03_PROJECTS/NICODEMUS/03_PROMPT_LIBRARY/
├── VALIDATION_RULES.md (includes Rule 3.4)
└── (future) ASSEMBLY_CHECKLIST_SHOT_001.md (working example)
```

---

## PART 5: INTERACTION WITH EXISTING DOCUMENTS

### 5.1 How Assembly Process Interacts with PROMPT_BUILD_ORDER.md

**Current State:**
```
PROMPT_BUILD_ORDER.md
├── Lists order (1-12)
└── No implementation details
```

**With Assembly Process:**
```
PROMPT_BUILD_ORDER.md (unchanged)
└── MASTER_STYLE_ASSEMBLY_PROCESS.md
    ├── Explains HOW to execute order 1-12
    ├── Provides decision logic
    ├── Implements Steps 1-6
    └── Steps 7-12 continue to Image Prompt
```

---

### 5.2 How Assembly Process Interacts with VALIDATION_RULES.md

**Current State:**
```
VALIDATION_RULES.md Rule 3.4
├── Requires all three layers
└── Validates AFTER assembly
```

**With Assembly Process:**
```
VALIDATION_RULES.md Rule 3.4 (unchanged)
└── MASTER_STYLE_ASSEMBLY_PROCESS.md
    ├── Ensures completeness DURING assembly
    ├── Performs Rule 3.4 check (Step 8)
    ├── If fails, returns to Step 3
    └── Submits only when validated
```

---

### 5.3 How Assembly Process Interacts with PROMPT_BLOCKS

**Current State:**
```
09_PROMPT_BLOCKS/ (10 files)
└── Manual reference by Prompt Engineer
```

**With Assembly Process:**
```
09_PROMPT_BLOCKS/ (unchanged)
└── MASTER_STYLE_ASSEMBLY_PROCESS.md
    ├── Step 6: Applies blocks in priority order
    ├── Enforces MASTER_LOCKS override
    ├── Resolves conflicts systematically
    └── Documents reasoning
```

---

### 5.4 How Assembly Process Interacts with SHOT_PROMPT_TEMPLATE.md

**Current State:**
```
SHOT_PROMPT_TEMPLATE.md
├── Shows structure
└── Shows example Master Style section
```

**With Assembly Process:**
```
SHOT_PROMPT_TEMPLATE.md (unchanged)
└── MASTER_STYLE_ASSEMBLY_PROCESS.md
    ├── Explains how to populate that template
    ├── Shows worked examples
    ├── Provides validation
    └── Ensures consistency
```

---

### 5.5 How Assembly Process Interacts with PRODUCTION_PIPELINE.md

**Current State:**
```
Stage 4: Prompt Package
└── "Prompt Engineer AI assembles technical prompt packages"
    (No details on HOW)
```

**With Assembly Process:**
```
Stage 4: Prompt Package
└── Prompt Engineer AI follows MASTER_STYLE_ASSEMBLY_PROCESS.md
    ├── Step 1-6: Assemble Master Style
    ├── Step 7-12: Assemble remaining Image Prompt
    └── Validate against VALIDATION_RULES.md
```

---

## PART 6: BENEFITS OF PROPOSED SOLUTION

### 6.1 For Prompt Engineer

- **Clear Process:** Step-by-step instructions, not intuition
- **Decision Tree:** Know which rules apply to each shot type
- **Examples:** Worked examples for reference
- **Faster:** Systematic approach = fewer decisions
- **Consistent:** Same shot type = same approach
- **Auditable:** Can show reasoning for each rule choice

---

### 6.2 For QC / Validation

- **Verifiable:** Can trace back to assembly rules
- **Consistent:** Can compare against examples
- **Documented:** Process is explicit, not hidden
- **Testable:** Can check Rule 3.4 compliance systematically

---

### 6.3 For Director AI

- **Delegatable:** Can trust Prompt Engineer to follow process
- **Transparent:** Can audit assembly if needed
- **Escalation Path:** Clear when to ask for shot package revision

---

### 6.4 For Future Automation

- **Foundation:** Written process → automated script
- **Specification:** Automation can follow documented steps
- **Validation:** Automated checking against Rule 3.4

---

## PART 7: RISKS & MITIGATION

### Risk 1: Assembly Process Too Complex

**Mitigation:**
- Start with simple shot types (establishing shots)
- Add complexity gradually
- Provide worked examples for each shot type

---

### Risk 2: Prompt Engineer Doesn't Follow Process

**Mitigation:**
- Process is mandatory for Gate 2 pass
- VALIDATION_RULES.md Rule 3.4 enforces compliance
- QC validates based on process steps

---

### Risk 3: Process Becomes Outdated

**Mitigation:**
- Document as versioned file (MASTER_STYLE_ASSEMBLY_PROCESS_v1.0.md)
- Link to MASTER_STYLE files with version numbers
- Review quarterly for needed updates

---

### Risk 4: Automation Comes Later and Breaks Process

**Mitigation:**
- Keep documentation separate from automation
- Automation should follow documented process exactly
- Process defines specification for automation

---

## PART 8: RECOMMENDATIONS

### Immediate (Before Next Shot Generation)

1. **Create MASTER_STYLE_ASSEMBLY_PROCESS.md**
   - Document 12-step process
   - Provide decision tree
   - Include worked examples

2. **Update PRODUCTION_PIPELINE.md**
   - Add reference to Assembly Process in Stage 4
   - Link to assembly documentation

3. **Create ASSEMBLY_CHECKLIST template**
   - Prompt Engineer can print/use for each shot
   - Ensures no steps are skipped

---

### Short Term (Next 1-2 Scenes)

1. **Test process with SHOT_002_A**
   - Train Prompt Engineer on new process
   - Track time and accuracy
   - Collect feedback

2. **Refine based on feedback**
   - Update examples if needed
   - Clarify ambiguous steps
   - Add decision tree branches as needed

---

### Medium Term (After Scene 3)

1. **Consider automation feasibility**
   - Evaluate Python/Zsh script approach
   - Estimate development effort
   - Decide on Phase 2 automation

2. **Formalize training for new Prompt Engineers**
   - Create training doc based on process
   - Use worked examples as training materials

---

### Long Term (Future Phases)

1. **Implement automation if justified**
   - Create `assemble_master_style.py`
   - Test against manual results
   - Integrate into workflow

2. **Monitor process effectiveness**
   - Track QC failures related to Master Style
   - Measure time per shot
   - Improve based on metrics

---

## CONCLUSION

### Current State Assessment

**The project has:**
- ✅ Documented prompt build order
- ✅ Locked prompt blocks (LOCKS files)
- ✅ Templates and examples
- ✅ Validation rules
- ❌ No systematic assembly process
- ❌ No automation mechanism
- ❌ No assembly guidance for Prompt Engineer

**Result:** Prompt Engineer must manually synthesize everything, which is:
- Error-prone (13+ manual steps)
- Time-consuming (30-60 min per shot)
- Undocumented (no recorded reasoning)
- Inconsistent (different approach per engineer)

### Recommended Solution

**Create MASTER_STYLE_ASSEMBLY_PROCESS.md**
- Systematic 12-step process
- Decision tree for shot types
- Conflict resolution rules
- Worked examples
- Validation checklist
- Escalation procedures

**Benefits:**
- Immediate: Better consistency and speed
- Medium-term: Reliable training material
- Long-term: Foundation for automation

**No files need modification today** — only new documentation needed.

---

**Report Completed**  
**Audit Type:** Architecture review only  
**Files Modified:** 0  
**Files Created:** 0  
**Recommendations:** Ready for implementation
