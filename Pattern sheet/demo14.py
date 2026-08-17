'''
1
23
456
78910
'''

n = int(input("n = "))
i=1
no = 1
while i<=n:
    j = 1
    while j<=i:
        print(no,end="")
        no=no+1
        j+=1
    print()
    i+=1