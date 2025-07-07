#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from .crew import CodeBuilder


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the project generation crew.
    """
    topic = input("Enter project topic: ")
    language = input("Enter programming language: ")
    extra = input("Any preferences or features? ")
    save_path = input("Enter file save path (e.g., /home/user/code.py): ")

    inputs = {
        "topic": topic,
        "language": language,
        "extra": extra,
        "path": save_path,
        "current_year": str(datetime.now().year)
    }

    try:
        CodeBuilder().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        "language": "Python",
        "extra": "Simple print program",
        "path": "/tmp/output.py",
        "current_year": str(datetime.now().year)
    }

    try:
        CodeBuilder().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CodeBuilder().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "language": "Python",
        "extra": "Just print Hello",
        "path": "/tmp/output.py",
        "current_year": str(datetime.now().year)
    }

    try:
        CodeBuilder().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
