import pandas as pd
import multiprocessing
def read_student(filename):
    students= pd.DataFrame()
    df = pd.read_csv(filename,chunksize=1)
    for d in df:
        #print(d)
        students = pd.concat([students, d],axis=0, ignore_index=True)
    return students
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=2)
    df1 = pool.apply_async(read_student,args=('./part6/students1.csv',))
    df2 = pool.apply_async(read_student,args=('./part6/students2.csv',))
    pool.close()
    pool.join()
    students = pd.concat([df1.get(),df2.get()],axis=0,ignore_index=True)
    print(students)