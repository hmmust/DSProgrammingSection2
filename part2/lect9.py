from numpy import random
import numpy as np
print(np.around(random.rand()*10)+20,3) # random float 20-30
print(random.rand(5))

print(random.randint(100))
print(random.randint(50,100,50))
print(random.randint(low=50,high=100,size=50))
print(random.randint(low=50,high=100,size=(3,3)))

marks= ['A','A-','B+','B-','C','C+','C-','D-','D','D+']
print(random.choice(marks))
print(random.choice(marks,size=25))
print(random.choice(marks,size=(3,3),
                    p=[0.05,0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1,0.05]))
#random.shuffle(marks)
marks_shuffled = random.permutation(marks)
print(marks)
print(marks_shuffled)
# given 5 employees in shop, generate schedule for 3-shifts in 5 days
employees = ['Ahmad','Omar','Nour','Sadeen','Nada']
shifts = random.choice(employees, size=(5,3),
                       p=[0.2,0.2,0.2,0.2,0.2])
print(shifts)