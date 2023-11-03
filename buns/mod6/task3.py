def check():
    for num in range(10, 100000):
        order = len(str(num))
        sum = 0
        elem = num
        while elem > 0:
            digit = elem % 10
            sum += digit ** order
            elem //= 10
        if num == sum:
            yield num

example = check()
def get_check():
    return next(example)

for i in range(8):
    print(get_check(), end=' ')