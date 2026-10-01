from typing import TypedDict, List, Dict


class AgentState(TypedDict, total=False):

    # User input
    user_input: str

    # Routing
    route: str

    # RAG
    answer: str
    retrieved_documents: List[dict]

    # Study planner
    subjects: List[str]
    exam_dates: Dict[str, str]
    study_hours: float
    study_plan: str
