r = int(input())
g = int(input())
b = int(input())

print("#" + hex(r).lstrip('0x').upper().zfill(2), hex(g).lstrip('0x').upper().zfill(2),hex(b).lstrip('0x').upper().zfill(2), sep='')
