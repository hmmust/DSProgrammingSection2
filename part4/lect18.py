import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,Binarizer,MinMaxScaler,StandardScaler,normalize

students = pd.read_csv("./part3/students.csv")
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)

binarizer = Binarizer(threshold=2.99)
students['GPA_vgood'] = binarizer.fit_transform(students.loc[:,['GPA']])

mm_scaler = MinMaxScaler(feature_range=(0,1))
students['GPA_mm']= mm_scaler.fit_transform(students.loc[:,['GPA']])
s_scaler = StandardScaler()
students['GPA_sc']= s_scaler.fit_transform(students.loc[:,['GPA']])
students['GPA_l1']= normalize(students.loc[:,['GPA']],norm="l1",axis=0)
students['GPA_l2']= normalize(students.loc[:,['GPA']],norm="l2",axis=0)
print(students)

