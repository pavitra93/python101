# if else statement syntax

print("Welcome to roller coster ticket booking!")
height = int(input("Please enter your height in cm.\n"))

if (height >= 120):
    age = int(input("Please enter your age.\n"))
    if(age < 12):
        print("Please pay $50.")
    elif( age <= 18):
        print("Please pay $80")
    else:
        print("Please pay $100")
else: 
    print("Sorry kiddo! Grow yourself taller and come back later.")
    print("I will be waiting again.")

# Below print() runs out of if-else statements
print("Enjoy!")