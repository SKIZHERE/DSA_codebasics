arr = []
d = {}
with open("../poem.txt", "r") as f:
    for i in f:
        sep = i.strip().lower().split()
        arr.append(sep)
    for j in arr:
        for k in j:
            if k not in d.keys():
                d[k] = 1
            else:
                d[k] = d[k]+1
print(arr)
for i in d.items():
    print(f"{i[0]} : {i[1]}")
