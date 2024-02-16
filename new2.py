class abc:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name)
    def __str__(self):
       return(self.name)
    def __repr__(self):
        return(self.age)
a1=abc("ak",12)
print(a1)
    
