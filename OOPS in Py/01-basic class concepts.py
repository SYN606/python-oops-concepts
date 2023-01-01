"""
    Classes - Templates --> templates are used as pre written messages or a boiler plate.
    Objects - Instance of the class --> an object that is created using that template that is provided by class.

"""


class Student:  # while creating a class always use capital letter as the first letter of the class.
    # the class variables are written here
    pass


# creating class objects

student_1 = Student()

student_1.name = 'Ram'
student_1.std = 9
student_1.section = 'B'
student_1.subjects = [
    "hindi",
    "english",
    "math"
]

student_2 = Student()

student_2.name = 'Shyam'
student_2.std = 10
student_2.section = 'A'
student_2.subjects = [
    "hindi",
    "english",
    "math"
]
"""
    --> these are known as instance variables while if there is a varible that is inside a class in known as class variable.
"""

print(f"The name of student is {student_1.name} and the class is {student_1.std}\n")

print(f"The name of student is {student_2.name} and the class is {student_2.std}")