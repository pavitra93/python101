# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
float_height = float(height)
float_weight = float(weight)

bmi = round(float_weight / (float_height ** 2))

if(bmi < 18.5):
    type = "underweight"
    print(f"Your BMI is {bmi}, you are {type}.")
elif(bmi < 25):
    type = "normal weight"
    print(f"Your BMI is {bmi}, you have a {type}.")
elif(bmi < 30):
    type = "slightly overweight"
    print(f"Your BMI is {bmi}, you are {type}.")
elif(bmi < 35):
    type = "obese"
    print(f"Your BMI is {bmi}, you are {type}.")
else:
    type = "clinically obese"
    print(f"Your BMI is {bmi}, you are {type}.")
