class A:
    classvar = "I am a class variable in class A"

    def __init__(self):
        self.var = "I am inside Class A's constructor"
        self.classvar = "Instance variable in Class A"
        self.special = "Special"

class B(A):
    classvar_2 = "I am class B"

    def __init__(self):
        super().__init__() 
        self.var = "I am inside Class B's constructor"
        self.classvar = "Instance variable in Class B"


a = A()
b = B()

print(b.special)