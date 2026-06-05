# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def get_status(task):
    return "[✓]" if task["done"] else "[ ]"

def format_task(task):
    due = task.get("due_date", "Sem prazo")
    return f"{get_status(task)} [{task['priority']}] #{task['id']} - {task['title']} (prazo: {due})"

def filter_tasks(tasks, show_done=True, priority=None):
    result = tasks

    if not show_done:
        result = [t for t in result if not t["done"]]

    if priority:
        result = [t for t in result if t["priority"] == priority]

    return result