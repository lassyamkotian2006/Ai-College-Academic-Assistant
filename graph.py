from langgraph.graph import StateGraph, START, END

from state import AgentState
from router import router
from rag_node import rag_node
from study_planner import study_planner_node


builder = StateGraph(AgentState)


# Add nodes
builder.add_node("router", router)
builder.add_node("rag", rag_node)
builder.add_node("study_planner", study_planner_node)


# START → Router
builder.add_edge(START, "router")


# Router decides where to go
builder.add_conditional_edges(
    "router",
    lambda state: state["route"],
    {
        "rag": "rag",
        "study_planner": "study_planner"
    }
)


# Both paths finish
builder.add_edge("rag", END)
builder.add_edge("study_planner", END)


graph = builder.compile()
