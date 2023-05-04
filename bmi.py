# Python code to calculate BMI

def calculate_bmi(height, weight):


    # Add code here to display BMI
    bmi = weight/height**2

    print("Your BMI is: ", bmi)

    if bmi <= 18.5:
        print("You are underweight.")
        return -1

    elif 18.5 < bmi <= 24.9:
        print("Your weight is normal.")
        return 0

    elif 25 < bmi <= 29.29:
        print("You are overweight.")
        return 1
x = calculate_bmi(1.78,78)




print(x)
 # else:
   # print("You are obese.")
