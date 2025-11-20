# src/memory.py
import json
from datetime import datetime
from typing import Dict, List

class MemoryBank:
    """Simple file-backed memory bank for demo purposes."""
    def __init__(self, path="memory_store.json"):
        self.path = path
        try:
            with open(self.path, "r") as f:
                self.store = json.load(f)
        except FileNotFoundError:
            self.store = {"users": {}}
            self._commit()

    def _commit(self):
        with open(self.path, "w") as f:
            json.dump(self.store, f, default=str, indent=2)

    def add_user(self, user_id: str):
        if user_id not in self.store["users"]:
            self.store["users"][user_id] = {"meds": [], "adherence": []}
            self._commit()

    def save_med_schedule(self, user_id: str, med_obj: Dict):
        self.add_user(user_id)
        self.store["users"][user_id]["meds"].append(med_obj)
        self._commit()

    def record_adherence(self, user_id: str, med_name: str, timestamp: str, status: str):
        self.add_user(user_id)
        entry = {"med": med_name, "ts": timestamp, "status": status}
        self.store["users"][user_id]["adherence"].append(entry)
        self._commit()

    def get_user(self, user_id: str):
        return self.store["users"].get(user_id, {})
