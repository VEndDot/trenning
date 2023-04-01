n = ' '.join(input()).split()
count_n = [0] * (len(n) + 2)
len_n = len(count_n) 
for i in n:
    count_n[int(i)] += 1
for i in range(len_n):
    if count_n[int(i)] > 0:
        print(i, count_n[i])