def f(k):
    l=k[0][0]
    r=k[0][1]
    t=k[0][2]
    for i in range(1,len(k)):
        if (k[i][1]<r and k[i][0]!=l) or k[i][2]==t:
            t=k[i][2]
            l=k[i][0]
            r=k[i][1] if k[i][1]<r else r
            continue
        return 'NO'
    return 'YES'
a=int(input())
k=[]
for i in range(a):
    k.append([int(i) for i in input().split()])
k.sort(key=lambda x:x[0])
print(f(k))
