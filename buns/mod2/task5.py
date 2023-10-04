slice = 0

def shift_symbols(char, shift_count_x):
    symbols = 'abcdefghijklmnopqrstuvwxyz'

    index = symbols.index(char)
    shift_index = index + shift_count_x
    shift_char = symbols[shift_index]

    return shift_char


user_input = input("Введите символ и число: ")

for item in user_input:
    if item != ",":
        slice += 1
    else:
        break

char = user_input[0:slice:]
shift_count_x = int(user_input[slice + 1:])
shift_char = shift_symbols(char, shift_count_x)
print(shift_char)