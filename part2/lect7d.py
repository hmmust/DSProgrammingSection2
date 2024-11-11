import numpy as np
arr1 = np.array([10,20,30,40,25,30])
print(arr1[0])
print(arr1[0:2])
#print(arr1[[0,1,-2,-1]]) #advanced indexing
#print(arr1[[True,False,True,False,True,False]]) #filtering
#print(arr1 == 25)
print(arr1[arr1 == 25])
print(arr1[arr1 > 25])

print(np.where(arr1 > 25))
print(arr1[np.where(arr1 > 25)])
