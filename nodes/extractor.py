from .llm import llm


def extract_claims(state):
    response = llm.invoke(
        f"""
        Extract factual claims from this text.
        Return as comma-separated list.

        Text:
        {state['answer']}
        """
    )

    claims = [c.strip() for c in response.content.split(",")]
    state["claims"] = claims
    return state
