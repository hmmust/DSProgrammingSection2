students = ['Sara Mansrah','Ayman Jamal','Osama Ahmad','Taleb Jarrar']

get_firtname= lambda name: name.split(" ")[0].lower()

print(sorted(students,key=lambda name: name.split(" ")[1]))