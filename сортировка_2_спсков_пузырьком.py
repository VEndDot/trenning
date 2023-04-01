n, b = map(int,input().split())
list_n = list(map(int,input().split()))
list_b = list(map(int,input().split()))

index_list_n = 0
index_list_b = 0

litc_c = []

while (index_list_n < n) and (index_list_b < b):
    if list_n[index_list_n] < list_b[index_list_b]:
        litc_c.append(list_n[index_list_n])
        index_list_n += 1
    else:
        litc_c.append(list_b[index_list_b])
        index_list_b += 1

while index_list_n < n:
    litc_c.append(list_n[index_list_n])
    index_list_n += 1

while index_list_b < b:
    litc_c.append(list_b[index_list_b])
    index_list_b += 1
    
print(*litc_c)