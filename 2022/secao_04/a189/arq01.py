import os

with open('arq01.py', 'a', encoding='utf-8') as arq:
    for c in range(1, 11):
        arq.write(f'Line {c}\n')


os.rename('arq01.py', 'arq02.txt')
os.remove('arq02.txt')