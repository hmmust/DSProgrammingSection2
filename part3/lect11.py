import pandas as pd
import numpy as np

data1 = pd.Series(["Sara","Leen","Diala","Osama"])
data2 = [{'name':'Ahmad','age':22},{'name':'Sadeen','age':20}]
data3 = {'name':pd.Series(['Sara','Leen','Diala','Osama'],index=['a','b','c','g']),
         'age': pd.Series([20,19,21,18],dtype=np.float32,index=['a','b','f','d']),
         'rank':np.random.choice(['A','B','C'],size=4)
         #'age': np.array([20,19,21,18])
         }
data3 = {'name':pd.Series(['Sara','Leen','Diala','Osama']),
         'age': pd.Series([20,19,21,18],dtype=np.float32),
         'rank':np.random.choice(['A','B','C'],size=4)
         #'age': np.array([20,19,21,18])
         }
df1 = pd.DataFrame(data1,columns=["name"])
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3,index=['a','b','c','h'])
print(df1)
print(df2)
print(df3)


