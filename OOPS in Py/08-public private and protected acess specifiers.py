"""
    Public --> Everyone can see
    Protected --> Only some can see (Child classes can see the variable)
    Private --> Only you can see (Only the base class can see the variable)
"""

class Dad:
    __basketball = 1 # --> if we put __ in front of a variable it becomes private varibale.

class Son(Dad):

    _dance = 1   # --> this is a protected variable that can be accessed in only base classes and derived classes.
    def is_dance(self):
        return f"Yes, I dance {self.dance} no of times"

class GrandSon(Son):
    guitar = 1
    dance = 6
    def is_dance(self):
        return f"I am grandson and i dance {self.dance} no. of times."


ayush = Dad()
ram = Son()
shyam = GrandSon()

# print(shyam.basketball)

print(ram._dance)

# print(ayush._Dad__basketball) # --> print a private variable