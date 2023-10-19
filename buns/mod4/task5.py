filename = input("Введите имя файла: ")

with open(filename, "r") as file:
    content = file.read()

letter_counts = {}
for letter in content:
    if letter.isalpha():
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

results = sorted(letter_counts.items(), key=lambda x: x[1])

with open("result.txt", "w") as file:
    for letter, count in results:
        file.write(f"{letter}: {count}\n")

