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
    def show(self):
        print(self.money)
class doug(son):
    def __init__(self):
        self.money=1000
        print("doughter class const")
    def see(self):
        print(self.money)
d=doug()
d.display()
d.show()
d.see()
