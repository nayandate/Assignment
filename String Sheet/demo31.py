'''
31. Remove duplicate words. 
S = "the cat and the dog" 
"the cat and dog"
'''

s = input("String: ")
word = s.split()
result=""
i=0
while i<len(word):
     if word[i] not in result:
           result+=word[i]+" "
     i+=1
print("Updated:",result)