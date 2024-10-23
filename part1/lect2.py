courses = ("DS Programming","ProgrammingI","Data  Structures","Database")
"""print(type(courses))
for n in courses:
    print(n)
print(*courses)"""

courses_iter= iter(courses)
while True:
    try:
        print(next(courses_iter))
    except:
        break
