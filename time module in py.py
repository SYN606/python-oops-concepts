
import time

initial = time.time()

# checking the run time  of a for loop

# for i in range(45):
#     print("This  is statement for cheking the runtime of for loop in python")

# print(f"\nFor loop ran in {time.time() - initial} seconds")


# returning localtime

localtime = time.asctime(time.localtime(time.time())) 
# --> time.time() will return ticks then time.localtime() will convert it into localtime but in a tuple then time.asctime() will change it into readable format.
print(localtime)


