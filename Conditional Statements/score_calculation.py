#Write a program that asks the user to input their score (0 to 100), and then outputs the corresponding grade according to the following scale:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

score= int(input("Enter the Score (score in between 0 to 100): " ))

# if( 90<= score <= 100):

#     print("grade is A")

# elif(80 <= score <= 89):

#     print("garde is B")

# elif(70 <= score <= 79):

#     print("grade is C")

# elif(60 <= score <= 69):

#     print("grade is D")

# elif(score < 60):

#     print("grade is F")


if(score in range(90,100)):

    print("grade is A")

elif(score in range(80,89)):

    print("garde is B")

elif(score in range(70,79)):

    print("grade is C")

elif(score in range(60,69)):

    print("grade is D")

elif(score < 60):

    print("grade is F")
