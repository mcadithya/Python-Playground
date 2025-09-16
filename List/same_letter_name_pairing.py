# Amal Annu
# Sasi Sonu

names = ["Annu","Amal","Jasmin","Sonu","Sasi",'Salu']

sorted_names = sorted(names)

start = 0

end = len(names)-1

while start<end:
        
        if sorted_names[start][0] == sorted_names[start+1][0]:
        
            print(sorted_names[start],sorted_names[start+1])

            start +=2

        else:
            
            start +=2

 