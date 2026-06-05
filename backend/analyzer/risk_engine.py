def calculate_risk(scan_data):

    score = 0

    emails = scan_data.get("emails", [])
    phones = scan_data.get("phones", [])
    gps = scan_data.get("gps", [])
    pan = scan_data.get("pan", [])
    documents = scan_data.get("documents", [])

    photos = scan_data.get("photos", [])

    if isinstance(photos, int):

        photo_count = photos

    else:

        photo_count = len(photos)


    score += len(emails) * 2
    score += len(phones) * 3
    score += len(gps) * 5
    score += len(pan) * 10
    score += len(documents) * 1
    score += photo_count * 2


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