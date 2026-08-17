'''
30. Replace a word with another word. 
S = "old data", Old="old", New="new" 
"new data"
'''

s = input("String: ")
old = input("Old: ")
new = input("New: ")
l = s.split()
result=""
i=0
while i<len(l):
     if l[i] != old:
           result+=l[i]+" "
     else:
           result+=new+" "
     i+=1
print("Updated:",result)