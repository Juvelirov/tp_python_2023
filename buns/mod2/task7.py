digit = input("Введите число: ")
zero_counter = 0
one_counter = 0

for symbol in digit: 
    if symbol == '0':
        zero_counter += 1
    elif symbol == '1':
        one_counter += 1

if zero_counter == one_counter: 
    print('yes')
else:
    print('no')