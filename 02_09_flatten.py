# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

## Extend method approach
flattened_list = []
for item in starter_list:
    flattened_list.extend(item)
print(flattened_list)

## List comprehension
flattened_list = []
[flattened_list.append(num) for item in starter_list for num in item]
print(flattened_list)

## Itertools Chain approach
from itertools import chain
flattened_list = []
flattened_list = list((chain.from_iterable(starter_list)))
print(flattened_list)