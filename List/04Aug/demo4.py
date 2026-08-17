'''
4. Palindrome Number List Checker Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

n = int(input("Enter size: "))
nums = []
for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    nums.append(x)
print("\nInput: ",nums)

pal_count = 0
palindrome = []
for ch in nums:
    if str(ch) == str(ch)[::-1]:
        pal_count += 1
        palindrome.append(ch)

print("\nPalindromes:",palindrome)
print("Count:",pal_count)
print("Largest:",max(palindrome))
print("Sorted:",sorted(palindrome))