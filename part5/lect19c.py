import json

fh = open("./part5/students.json",mode="r")
students = json.load(fh)
fh.close()

for i,v in students.items():
    print(v)

