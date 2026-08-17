'''
3. Industrial Sensor Peak Energy Monitoring System

Problem Statement

A factory machine records energy consumption at regular intervals.

A peak is defined as a value greater than or equal to its neighbors.

Tasks:

Find all peak energy values
Compute sum of squares of peak values
Compute average of peak values
Return difference between max peak and min peak
If no peaks, return -1

Test Case 1

Input:
energy = [20, 40, 30, 60, 50]

Output:
Peaks = [40, 60]
Sum of squares = 5200
Average = 50
Difference = 20

Test Case 2

Input:
energy = [10, 20, 15, 25, 20, 30]

Output:
Peaks = [20, 25, 30]
Sum of squares = 1525
Average = 25
Difference = 10

Test Case 3

Input:
energy = [5]

Output:
Peaks = [5]
Sum of squares = 25
Average = 5
Difference = 0
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
sum_square=0
peak=[]
if n == 1 :
    add+=arr[0]
    sum_square=arr[0]*arr[0]
    peak.append(arr[0])
else:
    for i in range(n):
        x=0
        if (i == 0 and arr[i] >= arr[i+1]) or (i == n-1 and arr[i] >= arr[i-1]) :
            x=1
        elif arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            x=1
        if x==1:
            add+=arr[i]
            sum_square+=arr[i]*arr[i]
            peak.append(arr[i])


print("Peaks:",peak)
print("Sum of squares:",sum_square)
print("Average:",add//len(peak))
print("Difference:",abs(max(peak)-min(peak)))