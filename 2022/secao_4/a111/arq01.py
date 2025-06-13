def soma(*args):
    try:
        total = 0
        for num in args:
            total += num
        return total
    except:
        return None

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 1.9))
