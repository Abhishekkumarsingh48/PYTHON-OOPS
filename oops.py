class per:
    def setdata(self,name,age):
        self.name=name
        self.age=age
    def getdata(self):
        print("name:",self.name)
        print("age:",self.age)
p=per()
q=per()
r=per()
p.setdata("abc",21)
q.setdata("wir",32)
p.getdata()
q.getdata()
