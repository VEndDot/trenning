"""def count_strings(*args):
    return sum(isinstance(i, str) for i in args) """

#Сортировка без учета регистра 
def find_keys(*args, **kwargs):
    list_text = [k for k, v in kwargs.items() if isinstance(v, (list, tuple))]
    return sorted(list_text, key = lambda s: s.casefold())
print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))
