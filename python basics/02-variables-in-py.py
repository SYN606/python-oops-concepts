# name, Name -----> concept of case sensitive in python
# python is case sensitive that means name and Name are different variable and can hold different values.

name = "Ethen Winters" 
Name ="Kang The Conquerer"
print(name + "\n",Name)

# type :- this prints the type of given variable or object.

num = "3882" # this is a string containing numbers.
string = 3882 # this variable contains numerical values that are knowns as integer.
print(type(num))
print(type(string))


# if we want to write sentence like this we can write in this manner :--

string_2 = 'he said "i am going to school"'
print(string_2)

# we can also write a variable that can hold true value in python :--

t = True
# True and False are boolean values


# Concept of complex float in python

fl = 3.14j

"""
why we can only write 'j' in a complex float ?

According to python bug tracer python follows electrical engineering convention :
                    In Python, the letter 'j' denotes the imaginary unit. It would be great if we would follow mathematics in this regard and let the imaginary unit be denoted with an 'i'.


"""

# we can assign same values to multiple variables in this manner.
a = b = c = 1
x = y = z = "This is a string"

print(z)


i = None # None is used to represent store a null value in python. it is not the same as empty string or any false or zero.We can assign None to any variable, but can't create other NoneType objects.

# we can assign multiple value to multiple variables in this manner :---

f, g, h = 13, "name", 3.14j #  here f = 13, g = "name" and h = 3.14j

print(f)
print(g)
print(h)