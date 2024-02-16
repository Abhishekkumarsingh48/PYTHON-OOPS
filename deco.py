def deco_hello(fun):
    def inner():
        c=fun()
        return c + " How are you"
    return inner
@deco_hello
def fun():
    return "Hello!"
print(fun())
