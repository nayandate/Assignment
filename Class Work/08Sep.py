'''
def display(name):
    message = f"Hello {name}"

    def displaymessage():
        print(message)
    return displaymessage

ref = display("Deepika")
ref()
'''

'''
def display(x):
    def cal(y):
        return x*y
    return cal

b = display(10)
c = display(4)
d = display(2)

print(b(5))
print(c(5))
print(d(5))

print(c(8))
print(b(8))
print(d(8))
''']