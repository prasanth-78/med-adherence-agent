# demo_run.py
from datetime import datetime, timedelta
from src.agent_controller import MedAgent
import time

agent = MedAgent()
user = "demo_user"

# Create 3 accelerated reminder times (now + 10s, +20s, +30s)
now = datetime.utcnow()
times = [
    (now + timedelta(seconds=10)).isoformat(),
    (now + timedelta(seconds=20)).isoformat(),
    (now + timedelta(seconds=30)).isoformat()
]

print("Adding medication and scheduling reminders...")
agent.add_med(user, "Lisinopril 10mg", times)

# Simulate ticks: wait and then call run_once to fire reminders
for i in range(6):
    print(f"Tick {i} — running scheduler pass")
    fired = agent.scheduler.run_once()
    if fired:
        # simulate user confirms first fired reminder
        ts = datetime.utcnow().isoformat()
        job = fired[0]
        print("Simulating user confirmation for:", job['med'])
        agent.confirm_dose(user, job['med'], ts, status='on_time')
    time.sleep(6)  # pause so scheduled times get into the past (adjust as needed)

# Generate a report
report = agent.generate_report(user)
print("Report metrics:", report["metrics"])
