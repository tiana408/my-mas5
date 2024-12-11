from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment and import any custom tools if needed
# from my_mas.tools.custom_tool import MyCustomTool
# from crewai_tools import SerperDevTool

@CrewBase
class MyMasCrew():
    """Multi-Agent System for Product Comparison"""

    @agent
    def analyst(self) -> Agent:
        """Creates the Analyst Agent for defining comparison framework"""
        return Agent(
            config=self.agents_config['analyst'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @agent
    def researcher(self) -> Agent:
        """Creates the Researcher Agent for data collection"""
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @agent
    def summary_agent(self) -> Agent:
        """Creates the Summary Agent for synthesizing findings"""
        return Agent(
            config=self.agents_config['summary_agent'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        """Creates the Reporting Analyst for generating insights and recommendations"""
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @task
    def analyst_task(self) -> Task:
        """Creates the Analyst Task for defining comparison framework"""
        return Task(
            config=self.tasks_config['analyst_task'],
        )

    @task
    def researcher_task(self) -> Task:
        """Creates the Researcher Task for collecting product data"""
        return Task(
            config=self.tasks_config['researcher_task'],
        )

    @task
    def summary_agent_task(self) -> Task:
        """Creates the Summary Agent Task for synthesizing findings"""
        return Task(
            config=self.tasks_config['summary_agent_task'],
        )

    @task
    def reporting_analyst_task(self) -> Task:
       """Creates the Reporting Analyst Task for generating final report"""
       return Task(
           config=self.tasks_config['reporting_analyst_task'],
           output_file='product_report.md'
       )




    @crew
    def crew(self) -> Crew:
        """Creates the Product Comparison Crew with sequential processing"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )