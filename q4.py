def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):
        print("In function {}: argument is not string: {}".format(__name__, s))

    return s[::-1]


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

s = "Hello World"
new_s = string_reverse(s)
print("{}".format(new_s))

s = "Python"
new_s = string_reverse(s)
print("{}".format(new_s))

