def recommend(scan_data):

    recs = []

    if len(scan_data.get("gps", [])) > 0:

        recs.append(
            "Remove image metadata"
        )

    if len(scan_data.get("pan", [])) > 0:

        recs.append(
            "Encrypt sensitive documents"
        )

    if len(scan_data.get("emails", [])) > 5:

        recs.append(
            "Reduce exposed accounts"
        )

    return recs