# LangGraph Agentic AI Chatbot

A powerful AI chatbot built with LangGraph and Streamlit, featuring Groq LLM integration for high-performance language model interactions.

## Features & Functionalities

- **Interactive Chat Interface**: Built with Streamlit, providing a modern, user-friendly chat experience.
- **Groq LLM Integration**: Supports high-performance language models via Groq, with selectable models and secure API key management.
- **LangGraph-Based Orchestration**: Uses LangGraph to manage conversation flow and state, supporting modular graph-based chatbot logic.
- **Multiple Use Cases**:
  - **Basic Chatbot**: Standard conversational AI using only the LLM.
  - **Chatbot With Web**: Enhanced chatbot with access to external tools for web search and knowledge retrieval.
- **Tool Integration**: The chatbot can leverage external tools for richer responses:
  - **Arxiv Search**: Retrieves academic papers from Arxiv.
  - **Tavily Web Search**: Performs general web searches.
- **Dynamic Graph Construction**: The conversation graph is built dynamically based on the selected use case, with nodes for chat and tool invocation.
- **State Management**: Maintains conversation state using a typed dictionary structure.
- **Configurable UI**: Sidebar options for LLM selection, model choice, use case, and API keys (Groq, Tavily).

## Main Tools & Modules

- **LLMS/groqllm.py**: Handles Groq LLM initialization and model selection.
- **graph/graph_builder.py**: Builds the conversation graph, supporting both basic and tool-augmented chatbots.
- **nodes/basic_chatbot_node.py**: Implements the basic chatbot node logic.
- **nodes/chatbot_with_Tool_node.py**: Implements the chatbot node with tool integration.
- **tools/search_tool.py**: Provides access to Arxiv, Wikipedia, and Tavily search tools, and creates tool nodes for the graph.
- **state/state.py**: Defines the structure for maintaining conversation state.
- **ui/streamlitui/loadui.py**: Loads and configures the Streamlit UI, including sidebar controls.
- **ui/streamlitui/display_result.py**: Handles displaying chat and tool results in the UI.
- **ui/uiconfigfile.py & uiconfigfile.ini**: Manage and store UI configuration options.

## Example Use Cases

- **Basic Chatbot**: For general conversation and Q&A.
- **Chatbot With Web**: For enhanced answers using real-time web, Wikipedia, and Arxiv search.

## Prerequisites

- Python 3.8+
- Groq API key
- Streamlit

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Agentic-Chatbot.git
cd Agentic-Chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Place your `uiconfigfile.ini` in the `src/langgraphagenticai/ui/` directory with the following structure:
```ini
[DEFAULT]
PAGE_TITLE = LangGraph Agentic AI
LLM_OPTIONS = Groq
USECASE_OPTIONS = Basic Chatbot, Chatbot With Web
GROQ_MODEL_OPTIONS = llama-3.1-8b-instant, llama-3.3-70b-versatile, gemma2-9b-it
```

2. Set up your Groq API key in the Streamlit interface. For the "Chatbot With Web" use case, you will also need a Tavily API key.

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (typically http://localhost:8501)

3. In the Streamlit interface:
   - Select your preferred Groq model
   - Enter your Groq API key
   - Choose the use case
   - (If using web tools) Enter your Tavily API key
   - Start chatting!

## Project Structure

```
src/
├── langgraphagenticai/
│   ├── LLMS/                # LLM integrations (Groq)
│   ├── graph/               # Graph construction and orchestration
│   ├── nodes/               # Chatbot node logic (basic, with tools)
│   ├── state/               # State management
│   ├── tools/               # External tool integrations
│   └── ui/                  # Streamlit UI and configuration
└── __init__.py
```

## About

The `Agentic Chatbot` project is designed to be modular, extensible, and easy to use for both end-users and developers. It leverages the latest in LLM and graph-based orchestration technology to provide a robust conversational AI platform. The codebase is organized for clarity, with each major functionality in its own module or directory.

## Troubleshooting

- **Dependency Issues:** Ensure all packages in `requirements.txt` are installed. Use a virtual environment to avoid conflicts.
- **API Key Errors:** Double-check that your Groq and Tavily API keys are correct and set in the UI.
- **Streamlit Not Launching:** Make sure you are running the command from the project root and that `app.py` exists.
- **Merge Conflicts or Git Issues:** If you encounter git errors, ensure your branch is up to date with the remote and resolve any conflicts as needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Groq](https://groq.com/)
- [Streamlit](https://streamlit.io/)
- [Tavily](https://tavily.com/)
- [arXiv](https://arxiv.org/)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for suggestions and improvements.