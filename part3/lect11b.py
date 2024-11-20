import pandas as pd
import numpy as np

data1 = [{'name':'Ahmad','age':22},{'name':'Sadeen','age':20}]
data2 = {'name':pd.Series(['Sara','Leen','Diala','Osama']),
         'age': pd.Series([20,19,21,18],dtype=np.float32),
         }
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.concat([df1,df2],ignore_index=True)
#df3.reset_index(drop=True,inplace=True)
df3.drop([2,5],inplace=True)
df3.reset_index(drop=True,inplace=True)
#del df3['age']
#df3.pop('age')
df3['bithyear']=2024-df3['age']
df3['married']=True
df3['married']=np.random.choice(['A','B','C'],len(df3))
print(df3)
print(df3[['age','married']])
print(df3[0:2])
print(df3.loc[0:2, ['age','married']])
print(df3.iloc[0:2,0:2])
print(df3[(df3['age']>20)&(df3['name'].str[0]=='D')])








