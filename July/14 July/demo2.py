'''
2. Mobile Number Digit Counter

A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.

Input:
Enter contact number: +91 98765-43210

Output:
Total digits: 12

'''

num = input("Enter Contact Number: ")
length = len(num)
count = 0
i = 0
while(i<length):
       if num[i] >= chr(48) and num[i] <= chr(57):
              count+=1
       else:
              print
       i=i+1
print("Total digits: ",count)