# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

from collections import Counter
my_list = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

counting = Counter(my_list)
unique_list = []
for item, count in counting.items():
    if count == 1:
        unique_list.append(item)
print(unique_list)

## List comprehension method
# unique_list = [item for item, count in counting.items() if count == 1]
