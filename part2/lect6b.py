import numpy as np

arr1 = np.zeros(10) #np.ones(10)
print(arr1)
arr2 = np.zeros((5,6)) #np.ones((5,6))
arr2.fill(10)
print(arr2)
arr3 = np.eye(5)
print(arr3)
arr4= np.full((3,4),fill_value=10)
print(arr4)
arr5= np.full((4,4),fill_value=np.arange(1,5))
print(arr5)
