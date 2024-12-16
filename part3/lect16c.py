import pandas as pd
import numpy as np
import datetime

dt1 = datetime.datetime(2024,10,15,8,0,0)
dt2 = datetime.datetime(2024,10,15,16,0,0)

ts = pd.date_range('12/11/2024',periods=5, freq='D')
ts = pd.date_range(dt1,periods=8, freq='H')
ts = pd.date_range(dt1,dt2,periods=10)

#df = pd.DataFrame(ts)
#print(df)
print(ts)

periods=8