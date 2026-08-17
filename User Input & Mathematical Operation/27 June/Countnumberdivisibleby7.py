'''
2. Count Numbers Divisible by 7 Between Two Numbers

A company filters lucky coupon numbers divisible by 7.
Write a program using loops to count such numbers in range.

Input:
1 30

Output:
Count = 4
'''
n1=int(input("Enter First Number = "))
n2=int(input("Enter Second Number = "))
count=0
'''
for i in range(n1,n2+1):
	if i%7==0:
		count=count+1
		print(i,end=" ")
print("\nCount = ",count)
'''
while n1<=n2:
	if n1%7==0:
		count=count+1
		print(count,end=" ")
	n1=n1+1
print("\nCount = ",count)