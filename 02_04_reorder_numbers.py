# Read in 10 numbers from the user.
# Place all 10 numbers into an list in the order they were received.
# Print out the second number received, followed by the 4th, 
# then the 6th, then the 8th, then the 10th.
# Then print out the 9th, 7th, 5th, 3rd, and 1st number:
#
# Example input:  1,2,3,4,5,6,7,8,9,10
# Example output: 2,4,6,8,10,9,7,5,3,1

numbers = [1,2,3,4,5,6,7,8,9,10]
#for i in range(1,11):
#    reply = input("Input a number: ")
#    numbers.append(reply)
print(numbers)

## Approach 1: Add values from indices using append function on new lines
new_list = []
new_list.append(numbers[1])
new_list.append(numbers[3])
new_list.append(numbers[5])
new_list.append(numbers[7])
new_list.append(numbers[9])
new_list.append(numbers[8])
new_list.append(numbers[6])
new_list.append(numbers[4])
new_list.append(numbers[2])
new_list.append(numbers[0])
print(new_list)

## Approach 2: Use For loops, enumerate, and modulo to add values
new_list_2 = []

#Start index at 1 and if index is divisible by 2, add the value
for num, count in enumerate(numbers, start=1): 
    if count % 2 == 0:
        new_list_2.append(num)

#Start index at 1 and if index is not divisible by 2, add the value
for num, count in enumerate(numbers, start=1):
    if count % 2 != 0:
        new_list_2.append(num)

print(new_list_2)

## Approach 3: Use While loops and nested For & If loops (more complicatd though)
new_list_3 = []
list_counter = 0

while list_counter < 5:
    for num, count in enumerate(numbers, start=1):
        if count % 2 == 0:
            new_list_3.append(num)
            list_counter += 1
while list_counter >= 5:
    for num, count in enumerate(numbers, start=1):
        if count % 2 != 0:
            new_list_3.append(num)
            list_counter += 1
print(new_list_3)



