print("=" * 40)
print("💪 BMI CALCULATOR 💪".center(40))
print("=" * 40 + "\n")
# Input
weight = float(input("⚖️  Enter Your Weight (kg): "))
height = float(input("📏 Enter Your Height (m): "))
# BMI Calculation
bmi = weight / (height ** 2)
# Conditions
if bmi >= 25:
    print("You are Overweight⚠️")
elif bmi >= 18.5 :
    print("You are Normalweight✅")
else:
    print("You are Underweight⚠️")
