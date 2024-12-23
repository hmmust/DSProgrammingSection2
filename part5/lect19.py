import json
students = [{"name":"Sarah Manasrah","age":20, "married":False},
         {"name":"Leen Mahdi","age":22, "married":False}]

fh = open("./part5/students.json",mode="w")
json.dump(students,fh)
fh.close()

