from .llm import llm


def verify_claims(state):
    results = []

    for claim in state["claims"]:
        response = llm.invoke(
            f"""
            Is the following claim factually correct?
            Answer only TRUE or FALSE.

            Claim: {claim}
            """
        )

        results.append("TRUE" in response.content.upper())

    state["verified_claims"] = results
    return state
