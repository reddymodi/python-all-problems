#Python Program to Find the Sum of All the Items in a Dictionary
d={"a":12, "b":23, "c":45}
s = 0
for i,v in d.items():
    s += int(v)
print(s)