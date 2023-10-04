digit = int(input("Число: "))
def make_repres_digit(digit, digit_system):
    num = ""

    if digit_system != 16:
        while digit > 0:
            remainder = digit % digit_system
            num = str(remainder) + num
            digit //= digit_system

    else:
        while digit > 0:
            remainder = digit % digit_system
            if remainder < 10:
                num = str(remainder) + num
            else:
                if remainder == 10:
                    num += "A"
                elif remainder == 11:
                    num += "B"
                elif remainder == 12:
                    num += "C"
                elif remainder == 13:
                    num += "D"
                elif remainder == 14:
                    num += "E"
                elif remainder == 15:
                    num += "F"
            digit //= digit_system

    return num


binSys = make_repres_digit(digit, 2)
octSys = make_repres_digit(digit, 8)
hexSys = make_repres_digit(digit, 16)

if digit < 1:
    print("Введите положительное ненулевое число!")
else:
    print(binSys, octSys, hexSys, sep=", ")