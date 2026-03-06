def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if key in dct:
        print("key {} exists: value = {}".format(key, dct[key]))
    dct[key] = value
    return dct


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26
dct = {}
key = "name"
value = "Alice"

update_dictionary(dct, key, value)
print("updated dictionary: {}".format(dct))


dct = {"age": 25}
key = "age"
value = "26"

update_dictionary(dct, key, value)
print("updated dictionary: {}".format(dct))

