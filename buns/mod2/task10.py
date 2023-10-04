user_input = input()
new_string = ""
last_letter = ""

for i in range (len(user_input)):
    if user_input[i] == " ":
        new_string += last_letter
        last_letter = ""
    else:
        last_letter = user_input[i]

new_string += last_letter
print(new_string)
