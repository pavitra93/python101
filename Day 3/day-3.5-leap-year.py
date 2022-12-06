'''
Find if the year is leap year or not with below conditions

This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
'''

year = int(input("Please enter the year to check if it is leap year or not\n"))

if (year % 4 == 0):
    if(year % 100 == 0):
        if(year % 400 == 0):
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else: 
    print("Not leap year.")
