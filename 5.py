a = [
    [-1,3,4,5,4],
    [4,3,5,-2,6],
    [5,3,-4,8,5],
    [4,6,3,-5,2],
    [-5,3,3,5,6],
]
sum = 0
k = len(a)
j = 0
while j < k:
    i = 0
    while i < k:
        el = a[i][j]
        if el < 0:
            i = 0
            while i < k:
                sum += a[i][j]
                i += 1
        i += 1
    j += 1
print(sum)