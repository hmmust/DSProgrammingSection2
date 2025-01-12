from typing import Union
from fastapi import FastAPI
import pandas as pd
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/students/{Id}")
def read_item(Id: int):
    students_df = pd.read_csv("../part6/student1.csv")
    return  students_df[students_df['Id']== Id]