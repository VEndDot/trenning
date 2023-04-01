"""# Создайте генератор
from_10_to_20 = (i for i in range(10, 21))

# Распечатайте три первых значения
print(next(from_10_to_20))
print(next(from_10_to_20))
print(next(from_10_to_20))

# выведите все оставшиеся
for value in from_10_to_20:
    print(value)
    """

count = 5
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = (i for i in range(1, 78))
for i in days:
    if count > 6:
        count = 0
    print((i, day[count]))
    count += 1     
