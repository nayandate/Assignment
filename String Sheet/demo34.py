'''
34. Find the shortest word. 
S = "find the shortest word" 
"the"
'''

s = input("Input: ")
spl = s.split()
largest=len(s)
i = 0
while i<len(spl):
    count = len(spl[i])
    if count<largest:
          largest=count
          var = spl[i]
    i+=1
print("Longest word:",var)