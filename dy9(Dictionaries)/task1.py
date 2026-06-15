programming_dictionary = {"Bug":"Computer Errors",
    "Function": "Code that can be called over and over"}

print(programming_dictionary["Function"])

programming_dictionary["Loop"]="Over and over again"

empty_dictionary = {}

programming_dictionary["Bug"]= "A moth in your computer"



#wipe existng dictionary

#programming_dictionary ={}
#print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])