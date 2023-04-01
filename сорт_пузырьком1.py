n = int(input())
list_n = list(map(int, input().split()))
count_step = 0

for i in range(n - 1):
    for j in range(n - 1 - i):
        if list_n[j] > list_n[j + 1]:
            count_step += 1 # Кол-во перестановок
            list_n[j], list_n[j+1] = list_n[j+1], list_n[j] 
print(*list_n)
print(count_step)