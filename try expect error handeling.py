num1 = input("Enter a number : ")
num2 = input("Enter a number : ") 

try:
    print("The sum of two numbers is :", int(num1) + int(num2)) # -> if we remove int from hereit will throw an error. that case we can use Try Expect case

except Exception as e:
    print(e)


print("this is very important line.")