import pickle

"""
    pickling is the process of preserving the objects.
    or
    Create portable serialized representations of Python objects.

"""

cars = [
    'audi',
    'BMW',
    'ferrari'
]

# pickling an object

# file = 'mycar.pkl'
# fileobj = open(file, 'wb')

# pickle.dump(cars, fileobj)

# depickling an object

file = 'mycar.pkl'
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)


print(mycar)