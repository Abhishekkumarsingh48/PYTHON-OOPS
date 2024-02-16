#Method Resolution order(MRO)
class a():
    pass
class b():
    pass
class c(a):
    pass
class d(b):
    pass
class e(c,d):
    pass
for i in e.mro():
    print(i)
