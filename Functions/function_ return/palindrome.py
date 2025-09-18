#4. write a function to check a text is palindrome or not

def palindrome(str):

    str_copy = str

    status = False

    reverse_string = str_copy[::-1]

    if reverse_string == str:

        status = True

    return status


input_string = input("Enter the string for check palindrome : ")

result = palindrome(input_string)

if result == True: 

    print(f"{input_string} is palindrome")

else:

    print(f"{input_string} is not palindrome")

