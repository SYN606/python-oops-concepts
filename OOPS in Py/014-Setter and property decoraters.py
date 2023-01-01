

class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname


    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    # creating email by using decorator-->
    @property # |> property is a decorator
    def email(self):
        """
        This will be change the email od employee's dynamically.
        """
        if (self.fname==None or self.lname==None): # --> if we dont use this 'if' statement it will print none.none@email.com
            return f"Email isn't set, Please set an Email."

        return f"{self.fname}.{self.lname}@email.com"

    # setting the 'setters'
    @email.setter
    def email(self, string):
        print("Setting now....")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]



    # --> making a that can delete an attribute
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

emp_1 = Employee("John", "smith")
# emp_2 = Employee("Ethen", "winters")

# emp_1.email = "this.that" # --> this will run the setter and set the new emailby changing that method. if we try this withour setter method it doesn't change the email. 

# print(emp_1.explain())

del emp_1.email

print(emp_1.email)