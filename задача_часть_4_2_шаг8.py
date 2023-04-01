"""
Задача про мальчиков и девочек 4.2 шаг 8(последняя задача) 
Кайф, когда сделал сам )))))
"""

# Ввод кол-ва мальчиков и девочек и их уровня мастерства
m = int(input())
list_m = list(map(int, input().split()))
f = int(input())
list_f = list(map(int, input().split()))

# Создали индексы для движения по спискам
index_m = 0
index_f = 0

# Подсчет возможных пар
count_mf = 0

# Сортировка массивов
list_m.sort()
list_f.sort()

while index_m < m and index_f < f:
    
    mf_l = abs(list_m[index_m] - list_f[index_f]) # ищем единицу или ноль

    if (mf_l == 1) or (mf_l == 0): # Если 0 или 1, то считаем пару и сдвигаем оба массива на один шаг  
        index_m += 1
        index_f += 1   
        count_mf += 1
    elif list_m[index_m] < list_f[index_f]: # Сдвигаем массив мальчиков вправо        
        index_m += 1
    elif list_m[index_m] > list_f[index_f]: # Сдвигаем массив девочек вправо
        index_f += 1

print(count_mf)