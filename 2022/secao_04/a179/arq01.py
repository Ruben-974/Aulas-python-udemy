def count(start=0, stop=10):

    print(start)

    if start == stop:
        return start

    start += 1

    return count(start, stop)


count()
