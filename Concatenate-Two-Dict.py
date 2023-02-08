#Python Program to Concatenate Two Dictionaries
d={"a":12, "b":23, "c":45}
d1={"e":46, "d":54}
for i,v in d1.items():
    d[i]=v
print(d)