# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1.lower() + name2.lower()
count_true = 0
count_love = 0

count_true += name.count('t')
count_true += name.count('r')
count_true += name.count('u')
count_true += name.count('e')


count_love += name.count('l')
count_love += name.count('o')
count_love += name.count('v')
count_love += name.count('e')

count = str(count_true) + str(count_love)

total = int(count)

if(total < 10 or total > 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif(total >= 40 and total <=50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")