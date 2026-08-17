'''
1. Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''

email = input("Enter Email :").lower()
count = 0
len = len(email)
if len < 5 or len > 12:
      print()
else:
     for i in range (0,len):
         if (email[i]  >= 'a' and email[i] <= 'z') or (email[i]  >= chr(48) and email[i] <= chr(57) or email[i] == chr(95)):
               count+=1
          
if count == len:
        print("Valid Number....")
else:
     print("Invalid Number...")