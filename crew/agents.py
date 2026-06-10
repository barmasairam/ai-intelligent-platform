from crewai import Agent, LLM

llm = LLM(model="ollama/phi3")

insight_agent = Agent(
    role="Business Analyst",
    goal="Explain data and predictions clearly",
    backstory="Expert in analyzing business data and providing simple insights.",
    llm=llm
)