import json
from datetime import datetime

PROJECT_ROOT = "/Users/ihorsedy/Documents/AI_FILM_STUDIO 2"

PLAN_FILE = (
"05_AUTOMATION/AI_AGENT/tasks/current_plan.json"
)


def create_plan(task):

    plan = {

        "created":
        str(datetime.now()),

        "task":
        task,

        "mode":
        "PLAN",

        "steps":[

            "Analyze project memory",

            "Identify affected files",

            "Check governance rules",

            "Prepare modification list",

            "Wait for execution approval"

        ],

        "status":
        "WAITING_APPROVAL"

    }


    with open(
        PLAN_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            plan,
            f,
            indent=4,
            ensure_ascii=False
        )


    return plan



if __name__ == "__main__":

    print("AI FILM STUDIO TASK PLANNER")
    print("==========================")

    task = input("\nTask: ")

    result = create_plan(task)

    print("\nPLAN CREATED")
    print(json.dumps(
        result,
        indent=4,
        ensure_ascii=False
    ))
