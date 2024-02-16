class circle():#class
    pi=3.14 #class variable
    def __init__(self,radius): #constructor
        self.radius=4
        #self.radius=int(input("enter radius"))
        self.area=(circle.pi)*(self.radius**2)
        self.circum=2*(circle.pi)*(self.radius)
    def display(self):
        print("area:",self.area)
        print("circum:",self.circum)
c1=circle(4)
c1.display()
    
    
    
