class Employee:
    num_of_leaves = 5 # --> class varibales are accesable but they can be only be changes by only using class variables.

"""
    --> class variables cant be changed by instance variables. if we try to change a class variable by using a instance var then it create a new instance var.
"""

ram = Employee()

ram.name = "Ram"
ram.salary = 18000
ram.role = "Instructor"


shyam = Employee()

shyam.name = "Shyam"
shyam.salary = 15000
shyam.role = "Clerk"

# shyam.num_of_leaves = 9 # --> this will create a new instance variable

# print(shyam.num_of_leaves)
# print(Employee.num_of_leaves)

print(f"The name of employee is {ram.name}, salary is {ram.salary} and role is {ram.role}.\n")

print(f"The name of employee is {shyam.name}, salary is {shyam.salary} and role is {shyam.role}.")


# also if we do .__dict__ on a class then it will show all instance variables

# print(Employee.__dict__)