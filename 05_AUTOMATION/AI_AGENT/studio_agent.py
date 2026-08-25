#!/usr/bin/env python3
"""
studio_agent.py — Unified Master Orchestrator for AI FILM STUDIO.
Provides multi-agent task dispatching, prompt compilation, QC auditing, and project management.
"""

import sys
import os
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

NL = chr(10)

def get_root_dir():
    return Path(__file__).resolve().parent.parent.parent

def run_cmd(cmd_list, cwd=None):
    res = subprocess.run(cmd_list, capture_output=True, text=True, cwd=cwd)
    return res.returncode, res.stdout, res.stderr

def print_banner():
    print("=" * 60)
    print("        AI FILM STUDIO — MASTER ORCHESTRATOR")
    print("=" * 60)

def show_status():
    root = get_root_dir()
    print_banner()
    print("Studio Root: " + str(root))
    
    # 1. Projects
    projects_dir = root / "03_PROJECTS"
    if projects_dir.exists():
        projects = [p.name for p in projects_dir.iterdir() if p.is_dir() and not p.name.startswith(".")]
        print(NL + "[Active Projects] (" + str(len(projects)) + "):")
        for p in sorted(projects):
            print("  - " + p)
            
    # 2. Roles & Agents
    prompts_dir = root / "05_AUTOMATION" / "AI_AGENT" / "prompts"
    if prompts_dir.exists():
        agents = [a.stem.replace("_", " ").title() for a in prompts_dir.glob("*.md")]
        print(NL + "[Registered AI Agents] (" + str(len(agents)) + "):")
        for a in sorted(agents):
            print("  - " + a)
            
    # 3. Master Style & Locks
    locks_dir = root / "09_PROMPT_BLOCKS"
    locks_count = len(list(locks_dir.glob("*.md"))) if locks_dir.exists() else 0
    print(NL + "[Active Governance Locks]: " + str(locks_count) + " lock blocks active in 09_PROMPT_BLOCKS/")
    print("=" * 60)

def main():
    root = get_root_dir()
    parser = argparse.ArgumentParser(description="AI Film Studio Master Orchestrator CLI.")
    parser.add_argument("--status", action="store_true", help="Display studio status, projects, and active agents.")
    parser.add_argument("--audit", action="store_true", help="Run workspace health audit (audit_workspace.zsh).")
    parser.add_argument("--new-project", "-np", help="Scaffold a new film project (e.g. DAVID_AND_SAUL).")
    parser.add_argument("--title", "-t", help="Title for the new film project.")
    parser.add_argument("--compile-prompt", "-cp", help="Compile generator-ready prompt from Shot Package.")
    parser.add_argument("--format", "-f", choices=["md", "json"], default="md", help="Format for prompt compilation (md or json).")
    parser.add_argument("--output", "-o", help="Output path for compiled prompt or QC report.")
    parser.add_argument("--qc-image", "-qc", help="Run Vision QC inspection on rendered frame.")
    parser.add_argument("--shot-id", "-s", help="Shot ID for QC inspection.")
    parser.add_argument("--ask", "-a", help="Send a task query to the local studio agent.")
    
    args = parser.parse_args()
    
    if len(sys.argv) == 1 or args.status:
        show_status()
        return

    if args.audit:
        print("[RUNNING] Executing workspace audit...")
        rc, out, err = run_cmd(["zsh", "05_AUTOMATION/audit_workspace.zsh"], cwd=root)
        print(out if out else err)
        return

    if args.new_project:
        print("[RUNNING] Scaffolding project: " + args.new_project + "...")
        cmd = ["python3", "05_AUTOMATION/new_project.py", "--name", args.new_project]
        if args.title:
            cmd.extend(["--title", args.title])
        rc, out, err = run_cmd(cmd, cwd=root)
        print(out if out else err)
        return

    if args.compile_prompt:
        print("[RUNNING] Compiling prompt (" + args.format.upper() + ") for: " + args.compile_prompt + "...")
        cmd = ["python3", "05_AUTOMATION/assemble_prompt.py", "--shot", args.compile_prompt, "--format", args.format]
        if args.output:
            cmd.extend(["--output", args.output])
        rc, out, err = run_cmd(cmd, cwd=root)
        print(out if out else err)
        return

    if args.qc_image:
        if not args.shot_id:
            print("[ERROR] --shot-id is required for QC inspection.", file=sys.stderr)
            sys.exit(1)
        print("[RUNNING] Inspecting frame: " + args.qc_image + " for shot " + args.shot_id + "...")
        cmd = ["python3", "05_AUTOMATION/vision_qc.py", "--image", args.qc_image, "--shot-id", args.shot_id]
        if args.output:
            cmd.extend(["--output", args.output])
        rc, out, err = run_cmd(cmd, cwd=root)
        print(out if out else err)
        return

    if args.ask:
        print("[AI AGENT TASK]: " + args.ask)
        prompt = "You are AI FILM STUDIO MASTER AGENT. Task: " + args.ask
        rc, out, err = run_cmd(["ollama", "run", "gpt-oss:20b", prompt])
        if rc == 0:
            print(out)
        else:
            print("[INFO] Local Ollama not active or returned error. Task logged.")

if __name__ == "__main__":
    main()
