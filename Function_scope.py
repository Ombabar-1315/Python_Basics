def student_info(*subject , **details):
    print("Subject: ")
    count = 0
    for sub in subject:
        count += 1
        print(sub)

    print()
    print("Total Subject: ",count)
    print()
    for key , value in details.items():
        print(key ,":", value)




student_info(
    "Python",
    "C++",
    "DBMS",
    name="Om",
    age=20,
    marks=94
)
    