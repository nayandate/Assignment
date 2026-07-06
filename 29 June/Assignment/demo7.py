'''
7.Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number
'''

n = int(input("enter number = "))
sum = 0
while n > 0:
    sum += (n%10)
    n//=10
print("Sum =",sum)
for i in range(2,sum//2):
    if sum % i == 0:
        print("Normal Number")
        break
else:
    print("Lucky Number")