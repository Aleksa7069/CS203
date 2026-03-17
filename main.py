# Github test

def decorator_function(orignial_function):
    def wrapper(a, b):
        a += 1
        b += 1
        return orignial_function(a, b)
    return wrapper

@decorator_function
def zameni(a,b):
    a += 1
    b += 1
    temp = a;
    a = b
    b = temp
    return a,b

c = 3
d = 4
c, d = zameni(c,d)
print(c, d)