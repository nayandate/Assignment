'''
1. Two Sum
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

nums = []
n = int(input("Enter no. of elemnets in list: "))
for i in range(n):
    nums.append(int(input(f"Enter element {i+1}: ")))
print(nums)
target = int(input("Enter target: "))
x=0
s=[]
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j] == target:
            s.append(i)
            s.append(j)
            print(s)
            x = 1
            break
    if x==1:
        break