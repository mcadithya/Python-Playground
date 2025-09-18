
def calculate_area_perimeter(len,brdth):

    area = len * brdth

    perimeter = 2* (len+brdth)

    return area , perimeter

area, perimeter = calculate_area_perimeter(15,25)

print("area of rectangle : ", area)

print ("Perimeter of rectangle : ", perimeter)