import pandas as pd
def read_student(filename):
    students= pd.DataFrame()
    df = pd.read_csv(filename,chunksize=1)
    for d in df:
        #print(d)
        students = pd.concat([students, d],axis=0, ignore_index=True)
    return students

print(read_student('./part6/students1.csv'))