import numpy as np
arr1 = np.array([40,25,30])
arr2 = np.array([10,20,30])
print(arr1+arr2)
print(np.add(arr1,arr2))
print(arr1*arr2)
print(np.multiply(arr1,arr2))
arr3 = np.array([[10,20,30],[40,25,30]])
arr4 = np.array([[1,2,3]])
print(arr3+arr4)
print(arr3+5) #broadcasting

arr1 = np.array([40,25.455,30,40])
arr2 = np.array([10,20.101,30,40])
print(np.trunc(arr1))
print(np.around(arr1,2))
print(np.ceil(arr1))

print(np.unique(arr1))
print(np.intersect1d(arr1,arr2))
print(np.union1d(arr1,arr2))

