'''
28. Count occurrences of a word. 
S = "word word other word", 
Word = "word" 
3
'''

s = input("String: ")
word = input("Word: ")
l = s.split()
count=0
i=0
while i<len(l):
     if l[i] == word:
           count+=1
     i+=1
print("Count:",count)