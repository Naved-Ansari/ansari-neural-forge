from agents.task_agent import (
    create_task, get_tasks, delete_task, delete_all_tasks, update_task
)
from agents.calendar_agent import (
    create_event, get_events, delete_event, delete_all_events, update_event
)
from agents.notes_agent import (
    save_note, get_notes, delete_note, delete_all_notes, update_note
)


def extract_text(user_input, keyword):
    """
    Extract meaningful text after keyword and clean quotes
    """
    parts = user_input.split(keyword, 1)
    if len(parts) > 1:
        text = parts[1].strip()
    else:
        text = user_input

    text = text.replace('"', '').replace("'", "")
    return text


def orchestrator(user_input):
    text = user_input.lower().strip()

    # GREETING
    if text in ["hi", "hello", "hey"]:
        return (
            "👋 Hello! I'm Ansari AI.\n\n"
            "I can help you with:\n\n"
            "📝 Tasks\n"
            "📅 Scheduling\n"
            "🗒️ Notes\n\n"
            "Try:\n"
            "- create task submit report\n"
            "- schedule meeting tomorrow at 5pm\n"
            "- show tasks\n"
        )

    # DELETE ALL (SAFE ENTITY CONTROL)
    if "delete all" in text:
        if "task" in text:
            return delete_all_tasks()

        elif "schedule" in text or "event" in text:
            return delete_all_events()

        elif "note" in text:
            return delete_all_notes()

    # DELETE SINGLE
    elif "delete task" in text:
        task_id = int(text.split()[-1])
        return delete_task(task_id)

    elif "delete event" in text or "delete schedule" in text:
        event_id = int(text.split()[-1])
        return delete_event(event_id)

    elif "delete note" in text:
        note_id = int(text.split()[-1])
        return delete_note(note_id)

    # UPDATE
    elif "update task" in text:
        parts = user_input.split()
        task_id = int(parts[2])
        new_text = " ".join(parts[3:])
        return update_task(task_id, new_text)

    elif "update event" in text or "update schedule" in text:
        parts = user_input.split()
        event_id = int(parts[2])
        new_text = " ".join(parts[3:])
        return update_event(event_id, new_text)

    elif "update note" in text:
        parts = user_input.split()
        note_id = int(parts[2])
        new_text = " ".join(parts[3:])
        return update_note(note_id, new_text)

    # FETCH (HIGH PRIORITY)
    elif "show" in text:
        if "task" in text:
            return get_tasks()

        elif "schedule" in text or "event" in text:
            return get_events()

        elif "note" in text:
            return get_notes()

    # MULTI-STEP WORKFLOW
    elif "plan my day" in text:
        t1 = create_task("Complete work")
        t2 = create_event("Meeting at 5 PM")
        return {"workflow": [t1, t2]}

    # CREATE (SMART PARSING)

    elif "schedule" in text or "meeting" in text:
        clean_text = extract_text(user_input, "schedule")
        if clean_text == user_input:
            clean_text = extract_text(user_input, "meeting")
        return create_event(clean_text)

    elif "note" in text:
        clean_text = extract_text(user_input, "note")
        return save_note(clean_text)

    elif "task" in text:
        clean_text = extract_text(user_input, "task")
        return create_task(clean_text)

    # FALLBACK
    else:
        return (
            "🤖 I didn’t understand that.\n\n"
            "Try:\n"
            "- create task submit report\n"
            "- schedule meeting tomorrow at 5pm\n"
            "- show tasks\n"
        )