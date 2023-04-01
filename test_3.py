import string
def longest_word_in_file(file_name):
    for i in file_name:
        if i in string.punctuation:
            file_name = file_name.replace(i, "")  
    b = [""]
    for i in file_name.split():
        if len(b[0]) < len(i):
            b[0] = i
    print(b)
fil = open("text.txt", encoding="utf-8")
longest_word_in_file(fil.read())