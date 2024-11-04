import numpy as np

arr1 = np.array([10,20,30,40])
print(arr1.ndim)
print(arr1.shape)
print(arr1[0]) # indexing
print(arr1[-1])
print(arr1[0:2]) #slicing
students = np.array([[15,20,25],
                    [17,22,30],
                    [19,23,27]])
print(students)
print(students.ndim)
print(students.shape)
print(students[0,]) #first row (student)
print(students[:,0]) #first colomn (first exam)
print(np.mean(students[:,0])) #average of first exam

print(students[1:,1:])
print(students[1:3,1:3])
