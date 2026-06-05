# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def get_status(task):
    return "[✓]" if task["done"] else "[ ]"

def format_task(task):
    due = task.get("due_date", "Sem prazo")
    return f"{get_status(task)} PRIORIDADE={task['priority']} | #{task['id']} | {task['title']} (prazo: {due})"

def filter_tasks(tasks, show_done=True, priority=None):
    filtered = tasks

    if not show_done:
        filtered = [t for t in filtered if not t["done"]]

    if priority:
        filtered = [t for t in filtered if t["priority"] == priority]

    return sorted(filtered, key=lambda t: t["priority"])