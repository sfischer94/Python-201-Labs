# Using f-strings, print out the name, last name,
# and quote of each person in the given dictionary,
# formatted like so:
#
# "The inspiring quote" - Lastname, Firstname

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

## Approach using f strings
for item in famous_quotes:
    print(f"{item['quote']} - {item["full_name"].split(" ")[-1]} , {item["full_name"].split(" ")[0]}")


## Alternative approach - use nested loops
for pair in famous_quotes:
    for key, value in reversed(pair.items()): # Use reversed method to iterate backwards
        if key == "quote":
            print(value, end = " - ")
        elif key == "full_name":
            print(value.split(" ")[-1] + ", " + value.split(" ")[0])
