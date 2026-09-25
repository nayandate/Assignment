'''
def bill(**items):
    total = 0
    for item,price in items.items():
'''
'''
# Positional Only Parameters:

def a(p1,p2,/):
    print(p1,p2)
a("Nayan",60) 
a("10",p2 = 20) -->Error(Positional Only Parameters)
'''
'''
# Keyword Only Parameters:

def a(*,p1,p2):
    print(p1,p2)
#a("Nayan",60)  -->Error(Keyword Only Parameters)
a(p1 = "10",p2 = 20)

def a(p1,*,p2):
    print(p1,p2)
#a("Nayan",60)  -->Error(Keyword Only Parameters)
a("10",p2 = 20)
'''
'''
def pay(id,name,/,amount,method,*,currency,tax):
     print(id,name,amount,method,currency,tax)

pay(101,"Nayan",5000,UPI,currency = "INR",tax = 5)
pay(101,"Nayan",amount = 5000,UPI,currency = "INR",tax = 5)
'''
'''
# By Normal funtion:

def add(a,b):
   return(a+b)
print(add(10,20))

# By lambda funtion:

add = lambda a,b:b+a
print(add(10,20))
'''

# By Normal funtion:
'''
def add(a,b):
  if a>b:
   return a
  else:
    return b
print(add(10,20))

# By lambda funtion:

grst = lambda a,b:a if a>b else b
print(grst(10,20))
'''
'''
# Map Function

num = [1,2,3,4,5]
def square(n):
    return n*n
result = map(square,num)
print(tuple(result))

# Lambda Function

num = [1,2,3,4,5]
result = map(lambda x:x*x,num)
print(tuple(result))
'''
'''
# Map Function

names = ["muskan","mehak","muski","makdi","nagin"]
def change(n):
    return n.upper()
result = map(change,names)
print(tuple(result))

# Lambda Function

names = ["muskan","mehak","muski","makdi","nagin"]
result = list(map(lambda x:x.upper(),names))
print(result)
'''

'''
1. WAP to capitalize every word of a list.

# Map Function

names = ["muskan","mehak","muski","makdi","nagin","sapoli"]
def change(n):
    return n.capitalize()
result = map(change,names)
print(tuple(result))

# Lambda Function

names = ["muskan","mehak","muski","makdi","nagin","sapoli"]
result = list(map(lambda x:x.capitalize(),names))
print(result)
'''
'''
# 2. WAP to find length of every word of a list.

# Map Function

names = ["muskan","mehak","muski","makdi","nagin","sapoli"]
def change(n):
    return len(n)
result = map(change,names)
print(tuple(result))

# Lambda Function

names = ["muskan","mehak","muski","makdi","nagin","sapoli"]
result = list(map(lambda x:len(x),names))
print(result)
'''

'''
# 3. WAP to add two list.

# Map Function

list1 = [5,6,7,8,9,10]
list2 = [10,11,20,12,14,15]
def add(a,b):
    return a+b
result = map(add,list1,list2)
print(tuple(result))

# Lambda Function

list1 = [5,6,7,8,9,10]
list2 = [10,11,20,12,14,15]

result = list(map(lambda x,y:x+y,list1,list2))
print(result)
'''
'''
# 4. WAP to take list of integers and print even or odd.

# Map Function

list1 = [5,6,7,8,9,10]
def check(a):
    if a%2 == 0:
       return "Even"
    else:
       return "Odd"
result = map(check,list1)
print(tuple(result))

# Lambda Function

list1 = [5,6,7,8,9,10]

result = list(map(lambda x:"Even" if x%2==0 else "Odd",list1))
print(result)
'''

'''
# 4. WAP to convert numbers of a list into string.

# Map Function

x = [5,6,7,8,9,10]
def check(a):
    return str(a)
result = map(check,x)
print(tuple(result))

# Lambda Function

x = [5,6,7,8,9,10]

result = list(map(lambda y:str(y),x))
print(result)
'''

'''
# 5. WAP to calculate student grades.

# Map Function

marks = [60,80,95,70,33,55,40]
def cal(a):
  if a>85:
    return "A+"
  elif a>75:
    return "A"
  elif a>60:
    return "B"
  elif a>45:
    return "C"
  elif a>33:
    return "D"
  else:
    return "Fail"
result = map(cal,marks)
print(tuple(result))

# Lambda Function

marks = [60,80,95,70,33,55,40]

result = list(map(lambda x:"A" if x>75 else "B" if x>60 else "C" if x>45 else "D" if x>33 else "Fail",marks))
print(result)
'''





