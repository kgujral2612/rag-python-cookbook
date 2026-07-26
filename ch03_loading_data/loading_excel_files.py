import pandas as pd

file_path = "../datasets/tabular_files/census-income.xlsx"
df_excel = pd.read_excel(io=file_path)

def create_text_description_of_row(row):
    row["text_description"] = (
        f"""The candidate {row['age']} years old is working in the {row['workclass']} sector.
        The candidate was born in {row['native-country']}, is {row['marital-status']}
        and has a {row['relationship']} relationship.
        The candidate has a {row['education']} degree and is working as a {row['occupation']}.
        The income of the candidate is {row['income']}.
        """
    )
    return row

df_extended = df_excel.apply(create_text_description_of_row, axis=1)

print(df_extended)