# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

## Convert to different data type
no_dupes = set(list_)
print(no_dupes)

## Use a loop by appending to a new list
new_list = []
for num in list_:
    if num not in new_list:
        new_list.append(num)
    else:
        pass
print(new_list)

## Using fromkeys method
list_ = list(dict.fromkeys(list_))
print(list_)

