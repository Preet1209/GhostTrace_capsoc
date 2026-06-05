def generate_twin(scan_data):

    twin = {}

    twin["traveler"] = len(
        scan_data.get("gps", [])
    ) > 0

    twin["student"] = len(
        scan_data.get("documents", [])
    ) > 5

    twin["financial_activity"] = (
        "HIGH"
        if len(scan_data.get("pan", [])) > 0
        else "LOW"
    )

    twin["profile"] = "General User"

    return twin