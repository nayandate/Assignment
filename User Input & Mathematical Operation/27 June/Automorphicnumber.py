'''
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for special self-matching numeric codes. When a user enters a number, the system squares the number and checks whether the result ends with the same digits as the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number
'''

while True:
	n=int(input("Enter Number = "))
	r1=n%10
	sq=n*n
	sq1=sq%10
	if r1==sq1:
		print("Automorphic Number")
		break
	else:
		print("Not Automorphic Number")

'''
a=n**2
r=n%10
r1=a%10
if r==r1:
	print("Automorphic number")
'''
'''
n=int(input("Enter number = "))
for i in range(len(str(n))):
	a=n**2
	c=n%10
	b=a%10
if c==b:
	print("Automorphic number")
else:
	print("Not Automorphic number")
'''