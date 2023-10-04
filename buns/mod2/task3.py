numbers = input("Введите три числа в формате a b c: ")

length_a = 0
length_b = 0
space = 0

for symbol in numbers:
    if symbol == " ":
        space += 1
    if space == 0:
        length_a += 1
    elif space == 1:
        length_b += 1

a = int(numbers[0:length_a:])
b = int(numbers[length_a + 1:length_a + length_b:])
c = int(numbers[length_a + length_b + 1:])

if(a <= 1000 and b <= 1000 and c <= 1000 and a >= -1000 and b >= -1000 and c >= -1000):
    if (a > b):
        if (c > a): print(a)
        elif (c > b): print(c)
        else:print(b)
    elif(c > b):print(b)
    else:
        if (a > c):print(a)
        else:print(c)
else: print('Введите числа из допустимого диапазона!')
