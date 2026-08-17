'''
7. Factory Production - Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
'''

n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)

count=0
fac=[]
for ch in arr:
    add=1
    for i in range(ch,0,-1):
        add=add*i
    fac.append(add)
    if add%2 == 0:
       count+=1
print("Output:",fac)
print("Sum:",sum(fac))
print("Max:",max(fac))
print("Even Count:",count)
