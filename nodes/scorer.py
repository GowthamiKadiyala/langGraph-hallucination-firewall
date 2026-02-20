def score_risk(state):
    total = len(state["verified_claims"])
    true_count = sum(state["verified_claims"])

    if total == 0:
        state["risk_score"] = 1
    else:
        state["risk_score"] = 1 - (true_count / total)

    return state
