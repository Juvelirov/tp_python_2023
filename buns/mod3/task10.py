length = int(input("Размерность: "))
matrix = [[i for i in range(1,length+1)] for j in range(0,length*length,length)]
print("Исходная:")
for row in matrix:
    print(*row, sep=", ")

for i in range(length):
    for j in range(i+1,length):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("Транспонированная:")
for row in matrix:
    print(*row, sep=", ")