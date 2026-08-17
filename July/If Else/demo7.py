'''
7. Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''

vn = input("Enter vehicle number: ").upper()
length = len(vn)
x = 1

if length == 10:
   if (vn[0] >= "A" and vn[0] <= "Z") and (vn[1] >= "A" and vn[1] <= "Z") and (vn[4] >= "A" and vn[4] <= "Z") and (vn[5] >= "A" and vn[5] <= "Z"):
         if (vn[2] >= "0" and vn[2] <= "9") and (vn[3] >= "0" and vn[3] <= "9"):
              i = 4
              while i<length:
                   if vn[i] >= "0" and vn[i] <= "9":
                         x = 0
                   i+=1
if x == 0:
   print("Valid Vehicle Number")
else:
   print("Not Valid Vehicle Number")

