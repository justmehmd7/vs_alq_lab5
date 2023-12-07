import math

def f(x):
    return math.exp(x) - 1/x - 1

def x(a, b, e):
    if f(a) * f(b) >= 0:
        print("Verilen aralıkta kök yok.")
        return None

    while (b - a) >= e:
        c = (a + b) / 2  
        if f(c) == 0:
            return c
        elif f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

a = 0.5
b = 1.0
e = 0.01 

root = x(a, b, e)

if root is not None:
    print("Kök:", root)
