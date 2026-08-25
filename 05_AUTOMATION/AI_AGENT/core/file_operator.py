import os
import shutil
from datetime import datetime

PROJECT_ROOT = "/Users/ihorsedy/Documents/AI_FILM_STUDIO 2"

BACKUP_DIR = os.path.join(
    PROJECT_ROOT,
    "05_AUTOMATION/AI_AGENT/core/backups"
)


def backup_file(path):
    if not os.path.exists(path):
        return False

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.basename(path)

    backup_path = os.path.join(
        BACKUP_DIR,
        f"{filename}.{timestamp}.bak"
    )

    shutil.copy2(path, backup_path)

    return backup_path


def create_file(path, content):

    full_path = os.path.join(
        PROJECT_ROOT,
        path
    )

    if os.path.exists(full_path):
        return "FILE EXISTS"

    os.makedirs(
        os.path.dirname(full_path),
        exist_ok=True
    )

    with open(
        full_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return "CREATED"


def update_file(path, content):

    full_path = os.path.join(
        PROJECT_ROOT,
        path
    )

    if os.path.exists(full_path):
        backup_file(full_path)

    with open(
        full_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(content)

    return "UPDATED"


if __name__ == "__main__":

    print("AI FILM STUDIO FILE OPERATOR")
    print("============================")

    print("READY")
