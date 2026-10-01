from langchain_google_genai import ChatGoogleGenerativeAI


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


def study_planner_node(state):

    subjects = state.get("subjects", [])
    exam_dates = state.get("exam_dates", {})
    study_hours = state.get("study_hours", 0)

    prompt = f"""
You are a college study planning assistant.

Create a realistic study timetable.

Subjects:
{subjects}

Exam dates:
{exam_dates}

Available study hours per day:
{study_hours}

Requirements:
- Give appropriate time to each subject.
- Prioritize exams that are closer.
- Include revision.
- Include reasonable breaks.
- Do not exceed the available study hours.

Return the timetable in a clear format.
"""

    response = llm.invoke(prompt)

    state["study_plan"] = response.content
    state["answer"] = response.content

    return state
