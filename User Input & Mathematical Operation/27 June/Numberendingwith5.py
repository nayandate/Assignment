'''
3. Display Numbers Ending with 5

A supermarket tracks token numbers ending in 5.
Write a program using loops to display numbers ending with 5 between two numbers.

Input:
10 40

Output:
15 25 35
'''
num1,num2=map(int,input("Enter two number = ").split(" "))
for i in range(num1,num2+1):
	if i%5==0 and i%10!=0:
			print(i,end=" ")
'''
i=1
while num1<=num2:
	if num1%5==0 and num1%10!=0:
		print(num1,end=" ")
	num1=num1+1
'''