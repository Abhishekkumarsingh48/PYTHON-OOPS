#Method Resolution order(MRO)
class a():
    pass
class b():
    pass
class c:
    pass
class x(a,b):
    pass
class y(b,c):
    pass
class z(x,y,c):
    pass
for i in z.mro():
    print(i)
