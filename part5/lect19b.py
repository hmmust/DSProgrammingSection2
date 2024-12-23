import json
student_json= '[{"name": "Sarah Manasrah", "age": 20, "married": false}, {"name": "Leen Mahdi", "age": 22, "married": false}]'

students = json.loads(student_json)
print(type(students))
for i in students:
    print(i['name'])

