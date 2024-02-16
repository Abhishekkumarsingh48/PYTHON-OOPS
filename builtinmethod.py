class cmp:
    def __init__(self,a):
        self.a=a
    def __ge__(self,obj):
        return self.a>=obj.a
s1=cmp(5)
s2=cmp(5)
print(s1>=s2)
