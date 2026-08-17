'''
1
222
33333
4444444
555555555
'''

n = int(input("n = "))
i=1
no = 1
while i<=n:
    j = 1
    while j<=no:
        print(i,end="")
        j+=1
    no+=2
    print()
    i+=1