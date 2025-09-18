

def check_prime():

    num = int(input("Enter The Number : "))

    status = "Prime"

    for i in range(2,num):

        if num%i == 0:

            status = "Not Prime"

            break

    return status

result = check_prime()

print(result)