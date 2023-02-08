s =input("enter ur string: ")
l = len(s)
k=[]
for i in range(l):
    for j in range(i+1,l+1):
        k.append(s[i:j])
print(k)