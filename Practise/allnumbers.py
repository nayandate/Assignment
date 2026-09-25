'''
Enter Elements: 5 4 3 2 4 8 9 1
[6, 7]
'''
nums = list(map(int, input("Enter Elements: ").split()))
result = []

for i in range(1,len(nums)+1):
    if i not in nums:
        result.append(i)
print(result)