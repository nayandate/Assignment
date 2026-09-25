#1. WAP to take dictionary from keyboard and print sum.
'''
n = int(input("Enter no. of items: "))
d = {}
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key]=value

s = sum(d.values())
print("Sum is:",s)


d = eval(input("Enter dictionary: "))
s = sum(d.values())
print("Sum is:",s)
'''

#2. WAP to find no. of occurence of each letter present in the given string.
'''
word = input("Enter string: ")
d = {}
for x in sorted(word):
   d[x] = d.get(x,0)+1

print(d)

for k,v in sorted(d.items()):
     print(k,"occured:",v,"times")
'''

#3. WAP to find no. of occurence of each vowel present in the given string.
'''
word = input("Enter string: ")
d = {}
for x in sorted(word):
   if x in "aeiouAEIOU":
     d[x] = d.get(x,0)+1

print(d)

for k,v in sorted(d.items()):
     print(k,"occured:",v,"times")
'''

#4. WAP to track how many times each user try to login.
'''
n = int(input("Enter total users: "))
s = []
d = {}
for i in range(n):
    s.append(input("Enter user: "))
for x in s:
   d[x] = d.get(x,0)+1

print(d)

for k,v in sorted(d.items()):
     print(k,"occured:",v,"times")
'''

#5. WAP to group words based on their length.
'''
n = int(input("Enter n: "))
s = []
d = {}
for i in range(n):
    s.append(input("Enter user: "))

for word in s:
    length = len(word)
    if length not in d:
        d[length] = []
    d[length].append(word)
print(d)

for k,v in sorted(d.items()):
     print(k,"occured:",v,"times")
'''

#6. WAP to merge dictionaries and sum values.
'''
n = int(input("Enter no. of items for dict 1: "))
d1 = {}
for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d1[key]=value

n1 = int(input("\nEnter no. of items for dict 2: "))
d2 = {}
for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d2[key]=value

print()
print(d1)
print()
print(d2)

merge = d1.copy()

for k,v in d2.items():
    merge[k] = merge.get(k,0)+v
print(merge)
'''