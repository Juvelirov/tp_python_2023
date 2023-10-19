list = []

while True:
    num = input("Введите число (или 'STOP' для окончания ввода): ")
    if num == "STOP":
        break
    list.append(int(num)) # добавляю введенное число в список

if len(set(list)) == 1:
    print("Все числа равны")
elif len(set(list)) == len(list):
    print("Все числа разные")
else:
    print("Есть равные и неравные числа")