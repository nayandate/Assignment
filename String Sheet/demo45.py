'''
45. Check whether a string starts/ends with another string. 
S = "apple pie", Prefix = "apple", Suffix = "pie" 
Start: True, End: True
'''

s = input("String: ")
slen = len(s)
pre = input("Prefix: ")
suf = input("Suffix: ")

count=0
for i in range(len(pre)):
    if s[i] == pre[i]:
         count+=1
if count == len(pre):
     print("Start: True")
else:
     print("Start: False")

count=0

j = 0
for i in range(slen-len(suf),slen):
    if s[i] == suf[j]:
         count+=1
    j+=1
if count == len(suf):
     print("End: True")
else:
     print("End: False")

'''
if a[:len(b)] == b:
    print("Start: True")
else:
    print("Start: False")
if a[-len(c):] == c:
    print("End: True")
else:
    print("End: False")
'''