# ЛИнейный способ O(n)

n = 36   #например
i = 1
print("ВЫВОД: ", end=" ")
while i <= n:
    if n%i == 0:
        print(i, end=" ")
    i += 1
print()
print("#"*50)

# Способ 2 О(n//2)

n = 36   #например
i = 12
print("ВЫВОД: ", end=" ")
while i <= n//2:
    if n%i == 0:
        print(i, end=" ")
    i += 1
print(n)
print("#"*50)

# Способ 3 О(n**0.5) корень из n

n = 7   #например
i = 1
a = []
print("ВЫВОД: ", end=" ")
while i*i <= n:
    if n%i == 0:
        if i == n//i:
            a.append(i)
        else:
            a.append(i)
            a.append(n//i)
    i += 1
a.sort()
print(a)
print("#"*50)
