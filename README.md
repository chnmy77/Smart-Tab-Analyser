Smart Tab Analyzer
Overview

Modern users often keep many browser tabs open, leading to clutter, distraction, and decision fatigue. Instead of automatically closing tabs, users need clear, explainable insights to decide which tabs are still useful.

Smart Tab Analyzer is a rule-based Flask web application that analyzes browser tab usage data and provides human-readable recommendations to help users decide whether to keep, review, or archive tabs.

Problem Statement

With increasing multitasking, users hesitate to close browser tabs due to fear of losing important information. Existing solutions either group tabs or close them automatically, which can reduce user trust and control.

There is a need for a system that:

Analyzes tab usage patterns

Explains why a tab is important or not

Supports user decision-making instead of automation

Solution

This project implements a decision-support system that evaluates browser tabs using simple, explainable rules based on:

Recency of access

Frequency of usage

Tab category (study, work, entertainment)

The backend processes tab data and assigns:

Activity status (Active / Inactive)

Priority score

Recommendation (Keep / Review / Archive)

Clear, human-readable reasons for each recommendation

Key Features

Rule-based backend logic (no black-box decisions)

Dynamic analysis using external JSON datasets

Explainable recommendations for every tab

Displays most frequently used tabs

Shows category-wise distribution of tabs

Clean separation of logic, data, and presentation

Technology Stack

Python

Flask

HTML (Jinja Templates)

CSS

Data Source

For this prototype, browser tab usage data is simulated using JSON files (tabs.json, tabs_large.json, tabs_heavy.json).

In a real-world scenario, this data can be collected using browser extension APIs with appropriate user permissions.

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


Design Decisions

JSON is used instead of a database to keep the prototype lightweight and focused

Server-side rendering is used for clarity and simplicity

Logic is rule-based to ensure transparency and easy explainability

Future Enhancements

Browser extension integration for real usage data

User-specific tab behavior analysis

Optional AI-based natural language explanations

Interactive filtering using JavaScript