# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

phrase = input("Type in something: ")
phrase_dict = {}
for char in phrase:
    if char in phrase_dict:
        phrase_dict[char] += 1
    elif char == " ":
        pass
    else:
        phrase_dict[char] = 1

print(phrase_dict)

