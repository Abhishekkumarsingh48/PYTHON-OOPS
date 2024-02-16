class employ:
    def __init__(self):
        self.empname=input("enter name")
        self.empid=input("enter empid")
        self.salary=int(input("enter salary"))
        
    def display(self):
        self.salary1=self.salary+(self.salary*20)/100
        print("empname:",self.empname)
        print("empid:",self.empid)
        print("empsalary:",self.salary)
        print("after permotion salary:",self.salary1)
s1=employ()
s1.display()
