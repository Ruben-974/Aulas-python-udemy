l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = [1, 2, 3, 4, 5, 6]
l3 = []

for c in range(len(min(l1, l2))):
    l3.append(l1[c]+l2[c])

print(l3)
