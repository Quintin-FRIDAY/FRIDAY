from core.memory import Memory

memory = Memory()


def process_memory(command: str):
    if not command.startswith("/"):
        return None

    parts = command.split(maxsplit=3)

    # /memory set <key> <value>
    if len(parts) >= 4:
        if parts[0] == "/memory" and parts[1] == "set":
            key = parts[2]
            value = parts[3]

            memory.remember(key, value)

            return "Memory saved."

    # /memory get <key>
    if len(parts) == 3:
        if parts[0] == "/memory" and parts[1] == "get":
            value = memory.recall(parts[2])

            if value:
                return value

            return "Memory not found."

    # /memory delete <key>
    if len(parts) == 3:
        if parts[0] == "/memory" and parts[1] == "delete":
            memory.forget(parts[2])

            return "Memory deleted."

    # /memory list
    if command == "/memory list":
        memories = memory.list_memories()

        if not memories:
            return "No memories stored."

        output = []

        for row in memories:
            output.append(f"{row['key']} = {row['value']}")

        return "\n".join(output)

    return None