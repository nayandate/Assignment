'''
39. Search all occurrences of a character. 
S = "banana", Char='a' 
1, 3, 5 (indices)
'''

s = input("String: ")
word = input("Char: ")
i=0
while i<len(s):
     if s[i] == word:
           print(i,end=" ")
     i+=1