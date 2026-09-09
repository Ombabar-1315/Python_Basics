name = input("Enter Full Name        :")
age = int(input("Enter Age           :"))
city = input("Enter City             :")
mail = input("Enter Email            :")
lang = input("Enter fav langauge     :")
phone = int(input("Enter phone number   :"))

name = name.strip()

city = city.strip()
mail = mail.strip()
lang = lang.strip()


name = name.title()
city = city.upper()
lang = lang.lower()


##Email validation




## Name Analysis



print("\nReport Generation in Progress ...")

print("\n===========================================")



n= 3
while n > 0:
    print(n)
    n -=1

print("Report ready !")


print("===========================================")
print(" \t STUDENT REPORT ")
print("===========================================")

print(f"\n Name     \t:{name}")
print(f"\nAge       \t:{age}")
## age analysis
if age <= 18:
    status ="Minor Student"
else:
    status="Adult Student"
print(f"\nCategory \t:{status}")

print(f"\nCity     \t:{city}")

print(f"\nEmail   \t:{mail}") 

if "@" in mail:
    p= "Valid"
else:
    p ="Invalid"

print(f"\nEmail Status  \t:{p}")

if lang == "python":
    print(f"\nLanguage \t:{lang} \t: Excellent choice")
else:
    print(f"\nLanguage \t:{lang} \t: Good choice")
print("\nPhone last 4 digit \t: ",str(phone)[-4:])

print("\n\n")



print("Name Length     :",len(name))
print("\nFirst Letter  :",name[0])
print("\nLast Letter   :",name[-1])
print("\nFirst 3 Letters:",name[:3])
print("\nLast 3 Letters :",name[-3:])

letter = input("\nEnter one letter: ")
if letter in name:
    print("Letter found in name")
else:
    print("Letter not found in name")
print()
letter = input("Enter one letter : ")
print(name.count(letter),"times found in name")

print("\n======================================")


