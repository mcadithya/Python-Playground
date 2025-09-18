# f = open("hello.txt","r")

# try: 
#     for num in f:

#         num  = int(num.rstrip("\n"))

#         print(num)

# except:

#     print("some error raised")

# finally:

#     f.close()

#     print("file closed")



f = open("hello.txt","r")

try: 
    for num in f:

        num  = int(num.rstrip("\n"))

        print(num)

except Exception as e:

    print(e)

    print("some error raised")

finally:

    f.close()

    print("file closed")