d={"A":3, "b":1, "c":2,"d":5, "l":4, "m":9}
k=list(d.values())
k.sort()
l = len(k)-1

m={}
while l >= 0:
    for i,v in d.items():
        if v == k[l]:
            m[i]=k[l]
            l -= 1
print(m)