'''
40. Search all occurrences of a word. 
S = "a b a b", Word='b' 
2, 6 (start indices)
'''

s = input("String: ")
word = input("Word: ")
sp = s.split()
i=0
while i<len(sp):
     if sp[i] == word:
           print(i+i,end=" ")
     i+=1