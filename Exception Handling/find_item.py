def find_item(index):

    my_list  =  [1,5,8,9,7,10]

    # print(my_list[index])

    return my_list[index]

user_index = int(input("Enter a index : ")) 
      
try:

    find_item(user_index)

except Exception as error:

    print(error)

    