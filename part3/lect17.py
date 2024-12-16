import pandas as pd
import numpy as np
import datetime

dt1 = datetime.datetime(2024,10,15,8,0,0)
dt3 = datetime.datetime.now()
td1 = pd.Timedelta(days=15,hours=12)
td1 = pd.Timedelta('15 days 12 hours')

print(dt3 - td1)
print(dt3 + td1)
dr1= pd.date_range(dt3,periods=5,freq=td1)
print(dr1)
print(type(dt3-dt1))


