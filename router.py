def router(state):

    query = state["user_input"].lower()

    study_keywords = [
        "study plan",
        "study timetable",
        "study schedule",
        "timetable",
        "schedule",
        "exam preparation",
        "prepare for exam"
    ]

    if any(keyword in query for keyword in study_keywords):
        state["route"] = "study_planner"
    else:
        state["route"] = "rag"

    return state
