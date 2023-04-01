n, m = map(int, input().split())

a = []

for row in range(n):
    b = []
    for column in range(m):
        b.append(column+(row*m))
    a.append(b)

for i in range(1, n):
    if i%2 != 0:
        a[i].reverse()

for i in a:
    print(*i)
#column+(row*10)