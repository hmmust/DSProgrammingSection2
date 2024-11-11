import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = arr1.copy()
arr1[0]=20
print(arr1,arr2)

arr3 = arr1.view()
arr1[0]=25
print(arr1,arr3)
print(arr1.base,arr2.base,arr3.base)


students = np.array([[15,20,25],
                    [17,22,30],
                    [19,23,27]])#,dtype=float)
