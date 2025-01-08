# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.

from collections import Counter

answer = input("Type in a phrase: ")
answer = answer.split(" ")
ans_count = Counter(answer)
max_count = ans_count.most_common(1)[0][0] #Indices at the end look at the set within the list and then the word within the set
print(max_count)
