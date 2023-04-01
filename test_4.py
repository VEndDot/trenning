import string
def longest_word_in_file(file_name):
    fil = open(file_name, encoding="utf-8")
    fil =  fil.read()
    for i in fil:
        if i in string.punctuation:
            fil = fil.replace(i, "")  
    b = [""]
    for i in fil.split():
        if len(b[0]) <= len(i):
            b[0] = i
    return b[0]
    
print(longest_word_in_file("text.txt"))