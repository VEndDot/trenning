import json
with open("Abracadabra__1_.txt") as abra:
    abra = abra.read()
with open("Alphabet.json", "r") as alp:
    alp = json.load(alp)

for text in abra:
    if text.isalpha():
        print(alp[text], end="")
    else:
        print(text, end="")
    
    