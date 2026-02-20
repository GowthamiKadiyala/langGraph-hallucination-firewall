from .llm import llm


def rewrite_answer(state):
    state["iteration"] += 1

    response = llm.invoke(
        f"""
        The previous answer had hallucinations.
        Rewrite it carefully and only include well-known verified facts.

        Question:
        {state['question']}
        """
    )

    state["answer"] = response.content
    return state
