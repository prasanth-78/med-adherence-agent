# src/tools/calendar.py
def add_to_calendar(user_id: str, title: str, start_iso: str, duration_minutes: int=10):
    """Stub: in a real system, integrate with Google Calendar. For demo, just return a dict."""
    return {"status": "ok", "user": user_id, "title": title, "start": start_iso, "duration": duration_minutes}
