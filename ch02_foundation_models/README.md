# Running Open Source Models Locally with Ollama

Running language models locally may be useful in the below cases:
- Your data is too sensitive to send to external providers
- Self-hosting is more cost-effective at the application's API call volume

[Ollama](https://ollama.com/) is a free, open-source platform that provides the capability to run langauge models locally.
It runs a small local server in the background. The server loads the model, performs inference, and exposes an API on `localhost:11434` that can be called from inside our Python source code. 

### Prerequisites
- Install Ollama runtime: follow the istructions on the [Download Ollama Page](https://ollama.com/download). Run `ollama --version` to confirm that the download was successful. The Ollama server should be started in the background. 
- Download a language model: this can be done via `ollama pull` commands. A full list is available at the [Ollama Models web page](https://ollama.com/search).

### Ollama & local models: quick start
- Download a model: `ollama pull <model-name>`
- Download and start chatting `ollama run <model-name>`
- List downloaded models `ollama list`
- Delete a model: `ollama rm <model-name>`
- Show active models in memory: `ollama ps`
- View model metadata/license: `ollama show <model-name>`

### Getting Started

```bash
# Install required packages
pip install openai
```

Run the code with:
```shell
python3 local_model.py

python3 compare_local_models.py
```