class A:
    def print_a(self):
        print("This is a method from class A")

class B(A):
    pass
    # def print_a(self):
    #     print("This is a method from class B")

class C(A):
    pass
    # def print_a(self):
    #     print("This is a method from class C")

class D(B, C): # --> here D class is using multiple inheritance while class B and class C is using multi-level inheritnace
    pass

a = A()
b = B()
c = C()
d = D()

d.print_a()

"""
    |> This type of problem is known as diamond shape problem where, when we do multiple inheritances in a class thats creates a confusion and that problem looks like diamond shape
    |> In the solution of this problem we can avoid multiple inheritances and do multilevel inheritance. Because of this some language doesn't support multiple inheritance like java, while python and c++ supports multiple inheritance.
"""