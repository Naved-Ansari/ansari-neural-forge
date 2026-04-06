from db import insert_data, get_all, delete_item, update_item, delete_all

def create_task(text):
    insert_data("tasks", text)
    return f"Task created: {text}"

def get_tasks():
    data = get_all("tasks")
    return [row[1] for row in data]  # ✅ clean text only

def delete_task(task_id):
    delete_item("tasks", task_id)
    return f"Task {task_id} deleted"

def delete_all_tasks():
    delete_all("tasks")
    return "All tasks deleted"

def update_task(task_id, new_text):
    update_item("tasks", task_id, new_text)
    return f"Task {task_id} updated"