#!/usr/bin/env python3
"""
Personal Memory Schema — Session Extraction + Update
Run after a session to extract new beliefs, decisions, and project updates.
Usage: python3 update_memory.py --session "path/to/session_notes.txt"
       python3 update_memory.py --interactive  (paste session summary)
       python3 update_memory.py --show         (display current memory)
       python3 update_memory.py --query "what are my current working theories?"
"""

import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime, timezone

MEMORY_FILE = Path(__file__).parent / "memory.json"
BACKUP_DIR  = Path(__file__).parent / "memory_history"

def load_memory() -> dict:
    return json.loads(MEMORY_FILE.read_text())

def save_memory(memory: dict):
    """Save with backup and git commit."""
    BACKUP_DIR.mkdir(exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    backup = BACKUP_DIR / f"memory_{ts}.json"
    
    # Backup current
    if MEMORY_FILE.exists():
        import shutil
        shutil.copy(MEMORY_FILE, backup)
    
    # Update timestamp
    memory["last_updated"] = datetime.now(timezone.utc).isoformat()
    
    # Save
    MEMORY_FILE.write_text(json.dumps(memory, indent=2))
    print(f"✅ Memory saved. Backup: {backup.name}")

def show_memory(memory: dict):
    """Display memory in human-readable form."""
    print(f"\n{'='*60}")
    print(f"PERSONAL MEMORY — {memory['user_id']}")
    print(f"Last updated: {memory['last_updated']}")
    print(f"{'='*60}\n")

    print("📌 WORKING THEORIES")
    for t in memory["working_theories"]:
        status = "✅" if t["status"] == "active" else "⏸"
        print(f"  {status} [{t['confidence']}%] {t['title']}")
        print(f"     {t['thesis'][:120]}...")
    
    print("\n🔒 COMMITTED DECISIONS")
    for d in memory["committed_decisions"]:
        if d["status"] == "active":
            print(f"  • {d['decision'][:100]}")
    
    print("\n🚫 REJECTED OPTIONS")
    for r in memory["rejected_options"]:
        print(f"  • [{r['status'].upper()}] {r['option'][:80]}")
        print(f"    Reason: {r['reason'][:80]}")
    
    print("\n🔨 ACTIVE PROJECTS")
    for p in memory["active_projects"]:
        print(f"  • [{p['status'].upper()}] {p['name']}")
        if "next_actions" in p:
            for a in p["next_actions"][:2]:
                print(f"    → {a}")
    
    print("\n❓ OPEN QUESTIONS")
    for q in memory["open_questions"]:
        prio = "🔴" if q["priority"] == "high" else "🟡"
        print(f"  {prio} {q['question'][:100]}")
        print(f"    Lean: {q['current_lean']} ({q['confidence_in_lean']}%)")
    
    print(f"\n{'='*60}\n")

def query_memory(memory: dict, query: str) -> str:
    """Simple keyword search across memory."""
    query_lower = query.lower()
    results = []
    
    # Search theories
    for t in memory["working_theories"]:
        if any(k in t["thesis"].lower() or k in t["title"].lower() 
               for k in query_lower.split()):
            results.append(f"THEORY [{t['confidence']}%]: {t['title']}\n  {t['thesis']}")
    
    # Search decisions
    for d in memory["committed_decisions"]:
        if any(k in d["decision"].lower() for k in query_lower.split()):
            results.append(f"DECISION: {d['decision']}")
    
    # Search projects
    for p in memory["active_projects"]:
        if any(k in p["name"].lower() for k in query_lower.split()):
            results.append(f"PROJECT [{p['status']}]: {p['name']}\n  State: {p.get('current_state','')}")
    
    # Search open questions
    for q in memory["open_questions"]:
        if any(k in q["question"].lower() for k in query_lower.split()):
            results.append(f"OPEN Q: {q['question']}\n  Lean: {q['current_lean']}")
    
    if results:
        return "\n\n".join(results)
    return "No matching entries found."

def build_injection_prompt(memory: dict, context_query: str = None) -> str:
    """
    Build the pre-prompt injection block for agent tasks.
    This is what gets prepended to every agent interaction.
    """
    lines = [
        "=== PERSONAL CONTEXT (injected) ===",
        f"User: {memory['identity']['display_name']}",
        f"Role: {memory['identity']['role_context']}",
        f"Style: {memory['identity']['communication_preferences']['tone']}",
        "",
        "ACTIVE WORKING THEORIES:",
    ]
    for t in memory["working_theories"]:
        if t["status"] == "active" and t["confidence"] >= 75:
            lines.append(f"  - [{t['confidence']}%] {t['title']}: {t['thesis'][:200]}")
    
    lines.append("\nCOMMITTED DECISIONS (do not re-litigate):")
    for d in memory["committed_decisions"]:
        if d["status"] == "active":
            lines.append(f"  - {d['decision']}")
    
    lines.append("\nACTIVE PROJECTS:")
    for p in memory["active_projects"]:
        if p["status"] == "active":
            state = p.get("current_state", "")
            lines.append(f"  - {p['name']}: {state[:100]}")
    
    lines.append("\nCURRENT DOMAIN EXPERTISE:")
    lines.append(f"  Expert: {', '.join(memory['domain_expertise']['expert'][:3])}")
    lines.append(f"  Learning: {', '.join(memory['domain_expertise']['learning'][:2])}")
    
    lines.append("\n=== END PERSONAL CONTEXT ===\n")
    return "\n".join(lines)

def update_theory_confidence(memory: dict, theory_id: str, new_confidence: int, trigger: str):
    """Update confidence for a specific theory."""
    for t in memory["working_theories"]:
        if t["id"] == theory_id:
            old_confidence = t["confidence"]
            t["confidence"] = new_confidence
            t["confidence_history"].append({
                "date": datetime.now(timezone.utc).date().isoformat(),
                "value": new_confidence,
                "trigger": trigger
            })
            t["last_updated"] = datetime.now(timezone.utc).date().isoformat()
            
            # Add to belief history
            memory["belief_history"].append({
                "id": f"bh-{len(memory['belief_history'])+1:03d}",
                "theory_id": theory_id,
                "event": "confidence_increase" if new_confidence > old_confidence else "confidence_decrease",
                "from_value": old_confidence,
                "to_value": new_confidence,
                "date": datetime.now(timezone.utc).date().isoformat(),
                "trigger": trigger
            })
            print(f"✅ Theory '{t['title']}' confidence: {old_confidence} → {new_confidence}")
            return
    print(f"⚠ Theory {theory_id} not found")

def add_decision(memory: dict, decision: str, category: str, reasoning: str):
    """Add a new committed decision."""
    new_id = f"decision-{len(memory['committed_decisions'])+1:03d}"
    memory["committed_decisions"].append({
        "id": new_id,
        "decision": decision,
        "category": category,
        "reasoning": reasoning,
        "reversibility": "medium",
        "created_at": datetime.now(timezone.utc).date().isoformat(),
        "status": "active"
    })
    print(f"✅ Decision added: {decision[:60]}")

def update_project_state(memory: dict, project_id: str, current_state: str, next_actions: list):
    """Update project status."""
    for p in memory["active_projects"]:
        if p["id"] == project_id:
            p["current_state"] = current_state
            p["next_actions"] = next_actions
            p["last_updated"] = datetime.now(timezone.utc).date().isoformat()
            print(f"✅ Project '{p['name']}' updated")
            return
    print(f"⚠ Project {project_id} not found")

def stats(memory: dict):
    """Show memory statistics."""
    theories = len([t for t in memory["working_theories"] if t["status"] == "active"])
    decisions = len([d for d in memory["committed_decisions"] if d["status"] == "active"])
    rejected = len(memory["rejected_options"])
    projects = len([p for p in memory["active_projects"] if p["status"] in ["active", "ideation"]])
    questions = len(memory["open_questions"])
    history = len(memory["belief_history"])
    avg_confidence = sum(t["confidence"] for t in memory["working_theories"]) / max(len(memory["working_theories"]), 1)
    
    print(f"\nMemory Stats for {memory['user_id']}:")
    print(f"  Working theories:  {theories} active")
    print(f"  Avg confidence:    {avg_confidence:.0f}%")
    print(f"  Committed decisions: {decisions}")
    print(f"  Rejected options:  {rejected}")
    print(f"  Active projects:   {projects}")
    print(f"  Open questions:    {questions}")
    print(f"  Belief history:    {history} events")
    print(f"  Last updated:      {memory['last_updated']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Personal Memory Schema manager")
    parser.add_argument("--show", action="store_true", help="Display current memory")
    parser.add_argument("--stats", action="store_true", help="Show memory statistics")
    parser.add_argument("--query", help="Search memory")
    parser.add_argument("--inject", action="store_true", help="Print agent injection prompt")
    parser.add_argument("--update-confidence", nargs=3, metavar=("THEORY_ID", "CONFIDENCE", "TRIGGER"),
                        help="Update theory confidence")
    parser.add_argument("--add-decision", nargs=3, metavar=("DECISION", "CATEGORY", "REASONING"),
                        help="Add committed decision")
    args = parser.parse_args()

    memory = load_memory()

    if args.show:
        show_memory(memory)
    elif args.stats:
        stats(memory)
    elif args.query:
        print(query_memory(memory, args.query))
    elif args.inject:
        print(build_injection_prompt(memory))
    elif args.update_confidence:
        theory_id, confidence, trigger = args.update_confidence
        update_theory_confidence(memory, theory_id, int(confidence), trigger)
        save_memory(memory)
    elif args.add_decision:
        decision, category, reasoning = args.add_decision
        add_decision(memory, decision, category, reasoning)
        save_memory(memory)
    else:
        parser.print_help()
