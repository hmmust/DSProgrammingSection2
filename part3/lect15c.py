import pandas as pd
import numpy as np
def update_major(m): # m ="CS" or "DSS" str
    m = m.strip()
    m = m.replace("DSS","DS")
    return m

students = pd.read_csv('./part3/students.csv')
students['Year']= students['Id'].astype(str).str[0:4].astype(np.int16)

students['Major'] = students['Major'].apply(update_major)

students['Id']= students['Id'].astype(np.int16)
print(students)