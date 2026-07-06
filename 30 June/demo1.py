'''
1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime
'''
n = int(input("enter number"))
temp = n
sum = 0
rev = 0
diff = 0
while n > 0:
    rev = rev*10 + (n%10)
    sum += n%10
    n//=10
diff = abs(temp - rev)
result = diff + sum
print("Sum of Digits =",sum)
print("Reverse =",rev)
print("Difference =",diff)
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