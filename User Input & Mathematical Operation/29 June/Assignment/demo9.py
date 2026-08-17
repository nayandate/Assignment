'''
9.Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime
'''

n = int(input("enter number = "))
ecount = 0
ocount = 0
while n>0:
    temp = n%10
    if temp % 2 == 0:
        ecount+=1
    else:
        ocount+=1
    n//=10
diff = abs(ecount - ocount)
print("Even Count =",ecount)
print("Odd Count =",ocount)
print("Difference =",diff)
if diff < 2:
    print("Not Prime")
else:
    for i in range(2,diff//2):
        if diff % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")