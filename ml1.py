class father:
    def __init__(self):
        self.money=2000
        print("father class const")
    def display(self):
        print("father class method")
        print(self.money)
class son(father):
    def __init__(self):
        self.money=5000
        print("son class const")
    def display(self):
        print(self.money)
        print("hi")
class doug(son):
    def __init__(self):
        self.money=1000
        print("doughter class const")
    def disp(self):
        print(self.money)
y=doug()
y.display()
