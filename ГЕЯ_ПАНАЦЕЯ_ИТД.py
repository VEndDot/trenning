def find_lines_len_more_6(file_name:str):
    words = set()
    with open(file_name, encoding="utf-8") as f:
        f = f.read().split()
    for i in f:
        i = i.upper()
        if i[-2:] == "ЕЯ":
            words.add(i)
    for i in sorted(words, key= lambda x: (len(x), x)):
        print(i)
              
    #print(words)
    #print(a)
#sum(len(str(i)) > 6 for i in f)
#return len([i for i in f.read().replace("\n", "").split() if len(i) > 6])
find_lines_len_more_6("words (1).txt")
# for i in f: