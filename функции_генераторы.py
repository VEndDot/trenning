#Простой генератор
"""def gen_squares(n: int):
    for i in range(1, n+1):
        yield i**2
for i in gen_squares(5):
    print(i)"""
    
#Генератор последовательности Фибоначчи    
"""n = 10 #int(input())
def gen_fibonacci_numbers(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b
for i in gen_fibonacci_numbers(n):
    print(i)"""

# Мой вариант решения(Плохой) функция-генератор my_range_gen(start, stop, step), которая копирует работу range

def my_range_gen(*args):
    if len(args) == 1:
        start = 0
        while start < args[0]:
            yield start
            start += 1
    elif len(args) == 2:
        start = args[0]
        while start < args[1]:
            yield start
            start += 1
    elif len(args) == 3:
        start = args[0]
        step = args[2]
        stop = args[1]
        if step > 0:
            while start < stop:
                yield start
                start += step
        elif step < 0:
            while start > stop:
                yield start
                start += step
                
for i in my_range_gen(1, 10):
    print(i, end=" ")

# Хороший вариан задачи range (Решение со stepik)
def my_range_gen(start, stop=None, step=1):
    if stop is None:
        stop, start = start, 0
    while step and (start < stop, start > stop)[step < 0]:
        yield start
        start += step
print() 
for i in my_range_gen(1, 10):
    print(i, end= " ")