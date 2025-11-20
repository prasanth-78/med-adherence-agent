# src/agent_controller.py
from src.memory import MemoryBank
from src.tools.notification import ConsoleNotifier
from src.scheduler import ReminderScheduler
from src.observability import compute_adherence_metrics

class MedAgent:
    def __init__(self):
        self.memory = MemoryBank()
        self.notifier = ConsoleNotifier()
        self.scheduler = ReminderScheduler(self.notifier, self.memory)

    def add_med(self, user_id: str, med_name: str, times_list: list):
        """times_list: list of ISO datetime strings"""
        med_obj = {"name": med_name, "times": times_list}
        self.memory.save_med_schedule(user_id, med_obj)
        for t in times_list:
            from datetime import datetime
            dt = datetime.fromisoformat(t)
            self.scheduler.add_job(user_id, med_name, dt, interval_minutes=24*60)
        return {"status": "ok", "med": med_obj}

    def confirm_dose(self, user_id: str, med_name: str, timestamp: str, status: str='on_time'):
        self.memory.record_adherence(user_id, med_name, timestamp, status)
        return {"status": "recorded"}

    def generate_report(self, user_id: str):
        user = self.memory.get_user(user_id)
        metrics = compute_adherence_metrics(user.get("adherence", []))
        return {"metrics": metrics, "adherence": user.get("adherence", [])}
