import pandas as pd

students_df = pd.read_json('./part5/students.json')
print(students_df.info())
students_df['major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)

students_df.to_json("./part5/students_cleaned.json",orient="records")

