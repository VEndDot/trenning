a, b = map(int, input().split())
ac = a
bc = b
while b > 0:
    a, b = b, a%b
NOK = (ac*bc)/a
print(int(NOK)) 