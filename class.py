'''class xyz:
    x=10
x1=xyz()
print(x1.x)
print(xyz.x)
print(xyz)'''

'''
class xyz():
    def __init__(a,name,roll):#first argumet is here takes as self
        a.name="RAM"
        a.roll=1
s1=xyz('a',5)
print(s1.name)
print(s1.roll)
'''

class myclass:
    a=10
    def func(self):
        return "using self"
ob=myclass()
print(ob.func())
print(myclass.func(ob))















