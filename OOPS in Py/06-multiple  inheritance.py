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


class Player:
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game= game

    def print_game(self):
        return f"The name of player is {self.name} and the game he plays is {self.game}"


class Cool_Programmer(Employee, Player):
    pass


ram = Employee("Ram", 18000, "Instructor")
shyam = Employee("Shyam", 15000, "Clerk")

kabir = Player("Kabir", ['Cricket'])

rahim = Cool_Programmer("Rahim", 25000, "Programmer")

print(rahim.print_details())