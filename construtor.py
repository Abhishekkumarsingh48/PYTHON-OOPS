class student():
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name
        self.marks=[]
    def setmarks(self):
        self.name=input("enter name")
        self.roll=int(input("enter roll"))
        m=input("enter marks of three subject")
        marks=[int(i) for i in m]
        self.marks=marks
    def compute(self):
        sum1=0
        for m1 in self.marks:
            sum1=sum1+m1
        print("total marks")
    def display(self):
        print("name:",self.name)
        print("roll:",self.roll)
        print("total marks:",self.sum1)
s1=student('a',4)
s1.display()
