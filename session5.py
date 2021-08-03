students = ["Angela", "Jen", "Bel"]
#print(students[0])


#creating a dictionary
#Key needs to be unique, keys can be only immutable data type
#Immutable data types -> String, Integer, Float, Bool, List
#Values don't need to be unique, any data type
#dictionaries are unordered
students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}
#print(students_dict)

#print(students_dict["Angela"])
students_dict["Asli"] = 4
#print(students_dict)
students_dict["Jen"] = 10
#print(students_dict)

del students_dict["Asli"]
#print(students_dict)

#print(students_dict.keys())
#print(students_dict.items())

#Iteration
for key in students_dict:
#    print(key, students_dict[key])

for key,value in students_dict.items():
#    print(key, value)

print(students_dict.get("Bel", "hey"))
#above = print the value of Bel, if doesn't exist, return hey