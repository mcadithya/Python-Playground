

def number():

    num =  int(input("enter a  number : "))

    if num <0:

        raise Exception("error: number must be greater than zero")

    elif num >100:

        raise Exception("error : number must be less than 100")

    else:

            print(num)


try:
     number()
     
except Exception as e:
     
     print(e)

print("task4")