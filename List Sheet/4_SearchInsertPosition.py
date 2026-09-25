'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
'''

nums = []
n = int(input("Enter no. of elemnets in list: "))
for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))
print("List:",nums)
target = int(input("Enter target: "))
print()

nums.sort()
if nums[n-1]<target:
    print("Output:",n)
elif nums[0]>target:
    print("Output: 0")
else:
    for i in range(len(nums)):
        if nums[i]>target:
            print("Output:",i)
            break