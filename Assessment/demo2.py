# '''
# 2. Step Difference Number Analyzer(3.5 marks)

# A mathematics research center studies hidden patterns inside numbers.
# For every entered number, the system compares adjacent digits step by step.

# Write a program to:

# Find the absolute difference between every pair of adjacent digits
# Display all step differences
# Find the sum of all step differences
# Find the largest step difference
# If the sum of step differences is divisible by the number of digits, print Balanced Number
# Otherwise print Unbalanced Number

# Use loops wherever required.

# Input:
# 57294
# Output:
# Step Differences: 2 5 7 5
# Sum = 19
# Largest = 7
# Unbalanced Number

# '''

# no = int(input("Enter Number: "))
# length = len(str(no))
# n = 0
# max = 0
# sum=0

# while no>0:
#      n=no%10+n*10
#      no=no//10

# prev = n % 10
# n = n // 10
# print("Step Differences:",end=" ")
# while n > 0:
#     cur = n % 10
#     result = cur - prev
#     if result < 0:
#         result = (-1)*result
#     sum = sum+result
#     if result > max:
#         max = result
     
#     print(result,end=" ")
#     prev = cur
#     n = n // 10

# print("\nSum =",sum)
# print("Largest =",max)


# if sum%length==0:
#      print("Balanced Number")
# else:
#      print("Unbalanced Number")



n=input("Enter string ").split()
s=n[0]
i=1
res=""
temp=""
temp1=""
while i<len(n):
    c=n[i]
    j=0
    while j<len(s) and j<len(c):
        if i==1:
             if s[j]==c[j]:        
                temp1+=s[j]
         
             else:
                 break
        else:
            k=0
            temp1=""
            while k<len(temp) and k<len(c):
                 if temp[k]==c[k]:              
                     temp1+=temp[k]
                 
                      
                 else:
                     break
            
                 k+=1
        temp=temp1

        j+=1  
    i+=1


print(temp)