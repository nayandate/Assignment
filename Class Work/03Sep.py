# WAP to filter names of student whose length is greater than 5.
'''
names = ["abc","avi","nayanaa"]
result = list(filter(lambda x: len(x)>5, names))
print (result)
'''

# WAP to multiply all the elements of list using reduce.
'''
from functools import reduce
n = [1,2,3,4,5,6]
result = reduce(lambda x,y:x*y,n,100)
print(result)
'''

# WAP to find maximum element in a list using reduce.
'''
from functools import reduce
n = [1,2,3,4,5,6]
result = reduce(lambda x,y:x if x>y else y,n)
print(result)
'''

# WAP to concatenate strings in a list using reduce.
'''
from functools import reduce
word = ["nayan","date"]
result = reduce(lambda x,y:x+" "+y,word)
print(result)
'''

# Lambda Sorting
'''
st = [("abc",20),("xyz",30),("www",10)]
result = sorted(st,key = lambda x: x[1])
print(result)
result = sorted(st,key = lambda x: x[1],reverse=True)
print(result)
'''
'''
st = {"abc":20,"xyz":30,"www":10}
#result = sorted(st)
result = sorted(st.items(),key=lambda x:x[1])
print(result)

names = ["abc","Abc","bbc","BBC","ccc","DDD"]
result = sorted(names,key=lambda x:x.lower())
print(result)
'''

products = [
    {"name":"laptop","price":8000},
    {"name":"mobile","price":4000},
    {"name":"tablet","price":3000}
]
result = sorted(products,key=lambda x:x["price"])
print(result)