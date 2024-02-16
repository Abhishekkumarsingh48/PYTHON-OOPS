class person:
    def __init__(obj,name,age):
        obj.name=name
        obj.age=age
    def func(abc):
        print("hello my name is "+abc.name,+abc.age)
p1=person("abhishek",24)
p1.func()
