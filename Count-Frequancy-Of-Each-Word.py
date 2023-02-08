#Python Program to Count the Frequency of Each Word in a String using Dictionary
d={"a":"kes", "b":"redy", "c":"kes", "d":"redy"}
k=[]
for i,v in d.items():
    k.append(v)
c={}
for i in k:
    e=k.count(i)
    c[i]=e
print(c)
