'''
10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime
'''

n = int(input("enter number = "))
count = 0
sum = 0
min = 9
while n > 0:
    temp = n%10
    sum+=temp
    if temp == 0:
        count+=1
    if temp < min:
        min = temp
    n//=10
print("Zero Count =",count)
print("Sum =",sum)
print("Smallest Digit =",min)

sum = sum + count
result = sum * min
print("Final Result =",result)

if result < 2:
    print("Not Prime")
else:
    for i in range(2,result//2):
        if result % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")