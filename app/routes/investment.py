from flask import Blueprint, request, jsonify
from app.services.investment_logic import calculate_allocation
from app.staticfunds.funds import fund_suggestions
from app.utils.validators import validate_input

investment_bp = Blueprint("investment", __name__, url_prefix="/api")


@investment_bp.route("/investment-plan", methods=["POST"])
def investment_plan():
    data = request.json
    print(f"Received data: {data}")
    valid, error = validate_input(data)
    if not valid:
        return jsonify({"error": error}), 400

    amount = float(data["investmentAmount"])
    breakdown = calculate_allocation(amount, data["riskLevel"])

    # Example Python code for backend
    category_meta = {
        "debt": {"name": "Debt", "color": "#4F46E5"},
        "gold": {"name": "Gold", "color": "#F59E42"},
        "index": {"name": "Index", "color": "#10B981"},
        "large_cap": {"name": "Large Cap", "color": "#F43F5E"},
        "mid_cap": {"name": "Mid Cap", "color": "#FBBF24"},
        "reits": {"name": "REITs", "color": "#6366F1"},
    }

    total = sum(breakdown.values())
    breakdown_array = []
    for key, amount in breakdown.items():
        meta = category_meta.get(key, {"name": key.capitalize(), "color": "#888"})
        breakdown_array.append({
            "name": meta["name"],
            "amount": amount,
            "percentage": round(amount / total * 100),
            "color": meta["color"],
        })

    advice = []
    print(data["hasHealthInsurance"])
    if data["hasHealthInsurance"] == 'False' or data["hasHealthInsurance"] == False:
        advice.append("We recommend buying health insurance before investing.")
    if data["hasTermInsurance"] == 'False' or data["hasTermInsurance"] == False:
        advice.append("We recommend buying term life insurance before investing.")
    if data["hasEmergencyFund"] == 'False' or data["hasEmergencyFund"] == False:
        advice.append("You should maintain an emergency fund of at least 3–6 months of expenses.")

    funds = {cat: fund_suggestions.get(cat, []) for cat in breakdown}

    return jsonify({
        "advice": advice,
        "breakdown": breakdown_array,
        "funds": funds
    })
