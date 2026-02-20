from langgraph.graph import StateGraph, END

from state import FirewallState
from nodes.generator import generate_answer
from nodes.extractor import extract_claims
from nodes.verifier import verify_claims
from nodes.scorer import score_risk
from nodes.rewriter import rewrite_answer


def build_graph():

    builder = StateGraph(FirewallState)

    builder.add_node("generate", generate_answer)
    builder.add_node("extract", extract_claims)
    builder.add_node("verify", verify_claims)
    builder.add_node("score", score_risk)
    builder.add_node("rewrite", rewrite_answer)

    builder.set_entry_point("generate")

    builder.add_edge("generate", "extract")
    builder.add_edge("extract", "verify")
    builder.add_edge("verify", "score")

    def route(state):
        if state["risk_score"] > 0.3 and state["iteration"] < 2:
            return "rewrite"
        return END

    builder.add_conditional_edges("score", route)
    builder.add_edge("rewrite", "extract")

    return builder.compile()
