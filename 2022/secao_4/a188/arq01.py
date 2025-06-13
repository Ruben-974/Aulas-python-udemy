with open('arq01.txt', 'a', encoding='utf-8') as arq:
    for c in range(1, 11):
        arq.write(f'Line {c}\n')
