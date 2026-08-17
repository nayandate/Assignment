'''
32. Count frequency of each word. 
S = "apple banana apple" 
apple: 2, banana: 1
'''

s = input("String: ")
word = s.split()
result=""
i=0
while i<len(word):
     if word[i] not in result:
           result+=word[i]+" "
     i+=1

i=0
result=result.split()
while i<len(result):
     print(result[i],":",s.count(result[i]))
     i+=1