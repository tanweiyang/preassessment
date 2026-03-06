def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if num % divisor:
        return False
    return True


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

num = 10
divisor = 2
print("{} divisible by {}: {}".format(num, divisor, check_divisibility(num, divisor)))

num = 7
divisor = 3
print("{} divisible by {}: {}".format(num, divisor, check_divisibility(num, divisor)))

