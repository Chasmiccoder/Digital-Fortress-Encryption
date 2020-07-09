'''
Generating a Tier 3 list:

'''
import random

capital = [chr(j) for j in range(65, 91)]
small = [chr(j) for j in range(97, 123)]
numbers = [j for j in range(0, 10)]
special = ['!', '@,', '#', '$', '%', '^', '&', '*',
           '<', '>', '.', ',', ':', ';', ']', '(', ')', '[']

tier3List = capital + small + numbers + special
print("Old List: ", tier3List)
ns = []
new = []
while(len(ns) < len(tier3List)):
    r = random.randint(0, len(tier3List) - 1)

    if r not in ns:
        ns.append(r)
        new.append(tier3List[r])

print("New List: ", new)
