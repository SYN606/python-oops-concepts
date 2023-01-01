"""
    creating an library management system that is based on oop 

    |> create a library class
    |> create a method for displaying all books
    |> create a method for lending books (who owns the book if books isn't present.)
    |> create a method for adding books
    |> create a method for returning the books

"""


class Library:

    def display(self, name):
        return f"Welcome the Library. The books that we have {name}"

    def lend(self, list):

        print("Which book do you want?")
        a = input()
        print("Enter your name")
        name = input()

        with open("logs.txt") as f:
            f.write("The person is :" + name + "\n")

        print(f"{a} is now with you {name}")
        return f"{list.remove(a)}"

    def add(self, list):

        print("Write the name you want to add")
        a = input()
        print("Succesfully added")
        return list.append(a)

    def retn(self, list):
        print("What do you want to return")
        a = input()
        print("Your name")
        name = input()
        print("Done")
        return list.append(a)


World_Library = Library()

mainlist = [
    "In Search of Lost Time",
    "Ulysses",
    "Don Quixote",
    "The Great Gatsby",
    "Harry Potter",
]

print(World_Library.display(mainlist))

while True:

    do = int(input(f"choose one option 1.Lend, 2.Add and 3.Return\n"))

    if do == 1:
        World_Library.lend(mainlist)

    elif do == 2:
        World_Library.add(mainlist)

    elif do == 3:
        World_Library.retn(mainlist)