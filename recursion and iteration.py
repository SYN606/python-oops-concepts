# factorial using iteration


def factorial_itr(n):
    """    
    :param n: Integer
    :return: n * n-1 * n-2 * n-3...........1
    """
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac


# factorial using recursion 

def factorial_rec(n):
    if (n == 1):
        return 1
    else:
        return n * factorial_rec(n-1)



number = int(input("Enter a number : "))

print("Factorial using iterative method :",factorial_itr(number))
print("Factorial using recusion method :",factorial_rec(number))