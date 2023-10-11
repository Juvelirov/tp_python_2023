a = float(input("Введите число в десятичной СС: "))
print(bin(int(a))[2:], oct(int(a))[2:], hex(int(a))[2:]) if a > 0 and a % 1 == 0 else print("Неверный ввод")