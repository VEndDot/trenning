n = int(input())
a = []

for row in range(n):
    a.append(list(map(int, input().split())))

for row in range(n):
    for column in range(n):
        print(a[column][row], end=' ')
    print()
        