from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CodeBuilder():
    """CodeBuilder crew - collects requirements, builds, tests, saves and runs code"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def requirement_collector(self) -> Agent:
        return Agent(
            config=self.agents_config["requirement_collector"],  # type: ignore[index]
            verbose=True
        )

    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config["developer"],  # type: ignore[index]
            verbose=True
        )

    @agent
    def tester(self) -> Agent:
        return Agent(
            config=self.agents_config["tester"],  # type: ignore[index]
            verbose=True
        )

    @agent
    def file_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["file_manager"],  # type: ignore[index]
            verbose=True
        )

    @agent
    def runner(self) -> Agent:
        return Agent(
            config=self.agents_config["runner"],  # type: ignore[index]
            verbose=True
        )

    @task
    def collect_requirements(self) -> Task:
        return Task(
            config=self.tasks_config["collect_requirements"],  # type: ignore[index]
        )

    @task
    def generate_code(self) -> Task:
        return Task(
            config=self.tasks_config["generate_code"],  # type: ignore[index]
        )

    @task
    def test_code(self) -> Task:
        return Task(
            config=self.tasks_config["test_code"],  # type: ignore[index]
        )

    @task
    def save_code(self) -> Task:
        return Task(
            config=self.tasks_config["save_code"],  # type: ignore[index]
        )

    @task
    def run_code(self) -> Task:
        return Task(
            config=self.tasks_config["run_code"],  # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates and connects all agents and tasks for CodeBuilder"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
