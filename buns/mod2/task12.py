def cleaner(phone_number):
    cleaned_number = ''
    for char in phone_number:
        if char in '0123456789+':
            cleaned_number += char
    return cleaned_number

user_input = input("Введите номер телефона: ")

cleaned_phone_number = cleaner(user_input)
print(cleaned_phone_number)