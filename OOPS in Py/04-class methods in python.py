
class Employee:
    num_of_leaves = 5 

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"The name of employee is {self.name}, salary is {self.salary} and role is {self.role}."
    
    @classmethod # --> class methods can be used as alternative of constructors.
    def change_leaves(cls, new_leaves):
        cls.num_of_leaves = new_leaves

    @classmethod
    def from_dash(cls, string):
        params = string.split("-")
        return cls(params[0], params[1], params[2])
        # return cls(*string.split("-"))
 
    @staticmethod # --> this is static method, is used for doing simple tasks and only accessable via either class variables or instance variables
    def print_good(string):
        print("This is good " + string)

ram = Employee("Ram", 18000, "Instructor")
shyam = Employee("Shyam", 15000, "Clerk")


karan = Employee.from_dash("Karan-1500-Adviser")

# print(karan.print_details())
# ram.change_leaves(25)
# print(ram.num_of_leaves)

# printing employee details
print(karan.print_details())

# printing static method 
# karan.print_good('karan')
