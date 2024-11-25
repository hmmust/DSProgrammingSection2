import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')

print(students['Age'].corr(students['GPA']))
print(students['Age'].corr(students['Age']))

print(students[ students['Age'] >20 ])
print(students[ ~(students['Age'] >20) ])
print(students[ (students['Age'] >20) & (students['GPA']>3) ])
print(students[  students['Major'].isin([' SE','IS'])])

print(students.query("Age > 20 and GPA>3"))
print(students.loc[ (students['Age'] >20) & (students['GPA']>3),['Name'] ])







