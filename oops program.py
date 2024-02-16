class student:
    def __init__(self):
        self.emp=int(input("enter number of employ"))
        self.ts=0
    def getdata(self):
        for i in range(self.emp+1):
            self.name=input("enter name")
            self.des=input("enter designation")
            self.salary=float(input("enter salary"))
            self.ts=self.ts+self.salary
        self.k=self.ts
    def average(self):
        self.avg=self.k/self.emp
    def display(self):
        print("total salary:",self.k)
        print("avreage salary:",self.avg)
s1=student()
s1.getdata()
s1.average()
s1.display()
        
