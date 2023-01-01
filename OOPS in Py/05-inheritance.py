
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

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod 
    def print_good(string):
        print("This is good " + string)


# inheriting parent class into child class / single inheritance

class Programmer(Employee):
    def print_prog(self):
        return f"The name of Programmer is {self.name}, salary is {self.salary} and role is {self.role}."



ram = Employee("Ram", 18000, "Instructor")
shyam = Employee("Shyam", 15000, "Clerk")
karan = Employee.from_dash("Karan-1500-Adviser")

ayush = Programmer("Ayush", 22000, "Programmer")

print(ayush.print_prog())