num= int(input("enter a number : "))

text = input("enter a text : ")

try:
    print(num+text)

except:
    
    print("error raised, number and string cant add")

print(text*3)

print(num**2)