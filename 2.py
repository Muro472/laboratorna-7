from math import sin
from math import cos
x = int(input('ведіть число x '))
n = int(input('ведіть число n'))
m = int(input('ведіть число m'))
alpha = []
i = 1
while i < n + 1:
    b = []
    j = 1
    while j < m + 1:
        el = i * (sin(i * x) + cos(j * x))
        b.append(el)
        j += 1
    i += 1
    alpha.append(b)
for i in range(len(alpha)):
    print(alpha[i])
kek = 1
for i in range(n):
    for j in range(m):
        if i * j < x:
            kek *= alpha[i][j]
print(kek)