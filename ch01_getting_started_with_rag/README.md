# Harry Potter RAG System

This project creates a RAG system that answers questions about Harry Potter. 

### Project Structure
```text
ch01_getting_started_with_rag
├── datasets/              # Harry Potter Knowledge Base source text files
├── main.py                # Source code
└── README.md              # Project documentation
```

### Getting Started

```bash
# Install required packages
pip install openai
pip install chromadb
pip install python-dotenv

# Create venv
python3 -m venv .venv

# Activate venv
. ./.venv/bin/activate
```

Create a `.env` file and add the OpenAI API key.
You can find that from the [OpenAI Platform API Keys Page](https://platform.openai.com/settings/organization/api-keys)
```
OPENAI_API_KEY=your_openai_api_key_here
```

Run the code with:
```shell
python3 main.py
```
