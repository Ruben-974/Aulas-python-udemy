numbers = [1, 3, -7, -2, 10, 5, 2]

new_numbers = [
    number
    if number%2 == 0 else number-1
    for number in numbers
    if number > 0
]

print(new_numbers)