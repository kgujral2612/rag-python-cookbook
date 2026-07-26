import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

connection_string = os.environ.get("CONNN_STR")

engine = create_engine(connection_string)

with engine.connect() as connection:
    query = """SELECT * from categories"""
    result = pd.read_sql(query, connection)
    print(result)
