'''
*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even
'''

n = int(input("Number = "))
count=0
count1=0
rem = 0
while(n>0):
    rem = n%10
    if rem%2 == 0:
         count = count+1
    count1+=1
    n=n//10
    
if count1 == count:
    print("All Even digits ")
else:
    print("Not All Even digits ")
