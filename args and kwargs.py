# def func_print_name(a, b, c, d):
#     print(a, b, c, d)

# func_print_name("Lmao", "Lmau", "Lol", "Loml")

# solving this problem with *args

def func_name_1(normal, *args, **kwargs):
    print(normal,"\n")
    # for item in args:
    #     print(item)


    for key, value in kwargs.items():
        print(f"{key} is used for {value}\n") # --> using f string method
    
# the basic funtion in args is passed as tuple and *args & **kwargs are optional.
# if we want to use a normal arguement the use all the normal arguements and then write the *args 

#  -> by using *args we dont have to change in function's parameter we just have to update the variable value and our work is done.

name = ["bachha 1", "bachha 2", "bachha 3", "bachha 4"]

normal = "I am a normal function arguement"

kw = {
    # key : value
    "python" : "developement",
    "C language" : "core programming",
    "java" : "Game developement",
    "c++" : "Game developement"

}


func_name_1(normal, *name, **kw)


# *args and **kwargs are optional in python. this syntax for using args and kwargs is first use normal arguements the use *args and then use **kwargs.
