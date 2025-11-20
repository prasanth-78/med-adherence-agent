# src/scheduler.py
import time
from datetime import datetime, timedelta
from typing import List, Dict

class ReminderScheduler:
    """Simple scheduler that supports scheduling reminders and running them in a demo loop."""
    def __init__(self, notifier, memory):
        self.notifier = notifier
        self.memory = memory
        self.jobs = []  # list of dicts: {user_id, med, next_ts_iso, interval_minutes}
        self.running = False

    def add_job(self, user_id: str, med_name: str, next_ts: datetime, interval_minutes: int=24*60):
        job = {"user": user_id, "med": med_name, "next_ts": next_ts.isoformat(), "interval": interval_minutes}
        self.jobs.append(job)

    def run_once(self):
        """Run a single pass — useful in a notebook to simulate time / trigger due reminders."""
        now = datetime.utcnow()
        fired = []
        for job in list(self.jobs):
            next_ts = datetime.fromisoformat(job["next_ts"])
            if next_ts <= now:
                msg = f"Reminder: time to take {job['med']} (user {job['user']})"
                result = self.notifier.send(job["user"], msg)
                fired.append(job)
                # schedule next occurrence
                next_time = next_ts + timedelta(minutes=job["interval"])
                job["next_ts"] = next_time.isoformat()
        return fired

    # For local, optionally implement a background loop (not used in Kaggle demo)
    def start_loop(self, interval_seconds=60):
        import threading
        self.running = True
        def loop():
            while self.running:
                self.run_once()
                time.sleep(interval_seconds)
        t = threading.Thread(target=loop, daemon=True)
        t.start()
        return t

    def stop(self):
        self.running = False
