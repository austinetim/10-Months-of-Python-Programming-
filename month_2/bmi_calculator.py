#Advanced BMI calculator

#This program calculates the Body Mass Index of a person

height = float(input("Enter your height in m:  "))
weight = float(input("Enter your weight in kg:  "))

BMI_value =round(weight/height**2)
print(BMI_value)
if BMI_value < 18.5:
	print(f"Your BMI value is {BMI_value}, you are underweight")
elif BMI_value < 25:
	print(f"Your BMI value is {BMI_value}, you have normal weight")
elif BMI_value < 30:
	print(f"Your BMI value is {BMI_value}, you are overweight")
elif BMI_value < 35:
	print(f"Your BMI value is {BMI_value}, you are obese")
else:
	print(f"Your BMI value is {BMI_value}, you are clinically obese")