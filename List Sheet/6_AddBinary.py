'''
6. Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

a = input("Enter string1: ")
b = input("Enter string2: ")

i = len(a)-1
j = len(b)-1
carry = 0
result=""
while i>=0 or j>=0 or carry:
    if i>=0:
        x = int(a[i])
    else:
        x = 0
    if j>=0:
        y = int(b[j])
    else:
        y = 0
    total = x+y+carry
    result = str(total%2)+result
    carry = total // 2
    i-=1
    j-=1
print(result)
'''
result = int(a,2)+int(b,2)
print(bin(result)[2:])
'''