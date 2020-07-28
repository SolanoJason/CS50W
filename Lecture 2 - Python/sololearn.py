def cube(x):
    return x**3


def square(x):
    return x**2


def cube_2(func, x):
    return func(x)


print(cube_2(cube, cube_2(cube, 2)))
