'''
a
bc
def
ghij
klmno
'''

n = int(input("n = "))
i=1
no = 1
while i<=n:
    j = 1
    while j<=i:
        print(chr(96+no),end="")
        no = no+1
        j+=1
    print()
    i+=1