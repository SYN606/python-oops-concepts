class Employee:
    num_of_leaves = 5 

    # creating constructors

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    # function for printing details
    
    def print_details(self):
        return f"The name  of employee is {self.name}, salary is {self.salary} and role is {self.role}."

ram = Employee("Ram", 18000, "Instructor")

# ram.name = "Ram"
# ram.salary = 18000
# ram.role = "Instructor"


shyam = Employee("Shyam", 15000, "Clerk")

# shyam.name = "Shyam"
# shyam.salary = 15000
# shyam.role = "Clerk"


print(ram.print_details())

"""
    |> the self parameter is defined as the self which means that variable itself.
    |> the __init__ is used for initialize a variable to instanse variable while using in a class.
"""