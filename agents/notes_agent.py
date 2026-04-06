from db import insert_data, get_all, delete_item, update_item, delete_all

def save_note(text):
    insert_data("notes", text)
    return f"Note saved: {text}"

def get_notes():
    data = get_all("notes")
    return [row[1] for row in data]  # ✅ clean text only

def delete_note(note_id):
    delete_item("notes", note_id)
    return f"Note {note_id} deleted"

def delete_all_notes():
    delete_all("notes")
    return "All notes deleted"

def update_note(note_id, new_text):
    update_item("notes", note_id, new_text)
    return f"Note {note_id} updated"