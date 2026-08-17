# WAP to read 5 different types of values.

n = int(input("Enter size: "))
nums=[]
for i in range(n):
     if i==0:
         x = int(input("Enter integer value: "))
     elif i==1:
         x = float(input("Enter float value: "))
     elif i==2:
         x = complex(input("Enter complex value: "))
     elif i==3:
         x = (input("Enter string value: "))
     elif i==4:
         x = bool(input("Enter boolean value: "))
     else:
          print("BSDK 5 se jyada mujhe bhi data type nhi maalum")
          break
     nums.append(x)
print(nums)