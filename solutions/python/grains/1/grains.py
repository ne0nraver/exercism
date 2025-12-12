def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    a = 2**(number-1)
    return a

def total():
    s = 2**64 - 1
    return s
