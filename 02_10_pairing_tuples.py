# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

# Write your code below here
random_list = sorted(randlist)
print(random_list)

## Approach 1: Use nested loops to add item pairs to a list and convert them into tuples to add to a new list
"""
new_list = []
for count, item in enumerate(random_list):
    # If index is even number, add the item and next item (or 0) to a temp list. 
    # Convert to tuple and add to the new list.
    # Uses exception handling and nested loops
    if count % 2 == 0:
        temp_list = []
        temp_list.append(item)
        try:
            temp_list.append(random_list[count+1])
        except IndexError:
            temp_list.append(0)
        new_list.append(tuple(temp_list))
    else:
        pass

[print(i) for i in new_list]"""

## Approach 2: Use itertools batched method
from itertools import batched

if len(random_list) % 2 != 0:
    random_list.append(0)
new_list = list(batched(random_list, 2))
print(new_list)

