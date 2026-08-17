'''
5.Number Stability Analyzer
  A science lab studies whether digits are in increasing order.
  Write a program using for-else loop:
- If every next digit is greater than previous print Stable Number
- Else Unstable Number
Input:
12359
Output:
Stable Number
'''
n = input("enter number")
for i in range(len(n)-1):
    if int(n[i]) > int(n[i+1]):
        print("Unstable Number")
        break
else:
    print("Stable Number")