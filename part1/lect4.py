students = ['Sara Mansrah','Ayman Jamal','Osama Ahmad','Taleb Jarrar']
student_users= list( map( lambda s: s.lower().replace(" ",".")  , students) )
print(student_users)

students = {'Sara':2004,'Ayman':2001,'Osama':2000,'Taleb':2005}
"""for s  in students.items():
    print(s)"""
    
student_ages= dict( map( lambda s: (s[0], 2024-s[1]) , students.items()) )
print(student_ages)

old_students = dict(filter( lambda s: s[1]>21 , student_ages.items() ))
print(old_students)

student_sorted1= dict( reversed( sorted(student_ages.items(), key=lambda s: s[1] ) ))
print(student_sorted1)

student_sorted2= dict( sorted(student_ages.items(), key=lambda s: s[0][-1] ) )
print(student_sorted2)

