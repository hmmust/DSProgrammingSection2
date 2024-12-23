import json
sarah = {"name":"Sarah Manasrah","age":20, "married":False}
students = [{"name":"Sarah Manasrah","age":20, "married":False},
         {"name":"Leen Mahdi","age":22, "married":False}]
sarah_json = json.dumps(sarah)
print(sarah_json)
print(type(sarah_json))

students_json = json.dumps(students)
print(students_json)

