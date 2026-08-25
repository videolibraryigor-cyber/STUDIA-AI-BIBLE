import json
import subprocess
import os
from datetime import datetime


PROJECT_ROOT = "/Users/ihorsedy/Documents/AI_FILM_STUDIO 2"

MEMORY_FILE = os.path.join(
    PROJECT_ROOT,
    "05_AUTOMATION/AI_AGENT/memory/project_memory.json"
)

LOG_FILE = os.path.join(
    PROJECT_ROOT,
    "05_AUTOMATION/AI_AGENT/logs/ollama_bridge.log"
)

MODEL = "gpt-oss:20b"


def load_memory():

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



def search_memory(task, limit=10):

    memory = load_memory()

    results = []

    keywords = task.lower().split()

    for item in memory.get("documents", []):

        text = json.dumps(
            item,
            ensure_ascii=False
        ).lower()

        score = sum(
            1 for word in keywords
            if word in text
        )

        if score:
            results.append(
                (score, item)
            )


    results.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        x[1]
        for x in results[:limit]
    ]



def ask_ollama(task):

    context = search_memory(task)

    prompt = f"""
You are AI FILM STUDIO SYSTEM ARCHITECT.

Project memory:

{json.dumps(context, ensure_ascii=False, indent=2)}

Task:

{task}

Rules:

- Analyze project information only.
- Do not invent.
- Do not modify files.
- Return structured answer.
"""


    result = subprocess.run(
        [
            "ollama",
            "run",
            MODEL,
            prompt
        ],
        capture_output=True,
        text=True,
        timeout=300
    )

    return result.stdout



if __name__ == "__main__":

    print("AI FILM STUDIO OLLAMA BRIDGE")
    print("============================")

    task = input("\nTask: ")

    answer = ask_ollama(task)

    print("\nRESULT:")
    print(answer)


    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(
            f"""
DATE:
{datetime.now()}

TASK:
{task}

RESULT:
{answer}

====================
"""
        )
