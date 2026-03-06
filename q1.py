def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    if not isinstance(x,int) or not isinstance(y, int):
        return -1
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print("{} {}".format(x,y))
    return 0


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
x = "Apple"
y = 10
swap(x,y)

x = 9
y = 17
swap(x,y)
