# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def get_status(task):
    return "[✓]" if task["done"] else "[ ]"

def format_task(task):
    due = task.get("due_date", "Sem prazo")
    return f"{get_status(task)} [{task['priority']}] #{task['id']} - {task['title']} (prazo: {due})"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
