class SmartDoor:
    def __init__(self,location,owner,password,_is_locked = True):
        self.location = location
        self.owner = owner
        self.__password = password
        self._is_locked = _is_locked


    def unlock(self,password):
        if password == self.__password:
            self._is_locked = False
        else:
            print("Incorrect Password .")

    def lock(self):
        self._is_locked = True

    def show_status(self):
        print("Location: ",self.location)
        print("Owner: ",self.owner)
        print("Status: ",self._is_locked)


s1 = SmartDoor("Pune","Om","Abc@123")
s1.show_status()

s1.unlock("Abc@123")

s1.lock()
s1.show_status()

    

        