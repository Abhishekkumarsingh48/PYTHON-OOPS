class frut():   # we use __ for private the variable and without private variable value can be change by object
    def __init__(self):
        self.max=900
    def sell(self):
        print("sell:",self.max)
    def setmax(self,price):
        self.max=price
s1=frut()
s1.sell()
s1__max=1000 
s1.sell()
s1.setmax(1200)
s1.sell()
