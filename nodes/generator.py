from .llm import llm


def generate_answer(state):
    response = llm.invoke(
        f"Answer the question factually:\n{state['question']}"
    )
    state["answer"] = response.content
    return state
