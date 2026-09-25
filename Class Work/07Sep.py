#-------------------> Recurssion <------------------- 

# 1. WAP to find factorial of a no. using recurssion.
'''
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(int(input("Enter n: "))))
'''

# 2. WAP to find power function using recurssion.
'''
def power(num,pow):
    if pow==0:
        return 1
    return num*power(num,pow-1)
number =int(input("Enter number: "))
pow =int(input("Enter power: "))
print(power(number,pow))
'''

# 3. WAP to count digits in a no. using recurssion.
'''
def digit(count):
    if count==0:
        return 0
    return 1+digit(count//10)
number =int(input("Enter number: "))
print(digit(number))
'''

#-------------------> Nested Function <-----------------
'''
def hello(name):
    def message():
        return "Welcome guys"
    print("Hello",name)
    print(message())

hello("Nayan")
'''

'''
def outer():
    x = 10
    def inner():
        y = 20
        print("Outer: ",x)
    inner()
    print("Inner: ",y)
outer()
'''

'''
def cal(price,tax):
    def caltax():
        return price*tax
    return price+caltax()
print(cal(1000,0.18))
'''

def bill(amount):
    def disc():
        if amount>10000:
            return amount*0.10
        return 0
    discount = disc()
    final = amount-discount
    return final
print(bill(int(input("Enter amount: "))))
