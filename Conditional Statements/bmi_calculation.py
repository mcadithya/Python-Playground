# bmi = weight in kg /(height in metre)^2

name = str(input("Enter the name : "))

weight =  float(input("Enter the weight kg : "))

height_cm = float(input("Enter the height in cm : "))

height_m = height_cm / 100

bmi =  weight / (height_m) ** 2 

if(bmi <18.5):

    print(name,"is Underweight. Your bmi is less than 18.5")

elif(18.5<bmi<24.9):

    print(name,"is Normal weight. Your bmi is in between 18.5-24.9")

elif(25<bmi<29.9):

    print(name,"is Overweight. Your bmi is between 25-29.9")

elif(bmi>30):

    print(name,"is Obesity. Your bmi is between 25-29.9")