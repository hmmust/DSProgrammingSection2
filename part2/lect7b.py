import numpy as np

arr1 = np.array([10,20,30,40,25,30])
print(arr1.shape)
arr2 = arr1.reshape((2,3))
print(arr2)
arr3 = arr1.reshape((3,2))
print(arr3)
students = np.array([[15,20,25],
                    [17,22,30],
                    [19,23,27]])#,dtype=float)
print(students.reshape((9,1)))
print(students.reshape(-1))

