import itertools
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l=[0]
    l.append(x)
    l.append(y)
    l.append(z)
    a=[]
    perm=[p for p in itertools.product(l, repeat=3)]
    p=list(perm)
    print(p)
    for x in p:
        a.append(list(x))

    #newlist=[x for x in a if x(0)+x(1)+x(2)<n ]
    b=[]
    sum=0
    for x in a:
        for z in x:
            sum+=z
        if(sum!=n):
            b.append(x)
        sum=0
    print(b)
