'''
Enter Elements: 5 4 -1 7 8
Output: 23
Enter Elements: -2 1 -3 4 -1 2 1 -5 4
6
'''
nums = list(map(int,input("Enter Elements: ").split()))
sum = nums[0]

for i in range(len(nums)):
    total = 0
    for j in range(i,len(nums)):
        total += nums[j]
        if total > sum:
            sum = total

print("Output:",sum)