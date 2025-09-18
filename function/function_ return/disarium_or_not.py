#  3. write a function to check a number disarium or not 135 = 1^1 + 3^2 + 5^3


def disarium(num):

    str_num = str(num)

    num_length = len(str_num)

    sum = 0

    for i in range(num_length):

        digit = num % 10

        sum += digit ** num_length

        num//=10

        num_length -= 1

    return sum


num = int(input("enter the number : "))

result = disarium(num)

if result == num:

    print(f"{num}is disarium")

else:

    print(f"{num} is disarium")
    