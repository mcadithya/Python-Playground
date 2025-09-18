f=open("C:/Users/Adithya/Documents/PYTHON/Luminar/python programs/file_handling/years.txt","r")

leap_year = []

not_leap_year =[]

for year in f:

    year = int(year.rstrip("\n"))

    if (year)%4==0 and (year)%100!=0 or (year)==0:
     
     leap_year.append(year)

    else:
      
      not_leap_year.append(year)

print("leap year ",leap_year,"not leap year: ",not_leap_year)

f.close()
