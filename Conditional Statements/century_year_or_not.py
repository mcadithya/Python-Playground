#write a program that takes a year as input from user and display it is century year or not

year = int(input("enter the year : "))

if(year % 100 == 0):

    print(year,"is a century year")

else:
    print(year,"is not a century year")