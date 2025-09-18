#write a program that takes a year as input from user and display it is century year or not using short hand methord

year = int(input("enter the year : "))

result =  f"{year} is a century year" if year % 100 == 0 else f"{year} is not a century year"

print(result)
