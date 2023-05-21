# str()
# ord()
# tuple()
# hex()
# oct()
# set()
# list()
# dict()

""" explicit type-casting & implicit type-casting 

When a user does typecasting in a program it is known as explicit typecasting.On the other hand when python typecasts a variable value from one data type to another to prevent data lose it is known as implicit typecasting.

"""
# Ex :-
# num = input("Enter a num : ")
# print(type(num))
# num = int(num)
# print(type(num))

num_1 = 40
num_2 = input("Enter a number : ")
# By default whenever python takes input by a user its default data type is string, we can use type() function for checking the data type of a variabel.
print(type(num_2))
num_3 = 2

div_1 = num_1 / num_3
print(type(div_1)) # Implicit Typecasting
print(div_1)

num_2 = int(num_2) # Explicit Typecasting
div_2 = num_1 / num_2
print(type(div_2), div_2) # Implicit Typecasting
