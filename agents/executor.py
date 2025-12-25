from agno.agent import Agent
from utils.config import get_model
from agno.tools.python import PythonTools

def get_executor():
    """Returns the Executor Agent."""
    return Agent(
        name="Executor",
        model=get_model(),
        role="Python Execution and Testing Specialist",
        tools=[PythonTools()],
        description="You handle running code, testing functionality, and fixing bugs.",
        instructions=[
            "1. You are a specialist in the CODE_RUN and CODE_FIX buckets.",
            "2. When the Orchestrator assigns you a task in a 'Handoff Packet', use PythonTools to execute the code or run tests.",
            "3. If there are runtime errors, analyze the output and provide recommendations for fixes.",
            "4. Summarize the execution results, including any output or errors encountered."
        ],
        markdown=True
    )

