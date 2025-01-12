import pandas as pd
import multiprocessing
import requests
def read_student(filename):
    get_result = requests.get(filename)
    if get_result:
        students= pd.DataFrame(get_result.json())
        return students
    else:
        return pd.DataFrame()
if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=2)
    df1 = pool.apply_async(read_student,args=('https://raw.githubusercontent.com/hmmust/DSProgrammingSection2/refs/heads/main/part6/students1.json',))
    df2 = pool.apply_async(read_student,args=('https://raw.githubusercontent.com/hmmust/DSProgrammingSection2/refs/heads/main/part6/students2.json',))
    pool.close()
    pool.join()
    students = pd.concat([df1.get(),df2.get()],axis=0,ignore_index=True)
    print(students)