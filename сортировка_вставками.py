n = int(input())
list_n = list(map(int, input().split()))

for i in range(1, n):
    for j in range(0, len(list_n[:i])):
        if list_n[i] < list_n[j]:
            list_n[j], list_n[i] = list_n[i], list_n[j] 
print(*list_n)