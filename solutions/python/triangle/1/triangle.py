def isTriangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    is_triangle = True
    if (a == 0) | (b == 0 ) | (c==0):
        is_triangle = False
    
    if (a + b < c) | (b + c < a) | (a + c < b):
        is_triangle = False
            
    return is_triangle


def equilateral(sides):
    is_equilateral = False
    if (sides[0] != 0):
        if (sides[0] == sides[1]) & (sides[0] == sides[2]):
            is_equilateral = True

    return is_equilateral


def isosceles(sides):
    is_isosceles = False
    if (isTriangle(sides)):
        if ((sides[0] == sides[1]) | (sides[0] == sides[2]) | (sides[1] == sides[2])):
            is_isosceles = True
    return is_isosceles


def scalene(sides):
    a=sides[0]
    b=sides[1]
    c=sides[2]
    is_scalene = True
    if isTriangle(sides):
        if (a == b) | (b==c) | (a==c):
            is_scalene = False
    else:
        is_scalene = False
    return is_scalene
