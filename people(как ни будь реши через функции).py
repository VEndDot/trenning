import json
with open("group_people.json", "r") as peopl:
    a = json.load(peopl)
#print(json.dumps(a, indent= 4))]
women_1977 = {}
res = {}
s = 0
for i in a:
    count = 0
    print(f"____{i['id_group']}____")
    for j in i['people']:
        if j["gender"] == "Female" and j["year"] > 1977:
            count += 1
            print(j["year"])
    res[i['id_group']] = count
for v in res.values():
    if v > s:
        s = v
for k,v in res.items():
    if v == s:
        print(k, v)    
