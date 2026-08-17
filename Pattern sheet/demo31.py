'''
12345
1234
123
12
1
'''

n = int(input("n = "))
i=n
while i>=1:
    j = 1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i-=1