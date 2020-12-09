a = [
    [-1,3,4,5,4],
    [4,3,5,-2,6],
    [5,3,-4,8,5],
    [4,6,3,-5,2],
    [-5,3,3,5,6],
]
for i in range(len(a)):
    if i%2 == 0:
        a[i].sort(reverse=True)
for i in range(len(a)):
    print(a[i])
