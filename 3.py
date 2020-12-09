n = int(input('n = '))
a = [[float(input('A[{0}][{1}]='.format(i,j))) for j in range(n)] for i in range(n)]
print(a)
b = [float(input('Enter b[{0}] = '.format(j))) for j in range(n)]
print('b = {0}'.format(b))
c = []
for i in range(n):
    total = 0
    for j in range(n):
        total += b[j] * a[i][j]
    c.append(total)
print('c = {0}'.format(c))