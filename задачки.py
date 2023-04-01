# строка типа f(h(k(o)s)a

def rec(s):
    if len(s) == 1 or len(s) == 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]
s = input()
print(rec(s))

# возведение в степень целых чисел (и отрицательных, и положительных)

def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1/power(x, -n)
    if n % 2 == 0:
        return power(x, n//2)*power(x, n//2)
    else:
        return power(x, n-1)*power(x, n-1)

# глубина вложенного списка

a = [1,[3,[2,3,[4]]],2,[2,3,4,[3,4,[2,3],5]]]

def rec(spicok, level=1):
    print(*spicok, 'level=', level)
    for i in spicok:
        if type(i) == list:
            rec(i, level+1)

rec(a)

# из многомерного словаря сделай одномерный 
def flatten_dict(a: dict, key: str = '') -> dict:       # добавил ключ(что-бы передавать внешний ключ)
    c = {}                                              # пустой словарь для возврата готового списка
    for k, v in a.items():                              # проходимся по эл-м словаря(достаем ключ и значение)
        if type(v) == int:                              # если значение число
            c.update({(key+'_'+k)[1:]: v})              # обновляем словарь (ключ без первого эл-та "_")
        else:
            c.update(flatten_dict(v, key=key+'_'+k))    # иначе обновляем словарь вызывая фун-ю
    return c

nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}
print(flatten_dict(nested))