#Write a program that asks the user to input a number and determine if that number is an odd number greater than 10

num = int(input("enter the number : "))

if(num % 2 != 0 and num > 10):

    print(num,"is an odd number and  greater than 10")

elif(num % 2 == 0 and num > 10):

    print(num,"is not an odd number and  greater than 10")

elif(num % 2 == 0 and num == 10):

    print(num,"is not an odd number and  equal to 10")

elif(num % 2 !=0 and num <10):

    print(num,"is an odd number and less than 10")

else:
    
    print(num,"is not an odd number and less than 10")


    