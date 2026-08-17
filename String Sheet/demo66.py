'''
66. Count number of sentences in a paragraph. 
P = "This. Is. Test." 
3
'''

s = input("Enter String: ")
x=s.split()
count = 0
for i in x:
    if i.endswith("."):
        count+=1
print(count)
