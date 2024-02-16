class student:
    def __init__(self):
        self.name=input("enter name")
        self.roll=int(input("enter roll"))
        self.hin=int(input("enter"))
        self.eng=int(input("enter"))
        self.sansk=int(input("enter"))
    def display(self):
        print("name and roll:",self.name,self.roll)
class marks:
    def __init__(self):
        def show(self):
            print("per:",self.per)
            if(self.per>=30):
                print("pass")
            else:
                print("fail")
class result(student,marks):
    def __init__(self):
        super(marks,self).__init__()
        super(student,self).__init__()
        self.mark=(self.hin+self.eng+self.sansk)
        self.per=self.mark/3
    def seen(self):
        print("percentage=",self.per)
        

s1=result()
a=marks()
b=student()
s1.seen()
        
        
        
