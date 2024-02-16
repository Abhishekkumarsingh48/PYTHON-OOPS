class a:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def display(self):
        print(self.__salary)
e1=a("akb",10000)
e1.display()
print(e1.name)
print(e1._a__salary)#for acces private variable we use object._classname__variable
