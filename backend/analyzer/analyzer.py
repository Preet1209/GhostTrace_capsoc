import json

from risk_engine import calculate_risk
from digital_twin import generate_twin
from attack_engine import generate_attack_paths
from recommendation import generate_recommendations


with open("shared/scan.json", "r") as f:
    scan_data = json.load(f)


risk = calculate_risk(scan_data)

twin = generate_twin(scan_data)

attacks = generate_attack_paths(scan_data)

recs = generate_recommendations(scan_data)


final_output = {

    "risk_score": risk["risk_score"],

    "risk_level": risk["risk_level"],

    "digital_twin": twin,

    "attack_paths": attacks,

    "recommendations": recs
}


with open("shared/analysis.json", "w") as f:

    json.dump(
        final_output,
        f,
        indent=4
    )


print("analysis.json generated")