class vehicle:
    def __init__(self):
        self.name=input("enter name")
        self.max_speed=int(input("enter max_speed"))
        self.milage=int(input("enter milage"))
class bus(vehicle):
    def __init__(self):
        super(). __init__()
    def display(self):
        print(self.name)
        print(self.max_speed)
        print(self.milage)
s=bus()
s.display()
        
