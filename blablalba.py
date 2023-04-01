n, m = map(int, input().split())

array = []

for row in range(n):
    array.append(list(map(int, input().split())))

max_value = 0
max_row = 0
max_column = 0

for i in range(n):
    for j in range(m):
        if array[i][j] > max_value:
            max_value = array[i][j] 
            max_row = i
            max_column = j
            
print(max_value)
print(max_row, max_column)