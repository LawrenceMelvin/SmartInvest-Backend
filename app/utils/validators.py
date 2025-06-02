def validate_input(data):
    required = [
        "investmentAmount", "investmentType", "riskLevel",
        "hasHealthInsurance", "hasTermInsurance", "hasEmergencyFund"
    ]
    for key in required:
        if key not in data:
            return False, f"Missing field: {key}"

    if not isinstance(data["investmentAmount"], (int, float)) or data["investmentAmount"] < 1000:
        return False, "Amount must be a number >= 1000"
    if data["riskLevel"] not in ["1", "2", "3",1,2,3]:
        return False, "Invalid risk level"
    if data["investmentType"] not in ["sip", "lumpsum"]:
        return False, "Invalid investment type"

    return True, None
