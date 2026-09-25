username = "admin"
password = "python123"


class LoginError(Exception):
    pass

try:
    i = 0
   

    while(i < 3):
        name = input("Enter username:")
        pas = input("Enter Password: ")
        
        if name == username and pas == password:
            print("Login Successfull:")
            break
        else:
            i +=1 
            print("❌ Invalid username or password. Please try again.")

        if i == 3:

           raise LoginError("❌ Account temporarily locked.")



except LoginError as e:
    print(e)    