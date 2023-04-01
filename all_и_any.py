
"""for i in a:
    if "a" in i:
"""

"""print(all("a" in i for i in input().lower().split()))"""

print(any(i.endswith("ought") for i in "forethought".lower().split()))