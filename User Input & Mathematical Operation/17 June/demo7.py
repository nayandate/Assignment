'''
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
'''

run = int(input("Total runs : "))
over = float(input("Overs : "))


tb = int(((over*10)%10)+((over*10)//10)*6)
print("Total Balls = ",tb)

rr = float((run/tb)*6)
print("Run rate = ",rr)