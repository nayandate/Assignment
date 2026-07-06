'''
5. Harshad Number Checker

A number scanner is installed in a research laboratory where thousands of numeric access codes are tested every day. To identify mathematically balanced codes, the system checks whether the entered number qualifies as a Harshad number. Numbers passing this test are considered valid for the next stage of processing.

A Harshad number is a number that is exactly divisible by the sum of its digits.

Example:
18 → 1 + 8 = 9 and 18 ÷ 9 = 2

Write a program using loops to check whether the entered number is a Harshad number.

Input:
18

Output:
Harshad Number
'''
n1=int(input("Enter First Number = "))
temp=n1
sum=0
while n1>0:	
	r=n1%10
	sum=sum+r
	n1=n1//10
if temp%sum==0:
	print("Harshad Number")
else:
	print("Not Harshad Number")
'''
for i in range(1,n1+1):
	r=n1%10
	sum=sum+r
	n1=n1//10
if temp%sum==0:
	print("Harshad Number")
else:
	print("Not Harshad Number")
'''