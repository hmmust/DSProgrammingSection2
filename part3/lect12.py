import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
print(students.head(2))
print(students.tail())
print(students.describe())
print(students.info())
print(students.columns)
print(students.dtypes)

print(students.count())
print(students['Age'].count())
print(students.loc[:,['Age','GPA']].count())
students['rank_gpa']= students['GPA'].rank()
students['rank_gpa']= students['GPA'].rank(method="dense")

print(students)
print(students['Age'].corr(students['GPA']))
#print(students['Name'].mean())
print(students['Age'].corr(students['Age']))

#print(students.median())




