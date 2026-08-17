'''
29. Remove occurrences of a word. 
S = "a test b test c", 
Word = "test", Remove All 
"a b c"
'''

s = input("String: ")
word = input("Word: ")
l = s.split()
result=""
i=0
while i<len(l):
     if l[i] != word:
           result+=l[i]+" "
     i+=1
print("Updated:",result)