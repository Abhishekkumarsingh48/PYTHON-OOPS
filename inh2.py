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
    def disp(self):
        print(self.money)
s=son()
f=father()
s.display()
#f.display()
