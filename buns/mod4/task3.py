def myFunc(a, b):
    if b == 0:
        return a
    else:
        return myFunc(b, a % b)