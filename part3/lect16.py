import pandas as pd
import numpy as np
students = pd.read_csv('./part3/students.csv',
                       names=["student_id","fullname",
                              "major","age","year","gpa"],header=0,
                       dtype={'age':np.int16,'year':np.int16})

students['major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
students['major']=pd.Categorical(students['major'])
print(students["major"].cat.categories)
print(students["major"].cat.codes)
print(students.dtypes)

d = ["A","C","C","D","D","E"]
cd = pd.DataFrame(pd.Categorical(d,['A','B','C','D']),columns=['mark'])

print(cd['mark'])