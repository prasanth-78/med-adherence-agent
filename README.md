Medication Adherence Assistant

A simple, helpful AI agent that makes it easier for people to stay on track with their medications.

 What This Project Does

This project is a lightweight AI-powered assistant that reminds users to take their medications on time, tracks whether they took them, and creates easy-to-read reports that caregivers can use.

The goal isn’t to be a medical device — it’s to show how AI agents, memory, tools, and long-running behavior can come together to solve a meaningful real-world problem, especially for people who might struggle with remembering daily medications.

 Why I Built This

Many people forget their medications — especially seniors, people with chronic conditions, or anyone managing multiple prescriptions. Missing doses can quickly turn into health problems.

This agent offers a simple helping hand:

Remind users based on their schedule

Log whether they took their dose

Summarize their adherence in a caregiver-friendly way

It’s practical, easy to run, and showcases the concepts from Google’s 5-Day AI Agents Intensive course in a real, useful project.

 What’s Inside

This project uses several agent concepts from the course:

Long-running behavior (simulated reminder loop)

Memory (stored in a lightweight JSON file)

Custom tools (ConsoleNotifier for reminders)

Observability (adherence metrics + optional charts)

Clean modular architecture (like an ADK-style agent)

 Project Structure
med-adherence-agent/
│
├── src/
│   ├── agent_controller.py     # Main agent orchestrator
│   ├── memory.py               # Long-term memory store
│   ├── scheduler.py            # Reminder scheduler
│   ├── observability.py        # Metrics + plots
│   └── tools/                  # Custom tools
│       ├── notification.py
│       └── calendar.py
│
├── notebooks/
│   └── demo_kaggle_notebook.ipynb
│
├── tests/
│   └── test_simulation.py
│
├── demo_run.py
├── requirements.txt
└── README.md

🚀 How to Run It (Super Simple)
1️ Clone the project
git clone https://github.com/prasanth-78/med-adherence-agent.git

2️ Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate      # On Windows

3️ Install dependencies
pip install -r requirements.txt

4️ Run the demo
python demo_run.py


This will:

Add a sample medication

Schedule reminders

Fire them automatically

Simulate confirmations

Print out an adherence report

 Example Output
[NOTIFY] To demo_user: Reminder: time to take Lisinopril 10mg
Simulating user confirmation...
Report metrics: {'on_time_rate': 1.0, 'total': 3}

 (Optional) Run the Test Suite
pytest -q

 What I Learned Building This

How to structure an agent with real “long-running” behavior

How to store and manage user state with a memory system

How to integrate basic tools to extend an agent’s abilities

How to turn agent output into usable insights (reports/plots)

How to turn an idea into a full, working capstone project

 Limitations

To keep things safe and simple:

This is not a medical device

Storage is plain JSON, not secure for real clinical data

Notifications are console-only (no real SMS or email yet)

No authentication or multi-user safeguards

Not intended for real patient use

 Future Ideas

If expanded after the capstone, the project could include:

SMS or email reminder support

A small dashboard for caregivers

Encrypted storage

Weekly adherence summaries

Automatic rescheduling or snoozing

Multi-agent design with specialized workers

 Author

Prasanth
