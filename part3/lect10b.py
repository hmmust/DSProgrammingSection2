import pandas as pd
import numpy as np

data1 = [["Sara",20],["Leen",19],["Diala",21],["Osama",22]]
data2 = np.array([[21,22],[23,25],[25,23],[30,28]])

df1 = pd.DataFrame(data1,columns=["name","age"])
print(df1)
df2 = pd.DataFrame(data2,columns=["first","second"])
df2['total']= df2['first']+df2['second']
print(df2)
df1['total'] = df2['total']
print(df1)