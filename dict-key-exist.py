#Python Program to Check if a Key Exists in a Dictionary or Not
d = {"a":12, "b":23, "c":45}
k = input("enter ur key: ")
for i,v in d.items():
    if i == k:
        print(f"{k} is in dictionary")