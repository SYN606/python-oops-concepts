import json

# creating json to dict

data = '{"var 1":"Data 1", "var 2":"Data 2"}'

parsed = json.loads(data) # --> it will print a py dict.
print(parsed)

# creating dict to json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

y = json.dumps(x)

# formatting the results
"""
    we can use indent, separators and also we can sort_keys the result.
"""
# y = json.dumps(x, indent=4) # --> by using indent we can format json in readable format.
# y = json.dumps(x, indent=4, separators=(". ", " = ")) # --> we can modify the json separators.

# |> using sort_keys
# y = json.dumps(x, indent=4, sort_keys=True) # --> by using sort_keys parameter we can specify if the result should be sorted or not.

print(y)