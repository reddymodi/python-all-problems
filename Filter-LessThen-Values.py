#filter dictionary where the value is less than 20000.
	#empdict = {'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
	
d={'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}
k={}
for i,v in d.items():
    if v < 20000:
        k[i]=v
print(k)
