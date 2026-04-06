from db import insert_data, get_all, delete_item, update_item, delete_all

def create_event(text):
    existing_events = get_events()

    # 🔥 Conflict Detection (simple but effective)
    for event in existing_events:
        if text.lower() in event.lower() or event.lower() in text.lower():
            return f"⚠️ Conflict detected: '{event}' already scheduled"

    insert_data("events", text)
    return f"Event scheduled: {text}"


def get_events():
    data = get_all("events")
    return [row[1] for row in data]  # clean text only


def delete_event(event_id):
    delete_item("events", event_id)
    return f"Event {event_id} deleted"


def delete_all_events():
    delete_all("events")
    return "All events deleted"


def update_event(event_id, new_text):
    update_item("events", event_id, new_text)
    return f"Event {event_id} updated"