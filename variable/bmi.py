# bmi.py
# Get input from user
name = input("Input student name: ")
height = int(input("Input student height(cm): "))
weight = int(input("Input student weight(kg): "))

# Calculation
height = height / 100
bmi = weight / (height * height)

# output
print(f"student: {name}, BMI: {bmi}")