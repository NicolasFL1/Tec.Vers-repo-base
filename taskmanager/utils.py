# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[✓]" if task["done"] else "[ ]"
    due = task.get("due_date", "Sem prazo")
    return f"{status} [{task['priority']}] #{task['id']} - {task['title']} (prazo: {due})"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
