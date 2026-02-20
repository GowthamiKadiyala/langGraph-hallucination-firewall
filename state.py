from typing import TypedDict, List


class FirewallState(TypedDict):
    question: str
    answer: str
    claims: List[str]
    verified_claims: List[bool]
    risk_score: float
    iteration: int
