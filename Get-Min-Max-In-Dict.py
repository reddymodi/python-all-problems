#How to get min and max keys corresponding to min and max value in Dictionary
     #fruitsDict = {'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
d={'Apple': 100,'Orange': 200,'Banana': 400,'pomegranate': 600}
k=[]
for i,v in d.items():
    v = int(v)
    k.append(v)
m=max(k)
n=min(k)
print(m,n)
