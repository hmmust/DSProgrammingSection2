import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
for i in students:
    print(i)
for i in students.itertuples():
    print(i.Id,i.Name,i.Major)

print(students['Name'].str.replace(" ","").str.lower())
students['Year'] = students['Id'].astype(str).str[0:4].astype(int)
print(students)

from numpy import random

print(students['Name'].str.split(" "))
students['FirstName'] = students['Name'].str.split(" ").str[0]
students['FamilyName'] = students['Name'].str.split(" ").str[1]
#del students['Name']

students['FirstName'] = [ i.split(' ')[0]  for i in students['Name']]
students['FamilyName'] = [ i.split(' ')[1]  for i in students['Name']]
students['Password'] = [ f'{i[0]}{random.randint(10000,99999)}'   
                        for i in students['Name']]

print(students)
print(students)
