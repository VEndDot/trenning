count_seconds = int(input())  # Вводим начальное кол-сек

seconds_hour = 3600     # Вычисляем сколько секунд в часу
seconds_minute = 60 # Вычисляем сколько секунд в минуте

hour = count_seconds // seconds_hour  # находим кол-часов
count_seconds_two = count_seconds - (hour*seconds_minute)*seconds_minute # изменяем  начальное кол-сек
minutes = count_seconds_two//seconds_minute  # находим кол-минут
seconds = count_seconds_two % seconds_minute  # находим кол-секунд
# Форматируем минуты и секунды
m1 = minutes // 10
m2 = minutes % 10
s1 = seconds // 10
s2 = seconds % 10

print(hour, str(m1) + str(m2) , str(s1) + str(s2), sep=":")