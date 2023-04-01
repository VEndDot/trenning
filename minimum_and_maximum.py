#480
n = int(input())

maximum = 0
minimum = 9


while n > 0:
    last_n = n%10
    if last_n > maximum:
        maximum = last_n
    elif last_n < minimum:
        minimum = last_n
    n = n//10
print(minimum, maximum, sep="\n")