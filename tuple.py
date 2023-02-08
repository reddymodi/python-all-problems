n=(10,10,20,10)
l = len(n)
i = 0
res=False
for i in n:
    for j in n:
        if i == j:
            res=True
        else:
            res=False
            break
if res == True:
    print("its same")
else:
    print("not same")
    