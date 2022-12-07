# Lists 
# For more information go to: https://docs.python.org/3.11/tutorial/datastructures.html
# Collection of any datatype of items 

names = ["Pavitra", "Monika", "Utkarsh", "Nidhi"]
print(names)
print(names[1]) 

print(names.count("Monika"))

names.append("Jitendra")
print(names)

names.extend(["Sahil, Utkarsh"])
print(names)

names.pop()
print(names)

names.append(5)
print(names)