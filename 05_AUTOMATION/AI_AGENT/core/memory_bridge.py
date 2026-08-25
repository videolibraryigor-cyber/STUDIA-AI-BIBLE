import json


MEMORY_FILE = "05_AUTOMATION/AI_AGENT/memory/project_memory.json"


def load_memory():

    with open(
        MEMORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)



if __name__ == "__main__":

    print("AI FILM STUDIO MEMORY BRIDGE")
    print("============================")

    memory = load_memory()

    print("MEMORY LOADED")

    if isinstance(memory, dict):
        print("TYPE: DICTIONARY")
        print("KEYS:")
        for key in memory.keys():
            print("-", key)

    else:
        print("ITEMS:", len(memory))
