# LangGraph Agentic AI Chatbot

A powerful AI chatbot built with LangGraph and Streamlit, featuring Groq LLM integration for high-performance language model interactions.

## Features

- 🤖 Interactive chat interface using Streamlit
- 🚀 Powered by Groq's high-performance LLMs
- 🔄 LangGraph-based conversation flow
- 🔒 Secure API key management
- 🎯 Multiple use case support

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
USECASE_OPTIONS = Basic Chatbot
GROQ_MODEL_OPTIONS = llama2-70b, mixtral-8x7b, gemma-7b
```

2. Set up your Groq API key in the Streamlit interface

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
   - Start chatting!

## Project Structure

```
src/
├── langgraphagenticai/
│   ├── LLMS/
│   │   └── groqllm.py
│   ├── graph/
│   │   └── graph_builder.py
│   ├── nodes/
│   │   └── basic_chatbot_node.py
│   ├── state/
│   │   └── state.py
│   └── ui/
│       ├── streamlitui/
│       │   ├── display_result.py
│       │   └── loadui.py
│       └── uiconfigfile.ini
└── app.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
