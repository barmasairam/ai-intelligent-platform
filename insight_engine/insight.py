from crewai import Crew, Process
from crew.tasks import create_insight_task

def generate_insight(data):

    task = create_insight_task(data)

    crew = Crew(
        agents=[task.agent],
        tasks=[task],
        process=Process.sequential
    )

    return crew.kickoff()