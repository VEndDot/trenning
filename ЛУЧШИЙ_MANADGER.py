import json
man_prace = {}
with open("manager_sales.json", "r") as f:
    data = json.load(f)
for i in data:
    name_manager = i["manager"]["first_name"] + " " + i["manager"]["last_name"]
    #print(name_manager)
    for j in i["cars"]:
        if name_manager not in man_prace:
            man_prace.setdefault(name_manager,j["price"])
        else:
            man_prace[name_manager] = man_prace.get(name_manager) + j["price"]
s_m = 0
for v in man_prace.values():
    if v > s_m:
        s_m = v
for k, v in man_prace.items():
    if v == s_m:
        print(k, v)
