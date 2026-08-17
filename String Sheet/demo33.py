'''
33. Find the longest word. 
S = "find the longest word" 
"longest"
'''

s = input("Input: ")
spl = s.split()
largest=0
i = 0
while i<len(spl):
    count = len(spl[i])
    if count>largest:
          largest=count
          var = spl[i]
    i+=1
print("Longest word:",var)