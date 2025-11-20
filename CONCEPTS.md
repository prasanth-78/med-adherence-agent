\# Where course concepts are implemented



\- Sessions \& Memory

&nbsp; - src/memory.py — MemoryBank class (persists med schedules and adherence)

\- Long-running operations (reminders)

&nbsp; - src/scheduler.py — ReminderScheduler (run\_once + start\_loop)

&nbsp; - src/agent\_controller.py — add\_med schedules jobs via ReminderScheduler

\- Observability (metrics \& plots)

&nbsp; - src/observability.py — compute\_adherence\_metrics, plot\_weekly\_adherence

\- Tools

&nbsp; - src/tools/notification.py — ConsoleNotifier (demo notifier)

&nbsp; - src/tools/calendar.py — calendar stub

\- Agent evaluation

&nbsp; - tests/test\_simulation.py — basic simulation test

\- Deployment (bonus)

&nbsp; - Dockerfile — container image for demo



