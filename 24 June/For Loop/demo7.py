'''
*7. Count Even Digits*
A data analyst is analyzing numeric IDs and needs to determine how many digits in the ID are even.
Write a program to *count the number of even digits in a given number using loops*.

Input: 123456
Output: Even digits count = 3
'''

n = int(input("Number = "))
count=0
rem = 0
for i in range(n,0):
    rem = n%10
    if rem%2 == 0:
         count = count+1
    i=n//10
    
print("Even digits count : ",count)