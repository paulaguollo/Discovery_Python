#!/usr/bin/env python3

def add_one(number):
    number = number + 1
    return number

my_var = 5
print(my_var)
add_one(my_var)
print(my_var)

# Observation:
# The value of my_var does not change after calling add_one(my_var).
# In Python, when we pass an integer to a function, only its value is
# copied into the function's local parameter ("number"). Modifying
# "number" inside add_one only affects that local variable, which
# exists in the function's own scope. Once the function returns, that
# local scope disappears and my_var in the main program is untouched.
