fibonacci = [0, 1]
while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(sum([n for n in fibonacci if n % 2 == 0]))

