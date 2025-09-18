groceries = {'Tamarind','Apple','Pineapple','Papaya','Lemon','Blueberry','pomegranates','Water','Salt','Banana','Bitter guard','Star fruit','Tomato'}

sweet_items = {'Apple','Pineapple','Papaya','Banana'}

sour_items = {'Tamarind','Lemon','Blueberry','Pomegranates','Star fruit','Tomato'}

vegetables = {'Bitter guard','Tomato'}

# qs1: find grocery items that are not  sweet and sour

groceries_not_sweet_sour = groceries-sweet_items - sour_items

print(groceries_not_sweet_sour)


# qs2 : find groceries that are not vegetables but have sour taste

groceries_not_vegetables_sour = groceries - vegetables & sour_items

print(groceries_not_vegetables_sour)

# qs3 : find count of vegetables that are not sor and sweet

vegetables_not_sour_sweet = vegetables - sour_items - sweet_items

print(len(vegetables_not_sour_sweet))

# qs4 : find items that are not vegetables, not sour, not sweet

not_vegetables_sour_sweet = groceries - vegetables - sour_items - sweet_items

print(not_vegetables_sour_sweet)