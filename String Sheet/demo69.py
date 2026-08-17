'''
69. Count how many times 'life' appears in a string. 
S = "life is life" 
2
'''

s = input("String: ")
sub = input("Enter word to count: ")
x = s.split()
count=0
for i in range(len(x)):
    if x[i] == sub:
        count+=1
print("Count:",count)