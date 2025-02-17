#15.Write a Python function to multiply all the numbers in a list.
from functools import reduce

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)


print(multiply_list([2, 3, 4]))  
