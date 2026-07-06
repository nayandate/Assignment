'''
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''
import math
n=int(input("Input = "))
l=len(str(n))
largest=0
sum=0
i=1
rev=0
while n>0:
	r=n%10
	rev=rev*10+r
	n=n//10
while i<l:
	r=rev%10
	rev=rev//10
	r1=rev%10
	diff=abs(r1-r)
	print(diff,end=" ")
	if diff>largest:
		largest=diff
	i=i+1
	sum=sum+diff
else:
	"#while-else concept"
	print(f"\n{sum}")
	print(largest)
	if sum%diff==0:
		print("Balnced Number")
	else:
		print("Unbalanced number")
'''
rev=0
while n>0:
	r=n%10
	rev=rev*10+r
	n=n//10
print(rev)
'''