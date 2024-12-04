import pandas as pd
import numpy as np

students = pd.read_csv('./part3/students.csv')
students_courses = pd.read_csv('./part3/students_courses.csv')
stds= pd.merge(students,students_courses, on=['Id'])
stds= pd.merge(students,students_courses, on=['Id'],how='left')
stds= pd.merge(students,students_courses, on=['Id'],how='right')
stds= pd.merge(students,students_courses, on=['Id'],how='outer')
print(stds)