# changing the variables value while the condition is true or not by using ternory condiotions

condition = True

# if condition:
#     x = 1
# else:
#     x = 0

x = 1 if condition else 0   # --> ternory method

# print(x)



# adding large numbers and writing a readable code.

# num_1 = 10000000000
# num_2 = 100000000

# using underscores we can seprate the integers in python that are human readable

num_1 = 10_000_000_000
num_2 = 10_000_0000  # --> this is more human readable 


total =  num_1 + num_2
# print(total)
# |> formatting the result

# print(f"{total:,}") # |> this will format the output.


# enumerating 

names = [
    'Jhon',
    'Ethen',
    'Ashley',
    'Odin',
    'Falkon Carmine'
]

# for index, name in enumerate(names, start=1):
#     print(index, name)


# zip

name = [
    'Peter Parker',
    'Bruce Wayne',
    'Jhony Blaze',
    'Vitor Stone'
]

heros = [
    'Spoidermon',
    'Batman',
    'Ghost Rider',
    'Cyborg'
]
universes = [
    'Marvel',
    'DC',
    'Marvel',
    'DC'
]
# for index, n in enumerate(name):
#     hero = heros[index]
#     print(f"{hero} is {n}")

# |> we can write that function in more easy way

# for hero, n, universe in zip(name, heros, universes):
#     print(f"{hero} is {n}, belongs to {universe}.")


