# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

tup_string = tuple(string)
print(tup_string)
my_list = list(tup_string)
print(my_list)
new_list = []
for char in my_list:
    if char.lower() == "c":
        char = "k"
        new_list.append(char)
    else:
        new_list.append(char)
print(new_list)
new_tup = tuple(new_list)
print(new_tup)

    