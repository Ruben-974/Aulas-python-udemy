questions = [
    {
        'question': '5 + 7 = x',
        'options': (10, 5, 12, 15, 13),
        'response': 12,
    },
    {
        'question': '3 + y = 20',
        'options': (17, 9, 13, 22, 19),
        'response': 17,
    },
    {
        'question': 'x - 7 = 1',
        'options': (0, 9, 1, 8, 2),
        'response': 8,
    }
]

letters = 'abcde'
hit = 0

for question in questions:
    print(f'\nQuestion: {question["question"]}:\n')

    for idx, option in enumerate(question['options']):
        print(f'    {letters[idx]}) {option}')

    response = input('\nx is: ').strip().lower()

    while response not in letters:
        response = input('\nInvalid response. Please enter a valid letter: ').strip().lower()

    response_idx = letters.find(response)

    if question['options'][response_idx] == question['response']:
        hit += 1

print(f'\nYou got {hit} out of {len(questions)} questions right!\n')
