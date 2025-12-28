import json
from flask import Flask, render_template
from typing import List, Dict

app = Flask(__name__)

# ---------------- BACKEND LOGIC ---------------- #

def analyze_tabs(tabs: List[Dict]) -> Dict:
    analyzed_tabs = []
    category_distribution = {}

    def get_recency_label(days):
        if days == 0:
            return "Opened today"
        elif 1 <= days <= 2:
            return "Recently used"
        elif 3 <= days <= 7:
            return "Moderately used"
        elif 8 <= days <= 14:
            return "Rarely used"
        else:
            return "Forgotten"

    def get_usage_intensity(freq):
        if freq >= 6:
            return "Heavy usage"
        elif 3 <= freq <= 5:
            return "Moderate usage"
        elif 1 <= freq <= 2:
            return "Low usage"
        else:
            return "Unused"

    def get_status(days):
        return "Active" if days <= 5 else "Inactive"

    def calculate_score(days, freq, category):
        score = 0

        if days <= 2:
            score += 40
        elif days <= 5:
            score += 25
        else:
            score += 5

        if freq >= 5:
            score += 30
        elif freq >= 2:
            score += 15
        else:
            score += 5

        if category in ["study", "work"]:
            score += 20
        else:
            score += 5

        return score

    def get_value(category, usage):
        if category in ["study", "work"] and usage in ["Heavy usage", "Moderate usage"]:
            return "High value"
        elif usage == "Moderate usage":
            return "Medium value"
        else:
            return "Low value"

    def get_recommendation(score):
        if score >= 70:
            return "Keep"
        elif 40 <= score < 70:
            return "Review"
        else:
            return "Archive"

    def generate_reason(tab):
        reasons = []

        if tab["recency_label"] in ["Forgotten", "Rarely used"]:
            reasons.append(f"Last accessed {tab['last_accessed_days']} days ago")

        if tab["usage_intensity"] in ["Low usage", "Unused"]:
            reasons.append("Low usage frequency")

        if tab["category"] == "entertainment":
            reasons.append("Entertainment category")

        if not reasons:
            reasons.append("Frequently used and important")

        return "; ".join(reasons)

    for tab in tabs:
        days = tab["last_accessed_days"]
        freq = tab["frequency"]
        category = tab["category"]

        recency_label = get_recency_label(days)
        usage_intensity = get_usage_intensity(freq)
        status = get_status(days)
        score = calculate_score(days, freq, category)
        value = get_value(category, usage_intensity)
        recommendation = get_recommendation(score)

        analyzed_tab = {
            "title": tab["title"],
            "domain": tab["domain"],
            "category": category,
            "status": status,
            "recency_label": recency_label,
            "usage_intensity": usage_intensity,
            "value": value,
            "priority_score": score,
            "recommendation": recommendation,
            "last_accessed_days": days,
            "frequency": freq
        }

        analyzed_tab["reason"] = generate_reason(analyzed_tab)
        analyzed_tabs.append(analyzed_tab)

        category_distribution[category] = category_distribution.get(category, 0) + 1

    top_used_tabs = sorted(
        analyzed_tabs, key=lambda x: x["frequency"], reverse=True
    )[:3]

    return {
        "tabs_analysis": analyzed_tabs,
        "top_used_tabs": top_used_tabs,
        "category_distribution": category_distribution
    }


# ---------------- DATA LOADER ---------------- #

def load_tabs_from_json(filename="tabs_large.json"):
    with open(filename, "r") as file:
        return json.load(file)


# ---------------- FLASK ROUTES ---------------- #

@app.route("/")
def home():
    tabs = load_tabs_from_json("tabs_large.json")
    result = analyze_tabs(tabs)
    return render_template(
        "index.html",
        tabs=result["tabs_analysis"]
    )


@app.route("/stats")
def stats():
    tabs = load_tabs_from_json("tabs_large.json")
    result = analyze_tabs(tabs)
    return render_template(
        "stats.html",
        top_tabs=result["top_used_tabs"],
        category_distribution=result["category_distribution"]
    )


# ---------------- RUN APP ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
