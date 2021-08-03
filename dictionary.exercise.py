groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

quantity = {
    "Baby Spinach": 1,
    "Hot Chocolate": 3,
    "Crackers": 2,
    "Bacon": 1,
    "Carrots": 4,
    "Oranges": 2
}


for key, item in groceries.items():
    print(f"{quantity[key]} {key} @ ${item} = ${round(quantity[key]*item)}.2")

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

colours = [
    "purple",
    "red",
    "yellow",
    "blue",
    "purple",
    "orange",
    "blue",
    "purple",
    "orange",
    "green"
]

for colour in colours:
    #    print(colour)
    #   print(colour_counts[colour])
    #    colour_counts[colour]
    #if colour exists in list
    colour_counts[colour] += 1

for colour in colour_counts:
    print(f"{colour}: {colour_counts[colour]}")


