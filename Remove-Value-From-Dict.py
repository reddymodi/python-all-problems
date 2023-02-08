#remove no value items from Dictionary
	#mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
d={'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
for i,v in d.items():
    if v == None:
        del d[i]
print(d)