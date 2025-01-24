# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

answer_dict = {}
for letter, number in dict_1.items():
    if letter in dict_2:
        answer_dict[letter] = dict_1[letter] + dict_2[letter]
    else:
        answer_dict[letter] = dict_1[letter]
for letter, number in dict_2.items():
    if letter not in dict_1:
        answer_dict[letter] = dict_2[letter]
print(answer_dict)