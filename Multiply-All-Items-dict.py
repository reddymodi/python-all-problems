#Python Program to Multiply All the Items in a Dictionary
d={"a":12, "b":23, "c":45}
m=1
for i,v in d.items():
    m *= int(v)
print(m)
