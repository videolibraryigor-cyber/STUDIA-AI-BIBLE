import os
import json
from datetime import datetime

PROJECT_ROOT = "/Users/ihorsedy/Documents/AI_FILM_STUDIO 2"

INDEX_FILE = "05_AUTOMATION/AI_AGENT/memory/project_index.json"

OUTPUT_FILE = "05_AUTOMATION/AI_AGENT/memory/project_memory.json"


def load_index():

    with open(
        os.path.join(PROJECT_ROOT, INDEX_FILE),
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def read_file(path):

    full_path = os.path.join(
        PROJECT_ROOT,
        path.lstrip("/")
    )

    if not os.path.exists(full_path):
        return None

    try:
        with open(
            full_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:
            return f.read()

    except:
        return None


def build_memory():

    index = load_index()

    memory = {
        "project": index["project"],
        "created": str(datetime.now()),
        "documents": []
    }

    for item in index["files"]:

        content = read_file(item["path"])

        if content:

            memory["documents"].append(
                {
                    "path": item["path"],
                    "content": content[:10000]
                }
            )

    with open(
        os.path.join(PROJECT_ROOT, OUTPUT_FILE),
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memory,
            f,
            indent=2,
            ensure_ascii=False
        )


    print("PROJECT MEMORY CREATED")
    print("DOCUMENTS:", len(memory["documents"]))


if __name__ == "__main__":
    build_memory()
