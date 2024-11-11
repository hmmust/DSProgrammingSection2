import numpy as np
arr1 = np.array([40,25,30])
arr2 = np.array([10,20,30])
arr1.sort() # inplace : sort the same array
arr5 = np.sort(arr1) # not inplace : sort & return
print(arr1)
for i in arr1:
    print(i)
arr3 = np.array([[10,20,30],[40,25,30]])
for i in np.nditer(arr3): # arr3.reshape(-1) 
    print(i) #[10,20,30,40,25,30]""

"""for i in arr3:
    for j in i:#i = row  [10 20 30]
        print(j) """    
"""for i in arr3.reshape(-1):
    print(i) #[10,20,30,40,25,30]""""""