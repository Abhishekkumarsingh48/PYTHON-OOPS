class student:
    def __init__(self):
        self.name=input("enter name")
        self.roll=int(input("enter roll"))
    def display(self):
        print("name and roll:",self.name,self.roll)
class marks(student):
    def __init__(self):
        super().__init__()
        '''self.hin=hin
        self.eng=eng
        self.sansk=sansk
        self.marks=(self.hin+self.eng+self.sansk)'''
    def show(self):
        print("percent=",self.name,self.roll)
'''class result(marks,student):
    def __init__(self):
        self.per=self.marks/3
    def seen(self):
        print("percentage=",self.per)
        if(self.per>=30):
            print("pass")
        else:
            print("fail")'''

s1=marks()
s1.show()
        
        
        
