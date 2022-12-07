# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_count = len(names)-1
random_user = names[random.randint(0,names_count)]
print(f"{random_user} is going to buy the meal today!")

# random.choice() for less code
random_user = random.choice(names)
print(f"{random_user} is going to buy the meal today!")
