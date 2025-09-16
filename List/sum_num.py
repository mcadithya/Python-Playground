lst = [1,2,3,4,5,6,7]

sum = 7

# count = 0

# for i in range(0,len(lst)-1):

#     for j in range(i+1,len(lst)):

#         count+=1

#         if lst[i]+lst[j]==sum:

#             print(lst[i],lst[j])


# print(count)



sorted_list = sorted(lst)

start = 0

end = len(lst)-1

while start<end:

    if sorted_list[start] + sorted_list[end] >sum:

        end-=1
    
    elif sorted_list[start] + sorted_list[end]<sum:

        start+=1
    
    else:

        print(lst[start],lst[end])

        start+=1
        end-=1





