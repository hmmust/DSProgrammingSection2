import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
students['Year']= students['Id'].astype(str).str[0:4].astype(np.int16)
students['Major'] = students['Major'].str.strip()
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
students['Id']= students['Id'].astype(np.int16)
print(students.groupby(['Major'])[['Major','GPA']]) 
print(students.groupby(['Major'])[['GPA']].count()) 
print(students.groupby(['Major'])[['GPA']].mean()) 

print(students.groupby(['Major','Year'])[['GPA']].count()) 
print(students.groupby(['Major']).groups) 






