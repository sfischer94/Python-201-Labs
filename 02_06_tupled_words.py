# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]


answer = input("Type in a phrase: ")
answer = answer.split()
result_list = []

# Iterate over each word and sub-iterate over each letter to add them to a temporary list
for item in answer:
    temp_list = []
    for letter in item:
        temp_list.append(letter)
    result_list.append(tuple(temp_list))

print(result_list)