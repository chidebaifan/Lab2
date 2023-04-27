# Python code to calculate BMI

def calculate_bmi(height, weight):
    return round((weight / height ** 2), 2)

    # Add code here to input weight and height
height = float(input("Enter your height in meters:  "))
weight = float(input("Enter your weight in kg:  "))

    # Add code here to display BMI
bmi = calculate_bmi(height, weight)
print("Your BMI is: ", bmi)

if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
