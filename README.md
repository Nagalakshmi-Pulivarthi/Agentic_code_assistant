# Agentic_Code_Assistant-Multi-Agent Local Development Assistant


Agentic_Code_Assistantis a sophisticated multi-agent system built using the [Agno](https://docs.agno.com/) framework. It serves as a local development assistant capable of exploring your filesystem, writing code, executing tests, and generating documentation through a coordinated team of AI agents.

## 🚀 Features

- **Multi-Agent Coordination**: Uses a specialized `Team` of agents with a dedicated Orchestrator.
- **Local File Operations**: Read, write, and explore your local directory safely.
- **Code Execution**: Run and test Python scripts directly from the terminal.
- **Technical Documentation**: Automatically generate project summaries and READMEs.
- **Flexible AI Models**: Integrated with OpenRouter to support various LLMs (defaults to GPT-4o-mini).

## 🛠️ Project Structure

- `main.py`: The entry point and team manager.
- `agents/`: Contains the specialized agent definitions.
  - `orchestrator.py`: Plans and delegates tasks.
  - `code_generator.py`: Writes and modifies Python code.
  - `executor.py`: Runs and tests code using PythonTools.
  - `documenter.py`: Generates technical documentation.
- `utils/`: Configuration and helper modules.
- `requirements.txt`: Project dependencies.

## ⚙️ Setup

### 1. Prerequisites
- Python 3.8+
- An [OpenRouter](https://openrouter.ai/) API key.

### 2. Installation
Clone the repository and install the dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory and add your API key:
```text
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

## 📖 Usage

Run the main application:
```bash
python main.py
```

### Example Commands
Once the terminal is active, you can interact with the team:
- **Explore**: "List all files in the agents folder."
- **Develop**: "Create a python script that calculates the area of a circle."
- **Test**: "Run the fibonacci.py script and tell me the output."
- **Document**: "Generate a summary of the orchestrator's role."

## 🤖 Meet the Team

| Agent | Role | Tools |
| :--- | :--- | :--- |
| **Orchestrator** | Intent classification and planning | `FileTools` |
| **Code Generator** | Expert Python development | `FileTools` |
| **Executor** | Code execution and debugging | `PythonTools` |
| **Documenter** | Technical writing and summarization | `FileTools` |

## ⚖️ License
MIT



