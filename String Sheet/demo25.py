'''
25. Count total words in a string. 
S = "This is a test" 
4
'''

s = input("String: ").lower()
s=s.strip()
count=1
i=0
while i<len(s):
      if ('a'<=s[i-1]<='z') and s[i]==" " :
           count+=1
      i+=1
print("Count:",count)
