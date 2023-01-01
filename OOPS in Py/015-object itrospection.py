"""
    object introspection means that knowing about a object that where is it coming from or other details.
    |> type --> print about the type of a object
    |> id --> print the id of that element
    |> dir --> tells about that what methods can we perfom on an object 

"""
class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname


    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property # |> property is a decorator
    def email(self):
        
        if (self.fname==None or self.lname==None): 
            return f"Email isn't set, Please set an Email."

        return f"{self.fname}.{self.lname}@email.com"

    @email.setter
    def email(self, string):
        print("Setting now....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]


    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None


emp_1 = Employee("Tony", "Stark")

print(emp_1.explain())

# print(emp_1.email)

# print(type(emp_1))
# print(id(emp_1))
# print(dir(emp_1))


# using inspect module

import inspect

# print(inspect.getmembers(emp_1))

# inspect.getmembers() is a method from inspect module.
# for more details of inspect the module visit |> https://docs.python.org/3/library/inspect.html