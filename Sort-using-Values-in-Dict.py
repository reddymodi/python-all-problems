#How can you sort the dictionary elements based on valuesd = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}

d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
val = list(d.values())
val.sort()
new={}
for i in val:
    for k,v in d.items():
        if i == v:
            new[k] = v 
print(new)