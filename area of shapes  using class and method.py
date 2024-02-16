class shape:
    def __init__(self):
        self.l=float(input("enter length"))
        self.b=float(input("enter breadth"))
    def area(self):
        if(self.l==self.b):
            print("area of square:",self.l**2)
        else:
            print("area of rectangle:",self.l*self.b)
    def peri(self):
        if(self.l==self.b):
            print("perimeter of square:",self.l*4)
        else:
            print(
    self.sa=self.l**2
        self.ra=self.l*self.b
        self.ps=4*self.l
        self.pr=2*(self.l*self.b)
    def display(self):
        print("area of square:",self.sa)
        print("arae of rectangle:",self.ra)
        print("perimeter of square:",self.ps)
        print("perimeter of rectangle",self.pr)
s1=shape()
s1.display()
