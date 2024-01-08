# Updated BMI Excerise
Weight = int(input("Please input your weight "))

height = float(input("Please input your height in metres " ))

bmi = round(int(Weight)/float(height)**2, 2)
if bmi <= 16.0:
    print(f"{bmi} : Underweight (severe thinness)")
elif bmi <= 16.9:
    print(f"{bmi} : underweight (moderate thinness)")
elif  bmi <= 18.4:
    print (f"{bmi} : Underweight (minld thinness)")
elif  bmi <= 24.9: 
    print(f"{bmi} : Normal range") 
elif  bmi <= 29.9:
    print(f"{bmi} : Overwight (pre-obese)")
elif  bmi <= 34.9:  
    print(f"{bmi} : Obese (class I)")
elif  bmi <= 39.9:
    print(f"{bmi} : obese (Class II)")
elif bmi >= 40:
    print( f" {bmi} : Obese (class III)")
else:
    print(f'{bmi} : You are overweight')





    
