from graph import build_graph

graph = build_graph()

initial_state = {
    "question": "When was Tesla founded and by whom?",
    "answer": "",
    "claims": [],
    "verified_claims": [],
    "risk_score": 0.0,
    "iteration": 0
}

result = graph.invoke(initial_state)

print("\nFinal Answer:")
print(result["answer"])
print("\nRisk Score:", result["risk_score"])
print("Iterations:", result["iteration"])
