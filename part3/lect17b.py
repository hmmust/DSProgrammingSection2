import pandas as pd
import numpy as np
import datetime

students = pd.read_csv("./part3/students.csv")
dt1 = datetime.datetime(2024,12,16,8,0,0)
td1 = pd.Timedelta(minutes=20)
dr1= pd.date_range(dt1,periods=len(students),freq=td1)
students['appoitment'] = dr1
students['appoitment'] = students['appoitment'] + pd.Timedelta(hours=1)
print(students)

