'''
10.
 Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
 only prime numbers are accepted because they have exactly two factors and are harder to predict using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes, access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not prime.

Input:
29
Output: Prime Number
n=int(input("Enter number = "))
count=0
i=2
while n>i:
	if n%i==0:
		count=count+1
	i=i+1
if count==0:
	print("Prime number")
else:
	print("Not prime")
'''for in range(2,(n//2)-1):
	if n%i==0:
		count=count+1
	i=i+1
if count==0:
	print("Prime Number")
else:
	print("Not Prime")
'''