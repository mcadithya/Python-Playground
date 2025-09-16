
year = [2024,2020,1999,2000,3000,3300]

leap_year = []

for items in year:
    
    if items%4 ==0 and items%100 != 0 or items%400:

        leap_year.append(items)

print(leap_year)