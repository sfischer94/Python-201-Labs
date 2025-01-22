# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

squared = {}
for i in range(1,11):
    squared[i] = i*i
print(squared)

# Formatted in List Comprehension:
# [squared[i] == i*i for i in range(1,11)]