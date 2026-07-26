from pathlib import Path
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# The OpeAI client looks for the OPENAI_API_KEY variable
client = OpenAI()
embedding_model = "text-embedding-3-small"

"""
chunk_text chunks text at natural boundaries such as paragraphs (ends with a \n\n)
or setences (ends with a .) with overlap to preserve context across chunks
"""
def chunk_text(text, size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        if end < len(text):
            bp = text.rfind("\n\n", start, end)
            if bp == -1:
                bp = text.rfind(".", start, end)
            if bp > start:
                end = bp + 1
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        start = end - overlap if end < len(text) and end - overlap > start else end
    return chunks

"""
embed_and_store generates and stores embeddings in a local persistent chromadb store.
"""
def embed_and_store(chunks, db_path, collection_name):
    chroma = chromadb.PersistentClient(path=str(db_path))
    collection = chroma.get_or_create_collection(
        name= collection_name,
        metadata = {"description": "Harry Potter Knowledge Base"}
    )

    embeddings = []

    for i in range(0, len(chunks), 100):
        batch = chunks[i: i + 100]
        res = client.embeddings.create(model=embedding_model, input=batch)
        embeddings.extend([x.embedding for x in res.data])

    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[{"chunk_index": i} for i in range(len(chunks))],
    )

    return collection

"""
retrieve finds relevant chunks for a given question
"""
def retrieve(question, top_k=3):
    q_emb = client.embeddings.create(
        model=embedding_model,
        input=question
    ).data[0].embedding

    res = collection.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=["documents"],
    )

    return res["documents"][0]

"""
answer geerates an answer to the question by feeding the retrieved documents and question to the LLM
"""
def answer(question, docs):
    context = "\n\n---\n\n".join(docs)
    prompt = f"""Answer the question using only the context below.

Context: 
{context}

Question:
{question}

Answer:"""
    res = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content":prompt}],
    )
    return res.choices[0].message.content


file_path = Path("../datasets/text_files/harry_potter_knowledge_base.txt")
text = file_path.read_text(encoding="utf-8")
chunks = chunk_text(text, 500)

chroma_db_dir = Path("chroma_db")
collection = embed_and_store(chunks, chroma_db_dir, "harry_potter_kb")

question = "Why did Ucle Vernon take the family to the hut by the sea?"
docs = retrieve(question)

answer_text = answer(question, docs)

print(f"Question: {question}\nAnswer: {answer_text}")