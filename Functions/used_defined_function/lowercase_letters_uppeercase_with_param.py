# without param without return

def countLoop():

    upercase_count=0

    lowercase_count=0

    text=input("Enter the string : ")

    for char in text:

        if('A' <= char <= 'Z'):
            
            upercase_count+=1
        
        elif('a' <= char <= 'z'):

            lowercase_count+=1

    print(f"lowercase count : {lowercase_count}")

    print(f" uppercase count : {upercase_count}")

countLoop()



