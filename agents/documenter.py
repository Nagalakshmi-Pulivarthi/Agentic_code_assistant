from pathlib import Path
from agno.agent import Agent
from utils.config import get_model
from agno.tools.file import FileTools

def get_documenter():
    """Returns the Document/Summary Agent."""
    return Agent(
        name="Documenter",
        model=get_model(),
        role="Technical Writer and Documentation Expert",
        tools=[FileTools(base_dir=Path("."))],
        description="You create READMEs, file summaries, and technical explanations.",
        instructions=[
            "1. You are a specialist in the DOC_GEN and FS_EXPLORE buckets.",
            "2. When the Orchestrator assigns you a task in a 'Handoff Packet', use FileTools to read the code context.",
            "3. Generate clear and concise documentation, README files, or file summaries as requested.",
            "4. Use FileTools to save the generated documentation if appropriate."
        ],
        markdown=True
    )
 
    
