a = "T y k P e"
print(list(map(lambda x: (x.upper(), x.lower()), a.replace(" ", ""))))



#Еще lambda map 
persons = [
    {
        'birthday': '1983-10-25',
        'job': 'Field seismologist',
        'name': 'Andrew Hernandez',
        'phone': '680-436-8521x3468'
    },
    {
        'birthday': '1993-10-03',
        'job': 'Pathologist',
        'name': 'Paul Harmon',
        'phone': '602.518.4130'
    },
    {
        'birthday': '2002-06-11',
        'job': 'Designer, multimedia',
        'name': 'Gregory Flores',
        'phone': '691-498-5303x079'
    },
    {
        'birthday': '2006-11-28',
        'job': 'Print production planner',
        'name': 'Jodi Garcia',
        'phone': '(471)195-7189'},
    {
        'birthday': '2019-12-05',
        'job': 'Warehouse manager',
        'name': 'Elizabeth Cannon',
        'phone': '001-098-434-5950x276'
    },
    {
        'birthday': '1984-06-12',
        'job': 'Visual merchandiser',
        'name': 'Troy Lucas',
        'phone': '+1-018-070-2288x18433'
    },
    {
        'birthday': '1993-09-14',
        'job': 'International aid/development worker',
        'name': 'Laurie Sandoval',
        'phone': '2930693269'
    },
    {
        'birthday': '1999-05-25',
        'job': 'Editor, film/video',
        'name': 'Jack Clark',
        'phone': '8643048473'
    },
    {
        'birthday': '1985-09-11',
        'job': 'Magazine journalist',
        'name': 'Kimberly Johnson',
        'phone': '+1-583-428-7663'
    },
    {
        'birthday': '1990-10-07',
        'job': 'Museum/gallery curator',
        'name': 'Austin Liu PhD',
        'phone': '714-879-5250'
    }
]
b = list(map(lambda x: x["phone"], persons))
print(b)

#и еще map lambda
# x**2 - x * y * w + w**4 
list_x = [25, 48, 23, 13, -18, -10, -3, 16, 2, -12, 20, -14, 14, 45, 41, 6, 11, 15, 22,
          -14, -11, 41, 15, 48, 47, 41, -8, 1, 4, 1, 40, 27, -11, -2, -14, -15, 35, 4,
          49, 4, 5, 13, 50, 35, -3, 3, 30, -11, 7, 12]

list_y = [-9, 17, 41, 47, -5, -10, -5, 13, 31, -11, 37, 9, 46, 27, -1, 36, 32, 23, -12,
          38, 8, 9, 17, 16, 29, -4, 4, 2, 1, 46, 6, 49, -16, 21, -19, -10, 15, -13, 20,
          13, -18, 21, -17, 21, 10, 5, 38, -1, 18, 22]

list_w = [9, -26, 3, 21, 48, -14, 43, -4, -16, 16, 41, 43, -27, -9, 10, -10, 4, -2, 1,
          7, 30, -29, 11, 17, 31, 31, -26, 38, 38, -17, 35, 17, 35, 10, -25, 42, -30,
          -10, -20, 20, 15, 0, 29, -30, -21, -13, -27, -21, -18, -26]

result = list(map(lambda x, y, w: (x**2 - x*y*w + w**4), list_x, list_y, list_w))
print(result)