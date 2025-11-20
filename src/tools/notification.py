# src/tools/notification.py
import time
import json

class ConsoleNotifier:
    """Simple notifier used in demo to simulate SMS/push notifications."""
    def __init__(self):
        pass

    def send(self, user_id: str, message: str):
        # In demo, print and return a simple event dict
        ts = time.time()
        out = {"status": "sent", "user": user_id, "message": message, "ts": ts}
        print(f"[NOTIFY {ts:.0f}] To {user_id}: {message}")
        return out
