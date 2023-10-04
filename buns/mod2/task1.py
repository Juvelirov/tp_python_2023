digits = input("Введите числа в формате a, b: ")
placeIndex = 0

for symbol in digits:
    if symbol != ",":
        placeIndex += 1
    else:
        break

a = int(digits[0:placeIndex:])
b = int(digits[placeIndex + 2:])

print(a % b)