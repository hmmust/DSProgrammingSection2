import numpy as np
arr1 = np.array([10,20,30,40,25,30])
arr2 = np.array([20,25,35,31,27,12])
arr3 = np.concatenate((arr1,arr2))
print(arr3)
students = np.array([[15,20,25],
                    [17,22,30]])#,dtype=float)
students2 = np.array([[17,21,27],
                    [5,22,5]])#,dtype=float)
students3 = np.concatenate((students,students2),axis=1) #0 rows, 1 cols
print(students3)

students4 = np.hstack((students,students2)) # vstack
print(students4)