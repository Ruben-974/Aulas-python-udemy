"""
while em python
utilizado para realizar ações enquanto
uma condição for verdadeira

Requisitos: Entender condições e operadores
"""
while True:
    try:
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
        op = input('Operador +, -, /, * [s]air: ')
    except:
        print('ERRO: Você deve digitar um número!')
        continue
    if op == '+':
        print(f'{n1} {op} {n2} = {n1+n2}\n')
    elif op == '-':
        print(f'{n1} {op} {n2} = {n1-n2}\n')
    elif op == '/':
        print(f'{n1} {op} {n2} = {n1/n2}\n')
    elif op == '*':
        print(f'{n1} {op} {n2} = {n1*n2}\n')
    elif op == 's':
        break
    else:
        print('ERRO: Digite um operador valido!')
