height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))
def BMI(height,weight):
	bmi = weight / (height/100)**2

if (bmi <= 18.4):
	return 'underweight', bmi
elif (bmi <= 24.9):
	return 'healthy', bmi
elif (bmi <= 29.9):
	return 'over weight', bmi
elif (BMI <= 34.9):
	return 'severely over weight', bmi
elif (BMI <= 39.9):
	return 'obese', bmi
else:
	return 'severely obese', bmi
quote, bmi = BMI(height, weight)
print('Your bmi is: {} and you are: {}',format(bmi, quote))
