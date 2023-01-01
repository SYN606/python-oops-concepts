# MAP --> apllies a whole function in a whole list.
# FILTER --> filter the things in a list or from a list
# REDUCEE --> almost as like map function 


# MAP FUNCTIONS

num = [
    "3", "4", "5", "6"
]  # --> we have numbers in string format

# changing all numbers in int from str

# for i in range(len(num)):
#     num[i] = int(num[i])  # --> this is not an efficient way

# using map func

num = list(map(int, num))
# --> syntax : list(map(new_function to apply, Where to apply / variable))


add = num[0] + num[3]

# print(add)


# --> printing squares using map func

# new_num = [2, 3, 4, 5, 6, 7, 8, 9]

# square = list(map(lambda x: x*x, new_num))

# print(square)


# def sqr(a):
#     return a*a
# def cube(a):
#     return a*a*a

# func = [sqr, cube]

# for i in range(10):
#     val = list(map(lambda x: x(i), func))
#     print(val)



# FILTER FUNCTION
# syntax : filter(function, sequence)

list_1 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9
]

def is_greater_5(number):
    return number > 5

gr_than_5 = list(filter(is_greater_5, list_1))

# print(gr_than_5)


# REDUCE FUNCTIONS

from functools import reduce

# syntax : reduce(function to apply, where to apply)

# printing the sum of numbers 

sum = reduce(lambda x,y: x+y, list_1)
# print(sum)