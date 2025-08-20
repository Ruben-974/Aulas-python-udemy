number = 13195
copy = 13195

while True:
    copy -= 1
    print(number, copy)
    if number % copy == 0:
        print(copy)
        break