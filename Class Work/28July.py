'''
WAP to find first non repeative word.

s  = input("Input: ")
found=0
i = 0
while i<len(s):
     ch = s[i]
     count = 0
     j=0
     while j<len(s):
         if ch == s[j]:
             count+=1
         j=j+1
     if count == 1:
          print(s[i])
          found=1
          break
     i+=1
if found == 0:
      print("Not Found")
'''

'''
WAP to find shortest word in a sentence.

s  = input("Input: ")
x = s.split()
smallest = s
i=0
while i<len(x):
      if len(smallest) > len(x[i]):
            smallest = x[i]
      i+=1
print(smallest)
'''

'''
WAP to find largest word in a sentence.

s  = input("Input: ")
x = s.split()
smallest = ""
i=0
while i<len(x):
      if len(smallest) < len(x[i]):
            smallest = x[i]
      i+=1
print(smallest)
'''

'''
WAP to find the no. of unique characters in a string

s  = input("Input: ")
result=""
found=0
i = 0
while i<len(s):
     ch = s[i]
     count = 0
     j=0
     while j<len(s):
         if ch == s[j]:
             count+=1
         j=j+1
     if count == 1:
          print(s[i],end=" ")
          result+=s[i]
          found=1
     i+=1
print("\nUnique Character",len(result))
if found == 0:
      print("Not Found")
'''

'''
WAP to find occurence of a word in a string

s  = input("Input: ")
word = input("Word: ")
'''
s  = input("Input: ")
word = input("Word: ")
i=0
count=0
while i<=len(s)-len(word):
      j=0
      match=1
      while j<len(word):
           if s[i+j] != word[j]:
               match = 0
               break
           j+=1
      if match == 1:
              count+=1
      i+=1
print(count)

