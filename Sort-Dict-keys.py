#How can you sort dictionary elements based on keysd = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
d = {'Tim': 18, 'Charlie': 12, 'Tiffany': 22, 'Robert': 25}
l = list(d.keys())
l.sort()
k = {}
for i in l:
    k[i]=d[i]
print(k)