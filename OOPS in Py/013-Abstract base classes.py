"""
    |> If there are multiple classes that are connected to each-other or sharing any common function then we can create a base class that contains that common method, This is known as Abstract base class method.
"""

"""
    for using abstract method we have to import some modules 
"""

from abc import ABC, abstractmethod
# ABC standa for  abstract base class

class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0 
"""
    we cant create an object by using abstract base class
"""



class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 5
        self.breadth = 6

    def print_area(self): 
        return self.length * self.breadth
        # if we remove this print_area() function the code will give an error because we are forcing that print_area() method present in base class


rect1 = Rectangle()

print(rect1.print_area())