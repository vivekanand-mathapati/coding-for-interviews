arr = [0,1,0,2,0,2,2,1,3]
d = {}
for x in arr:
    if d.get(x) is None:
        d[x] = 1
    else:
        d[x] += 1

for x, y in d.items():
    print(str(x)*y, end='')
print()