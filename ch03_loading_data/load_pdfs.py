import PyPDF2
import pandas as pd

file_path = "../datasets/pdf_files/AI_in_Factories_Discussion_Cleaned.pdf"

with open(file_path, "rb") as file: 
    reader = PyPDF2.PdfReader(file)

    list_of_pages = []
    page_counter = 1

    for page in reader.pages:
        page_dict = {
            "file_name": reader.metadata.get("/Title"),
            "producer": reader.metadata.get("/Producer"),
            "page_number": page_counter,
            "images": page.images
        }
        list_of_pages.append(page_dict)

        page_counter += 1

pages_df = pd.DataFrame(list_of_pages)

print(pages_df)