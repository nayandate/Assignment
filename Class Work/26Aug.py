# 1. WAP to create a function which receive one parameter as a no. & return list of all even number upto that number.

def even(n):
    even = []
    for i in range(n+1):
        if i%2 == 0:
           even.append(i)
    return even

result = even(int(input("Enter number: ")))
print("Result is:",result)