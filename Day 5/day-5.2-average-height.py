# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
total_students = len(student_heights)

for height in student_heights:
    total_height += height

avg_height = total_height / total_students
print(round(avg_height))