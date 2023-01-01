# def avg(a, b):
#     average = (a+b)/2
#     return average

#     # print(average)
#     # if we not use the return it will print a none value
# v = avg(5, 7)

# print(v)


# writing docstring 

def add(x, y):
    """This is a function for adding two numbers."""
    sum = x + y
    return sum

# n = add(3, 6)

# print(n)

# printing docstring

print(add.__doc__) # -> this will print {This is a function for adding two numbers.}