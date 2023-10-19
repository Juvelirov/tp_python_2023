def palindrome(word):
    letter_count = {}
    for letter in word:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    odd_count = 0
    odd_letter = ''
    palindrome = ''

    for letter, count in letter_count.items():
        if count % 2 != 0:
            odd_count += 1
            odd_letter = letter

    if odd_count > 1:
        print("Невозможно составить палиндром")
        return


    for letter, count in letter_count.items():
        if letter == odd_letter:
            palindrome += letter * (count // 2)
        else:
            palindrome = letter * (count // 2) + palindrome + letter * (count // 2)

    if odd_letter:
        palindrome = palindrome[:len(palindrome) // 2] + odd_letter + palindrome[len(palindrome) // 2:]

    print("Палиндром:", palindrome)


word = input("Введите слово: ")
palindrome(word)
