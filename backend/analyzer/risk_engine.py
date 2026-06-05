def calculate_risk(scan_data):

    score = 0

    score += len(scan_data.get("emails", [])) * 2

    score += len(scan_data.get("phones", [])) * 3

    score += len(scan_data.get("gps", [])) * 5

    score += len(scan_data.get("pan", [])) * 10

    score += len(scan_data.get("documents", []))

    score += scan_data.get("photos", 0) * 0.2

    if score > 80:
        level = "HIGH"

    elif score > 40:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {

        "risk_score": round(score),

        "risk_level": level
    }