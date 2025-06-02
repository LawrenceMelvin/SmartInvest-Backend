def calculate_allocation(amount, risk_level):
    risk_map = {
        "1": "low", 1: "low",
        "2": "medium", 2: "medium",
        "3": "high", 3: "high"
    }
    risk_key = risk_map.get(risk_level)
    if not risk_key:
        raise ValueError("Invalid risk level")
    allocations = {
        "low": {
            "debt": 0.50, "index": 0.20, "gold": 0.10,
            "reits": 0.10, "large_cap": 0.10
        },
        "medium": {
            "index": 0.30, "large_cap": 0.25, "mid_cap": 0.10,
            "debt": 0.20, "gold": 0.10, "reits": 0.05
        },
        "high": {
            "index": 0.35, "large_cap": 0.30, "mid_cap": 0.15,
            "gold": 0.10, "reits": 0.10
        }
    }
    return {k: round(amount * v) for k, v in allocations[risk_key].items()}
