#Loops - repetitive tasks
#Loop - for loops, while loops
#For loops - know how many times to repeat a task
#While llops - don't know how many times to repeat

#For Loops - sequence, strings, lists, dictionaries

#a = [1, 2, 3, 4]
#print(a[1:4])

#for num in range(1, 11): #iterate through sequence of numbers
#    print("num")

#for num in range(1, 12, 2):
#    print("num")

#use for loop to print number
#0 to 100 (inclusive
# 
# Use for loop to print numbers
# 0 to (skip 5) 0, 5, 10, 15

##for num in range(0,101):
#    print(num)

#for num in range(0,101,5):
#    print(num)

chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

#for item in range(len(chilli_wishlist)): #range (4) 
#    print(chilli_wishlist[item])

#for item in chilli_wishlist:
#    print(item)

#Adapt the for loop to print a  message for eahc item in the list
#for example "chilli wants: item"

#Use a for loop to print eahc item in a list
#form a previous exercie or example

#for item in chilli_wishlist:
#    print(f"Chilli wants: ", item)

chilli_wishlist = [["igloo"],
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box," "kong", "dig mat"]]

for category in chilli_wishlist:
    for item in category:
        print(item)


#While Loops - dont know how many time to repeat

#count = 0
#while count < 5:
#    print("Hello")
    #count = count + 1 (same as line below)
#    count += 1 #an interation
