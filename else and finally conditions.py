try:
    with open("file.txt") as f:
        a = f.readlines()
    print(a)

# we can write more than one exception statement.
# 
except Exception as e:
    print(e)

# else:  
#     print("this will run only when except will not work/run")


# using finally means that it will do a finally task doesn't matters try and except runs or not.

finally:
    print(f"Important Task")

"""
    it can be used for cleaning up the code.
"""