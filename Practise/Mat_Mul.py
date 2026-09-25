r1=int(input("enter the no of rows"))
c1=int(input("enter the no of columns"))
m1=[]
for i in range (r1):
    row=[]
    for j in range (c1):
        row.append(int(input()))
    m1.append(row)

r2=int(input("enter the no of rows"))
c2=int(input("enter the no of columns"))
m2=[]
for i in range (r2):
    row=[]
    for j in range (c2):
        row.append(int(input()))
    m2.append(row)
if c1!=r2:
    print("not possible")
else:
    res=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        res.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j]=res[i][j]+m1[i][k]*m2[k][j]
    for i in res:
        print(*i)