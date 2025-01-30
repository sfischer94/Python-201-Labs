# CHALLENGE: Write a script that sorts a dictionary into a
# list of tuples based on the dictionary's values. For example:

# input_dict = {"item1": 5, "item2": 6, "item3": 1}
# result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

# Check out the Python docs and see whether you can come up with a solution,
# even if you don't yet completely understand why it works the way it does:
# https://docs.python.org/3/howto/sorting.html#key-functions
# Feel free to discuss any questions you have with your mentor and on the forum!

my_dict = {"item1": 5, "item2": 6, "item3": 1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item:item[1]))
print(sorted_dict)
result_list = []

for key, value in sorted_dict.items():
    temp_list = []
    temp_list.append(key)
    temp_list.append(value)
    result_list.append(tuple(temp_list))
    
print(result_list)
