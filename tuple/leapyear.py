years =(1998,2024,2000,1870,1600,1995,2020)

# leap_year = ()

# for year in years:

#     if year%4==0 and year %100!=0 or year%400==0:

#         leap_year+=(year,)


# print(leap_year)


leap_year = tuple([year for year in years if year%4==0 and year %100!=0 or year%400==0])

print(leap_year)
