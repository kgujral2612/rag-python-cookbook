import os
from unstructured.partition.pdf import partition_pdf
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

pdf_file_path = "../datasets/pdf_files/adult_data_article.pdf"

tables = []
texts = []

# Partition the PDF file into its elements
raw_pdf_elements = partition_pdf(
    filename=pdf_file_path,
    strategy="hi_res",
)

for element in raw_pdf_elements:
    if "unstructured.documents.elements.Table" in str(type(element)):
        tables.append(str(element))


def summarize_tables(row):
    print("Summariziing row...")
    summary_prompt = (
        f"You are an assistant tasked with summarizing tables. "
        f"Give a concise summary of the table. "
        f"Table chunk: {row.table}"
    )

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": summary_prompt}],
        max_completion_tokens=150
    )

    row["table_summary"] = response.choices[0].message.content

    return row

tables_df = pd.DataFrame(tables, columns=["table"])

tables_df = tables_df.apply(summarize_tables, axis=1)

print(tables_df)