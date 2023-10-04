user_input = input()
vowels = "аеёиоуыэюя"
vowel_count = 0
consonant_count = 0

for letter in user_input:
    if letter == " ":
        continue
    elif letter.lower() in vowels:
        vowel_count += 1
    else:
        consonant_count += 1

print(vowel_count, consonant_count)