"""
    Dunder methods |> methods that are starting with __ (double underscore) and ending with __ are called as dunder methods as like __init__ (dunder init).
"""
class Employee:
    num_of_leaves = 5 

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name of employee is {self.name}, salary is {self.salary} and role is {self.role}."
    
    @classmethod
    def change_leaves(cls, new_leaves):
        cls.num_of_leaves = new_leaves

    
    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    # creating __repr__ and __str__ methods

    def __repr__(self):
        """
            |> if we have to print about variable details like this then we use __repr__ method
        """
        return f"Employee ({self.name}, {self.salary}, {self.role})"


    def __str__(self) -> str:
        """
            |> if we want to summrise an object then we use __str__ method
        """
        return self.print_details()


emp_1 = Employee("Ram", 18000, "Instructor")
emp_2 = Employee("Rohan", 11000, "Cleaner")

# add = emp_1 + emp_2 # |> if we add these variables like this it is known as operator overloading and runs dunder add method behind the scenes and throws an error

# print(emp_1 + emp_2)
# print(emp_1 / emp_2)

# https://pl.python.org/docs/lib/operator-map.html |> this link contains the mapping opreator to functions.

print(emp_1) # |> if there is any __str__ method is present and we use a print statement like this, it will always run __str__ method

# print(repr(emp_1)) # |> for printing __repr__ method we have to use a dedicated print statement for __repr__ method.