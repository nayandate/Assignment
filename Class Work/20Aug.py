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
'''
n = int(input("Enter no. of employees: "))
ages=[]
for i in range(n):
    ages.append(int(input(f"Enter age of Employee{i+1}: ")))

dif = int(input("\nDifference: "))
print("Age: ",ages)
count=0
for i in range(n):
    for j in range(i+1,n):
        if abs(ages[i]-ages[j])==dif:
            count+=1
print("Count: ",count)
'''

'''
2. Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''