from pathlib import Path
from agents.orchestrator import get_orchestrator
from agents.code_generator import get_code_generator
from agents.executor import get_executor
from agents.documenter import get_documenter
from agno.team import Team
from agno.tools.file import FileTools

def main():
    print("--- Agno Claude-Alt Terminal Application ---")
    print("Type 'exit' or 'quit' to end the session.\n")
    
    # Initialize individual agents
    orchestrator = get_orchestrator()
    code_gen = get_code_generator()
    executor = get_executor()
    documenter = get_documenter()
    
    # Create the Team coordination
    # We use the Team class for multi-agent orchestration
    agent_team = Team(
        members=[orchestrator, code_gen, executor, documenter],
        model=orchestrator.model, # Use the same reasoning engine
        # Add FileTools to the team level so the manager can also see files if needed
        tools=[FileTools(base_dir=Path("."))],
        instructions=[
            "You are the leader of a multi-agent system designed for local file operations.",
            "1. If a task requires exploring the directory, reading files, or planning, delegate to the 'Orchestrator'.",
            "2. If a task requires writing or updating Python code, delegate to the 'Code Generator'.",
            "3. If a task requires running, testing, or fixing code, delegate to the 'Executor'.",
            "4. If a task requires documentation or summaries, delegate to the 'Documenter'.",
            "5. After the members have responded, summarize the outcome and provide a final recommendation.",
            "Always ensure you use the best member for the job. You can also use FileTools directly to explore the environment."
        ],
        markdown=True,
        show_members_responses=True,
    )

    while True:
        try:
            user_input = input("User: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            if not user_input.strip():
                continue

            # Run the team logic
            # The 'run' method will use the team of agents to fulfill the request
            agent_team.print_response(user_input, stream=True)
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()

