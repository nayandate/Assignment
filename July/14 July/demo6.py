'''
6. Product Code Verification System

An e-commerce company wants to verify whether two product codes are rearranged versions of each other.

Conditions:
- Ignore spaces
- Ignore case sensitivity

Input:
Enter first product code: Dormitory
Enter second product code: Dirty Room

Output:
Both Product Codes are Matching
'''

word1 = input("Enter first product code: ").lower()
word2 = input("Enter second product code: ").lower()
copy1 = ""
copy2 = ""
x = 1

for i in word1:
     if i == " ":
         continue
     else:
         copy1+=i

for i in word2:
     if i == " ":
         continue
     else:
         copy2+=i

if len(copy1) == len(copy2):
    i = 0
    while i<len(copy1):
        ch = copy1[i]
        count1 = 0
        count2 = 0
        j = 0
        while j<len(copy1):
            if copy1[j] == ch:
                 count1+=1
            j+=1

        j = 0
        while j<len(copy2):
            if copy2[j] == ch:
                 count2+=1
            j+=1
        if count1 != count2:
            x = 0
            break
        i+=1
else:
    x = 0

if x==1:
   print("Both Product Codes are Matching")
else:
   print("Both Product Codes are not Matching")

