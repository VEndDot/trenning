len_n = int(input())

n = list(map(int, input().split()))

count_n =[0]*201
for i in n:
    count_n[i+100] += 1
print(count_n)
    
for i in range(201):
    if count_n[i] > 0:
        print(i - 100, count_n[i])
