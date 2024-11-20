import pandas as pd
import numpy as np

data1 = ["Sara","Leen","Diala","Osama"]
data2 = np.array([21,23,25,30])
data2 = np.random.randint(0,100,(4))
data3= {20201:15,20202:17,20203:18,20204:18}

ser1 = pd.Series(data1)
ser1 = pd.Series(data1,index=[10,20,30,40])
print(ser1)
#print(ser1[30])
ser2 = pd.Series(data2,index=["sara","leen","diala","osama"])
print(ser2)
print(ser2['sara'])
ser3 = pd.Series(data3,dtype=np.float64)
ser3 = ser3.astype(np.float16)
print(ser3)
print(ser3.iloc[0])
print(ser3[20203])
print(ser3[[20203,20204]])
print(ser3[-1:])
print(ser3[0:2])
print(ser3[ser3>17])
print(ser3.where(ser3>17))
print(ser3.dtype,ser3.size, ser3.empty)
print(ser3.head(n=2),ser3.tail(n=2))
print(ser3.value_counts())






