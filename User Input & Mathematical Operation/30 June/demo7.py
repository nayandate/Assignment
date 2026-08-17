'''
7.Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits

- Check whether sum is Prime or Not

Input: 12345

Output:
Alternate Sum = 9
Not Prime
'''

n = int(input("enter number = "))
sum = 0
while n > 0:
    sum += n%10
    n//=100
print("Alternate Sum =",sum)
if sum < 2:
    print("Not Prime")
else:
    for i in range(2,sum//2):
        if sum % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")