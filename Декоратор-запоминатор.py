# Напишите определение декоратора memoize  
from functools import wraps
b = {}
def memoize(func):
    @wraps(func)
    def inner(a):
        if a not in b: #Если ключа нет в словаре
            b.setdefault(a, func(a)) # То добавляет ключ и значение в словарь
        return b.get(a) # Передает значение ключа
    return inner

# Код ниже не удаляйте, он нужен для проверки   


@memoize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    return n if n < 2 else fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(50) == 12586269025
assert fibonacci(60) == 1548008755920
assert fibonacci(70) == 190392490709135
assert fibonacci(80) == 23416728348467685
assert fibonacci(90) == 2880067194370816120
assert fibonacci(100) == 354224848179261915075
assert fibonacci.__name__ == 'fibonacci'
assert fibonacci.__doc__.strip() == 'Возвращает n-ое число Фибоначчи'
print('Good')