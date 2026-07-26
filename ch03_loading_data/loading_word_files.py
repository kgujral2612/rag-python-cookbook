from unstructured.partition.docx import partition_docx
import pandas as pd


file_path = "../datasets/word_files/2023_Jan_7_Feature_Engineering_Techniques.docx"

elements = partition_docx(filename=file_path)

list_of_elements = []

for element in elements:
    element_dict = {
        "element_id": element.id,
        "category": element.category,
        "text": element.text,
        "last_modified": element.metadata.last_modified 
    }
    list_of_elements.append(element_dict)

elements_df = pd.DataFrame(list_of_elements)

print(elements_df)
