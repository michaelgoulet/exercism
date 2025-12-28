SQUARE_MAX = 64
SQUARE_MIN = 1

def square(number):
    if (number < SQUARE_MIN) | (number > SQUARE_MAX):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    i = SQUARE_MIN
    total_grains = 0
    while i <= SQUARE_MAX:
        total_grains = total_grains + square(i)
        i+=1
    return total_grains