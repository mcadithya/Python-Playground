lst =["apple","bitter guard","wallnut"]



filter_list = list(filter((lambda item : len(item)>=7),lst))


print(filter_list)