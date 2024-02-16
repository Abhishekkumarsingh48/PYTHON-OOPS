class emp:
    def __new__(cls):
        print("__new__magic method is called")
        inst=object.__new__(cls)
        return inst
    def __init__(self):
        print("__init__magic method is called")
        self.name='python'
    def display(self):
        print(self.name)
s1=emp()
