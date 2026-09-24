students ={
        "Name":"om",
        "Age" : 19,
        "Marks":94
    }


import os
import json

if os.path.exists("students.json"):
    print("File Exist")

else:
    print("Not Exists")

with open("students.json","w") as file:
    json.dump(students,file,indent=3)