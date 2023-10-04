user_input = input("Введите строку и символ через запятую: ")

repeat_symbols_count = 0
slicer = 0

for element in user_input:
    if element != ",":
        slicer += 1
    else:
        break

string = user_input[0:slicer:]
sym = user_input[slicer + 1:]

for symbol in string:
    if symbol == sym:
        repeat_symbols_count += 1
    else:
        break

print(repeat_symbols_count)