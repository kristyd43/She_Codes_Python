#demonstrate a function
def create_greeting(name):
    greeting = f"Hello, {name}!"
    return greeting

#print(create_greeting("Chilli"))
#print(create_greeting("Ivy"))
#print(create_greeting("Remus"))

#

def convert_cm_to_in(length_cm):
    length_in_inches = length_cm / 2.54
    return length_in_inches

#print(convert_cm_to_in(22))

#Demonstrate that varibales created in a function exist
#only in that function

length_in_cms = 20
#print(convert_cm_to_in(length_in_cms))

def calculate_mean(a, b):
    total = a+b
    mean = total/2
    return mean 

#print(calculate_mean(3,4))


#Exercises
#Q1
def convert_f_to_c(farentemp):
    celstemp = (farentemp -32)/1.8
    return celstemp

print(convert_f_to_c(350))

#Q2
#no idea

#Q3
def numbers(a, b, c, d):
    total = a+b+c+d
    mean = total/2
    return mean

#print(numbers(10, 5, 6)) ?? 
#won't let me calculate with just 3 integers

#Q4
def price(a, b):
    cost = a*b
    return cost

print(str(price(4.25, 3))