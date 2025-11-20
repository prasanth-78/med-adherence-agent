from datetime import datetime, timedelta, timezone
from src.agent_controller import MedAgent

def test_basic_flow():
    agent = MedAgent()
    user = "test_user"
    now = datetime.now(timezone.utc)
    times = [
        (now + timedelta(seconds=1)).isoformat(),
        (now + timedelta(seconds=2)).isoformat(),
    ]
    agent.add_med(user, "TestMed 1", times)

    # Run scheduler twice to fire reminders
    fired1 = agent.scheduler.run_once()
    fired2 = agent.scheduler.run_once()

    # Simulate confirmations for any fired jobs
    all_fired = fired1 + fired2
    for job in all_fired:
        agent.confirm_dose(user, job["med"], datetime.now(timezone.utc).isoformat(), status="on_time")

    report = agent.generate_report(user)
    
    # Basic sanity asserts
    assert isinstance(report, dict)
    assert "metrics" in report
    assert "total" in report["metrics"]
    assert report["metrics"]["total"] >= 0
    assert report["metrics"]["on_time_rate"] is None or 0.0 <= report["metrics"]["on_time_rate"] <= 1.0
