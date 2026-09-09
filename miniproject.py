name = input("Enter the your name :")
mail = input("Enter the your Email :")
city = input("Enter your City :")

name = name.strip()
mail = mail.strip()
city = city.strip()

name = name.title()
city = city.upper()


if '@' not in mail:
    mail = mail + "@gamail.com"

elif not mail.endswith("@gmail.com"):
    print("Invalid Email")
    

print("\n")

print("======================================")
print(" \t Student Profile")
print("======================================")

print(f"\n Name \t:{name} \nE-mail \t:{mail} \nCity \t:{city}")

print("\n======================================")
