'''
14.Floor Movement System (Elevator)
An elevator system takes the current floor and destination floor as input.

If current floor < destination → move upward and display floors
If current floor > destination → move downward and display floors
If both are same → display "Already on the same floor"

Write a program using if-elif-else and loops to simulate elevator movement.

Input: 1, 5
Output: 1 → 2 → 3 → 4 → 5

Input: 7, 3
Output: 7 → 6 → 5 → 4 → 3

Input: 4, 4
Output: Already on the same floor
'''

n1 = int(input("Current Floor "))
n2 = int(input("destination "))

if n1<n2:
   for i in range(n1,n2+1):
       print(n1,end="")
       if (n1!=n2):
          print(end = " → ")
       n1+=1
elif n1>n2:
   for i in range(n2,n1+1):
       print(n1,end="")
       if (n1!=n2):
          print(end = " → ")
       n1-=1
if n1==n2:
     print("Already on the same floor")
   