#!/usr/bin/env python3
"""
new_project.py — Automated Project Scaffolding CLI for AI FILM STUDIO.
Creates a complete, standardized multi-layer project structure for new film productions.
"""

import sys
import os
import argparse
from pathlib import Path

NL = chr(10)

def get_root_dir():
    return Path(__file__).resolve().parent.parent

def create_new_project(project_name, title=None):
    root = get_root_dir()
    proj_dir = root / "03_PROJECTS" / project_name.upper()
    
    if proj_dir.exists():
        print(f"[WARN] Project folder already exists: {proj_dir}")
        return False
        
    disp_title = title if title else project_name.replace("_", " ").title()
    
    # 1. Directory Structure
    folders = [
        "01_PRODUCTION_BOOK",
        "02_ASSET_LIBRARY/00_MASTER_REFERENCES",
        "02_ASSET_LIBRARY/CHARACTERS",
        "02_ASSET_LIBRARY/LOCATIONS",
        "02_ASSET_LIBRARY/PROPS",
        "02_ASSET_LIBRARY/COSTUMES",
        "03_PROMPT_LIBRARY/SHOTS",
        "03_PROMPT_LIBRARY/SCENES",
        "03_PROMPT_LIBRARY/NEGATIVE",
        "04_SCENES/SCENE_001",
        "05_QC",
        "06_RENDER_TRACKING",
        "07_FINAL_EXPORTS"
    ]
    
    for f in folders:
        (proj_dir / f).mkdir(parents=True, exist_ok=True)
        
    # 2. Template Files
    # Project Bible
    pb_text = NL.join([
        f"# PROJECT BIBLE — {disp_title}",
        f"**Project:** `{project_name.upper()}`",
        "**Status:** `DRAFT v1.0`",
        "**Single Source of Truth:** `FILM_BLUEPRINT.md`",
        "",
        "## 1. Core Dramatic Route",
        "Curiosity → Conflict → Realization → Resolution",
        "",
        "## 2. Creative Laws",
        "- Historical authenticity above visual spectacle.",
        "- Physically motivated lighting only.",
        "- Character identity locked across entire film."
    ])
    (proj_dir / "01_PRODUCTION_BOOK" / "PROJECT_BIBLE.md").write_text(pb_text, encoding="utf-8")
    
    # Master Timeline
    tl_text = NL.join([
        f"# MASTER TIMELINE — {disp_title}",
        "| Scene ID | Title | Timecode Range | Dramatic Function | Status |",
        "| :--- | :--- | :--- | :--- | :--- |",
        "| `SCENE_001` | Opening / Prologue | 00:00 - 00:45 | Ordinary World before change | `PLANNED` |"
    ])
    (proj_dir / "01_PRODUCTION_BOOK" / "MASTER_TIMELINE.md").write_text(tl_text, encoding="utf-8")
    
    # Asset Index
    idx_text = NL.join([
        f"# ASSET INDEX — {disp_title}",
        "| Asset ID | Category | Description | Status | Reference File |",
        "| :--- | :--- | :--- | :--- | :--- |",
        "| `CHAR_PROTAGONIST` | Character | Main Character | `IN_DESIGN` | `02_ASSET_LIBRARY/CHARACTERS/` |"
    ])
    (proj_dir / "02_ASSET_LIBRARY" / "INDEX.md").write_text(idx_text, encoding="utf-8")
    
    # Render Log
    rl_text = NL.join([
        f"# RENDER LOG — {disp_title}",
        "| Shot ID | Model Engine | Seed / Settings | Keyframe QC | Video QC | Export File |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ])
    (proj_dir / "06_RENDER_TRACKING" / "RENDER_LOG.md").write_text(rl_text, encoding="utf-8")
    
    # Scene 001 Package Scaffold
    sc_text = NL.join([
        f"# SCENE PACKAGE 001 — {disp_title}",
        "**Scene ID:** `SCENE_001`",
        "**Status:** `DRAFT v1.0`",
        "**Purpose:** Establish protagonist and historical environment.",
        "",
        "## Shot List",
        "- `SHOT_001_A_ESTABLISHING`: Wide shot establishing the space.",
        "- `SHOT_001_B_FOCUS`: Medium shot introducing the character."
    ])
    (proj_dir / "04_SCENES" / "SCENE_001" / "SCENE_PACKAGE_001_v1.0.md").write_text(sc_text, encoding="utf-8")
    
    print(f"[SUCCESS] New project created at: {proj_dir}")
    return True

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new film project in AI FILM STUDIO.")
    parser.add_argument("--name", "-n", required=True, help="Folder name for project (e.g. DAVID_AND_SAUL, MOSES)")
    parser.add_argument("--title", "-t", help="Human-readable title (e.g. 'David & Saul: The Anointing')")
    args = parser.parse_args()
    
    create_new_project(args.name, args.title)

if __name__ == "__main__":
    main()
