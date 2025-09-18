number = [1,2,3,4.5,6]

converted_num = list(map(float,number))


print(converted_num)

import math 

numbers = [1.000002,2.005542]

def truncate(f, n):
    
    return math.floor(f * 10 ** n) / 10 ** n

two_point_list = list(map(lambda x: truncate(x,".3f"),numbers))

print(two_point_list)