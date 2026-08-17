'''
1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)
'''

n = int(input("Enter no. of employees: "))
ages=[]
for i in range (n):
    ages.append(int(input(f"Enter {i+1} employee's age: ")))
print("\nAges:",ages)
k = int(input("Difference to find: "))

count=0
for j in range (len(ages)):
    for ch in range(j+1,len(ages)):
        if abs(j-ch) == k:
            count+=1
print("Count: ",count)