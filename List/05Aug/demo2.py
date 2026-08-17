'''
2. Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5
'''

n = int(input("Enter size: "))

if n <=0 :
    print("Invalid Size of List")
else:
    arr = []

    for i in range(n):
        x = int(input(f"Enter number {i+1} : "))
        arr.append(x)
    print("\nInput:",arr)

add=0
product=1
peak=[]
if n == 1 :
    add+=arr[0]
    product*=arr[0]
    peak.append(arr[0])
else:
    for i in range(n):
        x=0
        if (i == 0 and arr[i] >= arr[i+1]) or (i == n-1 and arr[i] >= arr[i-1]) :
            add+=arr[i]
            product*=arr[i]
            peak.append(arr[i])
        elif arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            add+=arr[i]
            product*=arr[i]
            peak.append(arr[i])

print("Peaks:",peak)
print("Sum of all leader element:",add)
print("Product of all leader element:",product)
print("Max Peak:",max(peak))
