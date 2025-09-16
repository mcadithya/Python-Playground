word ="hello"

print(isinstance(word,str))


lst =["hello",12.3,11.2,11,2,3,"python"]

str_list =[]
float_list =[]
int_list = []

for item in lst:

    if isinstance(item,str):

        str_list.append(item)

    elif isinstance(item,int):

        int_list.append(item)

    elif(isinstance(item,float)):

        float_list.append(item)


print("Float List : ",float_list)
print("Intiger List : ", int_list)
print("String List : ",str_list)


