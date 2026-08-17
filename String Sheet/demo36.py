'''
36. Reverse order of words. 
S = "one two three" 
"three two one"
'''

s = input("Input: ")
sp=s.split()
result=""
i=len(sp)-1
while i>=0:
    result+=sp[i]+" "
    i-=1
print(result)
#print(" ".join(sp[::-1]))