#Calculating BMI
def bmi_calculate(weight, height):
    bmi = weight / (height ** 2)
    return bmi

#Categorizing BMI
def bmi_categories(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

#Check weight
def check_weight(weight):
    return 3.00 <= weight <= 500.00

#Check height
def check_height(height):
    return 0.463 <= height <= 2.72

try:
    weight = float(input("Enter your Weight (in Kilograms): "))
    if check_weight(weight):
        try:
            height = float(input("Enter your Height (in Meters): "))
            if check_height(height):
                bmi = bmi_calculate(weight, height)
                category = bmi_categories(bmi)
                print(f"Your BMI is {bmi:.2f}, which means you are {category}.")
            else:
                print("Please enter a valid height between 0.463m and 2.72m.")
        except ValueError:
            print("Enter only a number for height.")
    else:
        print("Please enter a valid weight between 3kg and 500kg.")
except ValueError:
    print("Enter only a number for weight.")
