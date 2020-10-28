"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
# def XO(txt:str) -> bool:
#     x_count=0
#     o_count=0
#     txt = txt.lower()
#     for char in txt:
#         if char == "x": x_count += 1
#         elif char == "o": o_count += 1
    
#     if x_count == o_count: return True
#     else: return False


# def XO(txt:str) -> bool:
#     x_count=0
#     o_count=0
#     txt = txt.lower()
#     for char in txt:
#         if char == "x": x_count += 1
#         elif char == "o": o_count += 1

#     # return x_count is equal to o_count as a boolean to the caller
#     return x_count==o_count


def XO(txt:str) -> bool:
    lower_txt = txt.lower()

    # return the count of lower txt using "x" as a parameter == the count of 
    # lower txt using "o" as a parameter as a boolean value to the caller
    return lower_txt.count("x") == lower_txt.count("o")


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zpzpzpp"))
print(XO("zzoo"))
