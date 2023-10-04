barcode = input("Введите штрих код: ")
even_num = 0
odd_num = 0

for odd_num in range(0, len(barcode), 2):
    odd_num += int(barcode[odd_num])

for even_num in range(1, len(barcode), 2):
    even_num += int(barcode[even_num]) * 3

if (even_num + odd_num) % 10 == 0:
    print("yes")
else:
    print("no")