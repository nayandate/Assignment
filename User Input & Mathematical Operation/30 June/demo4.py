'''
4.Unique Digit Security Scanner
  A smart locker accepts only numbers whose all digits are unique.
  Write a program using for-else loop to:
- Check every digit
- If any repeated digit found reject
- Else accept

Input:
57294
Output:

Valid Unique Code
'''

n = input("enter number")
flag = True
l = len(n)
for i in range(1,l):
    j = i+1
    while j < l:
        if n[i] == n[j]:
            print("Reject")
            flag = False
            break
        j+=1
    if flag == False:
        break
else:  
    print("Valid Unique Code")