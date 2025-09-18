Accounts  = {"mohan lal","mammotty","nivin pauly","deepika","rashmika","vijay","surya","parvathi","asif ali","aishwarya"}

mohanlal_followers = {"mammotty","nivin pauly","parvathi","vijay"}
mohanlal_following ={"vijay","mammotty","asif ali"}
reshmika_followers = {"vijay","nivin pauly","deepika"}
reshmika_following ={"vijay","nivin pauly","surya","ishwarya"}


# 1 friendsuggestion for mohanlal

# friendsuggestion = Accounts - mohanlal_following
# friendsuggestion.discard("mohan lal")
# print(friendsuggestion)


#2 mutual friends of reshmika and mohan lal 


# 3 follower that follows only reshmika not mohan lal 

# reshmika_set = reshmika_followers - mohanlal_followers 
# print(reshmika_set)


#4 accounts reshmika follows but not mohan lal

print(reshmika_following -mohanlal_following  )