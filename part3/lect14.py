import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
print(students.info())
print(students['Year'].value_counts(dropna=False))
d_students=students.dropna(axis=0) #axis=1,inplace=True
#print(d_students)
#students['Year1']= students['Year'].fillna(2000)
#students['Year2']= students['Year'].fillna(method='pad')
#students['Year3']= students['Year'].fillna(method='backfill')
#students['Year4']= students['Year'].fillna(students['Year'].median())
students['Year']= students['Id'].astype(str).str[0:4].astype(np.int16)
students['Major'] = students['Major'].str.strip()
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
print(students['Major'].value_counts(dropna=False))
students['Id']= students['Id'].astype(np.int16)
print(students.dtypes)




