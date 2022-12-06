# if else statement syntax

print("Welcome to roller coster ticket booking!")
height = int(input("Please enter your height in cm.\n"))
price = 0

if (height >= 120):
    age = int(input("Please enter your age.\n"))
    if(age < 12):
        price = 50
    elif( age <= 18):
        price = 80
    else:
        price = 100
    
    need_photos = input("Do you need photos? Type Y fo yes or N for no")
    if(need_photos == 'Y'):
        price += 10
    
    print(f"Your total bill is ${price}. Enjoy!");
else: 
    print("Sorry kiddo! Grow yourself taller and come back later.")
    print("I will be waiting again.")
