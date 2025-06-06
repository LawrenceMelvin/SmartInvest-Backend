from flask import Flask, request, jsonify, Blueprint

homelone_advise = Blueprint("homeloan", __name__, url_prefix="/api")

@homelone_advise.route('/home-loan/advice', methods=['POST'])
def home_loan_advice():
    data = request.json

    income = data.get("monthlyIncome")
    existing_emi = data.get("existingEmis")
    loan_amount = data.get("desiredLoanAmount")
    interest_rate = data.get("interestRate") / 12 / 100  # Monthly interest rate
    tenure_months = data.get("tenure") * 12

    # EMI Calculation (Standard Formula)
    emi = loan_amount * interest_rate * (1 + interest_rate) ** tenure_months / ((1 + interest_rate) ** tenure_months - 1)
    total_emi = emi + existing_emi
    max_safe_emi = income * 0.4

    # Eligibility check
    status = "Eligible" if total_emi <= max_safe_emi else "We Recommend Not Taking This Loan"
    suggestions = []

    if total_emi > max_safe_emi:
        suggestions.append("Try reducing the loan amount or increasing tenure.")
        suggestions.append("Consider repaying existing loans first.")
        suggestions.append("Ensure your EMIs don't exceed 40% of your income.")

    return jsonify({
        "status": status,
        "monthly_emi": round(emi, 2),
        "total_monthly_emi_with_existing": round(total_emi, 2),
        "max_safe_emi": round(max_safe_emi, 2),
        "suggestions": suggestions
    })
