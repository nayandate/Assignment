'''
def hello(name,age):
    print(name,age)
hello("Nayan",age=30)
'''

# 1. WAP to perform sum of unlimited no.
'''
def add(*num):
    total = 0
    for sum in num:
        total+=sum
    return total
print(add(10,20))
'''

# 2. WAP to find average of any no.
'''
def avr(*marks):
    return sum(marks)/len(marks)
print(avr(10,20,30))
'''    

'''
4. Cloud Storage Duplicate File Name Resolver

A cloud storage company stores uploaded filenames from users.

Sometimes multiple duplicate filenames are uploaded.

The system should:

* Keep the first occurrence unchanged
* Add (1), (2), (3)... for duplicates

Input:

text
file file image file image data


Output:

text
file file(1) image file(2) image(1) data'''

s=input("Enter the string: ")
new_string=s.split()
result={}
for i in new_string:
    if i not in result:
        result[i]=0
        print(i,end=" ")
    else:
        result[i]+=1
        print(i,f"({result[i]})",end=" ")