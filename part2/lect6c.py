import numpy as np

arr1 = np.array([10,20,30,40])
print(type(arr1))
print(arr1.dtype)
arr1 = arr1.astype(float) #arr1.astype('f') 
print(arr1)
arr2 = arr1.astype(bool) #arr1.astype('b') 
print(arr2)

students = np.array([[15,20,25],
                    [17,22,30],
                    [19,23,27]])#,dtype=float)
print(students.astype(float))

print(np.zeros((3,3),dtype=bool))
print(np.eye(3,dtype=bool))

