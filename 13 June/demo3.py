#You and your friends went out to eat. The bill was quite high and you want to split it evenly.


bill=float(input("Enter the total bill:"))
split=float(input("Enter the no. of friends:"))
each=bill/split
print("Total bill={}\nFriend={}\nEach should pay ={}".format(bill,split,each))