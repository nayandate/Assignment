'''
1. Cyclic Rotate Array by one
   Give an array, rotate it cyclically one by one
'''
'''
n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)

last = arr[-1]
i=n-1
while i>0:
    arr[i]=arr[i-1]
    i = i-1
arr[0]=last
print(arr)
'''
'''
2. WAP to count pair with given sum.
Input: n = 4[2 4 5 1], k = 6
Output: 2
Explanation: 2 + 4 = 6
             1 + 5 = 6
'''
'''
n = int(input("Enter size: "))
arr = []

for i in range(n):
    x = int(input(f"Enter number {i+1} : "))
    arr.append(x)
print("\nInput:",arr)
k = int(input("Enter K: "))

count = 0
for i in range(n):
      for j in range(i+1,n):
            if arr[i]+arr[j]==k:
                 count+=1
print("No. of pairs:",count)
'''
'''
a = [1,2,3,4,5]

#b=[i*3 for i in a]         #[3, 6, 9, 12, 15]

#b = [val for val in a if val%2==0]          #[2, 4]

#b= [val*val for val in a if val>3 if val%2==0]        #[16]
print(b)
'''

# Nested List

a = [[1,2],[3,4],[5,6]]

print(a[2][1])    #6
#print(a[2][2])   #Error: Index out of range
print(a[2])       #[5,6]

for r in a:
    print(r)      #[5, 6] \n [1, 2] \n [3, 4] \n [5, 6]

for i in range(len(a)):
      for j in 
print(a)    #6