from glob import glob


l = 10 # --> * Global Variable

def func(n):
    # l = 5 # --> ** Local Variable
    global l # --> it allows to change the global variable's value.
    print(l)

    print("I have printed",n)

func("This is me")



"""--> * if a variable is declared outside of a function then it is a global variable and also it can be used inside of a function."""

"""--> ** if a variable id declared insdie of a function then its a local variable. Local variables can't be used outside of a function but if we create a variable that name is simiallier to global varible the will act like a local variable and also its value will be as declared as locally.
"""
"""
Note : if a variable isn't found locally or not declared in locally then python searches that variable globally. Also if a variable is globally then inside a function it can be only read
"""