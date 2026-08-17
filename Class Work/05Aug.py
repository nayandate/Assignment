'''
Q1. Peak Element Problem:

An element is called a peak element if its value is not smaller than its adjacent elements (if they exist).
Find the index of any one peak element.
'''
'''
n = int(input("Enter size: "))
arr = []
for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput: ",arr)

x=0
if arr[0] > arr[1]:
     x=1
     print("Element: ",arr[0])
     print("Index: 0")

elif arr[-1] > arr[-2]:
     x=1
     print("Peak Element: ",arr[-1])
     print("Index: ",len(arr)-1)

else:
     for i in range(1,len(arr)):
          if arr[i-1]<arr[i]>arr[i+1]:
                 x=1
                 print("Peak Element:",arr[i])
                 print("Index:",i)
                 break
if x==0:
    print("No peak element")
'''
'''
Q2. Sum of leaders in an List

An element is called a leader if it is greater than all elements to its right side.

Rightmost element is always a leader.
You need to return the sum of all leaders.

Input:
First line -> integer n
Second line -> n space-separated integers

Output:
Single integer -> Sum of all leader element
If array is empty return -1
'''

n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)

sum=0
for i in range(len(arr)):
       x=1
       for j in range(i+1,len(arr)):
             if arr[i]<=arr[j]:
                  x=0
                  break
       if x==1:
           sum+=arr[i]
if n == 0:
       print(-1)
else:
      print("Sum of all leader element:",sum)
