'''
2. Multi Stage Prime Lock System
   A smart locker opens only if final derived number is prime.
Write a program to:
- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234
Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17

Prime
'''

n = int(input("enter number"))
temp = n
sum = 0
pro = 1
diff = 0
while n > 0:
    pro *=  (n%10)
    sum += n%10
    n//=10
diff = abs(pro - sum)
temp2 = diff
digit = 0
while diff > 0:
    digit+=1
    diff//=10
result = temp2 + digit

print("Sum =",sum)
print("Product =",pro)
print("Difference =",temp2)
print("digit =",digit)
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