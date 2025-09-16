names = ["james","john","alexander","johnson","morgen","mitchel","anna","jefrey","ellys"]

result = {item[0].upper()+item[1:]:len(item) for item in names if item.startswith(("a" ,"i","o","u")) and len(item)>5 }  # use capitalize()

print(result)

