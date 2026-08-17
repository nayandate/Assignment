'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''

n = int(input("Enter size: "))
nums = []
for i in range(n):
    x = int(input(f"Enter {i+1} employee salary : "))
    nums.append(x)
print("Input: ",nums)
average=(sum(nums))//n
print("Average:",average)
avr=[]
rem=[]
for ch in nums:
    if ch > average:
         avr.append(ch)
    if ch>15000:
        rem.append(ch)

print("Above Average:",end=" ",*avr)
print("Remaining List:",rem)