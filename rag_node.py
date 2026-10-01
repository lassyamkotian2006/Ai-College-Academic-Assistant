from rag.rag_pipeline import ask_rag


def rag_node(state):

    question = state["user_input"]

    answer, sources = ask_rag(question)

    state["answer"] = answer
    state["retrieved_documents"] = sources

    return state
