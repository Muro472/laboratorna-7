a = [
    [42,34,43,5,43],
    [4,3,5,-2,6],
    [5,3,-4,3,5],
    [4,6,3,-5,2],
    [-5,3,3,1,6],
]
coords = []
for j in range(len(a)):
    d = 0
    minimal = min(a[j])
    i = a[j].index(minimal)
    for k in range(len(a)):
        if a[k][i] > minimal:
            d = 1
    if d == 0:
        coords.append((j,i))
print(coords)