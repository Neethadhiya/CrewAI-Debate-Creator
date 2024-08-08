from crewai import Agent, Task, Crew, Process
from tools import yt_tool
from agents import gandhi, hitler
from tasks import gandhi, hitler

crew = Crew(
    agents=[gandhi, hitler],
    tasks=[gandhi, hitler],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew = True,
    verbose=2
)
result = crew.kickoff(inputs={'debate_topic': 'The Ethics of Leadership During Times of Crisis'})
print(result)
