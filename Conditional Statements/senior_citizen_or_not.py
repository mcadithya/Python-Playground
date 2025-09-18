#Take name and age from user and display he is senior citizen or not

name = str(input("Enter the name : "))

age = int(input("Enter your age : "))

if(age>=60):

    print(name,"is a senior citizen")

else:
    
    print(name,"is not a senior citizen")