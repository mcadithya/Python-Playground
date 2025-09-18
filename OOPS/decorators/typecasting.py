def typecasting(fn):

    def wrapper(num_1,num_2):

        num_1 = int(num_1)

        num_2 = int(num_2)

        return fn(num_1,num_2)
    
    return wrapper

@typecasting

def sum(num_1,num_2):

    return num_1 + num_2

num_1 = input("enter the first number : ")

num_2 = input("enter the second number : ")

print(sum(num_1, num_2))


