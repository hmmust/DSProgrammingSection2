import pandas as pd
import numpy as np
import datetime

dt1 = datetime.datetime(2024,10,15,8,0,0)
dt_now = datetime.datetime.now()

print(dt1)
print(dt1.year)
print(dt_now.strftime("%H.%M"))
print(dt_now.strftime("%d/%m/%Y")) 