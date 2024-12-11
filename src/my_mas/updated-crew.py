from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class MyMas():
    """MyMas crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['summary_agent'],
            verbose=True
        )

    @agent
    def reporting_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_agent'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['summary_task'],
        )

    @task
    def report_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_generation_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.researcher, self.summary_agent, self.reporting_agent],
            tasks=[self.research_task, self.summary_task, self.report_generation_task],
            process=Process.sequential,
            verbose=True
        )