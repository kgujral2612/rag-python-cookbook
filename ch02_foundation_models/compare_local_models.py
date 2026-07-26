from openai import OpenAI

models = ['mistral', 'qwen3:4b']

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key="ollama",
)

for model in models:
    print(f"\n\n---Testing {model}--- \n")
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is retrieval augmented generation?"},
        ],
    )
    print(response.choices[0].message.content)