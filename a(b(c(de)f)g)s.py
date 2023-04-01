def skription(a): 
    if len(a) in {1, 2}:
        return a
    return a[0] + '(' + skription(a[1:-1]) + ")" + a[-1]
a = "abcdefgs"       
print(skription(a))
