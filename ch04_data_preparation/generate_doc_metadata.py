import os
from pprint import pprint
import PyPDF2
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

FILE_PATH = "../datasets/pdf_files/attention_is_all_you_need_paper.pdf"
text=""

with open(FILE_PATH, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    metadata = reader.metadata

    for page in reader.pages:
        text += page.extract_text()

metadata_ext = dict(metadata)
metadata_ext["page_count"] = len(reader.pages)
metadata_ext["file_size"] = os.path.getsize(FILE_PATH)
metadata_ext["file_name"] = os.path.basename(FILE_PATH)
metadata_ext["file_path"] = FILE_PATH
metadata_ext["text_length"] = len(text)

print("Metadata without LLM is")
pprint(metadata_ext)

class AuthorContact(BaseModel):
    """A pydantic dataclass for storing an author contact."""
    name: str
    company: str
    email: list[str]


class Contacts(BaseModel):
    """A pydantic dataclass for storing a list of author contacts."""
    entries: list[AuthorContact]


client = OpenAI()

response = client.beta.chat.completions.parse(
    model="gpt-5-mini",
    messages=[
        {
            "role": "system",
            "content": "Extract the contact information of all authors."
        },
        {
            "role": "user",
            "content": text,
        }
    ],
    response_format=Contacts,
)

author_contacts = response.choices[0].message.parsed

metadata_ext_llm = dict(metadata_ext)
metadata_ext_llm["author_contacts"] = author_contacts

print("Metadata with LLM is")
pprint(metadata_ext_llm)
