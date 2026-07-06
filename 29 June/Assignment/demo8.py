'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime
'''

n = int(input("enter number = "))
max = -1
min = 9

while n > 0:
    temp = n%10
    n//=10
    if temp >max:
        max = temp
    if temp < min:
        min = temp
sum = min + max
print("Largest =",max)
print("Smallest =",min)
print("Sum =",sum)
if sum < 2:
    print("Not Prime")
else:
    for i in range(2,sum//2):
        if sum % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")