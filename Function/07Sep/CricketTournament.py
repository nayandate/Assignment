'''
3. Cricket Tournament - Highest Run Scorer

A cricket academy wants to reward the player who scored the highest number of runs in a tournament.

Write a Python program to identify the highest run scorer using reduce() and a lambda expression.

Input
players = [
    ("Virat", 78),
    ("Rohit", 102),
    ("Gill", 89),
    ("KL Rahul", 65),
    ("Iyer", 91)
]
Expected Output
Highest Run Scorer: Rohit
'''

from functools import reduce
players = []
n = int(input("Enter no. of players: "))
for i in range(n):
    print()
    name = input("Enter name of player: ")
    age = int(input("Enter run of player: "))
    players.append((name,age))
    
print("Players: ",players)
run = reduce(lambda x,y: x if x[1]>y[1] else y,players)
print("Highest Run Scorer:",run[0])