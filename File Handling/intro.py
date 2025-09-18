# file open  by open() -- function

# open(file_path,mode_of_operation)

# mode  --- r,w,a(append)

# r ---  file path is not correct the raise error  --- file not found,curser at begining of the file
#r+ read 
#w+ 
#a+
# f = open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/text.txt","r")

# for name in f:
#     print(name.rstrip("\n"))   # in result have unwanted spaces in file. data store in one line with ending \n so when we read the data first remove \n

# f.close()

# f = open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/text.txt","r")
# consonant_name  =[]

# for name in f:
#     name.rstrip("\n")
#     if name[-1] not in "aeiou":
#         consonant_name.append(name.rstrip("\n"))
#     print(consonant_name)
# f.close()



#w
#file pathil file illengil puthiya file create cheyum
# oru file "w" modil open cheythal file data delete avum (fresh file ayitan open ava)
# with open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/writefile.tx","w") as f :
#     for num in range(1,11):
#         f.write(str(num)+"\n")


#a
# file illengil create cheyum.data ilengil strting poinrt. data undengil last data point cheyum

