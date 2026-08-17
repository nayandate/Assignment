'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''
n=int(input("Enter Number = "))
temp=n
fact=1
c=1
sum=0
while n>0:
	r=n%10
	i=1
	while r>=i:
		fact=fact*i
		i=i+1
	#print(fact)
	b=fact
	fact=c
	c=fact
	n=n//10
	sum=sum+b
print(sum)
if sum==temp:
	print(F"{temp} is a Strong Number")
else:
	print("Not Strong Number")
'''
for i in range(a):
	r=n%10
	i=1
	for i in range(1,r+1):
		fact=fact*i
	#print(fact)
	b=fact
	fact=c
	c=fact
	n=n//10
	sum=sum+b
print(sum)
print(sum)
if sum==temp:
	print(F"{temp} is a Strong Number")
else:
	print("Not Strong Number")
'''