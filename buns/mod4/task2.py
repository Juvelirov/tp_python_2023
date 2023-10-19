def recurs(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    elif n % 2 == 0:
        return recurs(a * a, n / 2)
    else:
        return a * recurs(a, n - 1)
