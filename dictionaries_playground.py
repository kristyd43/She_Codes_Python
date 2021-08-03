groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

#print(groceries)


#look at specific value
#print(groceries["Baby Spinach"])

#Add an item
groceries["Avocados"] = 1.00
#print(groceries)

#Remove an item
del groceries["Bacon"]
print(groceries)

#Iterating over the dictionary
for item in groceries:
#    print(f"{item}: ${groceries[item]}")

#another way to iterate over dictionary
for item, price in groceries.items():
    print(f"{item}: ${price}")
