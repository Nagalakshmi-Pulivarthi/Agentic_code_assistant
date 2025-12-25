from pathlib import Path
from agno.agent import Agent
from utils.config import get_model
from agno.tools.file import FileTools

def get_code_generator():
    """Returns the Code Generator Agent."""
    return Agent(
        name="Code Generator",
        model=get_model(),
        role="Expert Python Developer",
        tools=[FileTools(base_dir=Path("."))],
        description="You specialize in writing and updating high-quality Python code.",
        instructions=[
            "1. You are a specialist in the CODE_EDIT bucket.",
            "2. When the Orchestrator assigns you a task in a 'Handoff Packet', use FileTools to write or update the necessary Python files.",
            "3. Ensure the code is idiomatic, well-commented, and follows PEP 8.",
            "4. After writing the code, summarize the changes you made to the file(s)."
        ],
        markdown=True
    )

