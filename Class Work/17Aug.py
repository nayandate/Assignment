# WAP to check unique characters in a string.
'''
text = input("Enter string: ")
if len(text) == len(set(text)):
    print("All characters are unique.")
else:
    print("All characters are not unique.")
'''

# WAP to find first non repeating character in a string using set logic.

text = input("Enter string: ")
a = set()
b = set()

for i in text:
    if i not in a:
        a.add(i)
    else:
        b.add(i)

for i in text:
    if len(a) == 0:
        print("No repeating character")[.
        break
    if i in a:
        print("First non repeating character:",i)
        break
'''

# Dictionary

student = {
    "name":"abc",
    "age":30,
    "age":"yoyo",
    "city":"indore"
}
print(student)

for i in student:
    if i == 'age':
        print(student[i])
'''