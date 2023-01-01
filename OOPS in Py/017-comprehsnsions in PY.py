# list comprehension

# a simple python program looks like this

# ls = []
# for i in range(25):
#     if i%3==0:
#         ls.append(i)

# creating same program with the help of list comprehensions

ls = [i for i in range(25)
      if i % 3 == 0]  # --> this is known as list comprehension

# syntax : newlist = [expression for item in iterable if condition == True]

# print(ls)

# Dictionary comprehensions
# dict = {
#     0 : 'item_1',
#     1 : 'item_2',
#     3 : 'item_3'
# }

# ----> creating a Dictionary with comprehensions

# syntax : dict_name = {<new_key>:<new_value> for <item> in <iterable>}
dict = {i: f"item_{i}" for i in range(1, 10 + 1)}

# reverse a dictionary with the help of comprehensions
# dict = {vlaue : key for key,vlaue in dict.items()} # --> this will reverse the dictionary

# print(dict)

# set comprehensions
dresses = {
    dress
    for dress in [
        "dress_1", "dress_2", "dress_3", "dress_1", "dress_2", "dress_3",
        "dress_1", "dress_2", "dress_3", "dress_1", "dress_2", "dress_3",
        "dress_1", "dress_2", "dress_3", "dress_1", "dress_2", "dress_3"
    ]
}

# print(dresses)


"""
    There is also a generator comprehension that is created with the help of parenthesis ().
"""

gen = (i for i in range(20) if i%2==0)

for item in gen:
    print(item)