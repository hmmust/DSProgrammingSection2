import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
students['Year']= students['Id'].astype(str).str[0:4].astype(np.int16)
students['Major'] = students['Major'].str.strip()
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
students['Id']= students['Id'].astype(np.int16)
# Generate the highest (max) GPA of each major and year  
print(students.groupby(['Major','Year'])[['GPA']].max())
#print(students.groupby(['Year','Major'])[['GPA']].max())
# Generate average Age of each year
print(students.groupby(['Year'])[['Age']].agg('mean'))
print(students.groupby(['Year'])[['Age']].mean())








