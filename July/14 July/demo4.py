'''
4. Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

word = input("Enter Employee ID: ")
length = len(word)
count = 0
if length == 8:
    if word[0] == "E" and word[1] == "M" and word[2] == "P":
          count += 3

          i = 3
          while(i<length):
                if word[i] >= chr(48) and word[i] <= chr(57):
                   count += 1
                i += 1
    else:
         print("Not Valid Employee ID ")
if count == length:
   print("Valid Employee ID ")
else:
   print("Not Valid Employee ID ")
