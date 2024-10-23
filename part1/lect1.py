'''
Write a Python program to define list of 
students information:id,name,marks(fist/second)
the program will define method to generate
email/total marks
'''
def generate_new_information(students):
    result = []
    for s in students:
        email= f"{s[0]}@uop.edu.jo"
        #print(s[2][0]+s[2][1])
        totalmark = sum(s[2])
        result.append([email,totalmark])
        return result
    
information  = [[20201,"Omar",[12,15]],
                [20202,"Ahmad",[20,12]],
                [20203,"Qusai",[13,18]]]

r = generate_new_information(information)
print(r)