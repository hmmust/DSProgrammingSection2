students = ['Sara Mansrah','Ayman Jamal','Osama Jarrar','Taleb Jarrar']
students_first= [ s.split(" ")[0].lower() for s in students]
students_emails= [ s+"@uop.edu.jo" for s in students_first]
students_emails= [ f"{s}@uop.edu.jo" for s in students_first]
print(students_emails)

grades=[50,49,90,85,74]
grades_succ= len([ m for m in grades if m>=50])/len(grades)
print(grades_succ)

students_emails_d= { s:f"{s}@uop.edu.jo" for s in students_first}
print(students_emails_d['sara'])