centuary_year = lambda year : "centuary year" if year%100==0 else "not centuary year"

input_year = int(input("enter the year : "))

print(centuary_year(input_year))