n = 100


def f(x, n):
    print(f"f's n is {n}")
    n = 10
    y = g(x)
    return x, y


def g(x):
    print(f"g's n is {n}")
    return x**2


print(f(2, 15))
