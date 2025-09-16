fruits = ["Apple","orange","Banana"]

uper_list = []

lower_list = []

for items in fruits:

    if items[0].isupper():

        uper_list.append(items)

    elif(items[0].islower()):

        lower_list.append(items)

print(uper_list)

print(lower_list)