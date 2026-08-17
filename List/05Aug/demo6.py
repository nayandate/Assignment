'''
6. A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''

n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)

sum=0
prime=[]
for i in range(len(arr)):
    if arr[i] > 1:
        for j in range(2, arr[i]+1//2):
            if arr[i] % j == 0:
                break
        else:
            prime.append(arr[i])
            sum+=arr[i]

print("Prime IDs:",prime)
print("Sum:",sum)
if prime:
    print("Max:",max(prime))
else:
    print("Max:",-1)
print("Count:",len(prime))