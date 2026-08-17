'''
1
123
12345
1234567
123456789
'''

n = int(input("n = "))
i=1
no = 1
while i<=n:
    j = 1
    while j<=no:
        print(j,end="")
        j+=1
    no+=2
    print()
    i+=1