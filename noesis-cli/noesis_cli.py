# noesis_cli.py

import os
import json
import yaml
import hashlib
import datetime
from pathlib import Path

NODE_ROOT = Path("nodes")
NODE_ROOT.mkdir(exist_ok=True)


def prompt(question, default):
    answer = input(f"{question} [{default}]: ")
    return answer.strip() or default


def create_new_node():
    print("\n🌱 Launching Noēsis Node Creation Wizard...")

    node_id = prompt("Node ID", "noesis-node-001")
    persona_name = prompt("Persona Name", "Gaia")
    logic = float(prompt("Logic Weight (0-1)", "0.7"))
    empathy = float(prompt("Empathy (0-1)", "0.6"))
    curiosity = float(prompt("Curiosity (0-1)", "0.8"))

    ethics_core = ["Respect privacy", "Avoid harm", "Do not manipulate"]
    ethics_adaptive = {
        "open_access": 0.8,
        "radical_transparency": 0.6,
        "collaborative_autonomy": 0.9
    }

    node_path = NODE_ROOT / node_id
    node_path.mkdir(parents=True, exist_ok=True)

    # persona.yaml
    persona_data = {
        "name": persona_name,
        "traits": {
            "logic": logic,
            "empathy": empathy,
            "curiosity": curiosity
        }
    }
    with open(node_path / "persona.yaml", "w") as f:
        yaml.dump(persona_data, f)

    # ethics.json
    ethics_data = {
        "core": ethics_core,
        "adaptive": ethics_adaptive
    }
    with open(node_path / "ethics.json", "w") as f:
        json.dump(ethics_data, f, indent=2)

    # config.yaml
    config = {
        "node_id": node_id,
        "persona": persona_name,
        "memory_file": "memory.db",
        "swarm_enabled": False
    }
    with open(node_path / "config.yaml", "w") as f:
        yaml.dump(config, f)

    print(f"\n✅ Node '{node_id}' created at {node_path.absolute()}")


def run_node(node_id):
    node_path = NODE_ROOT / node_id
    if not node_path.exists():
        print(f"❌ Node '{node_id}' not found.")
        return

    print(f"\n🧠 Starting Noēsis node: {node_id}")
    with open(node_path / "persona.yaml") as f:
        persona = yaml.safe_load(f)
    with open(node_path / "ethics.json") as f:
        ethics = json.load(f)

    print(f"\nPersona: {persona['name']}")
    print(f"Traits: {persona['traits']}")
    print(f"Core Ethics: {ethics['core']}")
    print(f"Adaptive Values: {ethics['adaptive']}")

    print("\n🚀 Node is initialized. (Functionality simulation to be extended.)")


def reflect_node(node_id):
    node_path = NODE_ROOT / node_id
    journal_path = node_path / "reflection_log.json"

    if not node_path.exists():
        print(f"❌ Node '{node_id}' not found.")
        return

    # Generate reflection summary
    timestamp = datetime.datetime.utcnow().isoformat()
    summary = f"Reflection for node {node_id} at {timestamp}"
    graph_hash = hashlib.sha256((node_id + timestamp).encode()).hexdigest()

    entry = {
        "timestamp": timestamp,
        "summary": summary,
        "graph_hash": graph_hash
    }

    journal = []
    if journal_path.exists():
        with open(journal_path, "r") as f:
            journal = json.load(f)

    journal.append(entry)
    with open(journal_path, "w") as f:
        json.dump(journal, f, indent=2)

    print(f"\n🪞 Reflection added for node '{node_id}'")
    print(json.dumps(entry, indent=2))


def drift_log(node_id):
    node_path = NODE_ROOT / node_id
    journal_path = node_path / "reflection_log.json"

    if not journal_path.exists():
        print(f"❌ No reflection journal found for node '{node_id}'")
        return

    with open(journal_path, "r") as f:
        journal = json.load(f)

    print(f"\n📜 Cognitive Drift Log for '{node_id}':")
    for i, entry in enumerate(journal[-5:], 1):
        print(f"\n--- Entry {i} ---")
        print(f"Time: {entry['timestamp']}")
        print(f"Hash: {entry['graph_hash']}")
        print(f"Summary: {entry['summary']}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Noēsis CLI Tool")
    parser.add_argument("command", nargs="?", help="CLI command")
    parser.add_argument("--node", type=str, help="Node ID to run/reflect")

    args = parser.parse_args()

    if args.command == "new-node":
        create_new_node()
    elif args.command == "run" and args.node:
        run_node(args.node)
    elif args.command == "reflect" and args.node:
        reflect_node(args.node)
    elif args.command == "drift-log" and args.node:
        drift_log(args.node)
    else:
        print("🧠 Noēsis CLI — Commands: 'new-node', 'run --node NODE_ID', 'reflect --node NODE_ID', 'drift-log --node NODE_ID'")

