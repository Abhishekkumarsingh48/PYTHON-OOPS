class father:
    def __init__(self):
        print("father class const")
    def display(self):
        print("father class method")
class son:
    def __init__(self):
        print("son class const")
    def show(self):
        print("son class method")
class doug(son,father):
    def __init__(self):
        print("doughter class const")
    def see(self):
        print("doughter class method")
d=doug()
d.display()
d.see()

