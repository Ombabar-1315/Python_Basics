class Subscription:

    platform = "StreamBox"
    active_users = 0

    def __init__(self,username,plan,price,status=True):
        self.username = username
        self.plan = plan
        self.price = price
        self.status = status
        Subscription.active_users += 1
        

    def upgrade(self,new_plan,new_price):
        self.plan = new_plan
        self.price = new_price
        return

    def cancel(self):
        if self.status == True:
            self.status = False
            Subscription.active_users -= 1
            return "Subscription Cancelled"
        else:
            
            return "Already cancel."

    def show_subscription(self):
        s = ""
        print("Username: ",self.username)
        print("Plan: ",self.plan)
        print("Price: ",self.price)
        print("Platform: ",self.platform)
        if self.status == True:
            s = "Active"
        else:
            s = "Diactive"
        print("Status: ",s)

    @classmethod
    def change_platform(cls,platform):
        cls.platform = platform

    @classmethod
    def show_active_user(cls):
      print(cls.active_users)
           
    
    
s1 = Subscription("Om","Premium",1500)
s2 = Subscription("Rudra","Regular",300)
print("=====================================")
s1.show_subscription()
print("-------------------------")
s2.upgrade("Premium",10000)
s2.show_subscription()
print("======================================")
print()

Subscription.change_platform("Netflix")
s3 = Subscription("Zaid","regular",300)
s3.cancel()
s3.show_subscription()
Subscription.show_active_user()



