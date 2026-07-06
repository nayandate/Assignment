'''
8.
Mirror Difference Transaction Verification System
A multinational banking company processes thousands of daily transaction IDs. To detect suspicious patterns and validate system-generated IDs,
 the security software performs a Mirror Difference Verification Test.
For every entered transaction ID:

Reverse the digits of the transaction ID

Find the absolute difference between the original ID and the reversed ID


Count the total number of digits in the difference


Apply the following conditions using if-elif-else:

If the difference is 0, print Perfect Match


Else if the difference is divisible by 9, print Verified


Else print Rejected


Write a program to automate this verification process using loops and conditional statements.
Input:
4215
Output:
Reverse = 5124Difference = 909Digits = 3Verified
Input:
1221
Output:
Reverse = 1221Difference = 0Digits = 1Perfect Match
Input:
1234
Output:
Reverse = 4321Difference = 3087Digits = 4Verified
'''
'''
import math
n=int(input("Enter number = "))
temp=n
count=0
sum=0
a=len(str(n))
i=a
while n>0:
	r=n%10
	i=i-1
	sum=sum+(r*(10**i))
	n=n//10
difference=temp-sum
count=len(str(abs(difference)))
if sum-temp==0:
	print(f"Reverse= {sum} Difference = {abs(difference)} Digits = {count} Perfect Match")
elif (sum-temp)%9==0:
	print(f"Reverse= {sum} Difference = {abs(difference)} Digits = {count} Verified")
else:
	print(f"Reverse= {sum} Difference = {abs(difference)} Digits = {count} Rejected")
'''
import math
n=int(input("Enter number = "))
temp=n
a=len(str(n))
sum=0
for i in range(0,a):
	sum=n%10+sum*10
	n=n//10
print(sum)
difference=temp-sum
count=len(str(difference))
if sum-temp==0:
	print(f"Reverse= {sum} Difference = {abs(difference)} Digits = {count} Perfect Match")
elif (sum-temp)%9==0:
	print(f"Reverse= {sum} Difference = {abs(difference)} Digits = {count} Verified")
else:
	print(f"Reverse= {sum} Difference = {abs(difference)} Digits = {count} Rejected")