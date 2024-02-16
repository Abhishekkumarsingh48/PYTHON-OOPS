''' write a program that has a class polygon.drive two classes rectangle and triangle from polygon
and write method to get details of their dimension and hence calculate the are'''
class polygon():
    def __init__(self,sides):
        self.sides=sides
    def get_dimension(self):
        dimension=[]
        for i in range(self.sides):
            dimension=float(input("dimention"))
            dimension.append(domension)
        return dimension
class rectangle(polygon):
    def __init__(self):
        super(). __init__(4)
    def calculate(self):
        dimensions=self.get_dimension
        length,breadth=dimension[0]
        area =length*breadth
        return area
class triangle(polygon):
    def __init__(self):
        super().__init__(3)
    def calculate_area(self):
        print("print area of triangle:",self.ta)
s1=triangle
s2=rectangle
s1.display()
s2.display()
                   
        
