from crewai import Task
from crew.agents import insight_agent

def create_insight_task(data):

    return Task(
        description=f"""
Analyze this data:

{data}

Give simple business insight in 2 lines.
""",
        agent=insight_agent,
        expected_output="Insight"
    )