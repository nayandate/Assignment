'''
2. Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output: 4

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''

n = int(input("Enter no. of total passwords: "))
password=[]
for i in range (n):
    password.append(input(f"Enter password {i+1}: "))
print("\nPasswords:",password)

count=0
for i in range(n):
    for j in range(i+1,n):
        x=0
        for ch in password[i]:
            if ch in password[j]:
                x=1
                break
        if x==0:
            count+=1
print("Count:",count)