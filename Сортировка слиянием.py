# функция merge_two_list должна объединить два списка
def merge_two_list(a, b):
    i=j=0
    c=[]
    while i<len(a) and j<len(b):  # сравниваем длину списков
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    c+=a[i:]+b[j:]
    return c
# функция merge_sort должна выполнить сортировку
def merge_sort(s):
    if len(s)==1:
        return s
    middle=len(s)//2
    left=merge_sort(s[:middle])
    right=merge_sort(s[middle:])
    return merge_two_list(left,right)