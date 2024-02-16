class a:
    def __init__(self):
        print("parent class constructer")
    def abc(self):
        print("parent class method")
class b(a):
     def __init__(self):
    #super().__init__(a,b):
        print("child class constructer")
     def abd(self):
        print("child class method")
s1=b()
s1.abc()
s1.abd()
s2=a()
