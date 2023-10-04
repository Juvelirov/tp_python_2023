digits = input("")
flag = False

for num1 in range(0, len(digits), 2):
    for num2 in range(0, len(digits), 2):
        if digits[num1] == digits[num2 + 2]:
            print(True)
            flag = True
            break
        else:
            print(False)
            flag = True
            break
    if flag:
        break