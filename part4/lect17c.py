import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,Binarizer,MinMaxScaler,StandardScaler,normalize

students = pd.read_csv("./part3/students.csv")
students['Major'].replace({"DSS":"DS"," SE":"SE"},inplace=True)
encoder = LabelEncoder()
students['Major_2'] = encoder.fit_transform(students.loc[:,['Major']])

binarizer = Binarizer(threshold=2.99)
students['GPA_vgood'] = binarizer.fit_transform(students.loc[:,['GPA']])

print(students)

