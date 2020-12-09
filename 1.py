a = [
    [-1,3,4,5,4],
    [4,3,5,-2,6],
    [5,3,-4,8,5],
    [4,6,3,-5,2],
    [-5,3,3,5,6],
]
sum = 0
j = 0
for k in a:
    i = 0
    for el in k:
        if (i + j) % 2 == 1 and el > 0:
            sum += el
        i += 1
    j += 1
print(sum)