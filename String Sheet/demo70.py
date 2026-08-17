'''
70. Compare the number of times 'the' and 'is' appear. 
S = "the cat is on the mat" 
the: 2, is: 1 (theis)
'''

s = input("String: ")
sub = input("Enter first word to count: ")
sub1 = input("Enter second word to count: ")
x = s.split()
count=0
for i in range(len(x)):
    if x[i] == sub:
        count+=1
print(sub,":",count)

count=0
for i in range(len(x)):
    if x[i] == sub1:
        count+=1
print(sub1,":",count)