'''
1. WAP to find out the sum of all integer between 100 and 200 which are divisible by 9
'''

n = int(input("Enter number1 to find out sum which are divisible by 9 : "))
e = int(input("Enter number2 to find out sum which are divisible by 9 : "))
sum = 0
i = n
while i<=e:
      if i%9==0:
          sum = i+sum
      i+=1
print("Sum = ",sum)