'''
37. Reverse each word. 
S = "cat dog" 
"tac god"
'''

s = input("Input: ")
sp=s.split()
result=""
i=0
while i<len(sp):
    result+=sp[i][::-1]+" "
    i+=1
print(result)
