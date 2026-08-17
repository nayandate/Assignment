'''
*
*#
*#*
*#*#
*#*#*
'''

n = int(input("n = "))
i=1
while i<=n:
    j = 1
    while j<=i:
        if j%2==0:
            print("#",end="")
        else:
            print("*",end="")
        j+=1
    print()
    i+=1