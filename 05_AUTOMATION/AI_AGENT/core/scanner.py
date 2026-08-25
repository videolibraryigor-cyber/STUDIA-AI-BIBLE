import os
import json
from datetime import datetime


PROJECT_ROOT = "/Users/ihorsedy/Documents/AI_FILM_STUDIO 2"

OUTPUT = "05_AUTOMATION/AI_AGENT/memory/project_index.json"


IGNORE = [
    ".git",
    "__pycache__",
    "00_SOURCE_ARCHIVE"
]


def scan_project():

    index = {
        "project": "AI_FILM_STUDIO",
        "created": str(datetime.now()),
        "files": []
    }


    for root, dirs, files in os.walk(PROJECT_ROOT):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE
        ]


        for file in files:

            path = os.path.join(root, file)

            index["files"].append({
                "path": path.replace(PROJECT_ROOT, ""),
                "extension": os.path.splitext(file)[1]
            })


    with open(
        OUTPUT,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            index,
            f,
            indent=2,
            ensure_ascii=False
        )


    print("PROJECT INDEX CREATED")
    print("FILES:", len(index["files"]))


if __name__ == "__main__":
    scan_project()
