# Nested lists 

fruits = ["Oranges", "Apples", "Banana"]
vegetables = ["Carrots", "Onions", "Tomato", "Spinach" ]

nested_list = [fruits, vegetables]

print(nested_list) # [['Oranges', 'Apples', 'Banana'], ['Carrots', 'Onions', 'Tomato', 'Spinach']]
print(nested_list[1]) # ['Carrots', 'Onions', 'Tomato', 'Spinach']
print(nested_list[1][2]) # Tomato

nested_list.extend(["Cheese"])
print(nested_list) # [['Oranges', 'Apples', 'Banana'], ['Carrots', 'Onions', 'Tomato', 'Spinach'], 'Cheese']

nested_list.pop() # [['Oranges', 'Apples', 'Banana'], ['Carrots', 'Onions', 'Tomato', 'Spinach']]
nested_list.pop() # [['Oranges', 'Apples', 'Banana']]

print(nested_list) # [['Oranges', 'Apples', 'Banana']]