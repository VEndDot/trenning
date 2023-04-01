r, c = map(int, input().split())

a = []

for l in range(r):
    a.append(list(map(int, input().split())))

max_score = 0
max_summa = 0
max_index = 0

for row in range(r):
    m_try = 0
    s = 0
    for column in range(c):
        s += a[row][column]
        if a[row][column] > m_try:
            m_try = a[row][column]
    if m_try > max_score:
        max_score = m_try
        max_summa = s
        max_index = row
    elif m_try == max_score and s > max_summa:
        max_score = m_try
        max_summa = s
        max_index = row
print(max_index)         
        