import sys


iterable = iter([n for n in range(1000)])
list = [n for n in range(1000)]
generator = (n for n in range(1000))

print(sys.getsizeof(iterable))
print(sys.getsizeof(list))
print(sys.getsizeof(generator))