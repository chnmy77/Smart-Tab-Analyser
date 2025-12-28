Smart Tab Analyzer


Overview
Modern users often keep many browser tabs open, which leads to clutter, distraction, and decision fatigue. Users hesitate to close tabs due to fear of losing important information.
Smart Tab Analyzer is a rule-based Flask web application that analyzes browser tab usage data and provides clear, explainable recommendations to help users decide which tabs to keep, review, or archive.

Problem Statement
With increasing multitasking, browser tab overload has become common. Existing solutions typically focus on grouping tabs or automatically closing them, which can reduce user control and trust.

There is a need for a system that:
Analyzes tab usage behavior
Explains why a tab may no longer be useful
Supports user decision-making instead of automation

Solution:
This project implements a decision-support system that evaluates browser tabs using simple, transparent rules based on:
Recency of access
Frequency of usage
Tab category (study, work, entertainment)

The backend processes tab data and generates:
Activity status (Active / Inactive)
Priority scores
Recommendations (Keep / Review / Archive)
Human-readable reasons for each recommendation

Key Features
Rule-based backend logic (no black-box decisions)
Dynamic analysis using external JSON datasets
Explainable recommendations for every tab
Identification of most frequently used tabs
Category-wise distribution of tabs
Clean separation of data, logic, and presentation

Technology Stack
Python
Flask
HTML (Jinja Templates)
CSS

Data Source
For this prototype, browser tab usage data is simulated using JSON files:
tabs.json
tabs_large.json
tabs_heavy.json

These datasets are used to test the system with different tab usage patterns and scales.
In a real-world scenario, this data can be collected using browser extension APIs with appropriate user permissions.

Project Structure
Smart-Tab-Analyser/
│
├── app.py
├── tabs.json
├── tabs_large.json
├── tabs_heavy.json
│
├── templates/
│   ├── index.html
│   └── stats.html
│
├── static/
│   └── style.css
│
└── README.md

How to Run the Project
1. Install dependencies
pip install flask

2. Run the application
python app.py

3. Open in browser
http://127.0.0.1:5000/

Optional statistics page:
http://127.0.0.1:5000/stats
