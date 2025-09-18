# write a function that calculates area of rectangle 
# 2.with param without return

def area_rectangle(radius):

    area = 3.145 * radius

    return area

radius = int(input("Enter the radius : "))

print("Area of rectangle is : ",area_rectangle(radius))