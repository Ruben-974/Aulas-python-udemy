from itertools import count

r = range(10, 100)
c = count(10)

for i in r:

    # r __iter__, no __next__

    print(i)

print('/-'*10)

for i in c:

    # c __iter__ and __next__

    if i > 100:
        break
    print(i)


