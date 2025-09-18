def data_swap(fn):

    def wrapper(num_1,num_2):

        if num_2>num_1:

            num_1,num_2 = num_2,num_1

        return fn(num_1,num_2)
    
    return wrapper


@data_swap

def difference(num_1,num_2):

    return num_1-num_2


print(difference(10,5))

print(difference(10,25))