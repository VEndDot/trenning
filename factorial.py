#ДВойной факторилал 
def double_fact(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return double_fact(n-2) * n


#обычный факториал 
def fact(n):
    if n == 1:
        return 1
    return fact(n-1) * n

print(fact(4))