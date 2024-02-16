class acount:
    def __init__(self):
        balance=0
        print("acount created")
   # def deposit(self):
        self.ad=int(input("enter amount"))
        self.net=balance+self.ad
    #def withdrow(self):
        self.withdrowl=int(input("enter withdrowl amount"))
        if(self.net>=self.withdrowl):
            self.a=self.net-self.withdrowl
        else:
            print("insufficient ammount")
    def statement(self):
        print("create acount:")
        print("deposit amount:",self.ad)
        print("after deposit:",self.net)
        print("after withdrowl:",self.withdrowl)
        print("after withdrowl:",self.a)
s1=acount()
s1.statement()
        
    
