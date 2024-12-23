import multiprocessing
import time
#print(multiprocessing.cpu_count())
def printHi(n):
    for i in range(n):
        time.sleep(0.5)
        print(f"hi{n}")
if __name__ == "__main__":
    p1= multiprocessing.Process(target=printHi,args=(5,))
    p2= multiprocessing.Process(target=printHi,args=(7,))
    p3= multiprocessing.Process(target=printHi,args=(10,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print('done!')
  