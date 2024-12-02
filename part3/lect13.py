import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
students.sort_values(by=["Age","Name"],inplace=True,kind="heapsort")
students.sort_values(by=["Age","Name"],inplace=True,ascending=False)
students.reset_index(inplace=True)
students.set_index('Id',drop=True,inplace=True)
del students['index']
students.sort_index(axis=1,inplace=True)
students.sort_index(axis=0,inplace=True)

print(students)








