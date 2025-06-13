with open('arq01.txt', 'w+') as arq:

    print('Created the file "arq01.py" and closed it.')
    arq.write('Line 1\n')
    arq.write('Line 2\n')
    arq.write('-' * 6 + '\n')
    arq.writelines(('Line 3\n', 'Line 4\n', 'Line 5\n'))
    arq.write('-' * 6 + '\n')
    arq.seek(0, 0)  # Volta o cursor ao início do .txt
    print(arq.read())   # Podendo ler o arquivo desde o início

with open('arq01.txt', 'r') as arq:
    print(arq.read())
